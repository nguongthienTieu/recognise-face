import os
import io
import pickle
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import face_recognition
import cv2
import numpy as np
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from tqdm import tqdm
from PIL import Image
from config import CONFIG, ADVANCED_CONFIG

class FaceSearchEngine:
    def __init__(self, config):
        self.config = config
        self.drive_service = None
        self.target_encoding = None
        self.encodings_cache = {}
        
    def authenticate_drive(self):
        """Xác thực Google Drive API"""
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.config['CREDENTIALS_FILE'],
                scopes=['https://www.googleapis.com/auth/drive.readonly']
            )
            self.drive_service = build('drive', 'v3', credentials=credentials)
            print("✓ Đã kết nối Google Drive API")
        except Exception as e:
            print(f"✗ Lỗi xác thực: {e}")
            return False
        return True
    
    def load_target_face(self):
        """Load và encode ảnh mẫu"""
        try:
            target_image = face_recognition.load_image_file(self.config['TARGET_IMAGE_PATH'])
            encodings = face_recognition.face_encodings(target_image)
            
            if len(encodings) == 0:
                print("✗ Không tìm thấy khuôn mặt trong ảnh mẫu!")
                return False
            
            self.target_encoding = encodings[0]
            print(f"✓ Đã load ảnh mẫu: {self.config['TARGET_IMAGE_PATH']}")
            return True
        except Exception as e:
            print(f"✗ Lỗi load ảnh mẫu: {e}")
            return False
    
    def load_cache(self):
        """Load cache encodings nếu có"""
        if not self.config.get('ENABLE_CACHE', True):
            print("⚠ Cache đã bị tắt")
            return
            
        if os.path.exists(self.config['CACHE_FILE']):
            try:
                with open(self.config['CACHE_FILE'], 'rb') as f:
                    self.encodings_cache = pickle.load(f)
                print(f"✓ Đã load {len(self.encodings_cache)} encodings từ cache")
            except Exception as e:
                print(f"⚠ Không thể load cache: {e}")
                self.encodings_cache = {}
    
    def save_cache(self):
        """Lưu cache encodings"""
        if not self.config.get('ENABLE_CACHE', True):
            return
            
        try:
            with open(self.config['CACHE_FILE'], 'wb') as f:
                pickle.dump(self.encodings_cache, f)
            print(f"✓ Đã lưu {len(self.encodings_cache)} encodings vào cache")
        except Exception as e:
            print(f"⚠ Không thể lưu cache: {e}")
    
    def list_drive_images(self):
        """Lấy danh sách tất cả ảnh trong Google Drive folder"""
        try:
            query = f"'{self.config['DRIVE_FOLDER_ID']}' in parents and (mimeType contains 'image/')"
            results = []
            page_token = None
            
            print("📁 Đang quét thư mục Google Drive...")
            
            while True:
                response = self.drive_service.files().list(
                    q=query,
                    spaces='drive',
                    fields='nextPageToken, files(id, name, mimeType)',
                    pageToken=page_token,
                    pageSize=1000
                ).execute()
                
                files = response.get('files', [])
                results.extend(files)
                
                page_token = response.get('nextPageToken')
                if not page_token:
                    break
            
            print(f"✓ Tìm thấy {len(results)} ảnh")
            return results
        except Exception as e:
            print(f"✗ Lỗi khi quét thư mục: {e}")
            return []
    
    def download_image(self, file_id):
        """Download ảnh từ Google Drive về memory"""
        try:
            request = self.drive_service.files().get_media(fileId=file_id)
            file_buffer = io.BytesIO()
            downloader = MediaIoBaseDownload(file_buffer, request)
            
            done = False
            while not done:
                _, done = downloader.next_chunk()
            
            file_buffer.seek(0)
            image = Image.open(file_buffer)
            # Convert RGBA to RGB if necessary
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            return np.array(image)
        except Exception as e:
            # Silently return None for failed downloads to avoid cluttering output
            return None
    
    def process_single_image(self, file_info):
        """Xử lý một ảnh: download, detect face, compare"""
        file_id = file_info['id']
        file_name = file_info['name']
        
        # Kiểm tra cache
        if file_id in self.encodings_cache:
            encoding = self.encodings_cache[file_id]
        else:
            # Download và encode
            image = self.download_image(file_id)
            if image is None:
                return None
            
            try:
                face_locations = face_recognition.face_locations(image)
                if len(face_locations) == 0:
                    return None
                
                encodings = face_recognition.face_encodings(image, face_locations)
                if len(encodings) == 0:
                    return None
                
                encoding = encodings[0]
                self.encodings_cache[file_id] = encoding
            except Exception:
                return None
        
        # So sánh với ảnh mẫu
        try:
            distance = face_recognition.face_distance([self.target_encoding], encoding)[0]
            is_match = distance <= self.config['TOLERANCE']
            
            if is_match:
                return {
                    'file_id': file_id,
                    'file_name': file_name,
                    'distance': float(distance),
                    'similarity': float((1 - distance) * 100)
                }
        except Exception:
            pass
        
        return None
    
    def search_faces(self, image_files):
        """Tìm kiếm khuôn mặt trong danh sách ảnh với multi-threading"""
        matches = []
        
        print(f"\n🔍 Bắt đầu tìm kiếm với {self.config['NUM_THREADS']} threads...")
        
        with ThreadPoolExecutor(max_workers=self.config['NUM_THREADS']) as executor:
            futures = {executor.submit(self.process_single_image, file): file for file in image_files}
            
            with tqdm(total=len(image_files), desc="Xử lý ảnh", unit="ảnh") as pbar:
                for future in as_completed(futures):
                    result = future.result()
                    if result:
                        matches.append(result)
                    pbar.update(1)
        
        return matches
    
    def save_results(self, matches):
        """Lưu kết quả tìm kiếm"""
        if not os.path.exists(self.config['RESULTS_DIR']):
            os.makedirs(self.config['RESULTS_DIR'])
        
        # Sắp xếp theo độ tương đồng
        matches.sort(key=lambda x: x['similarity'], reverse=True)
        
        # Lưu JSON
        result_file = os.path.join(self.config['RESULTS_DIR'], 'results.json')
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(matches, f, indent=2, ensure_ascii=False)
        
        # Tạo báo cáo text
        report_file = os.path.join(self.config['RESULTS_DIR'], 'report.txt')
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(f"=== BÁO CÁO TÌM KIẾM KHUÔN MẶT ===\n\n")
            f.write(f"Tổng số ảnh tìm thấy: {len(matches)}\n")
            f.write(f"Ngưỡng độ chính xác: {self.config['TOLERANCE']}\n\n")
            f.write(f"{'STT':<5} {'Tên file':<40} {'Độ tương đồng':<15} {'Distance':<10}\n")
            f.write("="*80 + "\n")
            
            for idx, match in enumerate(matches, 1):
                f.write(f"{idx:<5} {match['file_name']:<40} {match['similarity']:.2f}% {match['distance']:.4f}\n")
        
        print(f"\n✓ Đã lưu kết quả vào thư mục: {self.config['RESULTS_DIR']}")
        print(f"  - results.json: Dữ liệu chi tiết")
        print(f"  - report.txt: Báo cáo văn bản")
    
    def run(self):
        """Chạy toàn bộ quy trình"""
        print("="*60)
        print("🔎 FACE RECOGNITION SEARCH ENGINE")
        print("="*60)
        
        # Bước 1: Xác thực Google Drive
        if not self.authenticate_drive():
            return
        
        # Bước 2: Load ảnh mẫu
        if not self.load_target_face():
            return
        
        # Bước 3: Load cache
        self.load_cache()
        
        # Bước 4: Lấy danh sách ảnh
        image_files = self.list_drive_images()
        if not image_files:
            print("✗ Không tìm thấy ảnh nào!")
            return
        
        # Bước 5: Tìm kiếm
        matches = self.search_faces(image_files)
        
        # Bước 6: Lưu cache
        self.save_cache()
        
        # Bước 7: Lưu kết quả
        if matches:
            self.save_results(matches)
            print(f"\n🎉 Hoàn thành! Tìm thấy {len(matches)} ảnh khớp")
        else:
            print("\n😔 Không tìm thấy ảnh nào khớp")

if __name__ == "__main__":
    import sys
    
    # Kiểm tra cấu hình cơ bản / Check basic configuration
    if CONFIG['DRIVE_FOLDER_ID'] == 'your_folder_id_here':
        print("⚠ CẢNH BÁO: Vui lòng cập nhật DRIVE_FOLDER_ID trong config.py!")
        print("⚠ WARNING: Please update DRIVE_FOLDER_ID in config.py!")
        sys.exit(1)
    
    if not os.path.exists(CONFIG['CREDENTIALS_FILE']):
        print(f"⚠ CẢNH BÁO: Không tìm thấy file {CONFIG['CREDENTIALS_FILE']}!")
        print(f"⚠ WARNING: {CONFIG['CREDENTIALS_FILE']} not found!")
        print("Vui lòng tạo file credentials.json hoặc xem hướng dẫn trong README.md")
        print("Please create credentials.json or see instructions in README.md")
        sys.exit(1)
    
    if not os.path.exists(CONFIG['TARGET_IMAGE_PATH']):
        print(f"⚠ CẢNH BÁO: Không tìm thấy ảnh mẫu {CONFIG['TARGET_IMAGE_PATH']}!")
        print(f"⚠ WARNING: Target image {CONFIG['TARGET_IMAGE_PATH']} not found!")
        print("Vui lòng thêm ảnh mẫu của bạn hoặc cập nhật TARGET_IMAGE_PATH trong config.py")
        print("Please add your target image or update TARGET_IMAGE_PATH in config.py")
        sys.exit(1)
    
    # Chạy công cụ / Run the tool
    engine = FaceSearchEngine(CONFIG)
    engine.run()
# Face Recognition Search Tool / Công cụ Tìm kiếm Khuôn mặt

[English](#english) | [Tiếng Việt](#tiếng-việt)

---

## English

### Overview
A powerful face recognition tool that can search and identify your photos among 10,000+ images stored on Google Drive. This tool uses advanced face recognition algorithms to compare faces and find matches efficiently.

### Features
- 🔍 **Smart Face Recognition**: Uses face_recognition library with high accuracy
- ☁️ **Google Drive Integration**: Direct access to your Google Drive folders
- ⚡ **Multi-threading**: Process multiple images simultaneously for faster results
- 💾 **Intelligent Caching**: Save face encodings to avoid reprocessing images
- 📊 **Detailed Results**: Get similarity scores and organized reports
- 🎯 **Configurable Tolerance**: Adjust matching sensitivity to your needs

### Prerequisites
- Python 3.8 or higher
- Google Cloud account with Drive API enabled
- Service account credentials for Google Drive API

**Using PyCharm?** Check out our [PyCharm Setup Guide](PYCHARM_SETUP.md) for IDE-specific instructions.

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/nguongthienTieu/recognise-face.git
cd recognise-face
```

2. **Create and activate virtual environment** (recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Setup Google Drive API

1. **Create a Google Cloud Project**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one

2. **Enable Google Drive API**
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google Drive API"
   - Click "Enable"

3. **Create Service Account**
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "Service Account"
   - Fill in the details and create
   - Click on the created service account
   - Go to "Keys" tab > "Add Key" > "Create New Key"
   - Choose JSON format and download

4. **Configure credentials**
   - Rename the downloaded JSON file to `credentials.json`
   - Place it in the project root directory
   - Or use `credentials.json.example` as a template

5. **Share Google Drive folder with service account**
   - Get the service account email from `credentials.json` (client_email)
   - Share your Google Drive folder with this email address
   - Get the folder ID from the folder URL: `https://drive.google.com/drive/folders/FOLDER_ID_HERE`

**Important Notes for Shared Folders:**
- ✅ **Personal Drive Folders**: Share the folder with the service account email (grant "Viewer" access)
- ✅ **Someone Else's Shared Folder**: Ask the folder owner to share with your service account email
- ✅ **Google Shared Drive (Team Drive)**: Add the service account as a member with "Viewer" access
- 📝 The tool automatically supports all types of drives (personal, shared, team drives)
- 📖 **See [SHARED_FOLDER_GUIDE.md](SHARED_FOLDER_GUIDE.md) for detailed instructions on accessing shared folders**

### Configuration

Edit the `CONFIG` dictionary in `face_search.py`:

```python
CONFIG = {
    'DRIVE_FOLDER_ID': 'your_folder_id_here',  # Google Drive folder ID
    'TARGET_IMAGE_PATH': 'target_person.jpg',   # Your reference photo
    'CREDENTIALS_FILE': 'credentials.json',      # Google Drive API credentials
    'CACHE_FILE': 'face_encodings.cache',       # Cache file for encodings
    'RESULTS_DIR': 'matched_results',            # Results directory
    'TOLERANCE': 0.6,                            # Matching tolerance (lower = stricter)
    'NUM_THREADS': 4,                            # Number of processing threads
    'BATCH_SIZE': 100                            # Images per batch
}
```

**Configuration Parameters:**
- `DRIVE_FOLDER_ID`: The ID of your Google Drive folder containing images
- `TARGET_IMAGE_PATH`: Path to your reference photo (the face you want to find)
- `TOLERANCE`: Face matching tolerance (0.0-1.0, default 0.6)
  - Lower values = more strict matching (fewer false positives)
  - Higher values = more lenient matching (more results but may include false positives)
- `NUM_THREADS`: Number of parallel threads (adjust based on your CPU)

### Usage

1. **Prepare your target image**
   - Place a clear photo of the person you want to find in the project directory
   - Name it `target_person.jpg` or update `TARGET_IMAGE_PATH` in config
   - Make sure the face is clearly visible

2. **Run the search**
```bash
python face_search.py
```

3. **View results**
   - Results are saved in the `matched_results/` directory
   - `results.json`: Detailed JSON data with all matches
   - `report.txt`: Human-readable text report

4. **Additional utilities** (optional)
```bash
# View detailed statistics and top matches
python view_results.py

# Download all matched images from Google Drive
python download_results.py
```

### Results Format

The tool generates two output files:

**results.json**: JSON format with detailed information
```json
[
  {
    "file_id": "google_drive_file_id",
    "file_name": "image_name.jpg",
    "distance": 0.4523,
    "similarity": 54.77
  }
]
```

**report.txt**: Text report with formatted results
```
=== FACE RECOGNITION REPORT ===

Total matches found: 15
Tolerance threshold: 0.6

STT   Filename                                  Similarity      Distance
================================================================================
1     vacation_2023.jpg                        95.23%          0.0477
2     party_photo.jpg                          87.45%          0.1255
...
```

### Performance Tips

- **First Run**: Will be slower as it processes all images
- **Subsequent Runs**: Much faster due to caching
- **Large Datasets**: Increase `NUM_THREADS` for faster processing
- **Memory Issues**: Reduce `NUM_THREADS` or `BATCH_SIZE`
- **Accuracy**: Adjust `TOLERANCE` based on your needs

### Helper Scripts

**view_results.py** - Analyze and view search results
- Display comprehensive statistics
- Show top matches with quality indicators
- Identify low confidence matches
- Export matched file list

**download_results.py** - Download matched images
- Automatically downloads all matched images from Google Drive
- Organizes files with similarity scores in filenames
- Saves to `matched_results/downloaded_images/`

**setup.py** - Interactive setup wizard
- Guides you through initial configuration
- Validates required files and settings
- Helps configure Google Drive folder ID

### Troubleshooting

**No faces detected in target image**
- Ensure the face is clearly visible and well-lit
- Try a different photo with better quality
- Face should be front-facing

**Authentication errors**
- Verify `credentials.json` is in the correct location
- Check that the service account has access to the Drive folder
- Ensure Google Drive API is enabled

**Out of memory errors**
- Reduce `NUM_THREADS` value
- Process images in smaller batches
- Close other memory-intensive applications

---

## Tiếng Việt

### Tổng quan
Công cụ nhận diện khuôn mặt mạnh mẽ có khả năng tìm kiếm và xác định ảnh của bạn trong hơn 10,000 ảnh được lưu trữ trên Google Drive. Công cụ này sử dụng thuật toán nhận diện khuôn mặt tiên tiến để so sánh và tìm kiếm khớp một cách hiệu quả.

### Tính năng
- 🔍 **Nhận diện Thông minh**: Sử dụng thư viện face_recognition với độ chính xác cao
- ☁️ **Tích hợp Google Drive**: Truy cập trực tiếp vào thư mục Google Drive
- ⚡ **Đa luồng**: Xử lý nhiều ảnh đồng thời để có kết quả nhanh hơn
- 💾 **Cache Thông minh**: Lưu encodings để tránh xử lý lại ảnh
- 📊 **Kết quả Chi tiết**: Nhận điểm tương đồng và báo cáo có tổ chức
- 🎯 **Cấu hình Linh hoạt**: Điều chỉnh độ nhạy khớp theo nhu cầu

### Yêu cầu
- Python 3.8 trở lên
- Tài khoản Google Cloud có Drive API được kích hoạt
- Service account credentials cho Google Drive API

**Sử dụng PyCharm?** Xem [Hướng dẫn Cài đặt PyCharm](PYCHARM_SETUP.md) để biết hướng dẫn cụ thể cho IDE.

### Cài đặt

1. **Clone repository**
```bash
git clone https://github.com/nguongthienTieu/recognise-face.git
cd recognise-face
```

2. **Tạo và kích hoạt môi trường ảo** (khuyến nghị)
```bash
python3 -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
```

3. **Cài đặt các thư viện phụ thuộc**
```bash
pip install -r requirements.txt
```

### Thiết lập Google Drive API

1. **Tạo Google Cloud Project**
   - Truy cập [Google Cloud Console](https://console.cloud.google.com/)
   - Tạo project mới hoặc chọn project có sẵn

2. **Kích hoạt Google Drive API**
   - Vào "APIs & Services" > "Library"
   - Tìm kiếm "Google Drive API"
   - Nhấn "Enable"

3. **Tạo Service Account**
   - Vào "APIs & Services" > "Credentials"
   - Nhấn "Create Credentials" > "Service Account"
   - Điền thông tin và tạo
   - Nhấn vào service account vừa tạo
   - Vào tab "Keys" > "Add Key" > "Create New Key"
   - Chọn định dạng JSON và tải về

4. **Cấu hình credentials**
   - Đổi tên file JSON vừa tải về thành `credentials.json`
   - Đặt nó trong thư mục gốc của project
   - Hoặc dùng `credentials.json.example` làm mẫu

5. **Chia sẻ thư mục Google Drive với service account**
   - Lấy email của service account từ `credentials.json` (client_email)
   - Chia sẻ thư mục Google Drive của bạn với email này
   - Lấy folder ID từ URL thư mục: `https://drive.google.com/drive/folders/FOLDER_ID_HERE`

**Lưu ý Quan trọng cho Thư mục Chia sẻ:**
- ✅ **Thư mục Drive Cá nhân**: Chia sẻ thư mục với email service account (cấp quyền "Viewer")
- ✅ **Thư mục của Người khác**: Yêu cầu chủ thư mục chia sẻ với email service account của bạn
- ✅ **Google Shared Drive (Team Drive)**: Thêm service account như thành viên với quyền "Viewer"
- 📝 Công cụ tự động hỗ trợ tất cả loại drive (cá nhân, chia sẻ, team drive)
- 📖 **Xem [SHARED_FOLDER_GUIDE.md](SHARED_FOLDER_GUIDE.md) để biết hướng dẫn chi tiết về truy cập thư mục chia sẻ**

### Cấu hình

Chỉnh sửa dictionary `CONFIG` trong file `face_search.py`:

```python
CONFIG = {
    'DRIVE_FOLDER_ID': 'your_folder_id_here',  # ID thư mục Google Drive
    'TARGET_IMAGE_PATH': 'target_person.jpg',   # Ảnh mẫu của bạn
    'CREDENTIALS_FILE': 'credentials.json',      # File credentials Google Drive API
    'CACHE_FILE': 'face_encodings.cache',       # File cache encodings
    'RESULTS_DIR': 'matched_results',            # Thư mục kết quả
    'TOLERANCE': 0.6,                            # Độ chính xác (càng thấp càng nghiêm ngặt)
    'NUM_THREADS': 4,                            # Số threads xử lý
    'BATCH_SIZE': 100                            # Số ảnh xử lý mỗi batch
}
```

**Các tham số cấu hình:**
- `DRIVE_FOLDER_ID`: ID của thư mục Google Drive chứa ảnh
- `TARGET_IMAGE_PATH`: Đường dẫn đến ảnh mẫu (khuôn mặt bạn muốn tìm)
- `TOLERANCE`: Ngưỡng khớp khuôn mặt (0.0-1.0, mặc định 0.6)
  - Giá trị thấp = khớp nghiêm ngặt hơn (ít kết quả sai)
  - Giá trị cao = khớp dễ dàng hơn (nhiều kết quả nhưng có thể sai)
- `NUM_THREADS`: Số luồng xử lý song song (điều chỉnh dựa trên CPU)

### Sử dụng

1. **Chuẩn bị ảnh mẫu**
   - Đặt một bức ảnh rõ nét của người bạn muốn tìm trong thư mục project
   - Đặt tên là `target_person.jpg` hoặc cập nhật `TARGET_IMAGE_PATH` trong config
   - Đảm bảo khuôn mặt hiện rõ ràng

2. **Chạy tìm kiếm**
```bash
python face_search.py
```

3. **Xem kết quả**
   - Kết quả được lưu trong thư mục `matched_results/`
   - `results.json`: Dữ liệu JSON chi tiết với tất cả kết quả khớp
   - `report.txt`: Báo cáo văn bản dễ đọc

4. **Công cụ bổ sung** (tùy chọn)
```bash
# Xem thống kê chi tiết và top kết quả khớp nhất
python view_results.py

# Tải về tất cả ảnh khớp từ Google Drive
python download_results.py
```

### Định dạng Kết quả

Công cụ tạo ra hai file kết quả:

**results.json**: Định dạng JSON với thông tin chi tiết
```json
[
  {
    "file_id": "google_drive_file_id",
    "file_name": "image_name.jpg",
    "distance": 0.4523,
    "similarity": 54.77
  }
]
```

**report.txt**: Báo cáo văn bản với kết quả được định dạng
```
=== BÁO CÁO TÌM KIẾM KHUÔN MẶT ===

Tổng số ảnh tìm thấy: 15
Ngưỡng độ chính xác: 0.6

STT   Tên file                                  Độ tương đồng   Distance
================================================================================
1     vacation_2023.jpg                        95.23%          0.0477
2     party_photo.jpg                          87.45%          0.1255
...
```

### Mẹo Tối ưu Hiệu suất

- **Lần chạy đầu tiên**: Sẽ chậm hơn vì phải xử lý tất cả ảnh
- **Các lần chạy tiếp theo**: Nhanh hơn nhiều nhờ cache
- **Dataset lớn**: Tăng `NUM_THREADS` để xử lý nhanh hơn
- **Vấn đề bộ nhớ**: Giảm `NUM_THREADS` hoặc `BATCH_SIZE`
- **Độ chính xác**: Điều chỉnh `TOLERANCE` theo nhu cầu

### Công cụ Hỗ trợ

**view_results.py** - Phân tích và xem kết quả
- Hiển thị thống kê toàn diện
- Hiển thị top kết quả khớp với chỉ số chất lượng
- Xác định các kết quả khớp độ tin cậy thấp
- Xuất danh sách file khớp

**download_results.py** - Tải ảnh khớp về
- Tự động tải tất cả ảnh khớp từ Google Drive
- Tổ chức file với điểm tương đồng trong tên file
- Lưu vào `matched_results/downloaded_images/`

**setup.py** - Trình thiết lập tương tác
- Hướng dẫn cấu hình ban đầu
- Kiểm tra các file và thiết lập bắt buộc
- Giúp cấu hình Google Drive folder ID

### Xử lý Sự cố

**Không phát hiện khuôn mặt trong ảnh mẫu**
- Đảm bảo khuôn mặt hiện rõ ràng và đủ ánh sáng
- Thử ảnh khác với chất lượng tốt hơn
- Khuôn mặt nên ở góc nhìn thẳng

**Lỗi xác thực**
- Kiểm tra `credentials.json` ở đúng vị trí
- Kiểm tra service account có quyền truy cập thư mục Drive
- Đảm bảo Google Drive API đã được kích hoạt

**Lỗi hết bộ nhớ**
- Giảm giá trị `NUM_THREADS`
- Xử lý ảnh theo batch nhỏ hơn
- Đóng các ứng dụng tốn bộ nhớ khác

### Giấy phép

MIT License - Xem file LICENSE để biết thêm chi tiết

### Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng tạo issue hoặc pull request.

### Liên hệ

Nếu có câu hỏi hoặc vấn đề, vui lòng tạo issue trên GitHub.

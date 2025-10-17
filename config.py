"""
Configuration file for Face Recognition Search Tool
Customize these settings based on your needs
"""

CONFIG = {
    # Google Drive Settings
    'DRIVE_FOLDER_ID': 'your_folder_id_here',  # ID thư mục Google Drive / Google Drive folder ID
    'CREDENTIALS_FILE': 'credentials.json',     # File credentials Google Drive API
    
    # Face Recognition Settings
    'TARGET_IMAGE_PATH': 'target_person.jpg',   # Ảnh mẫu của bạn / Your reference photo
    'TOLERANCE': 0.6,                           # Độ chính xác: 0.0-1.0 (càng thấp càng nghiêm ngặt)
                                                # Tolerance: 0.0-1.0 (lower = stricter matching)
    
    # Performance Settings
    'NUM_THREADS': 4,                           # Số threads xử lý / Number of processing threads
    'BATCH_SIZE': 100,                          # Số ảnh xử lý mỗi batch / Images per batch
    
    # Cache and Output Settings
    'CACHE_FILE': 'face_encodings.cache',       # File cache encodings
    'RESULTS_DIR': 'matched_results',           # Thư mục kết quả / Results directory
    'ENABLE_CACHE': True,                       # Bật/tắt cache / Enable/disable caching
}

# Advanced Settings (chỉ thay đổi nếu bạn biết mình đang làm gì)
# Advanced Settings (only change if you know what you're doing)
ADVANCED_CONFIG = {
    'MODEL': 'hog',                             # 'hog' (faster, CPU) or 'cnn' (more accurate, GPU)
    'UPSAMPLE_TIMES': 1,                        # Number of times to upsample the image (higher = slower but more accurate)
    'NUM_JITTERS': 1,                           # How many times to re-sample when calculating encoding (higher = more accurate but slower)
}

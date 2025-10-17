# Project Structure / Cấu trúc Project

## File Organization / Tổ chức File

```
recognise-face/
├── README.md                    # Complete documentation / Tài liệu đầy đủ
├── QUICKSTART.md               # Quick start guide / Hướng dẫn nhanh
├── LICENSE                     # MIT License
├── requirements.txt            # Python dependencies / Thư viện Python
├── .gitignore                 # Git ignore rules / Quy tắc Git ignore
│
├── config.py                   # Configuration file / File cấu hình
├── credentials.json.example    # Example credentials / Mẫu credentials
│
├── face_search.py             # Main search engine / Công cụ tìm kiếm chính
├── setup.py                   # Interactive setup wizard / Trình thiết lập
├── view_results.py            # Results viewer & analyzer / Xem & phân tích kết quả
├── download_results.py        # Download matched images / Tải ảnh khớp
│
└── data/
    └── raw/                   # Data directory / Thư mục dữ liệu
```

## Core Files / File Chính

### face_search.py
Main face recognition search engine that:
- Connects to Google Drive API
- Downloads and processes images
- Detects and compares faces
- Generates results with similarity scores

Công cụ tìm kiếm nhận diện khuôn mặt chính:
- Kết nối Google Drive API
- Tải và xử lý ảnh
- Phát hiện và so sánh khuôn mặt
- Tạo kết quả với điểm tương đồng

### config.py
Centralized configuration file containing:
- Google Drive settings
- Face recognition parameters
- Performance tuning options

File cấu hình tập trung chứa:
- Thiết lập Google Drive
- Tham số nhận diện khuôn mặt
- Tùy chọn điều chỉnh hiệu suất

## Utility Scripts / Script Tiện ích

### setup.py
Interactive setup wizard that helps with:
- Checking dependencies
- Configuring Google Drive folder ID
- Validating required files

Trình thiết lập tương tác giúp:
- Kiểm tra thư viện
- Cấu hình Google Drive folder ID
- Kiểm tra các file bắt buộc

### view_results.py
Results analysis tool providing:
- Statistical analysis
- Top matches display
- Quality distribution
- File list export

Công cụ phân tích kết quả cung cấp:
- Phân tích thống kê
- Hiển thị top kết quả khớp
- Phân bố chất lượng
- Xuất danh sách file

### download_results.py
Batch download utility that:
- Downloads all matched images
- Organizes files with similarity scores
- Saves to organized directory

Tiện ích tải hàng loạt:
- Tải tất cả ảnh khớp
- Tổ chức file với điểm tương đồng
- Lưu vào thư mục có tổ chức

## Configuration Files / File Cấu hình

### requirements.txt
Python package dependencies including:
- face_recognition: Core face detection/recognition
- opencv-python: Image processing
- google-api-python-client: Google Drive integration
- tqdm: Progress bars

### .gitignore
Excludes from version control:
- Sensitive files (credentials.json)
- Cache files (*.cache)
- Results directories
- Python artifacts

## Documentation / Tài liệu

### README.md
Comprehensive documentation with:
- Installation instructions
- Google Drive API setup
- Configuration guide
- Usage examples
- Troubleshooting
- Available in English and Vietnamese

### QUICKSTART.md
Quick reference guide for:
- 5-minute setup
- Basic usage
- Common problems

## Generated Files / File được Tạo

These files are generated during usage (not in version control):

**credentials.json** - Your Google Drive API credentials
**target_person.jpg** - Reference photo for face matching
**face_encodings.cache** - Cached face encodings for faster processing

**matched_results/** - Output directory containing:
- `results.json` - Detailed match data
- `report.txt` - Human-readable report
- `matched_files.txt` - List of matched filenames
- `downloaded_images/` - Downloaded matched images

## Workflow / Quy trình

1. **Setup** (one-time)
   ```
   pip install -r requirements.txt
   python setup.py
   ```

2. **Search**
   ```
   python face_search.py
   ```

3. **Analyze**
   ```
   python view_results.py
   ```

4. **Download** (optional)
   ```
   python download_results.py
   ```

## Key Features by File / Tính năng Chính theo File

| File | Purpose | Key Features |
|------|---------|--------------|
| face_search.py | Main engine | Face detection, Google Drive integration, Multi-threading |
| config.py | Configuration | Centralized settings, Easy customization |
| setup.py | Setup wizard | Interactive configuration, Validation |
| view_results.py | Analysis | Statistics, Quality indicators, Export |
| download_results.py | Download | Batch download, File organization |

## Dependencies / Phụ thuộc

- **Python**: 3.8+
- **face_recognition**: Face detection and recognition
- **OpenCV**: Image processing
- **Google API Client**: Drive API integration
- **PIL/Pillow**: Image handling
- **tqdm**: Progress tracking

## License / Giấy phép

MIT License - See LICENSE file for details

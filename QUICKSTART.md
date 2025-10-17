# Quick Start Guide / Hướng dẫn Nhanh

## English Version

### 5-Minute Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Google Drive credentials**
   - Download your `credentials.json` from Google Cloud Console
   - Place it in the project root directory
   - See README.md for detailed instructions

3. **Run setup wizard**
   ```bash
   python setup.py
   ```

4. **Add your target image**
   - Place a photo named `target_person.jpg` in the project directory
   - Make sure the face is clearly visible

5. **Run the search**
   ```bash
   python face_search.py
   ```

6. **Check results**
   - Open `matched_results/report.txt` for a summary
   - Open `matched_results/results.json` for detailed data

### Troubleshooting

**Problem**: "Module not found" errors
**Solution**: Run `pip install -r requirements.txt`

**Problem**: "credentials.json not found"
**Solution**: Follow the Google Drive API setup in README.md

**Problem**: "No faces detected"
**Solution**: Use a clearer photo with good lighting and front-facing pose

---

## Phiên bản Tiếng Việt

### Bắt đầu Nhanh trong 5 Phút

1. **Cài đặt thư viện**
   ```bash
   pip install -r requirements.txt
   ```

2. **Thiết lập Google Drive credentials**
   - Tải file `credentials.json` từ Google Cloud Console
   - Đặt nó trong thư mục gốc của project
   - Xem README.md để biết hướng dẫn chi tiết

3. **Chạy trình thiết lập**
   ```bash
   python setup.py
   ```

4. **Thêm ảnh mẫu của bạn**
   - Đặt một bức ảnh tên là `target_person.jpg` trong thư mục project
   - Đảm bảo khuôn mặt hiện rõ ràng

5. **Chạy tìm kiếm**
   ```bash
   python face_search.py
   ```

6. **Kiểm tra kết quả**
   - Mở `matched_results/report.txt` để xem tóm tắt
   - Mở `matched_results/results.json` để xem dữ liệu chi tiết

### Xử lý Sự cố

**Vấn đề**: Lỗi "Module not found"
**Giải pháp**: Chạy `pip install -r requirements.txt`

**Vấn đề**: "credentials.json not found"
**Giải pháp**: Làm theo hướng dẫn thiết lập Google Drive API trong README.md

**Vấn đề**: "No faces detected"
**Giải pháp**: Dùng ảnh rõ hơn với ánh sáng tốt và góc nhìn thẳng

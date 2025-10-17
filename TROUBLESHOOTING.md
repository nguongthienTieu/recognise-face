# Troubleshooting Guide / Hướng dẫn Xử lý Sự cố

## Common Issues / Các Vấn đề Thường gặp

### 1. Installation Issues / Vấn đề Cài đặt

#### Problem: `ModuleNotFoundError: No module named 'face_recognition'`
**English:**
- **Cause**: Dependencies not installed
- **Solution**: 
  ```bash
  pip install -r requirements.txt
  ```
- **Note**: face_recognition requires dlib, which needs C++ build tools. On Windows, you may need Visual Studio Build Tools.

**Tiếng Việt:**
- **Nguyên nhân**: Chưa cài đặt thư viện
- **Giải pháp**: 
  ```bash
  pip install -r requirements.txt
  ```
- **Lưu ý**: face_recognition cần dlib, yêu cầu công cụ build C++. Trên Windows, bạn có thể cần Visual Studio Build Tools.

---

#### Problem: `ImportError: No module named 'cv2'`
**English:**
- **Cause**: OpenCV not installed properly
- **Solution**: 
  ```bash
  pip uninstall opencv-python
  pip install opencv-python
  ```

**Tiếng Việt:**
- **Nguyên nhân**: OpenCV chưa được cài đúng
- **Giải pháp**: 
  ```bash
  pip uninstall opencv-python
  pip install opencv-python
  ```

---

### 2. Google Drive API Issues / Vấn đề Google Drive API

#### Problem: `FileNotFoundError: credentials.json not found`
**English:**
- **Cause**: Missing credentials file
- **Solution**: 
  1. Go to Google Cloud Console
  2. Create a service account
  3. Download JSON key
  4. Save as `credentials.json` in project root
- **See**: README.md "Setup Google Drive API" section

**Tiếng Việt:**
- **Nguyên nhân**: Thiếu file credentials
- **Giải pháp**: 
  1. Vào Google Cloud Console
  2. Tạo service account
  3. Tải JSON key
  4. Lưu thành `credentials.json` trong thư mục gốc
- **Xem**: phần "Thiết lập Google Drive API" trong README.md

---

#### Problem: `403 Forbidden` or `Permission denied`
**English:**
- **Cause**: Service account doesn't have access to the folder
- **Solution**: 
  1. Open your Google Drive folder
  2. Click "Share"
  3. Add the service account email (from credentials.json)
  4. Grant "Viewer" access

**Tiếng Việt:**
- **Nguyên nhân**: Service account không có quyền truy cập thư mục
- **Giải pháp**: 
  1. Mở thư mục Google Drive của bạn
  2. Nhấn "Chia sẻ"
  3. Thêm email service account (từ credentials.json)
  4. Cấp quyền "Viewer"

---

#### Problem: `Invalid folder ID`
**English:**
- **Cause**: Wrong folder ID in config
- **Solution**: 
  1. Open folder in Google Drive
  2. Copy the ID from URL: `https://drive.google.com/drive/folders/FOLDER_ID_HERE`
  3. Update `DRIVE_FOLDER_ID` in config.py

**Tiếng Việt:**
- **Nguyên nhân**: Folder ID sai trong config
- **Giải pháp**: 
  1. Mở thư mục trong Google Drive
  2. Sao chép ID từ URL: `https://drive.google.com/drive/folders/FOLDER_ID_HERE`
  3. Cập nhật `DRIVE_FOLDER_ID` trong config.py

---

### 3. Face Recognition Issues / Vấn đề Nhận diện Khuôn mặt

#### Problem: `No faces detected in target image`
**English:**
- **Cause**: Face not visible or poor image quality
- **Solutions**:
  1. Use a clear, well-lit photo
  2. Ensure face is front-facing
  3. Make sure face is not too small in the image
  4. Try a different photo
- **Test**: 
  ```python
  import face_recognition
  img = face_recognition.load_image_file('target_person.jpg')
  faces = face_recognition.face_locations(img)
  print(f"Found {len(faces)} face(s)")
  ```

**Tiếng Việt:**
- **Nguyên nhân**: Khuôn mặt không rõ hoặc chất lượng ảnh kém
- **Giải pháp**:
  1. Dùng ảnh rõ nét, ánh sáng tốt
  2. Đảm bảo khuôn mặt nhìn thẳng
  3. Khuôn mặt không quá nhỏ trong ảnh
  4. Thử ảnh khác
- **Kiểm tra**: 
  ```python
  import face_recognition
  img = face_recognition.load_image_file('target_person.jpg')
  faces = face_recognition.face_locations(img)
  print(f"Tìm thấy {len(faces)} khuôn mặt")
  ```

---

#### Problem: `No matches found` or `Too few results`
**English:**
- **Cause**: Tolerance too strict
- **Solution**: Increase tolerance in config.py
  ```python
  CONFIG = {
      'TOLERANCE': 0.7,  # Try 0.7 or 0.8 instead of 0.6
  }
  ```
- **Recommendation**: Start with 0.6, adjust based on results

**Tiếng Việt:**
- **Nguyên nhân**: Tolerance quá nghiêm ngặt
- **Giải pháp**: Tăng tolerance trong config.py
  ```python
  CONFIG = {
      'TOLERANCE': 0.7,  # Thử 0.7 hoặc 0.8 thay vì 0.6
  }
  ```
- **Khuyến nghị**: Bắt đầu với 0.6, điều chỉnh theo kết quả

---

#### Problem: `Too many false positives` (wrong faces matched)
**English:**
- **Cause**: Tolerance too lenient
- **Solution**: Decrease tolerance in config.py
  ```python
  CONFIG = {
      'TOLERANCE': 0.5,  # Try 0.5 or 0.4 instead of 0.6
  }
  ```
- **Note**: Lower tolerance = stricter matching

**Tiếng Việt:**
- **Nguyên nhân**: Tolerance quá dễ dàng
- **Giải pháp**: Giảm tolerance trong config.py
  ```python
  CONFIG = {
      'TOLERANCE': 0.5,  # Thử 0.5 hoặc 0.4 thay vì 0.6
  }
  ```
- **Lưu ý**: Tolerance thấp hơn = khớp nghiêm ngặt hơn

---

### 4. Performance Issues / Vấn đề Hiệu suất

#### Problem: `Process is very slow`
**English:**
- **Causes & Solutions**:
  1. **First run is always slow** - This is normal, cache will speed up future runs
  2. **Enable caching**: 
     ```python
     CONFIG['ENABLE_CACHE'] = True
     ```
  3. **Increase threads** (if you have powerful CPU):
     ```python
     CONFIG['NUM_THREADS'] = 8  # Adjust based on your CPU
     ```
  4. **Check internet speed** - Downloading images requires good bandwidth

**Tiếng Việt:**
- **Nguyên nhân & Giải pháp**:
  1. **Lần chạy đầu luôn chậm** - Đây là bình thường, cache sẽ tăng tốc các lần chạy sau
  2. **Bật caching**: 
     ```python
     CONFIG['ENABLE_CACHE'] = True
     ```
  3. **Tăng threads** (nếu có CPU mạnh):
     ```python
     CONFIG['NUM_THREADS'] = 8  # Điều chỉnh theo CPU của bạn
     ```
  4. **Kiểm tra tốc độ internet** - Tải ảnh cần băng thông tốt

---

#### Problem: `MemoryError` or system freezes
**English:**
- **Cause**: Too many concurrent processes
- **Solutions**:
  ```python
  CONFIG['NUM_THREADS'] = 2      # Reduce threads
  CONFIG['BATCH_SIZE'] = 50      # Smaller batches
  ```
- **Also**: Close other applications to free up memory

**Tiếng Việt:**
- **Nguyên nhân**: Quá nhiều tiến trình đồng thời
- **Giải pháp**:
  ```python
  CONFIG['NUM_THREADS'] = 2      # Giảm threads
  CONFIG['BATCH_SIZE'] = 50      # Batch nhỏ hơn
  ```
- **Ngoài ra**: Đóng các ứng dụng khác để giải phóng bộ nhớ

---

### 5. Cache Issues / Vấn đề Cache

#### Problem: `Getting outdated results`
**English:**
- **Cause**: Cache contains old data
- **Solution**: Clear cache and rerun
  ```bash
  rm face_encodings.cache
  python face_search.py
  ```

**Tiếng Việt:**
- **Nguyên nhân**: Cache chứa dữ liệu cũ
- **Giải pháp**: Xóa cache và chạy lại
  ```bash
  rm face_encodings.cache
  python face_search.py
  ```

---

#### Problem: `Cannot load cache` or `Corrupt cache file`
**English:**
- **Solution**: Delete cache and rebuild
  ```bash
  rm face_encodings.cache
  ```
- **Note**: Next run will be slower as cache rebuilds

**Tiếng Việt:**
- **Giải pháp**: Xóa cache và tạo lại
  ```bash
  rm face_encodings.cache
  ```
- **Lưu ý**: Lần chạy tiếp theo sẽ chậm hơn vì cache được tạo lại

---

### 6. Results Issues / Vấn đề Kết quả

#### Problem: `Cannot create results directory`
**English:**
- **Cause**: Permission issues
- **Solutions**:
  1. Check write permissions
  2. Run with appropriate privileges
  3. Change results directory in config:
     ```python
     CONFIG['RESULTS_DIR'] = '/path/to/writable/dir'
     ```

**Tiếng Việt:**
- **Nguyên nhân**: Vấn đề quyền truy cập
- **Giải pháp**:
  1. Kiểm tra quyền ghi
  2. Chạy với quyền phù hợp
  3. Đổi thư mục kết quả trong config:
     ```python
     CONFIG['RESULTS_DIR'] = '/đường/dẫn/có/thể/ghi'
     ```

---

### 7. Image Download Issues / Vấn đề Tải ảnh

#### Problem: `Failed to download some images`
**English:**
- **Causes**:
  1. Network timeout
  2. Image is corrupted in Google Drive
  3. Image format not supported
- **Solutions**:
  - Retry the download: `python download_results.py`
  - Check individual files in Google Drive
  - Skip problematic files (they're reported in output)

**Tiếng Việt:**
- **Nguyên nhân**:
  1. Timeout mạng
  2. Ảnh bị lỗi trong Google Drive
  3. Định dạng ảnh không được hỗ trợ
- **Giải pháp**:
  - Thử tải lại: `python download_results.py`
  - Kiểm tra từng file trong Google Drive
  - Bỏ qua các file có vấn đề (được báo trong output)

---

## Getting Help / Nhận Trợ giúp

### Check Logs / Kiểm tra Logs
**English:** Look at the console output for error messages and stack traces.

**Tiếng Việt:** Xem output console để tìm thông báo lỗi và stack trace.

### Debug Mode / Chế độ Debug
**English:** Add print statements or use Python debugger:
```python
import pdb; pdb.set_trace()  # Add breakpoint
```

**Tiếng Việt:** Thêm print statements hoặc dùng Python debugger:
```python
import pdb; pdb.set_trace()  # Thêm breakpoint
```

### Create Issue / Tạo Issue
**English:** If problem persists, create an issue on GitHub with:
- Error message
- Steps to reproduce
- Your configuration (remove sensitive data)
- Python version and OS

**Tiếng Việt:** Nếu vấn đề vẫn còn, tạo issue trên GitHub với:
- Thông báo lỗi
- Các bước tái hiện
- Cấu hình của bạn (xóa dữ liệu nhạy cảm)
- Phiên bản Python và hệ điều hành

---

## Prevention Tips / Mẹo Phòng ngừa

### Before First Run / Trước khi Chạy lần đầu
1. ✅ Install all dependencies
2. ✅ Setup Google Drive API correctly
3. ✅ Test with small folder first (10-20 images)
4. ✅ Use clear target image

### Regular Maintenance / Bảo trì Định kỳ
1. Clear cache monthly
2. Update dependencies: `pip install -r requirements.txt --upgrade`
3. Backup results regularly
4. Monitor disk space for cache

### Best Practices / Thực hành Tốt nhất
1. Keep target images in separate folder
2. Use descriptive result directory names
3. Document your tolerance settings
4. Backup credentials.json securely

# Accessing Shared Folders Guide / Hướng dẫn Truy cập Thư mục Chia sẻ

[English](#english) | [Tiếng Việt](#tiếng-việt)

---

## English

### Overview
The Face Recognition Search Tool now fully supports accessing Google Drive folders that are shared with you, including:
- ✅ Your own personal Google Drive folders
- ✅ Folders shared by others (regular shared folders)
- ✅ Google Shared Drives (Team Drives)

**No configuration changes needed!** The tool automatically detects and works with all drive types.

### How to Access Someone Else's Shared Folder

#### Step 1: Get the Service Account Email
1. Open your `credentials.json` file
2. Find the `client_email` field
3. Copy the email address (looks like: `your-service-account@project-id.iam.gserviceaccount.com`)

#### Step 2: Request Access from Folder Owner
Ask the person who owns the folder to share it with you:

**For Regular Shared Folders:**
1. Have them open the folder in Google Drive
2. Click the "Share" button (or right-click → Share)
3. Add your service account email address
4. Grant at least "Viewer" access
5. Click "Send" or "Done"

**For Google Shared Drives (Team Drives):**
1. Have the Shared Drive admin open the drive
2. Click the settings icon (⚙️) → "Manage members"
3. Add your service account email as a member
4. Grant at least "Viewer" access
5. Click "Send"

#### Step 3: Get the Folder ID
1. Open the shared folder in your Google Drive (after it's been shared)
2. Copy the folder ID from the URL:
   ```
   https://drive.google.com/drive/folders/FOLDER_ID_HERE
   ```
3. Update the `DRIVE_FOLDER_ID` in your `config.py`:
   ```python
   CONFIG = {
       'DRIVE_FOLDER_ID': 'the-folder-id-you-copied',
       ...
   }
   ```

#### Step 4: Run the Tool
```bash
python face_search.py
```

The tool will automatically detect whether the folder is:
- In your personal drive
- Shared with you by someone else
- In a Google Shared Drive (Team Drive)

### Troubleshooting Shared Folder Access

**Problem: "Permission denied" or "403 Forbidden"**
- **Solution**: The service account doesn't have access to the folder
  - Verify the folder was shared with the correct email (service account email from credentials.json)
  - Check that at least "Viewer" permission was granted
  - For Shared Drives, ensure the service account was added as a member

**Problem: "Folder not found" or "Invalid folder ID"**
- **Solution**: 
  - Double-check the folder ID in config.py
  - Make sure you copied the entire ID from the URL
  - Verify you can see the folder in your Google Drive web interface

**Problem: "No files found" in a shared folder**
- **Solution**:
  - Verify the folder actually contains image files
  - Check that images have the correct MIME types (jpg, png, etc.)
  - Try accessing the folder directly through Google Drive to confirm images are visible

### Technical Details

The tool now uses these Google Drive API v3 parameters:
- `supportsAllDrives=True` - Enables access to Shared Drives
- `includeItemsFromAllDrives=True` - Includes items from all drives in results
- `corpora='allDrives'` - Searches across all drives the service account can access

These parameters are automatically applied to all Drive API calls, so no manual configuration is needed.

---

## Tiếng Việt

### Tổng quan
Công cụ Tìm kiếm Nhận diện Khuôn mặt giờ đây hỗ trợ đầy đủ việc truy cập các thư mục Google Drive được chia sẻ với bạn, bao gồm:
- ✅ Thư mục Google Drive cá nhân của bạn
- ✅ Thư mục được chia sẻ bởi người khác (thư mục chia sẻ thông thường)
- ✅ Google Shared Drive (Team Drive)

**Không cần thay đổi cấu hình!** Công cụ tự động phát hiện và hoạt động với tất cả các loại drive.

### Cách Truy cập Thư mục Chia sẻ của Người khác

#### Bước 1: Lấy Email Service Account
1. Mở file `credentials.json` của bạn
2. Tìm trường `client_email`
3. Sao chép địa chỉ email (có dạng: `your-service-account@project-id.iam.gserviceaccount.com`)

#### Bước 2: Yêu cầu Quyền Truy cập từ Chủ Thư mục
Yêu cầu người sở hữu thư mục chia sẻ nó với bạn:

**Đối với Thư mục Chia sẻ Thông thường:**
1. Họ mở thư mục trong Google Drive
2. Nhấn nút "Chia sẻ" (hoặc nhấp chuột phải → Chia sẻ)
3. Thêm địa chỉ email service account của bạn
4. Cấp ít nhất quyền "Viewer" (Người xem)
5. Nhấn "Gửi" hoặc "Xong"

**Đối với Google Shared Drive (Team Drive):**
1. Admin của Shared Drive mở drive
2. Nhấn biểu tượng cài đặt (⚙️) → "Quản lý thành viên"
3. Thêm email service account của bạn như thành viên
4. Cấp ít nhất quyền "Viewer" (Người xem)
5. Nhấn "Gửi"

#### Bước 3: Lấy Folder ID
1. Mở thư mục được chia sẻ trong Google Drive của bạn (sau khi được chia sẻ)
2. Sao chép folder ID từ URL:
   ```
   https://drive.google.com/drive/folders/FOLDER_ID_HERE
   ```
3. Cập nhật `DRIVE_FOLDER_ID` trong file `config.py`:
   ```python
   CONFIG = {
       'DRIVE_FOLDER_ID': 'folder-id-bạn-đã-sao-chép',
       ...
   }
   ```

#### Bước 4: Chạy Công cụ
```bash
python face_search.py
```

Công cụ sẽ tự động phát hiện xem thư mục là:
- Trong drive cá nhân của bạn
- Được chia sẻ với bạn bởi người khác
- Trong Google Shared Drive (Team Drive)

### Xử lý Sự cố Truy cập Thư mục Chia sẻ

**Vấn đề: "Permission denied" hoặc "403 Forbidden"**
- **Giải pháp**: Service account không có quyền truy cập thư mục
  - Xác minh thư mục đã được chia sẻ với đúng email (email service account từ credentials.json)
  - Kiểm tra đã cấp ít nhất quyền "Viewer"
  - Đối với Shared Drive, đảm bảo service account đã được thêm như thành viên

**Vấn đề: "Folder not found" hoặc "Invalid folder ID"**
- **Giải pháp**: 
  - Kiểm tra lại folder ID trong config.py
  - Đảm bảo bạn đã sao chép toàn bộ ID từ URL
  - Xác minh bạn có thể thấy thư mục trong giao diện web Google Drive

**Vấn đề: "No files found" trong thư mục chia sẻ**
- **Giải pháp**:
  - Xác minh thư mục thực sự chứa file ảnh
  - Kiểm tra ảnh có đúng định dạng (jpg, png, v.v.)
  - Thử truy cập thư mục trực tiếp qua Google Drive để xác nhận ảnh hiển thị

### Chi tiết Kỹ thuật

Công cụ hiện sử dụng các tham số Google Drive API v3 sau:
- `supportsAllDrives=True` - Cho phép truy cập Shared Drive
- `includeItemsFromAllDrives=True` - Bao gồm các mục từ tất cả drive trong kết quả
- `corpora='allDrives'` - Tìm kiếm trên tất cả drive mà service account có thể truy cập

Các tham số này được tự động áp dụng cho tất cả lệnh gọi Drive API, nên không cần cấu hình thủ công.

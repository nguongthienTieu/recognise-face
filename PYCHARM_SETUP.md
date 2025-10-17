# PyCharm Setup Guide / Hướng dẫn Cài đặt PyCharm

[English](#english) | [Tiếng Việt](#tiếng-việt)

---

## English

### Prerequisites
- PyCharm IDE (Community or Professional Edition)
- Python 3.8 or higher installed on your system

### Setting Up the Project in PyCharm

#### 1. Open the Project
1. Open PyCharm
2. Click **File** → **Open**
3. Navigate to the `recognise-face` directory and select it
4. Click **OK**

#### 2. Configure Python Interpreter

##### Option A: Create New Virtual Environment (Recommended)
1. Go to **File** → **Settings** (or **PyCharm** → **Preferences** on macOS)
2. Navigate to **Project: recognise-face** → **Python Interpreter**
3. Click the gear icon ⚙️ → **Add**
4. Select **Virtualenv Environment**
5. Choose **New environment**
6. Set location to: `<project_dir>/venv`
7. Base interpreter: Select your Python 3.8+ installation
8. Check **Inherit global site-packages** if needed
9. Click **OK**

##### Option B: Use Existing Virtual Environment
1. If you already have a `venv` directory:
   - Go to **File** → **Settings** → **Project** → **Python Interpreter**
   - Click the gear icon ⚙️ → **Add**
   - Select **Virtualenv Environment** → **Existing environment**
   - Click the folder icon and navigate to `venv/bin/python` (Linux/Mac) or `venv\Scripts\python.exe` (Windows)
   - Click **OK**

#### 3. Install Dependencies
Once the interpreter is configured:

1. Open the **Terminal** tab at the bottom of PyCharm
2. The virtual environment should be activated automatically (you'll see `(venv)` in the prompt)
3. Run:
   ```bash
   pip install -r requirements.txt
   ```

Alternatively, PyCharm may show a banner at the top of `requirements.txt` offering to install dependencies - you can click **Install requirements**.

#### 4. Configure Google Drive API
1. Follow the Google Drive API setup instructions in [README.md](README.md)
2. Place your `credentials.json` file in the project root directory
3. PyCharm will automatically detect it in the project structure

#### 5. Using Pre-configured Run Configurations

The project includes ready-to-use run configurations:

##### **Setup** (First-time setup)
- Click the **Run Configuration** dropdown (top right)
- Select **Setup**
- Click the green play button ▶️
- Follow the interactive prompts to configure your project

##### **Face Search** (Main application)
- Select **Face Search** from the run configurations
- Make sure you have:
  - `credentials.json` in the project root
  - `target_person.jpg` (or configured image) in the project root
  - Updated `config.py` with your Google Drive folder ID
- Click the green play button ▶️

##### **View Results** (Analyze search results)
- Run this after **Face Search** completes
- Select **View Results** from run configurations
- Click the green play button ▶️

##### **Download Results** (Download matched images)
- Select **Download Results** from run configurations
- Click the green play button ▶️

#### 6. Creating Custom Run Configurations (Optional)

If you need to create additional configurations:

1. Go to **Run** → **Edit Configurations**
2. Click **+** → **Python**
3. Configure:
   - **Name**: Your configuration name
   - **Script path**: Select the Python file to run
   - **Working directory**: Set to `$PROJECT_DIR$`
   - **Python interpreter**: Should use the project interpreter
4. Click **OK**

#### 7. Debugging

To debug any script:
1. Set breakpoints by clicking in the gutter (left of line numbers)
2. Select the desired run configuration
3. Click the bug icon 🐛 instead of the play button
4. Use the debug panel to step through code, inspect variables, etc.

### PyCharm Tips for This Project

#### Code Navigation
- **Ctrl+Click** (or **Cmd+Click** on macOS) on any function/class to jump to its definition
- **Ctrl+B** to go to declaration
- **Alt+F7** to find usages

#### Terminal Usage
- The integrated terminal automatically activates your virtual environment
- Split terminals: right-click on terminal tab → **Split Right** or **Split Down**

#### Project Structure
- Use the **Project** tool window (left sidebar) to navigate files
- Excluded folders (like `venv`, `matched_results`) are marked in brown

#### Version Control
- The **Git** tool window (bottom) shows changes
- **Ctrl+K** for quick commit
- **Ctrl+Shift+K** for push

### Troubleshooting

**Issue**: "No module named 'face_recognition'"
**Solution**: 
- Make sure you've selected the correct Python interpreter with dependencies installed
- Try reinstalling: `pip install -r requirements.txt`

**Issue**: Run configurations not appearing
**Solution**:
- Go to **Run** → **Edit Configurations**
- The configurations should be listed under **Python**
- If missing, the `.idea/runConfigurations/*.xml` files may not have been loaded correctly

**Issue**: "Python interpreter not configured"
**Solution**:
- Follow step 2 above to configure the Python interpreter
- Restart PyCharm if needed

---

## Tiếng Việt

### Yêu cầu
- PyCharm IDE (Community hoặc Professional Edition)
- Python 3.8 trở lên đã cài đặt trên hệ thống

### Thiết lập Project trong PyCharm

#### 1. Mở Project
1. Mở PyCharm
2. Nhấn **File** → **Open**
3. Điều hướng đến thư mục `recognise-face` và chọn nó
4. Nhấn **OK**

#### 2. Cấu hình Python Interpreter

##### Tùy chọn A: Tạo Virtual Environment Mới (Khuyến nghị)
1. Vào **File** → **Settings** (hoặc **PyCharm** → **Preferences** trên macOS)
2. Điều hướng đến **Project: recognise-face** → **Python Interpreter**
3. Nhấn biểu tượng bánh răng ⚙️ → **Add**
4. Chọn **Virtualenv Environment**
5. Chọn **New environment**
6. Đặt vị trí là: `<thư_mục_project>/venv`
7. Base interpreter: Chọn Python 3.8+ của bạn
8. Đánh dấu **Inherit global site-packages** nếu cần
9. Nhấn **OK**

##### Tùy chọn B: Sử dụng Virtual Environment Có sẵn
1. Nếu bạn đã có thư mục `venv`:
   - Vào **File** → **Settings** → **Project** → **Python Interpreter**
   - Nhấn biểu tượng bánh răng ⚙️ → **Add**
   - Chọn **Virtualenv Environment** → **Existing environment**
   - Nhấn biểu tượng thư mục và điều hướng đến `venv/bin/python` (Linux/Mac) hoặc `venv\Scripts\python.exe` (Windows)
   - Nhấn **OK**

#### 3. Cài đặt Dependencies
Sau khi cấu hình interpreter:

1. Mở tab **Terminal** ở dưới cùng của PyCharm
2. Virtual environment sẽ tự động được kích hoạt (bạn sẽ thấy `(venv)` trong prompt)
3. Chạy:
   ```bash
   pip install -r requirements.txt
   ```

Ngoài ra, PyCharm có thể hiển thị banner ở đầu file `requirements.txt` đề nghị cài đặt dependencies - bạn có thể nhấn **Install requirements**.

#### 4. Cấu hình Google Drive API
1. Làm theo hướng dẫn thiết lập Google Drive API trong [README.md](README.md)
2. Đặt file `credentials.json` trong thư mục gốc của project
3. PyCharm sẽ tự động phát hiện nó trong cấu trúc project

#### 5. Sử dụng Run Configurations Có sẵn

Project đã bao gồm các run configurations sẵn sàng sử dụng:

##### **Setup** (Thiết lập lần đầu)
- Nhấn vào dropdown **Run Configuration** (góc trên bên phải)
- Chọn **Setup**
- Nhấn nút play màu xanh ▶️
- Làm theo các hướng dẫn tương tác để cấu hình project

##### **Face Search** (Ứng dụng chính)
- Chọn **Face Search** từ run configurations
- Đảm bảo bạn có:
  - `credentials.json` trong thư mục gốc project
  - `target_person.jpg` (hoặc ảnh đã cấu hình) trong thư mục gốc
  - Đã cập nhật `config.py` với Google Drive folder ID của bạn
- Nhấn nút play màu xanh ▶️

##### **View Results** (Phân tích kết quả tìm kiếm)
- Chạy sau khi **Face Search** hoàn thành
- Chọn **View Results** từ run configurations
- Nhấn nút play màu xanh ▶️

##### **Download Results** (Tải ảnh khớp về)
- Chọn **Download Results** từ run configurations
- Nhấn nút play màu xanh ▶️

#### 6. Tạo Custom Run Configurations (Tùy chọn)

Nếu bạn cần tạo thêm configurations:

1. Vào **Run** → **Edit Configurations**
2. Nhấn **+** → **Python**
3. Cấu hình:
   - **Name**: Tên configuration của bạn
   - **Script path**: Chọn file Python cần chạy
   - **Working directory**: Đặt là `$PROJECT_DIR$`
   - **Python interpreter**: Nên sử dụng interpreter của project
4. Nhấn **OK**

#### 7. Debug

Để debug bất kỳ script nào:
1. Đặt breakpoints bằng cách nhấn vào gutter (bên trái số dòng)
2. Chọn run configuration mong muốn
3. Nhấn biểu tượng bug 🐛 thay vì nút play
4. Sử dụng debug panel để bước qua code, kiểm tra biến, v.v.

### Mẹo PyCharm cho Project này

#### Điều hướng Code
- **Ctrl+Click** (hoặc **Cmd+Click** trên macOS) trên bất kỳ function/class nào để nhảy đến định nghĩa
- **Ctrl+B** để đi đến khai báo
- **Alt+F7** để tìm usages

#### Sử dụng Terminal
- Terminal tích hợp tự động kích hoạt virtual environment
- Chia terminal: nhấn chuột phải vào tab terminal → **Split Right** hoặc **Split Down**

#### Cấu trúc Project
- Sử dụng cửa sổ công cụ **Project** (thanh bên trái) để điều hướng files
- Các thư mục bị loại trừ (như `venv`, `matched_results`) được đánh dấu màu nâu

#### Version Control
- Cửa sổ công cụ **Git** (dưới cùng) hiển thị các thay đổi
- **Ctrl+K** để commit nhanh
- **Ctrl+Shift+K** để push

### Xử lý Sự cố

**Vấn đề**: "No module named 'face_recognition'"
**Giải pháp**: 
- Đảm bảo bạn đã chọn đúng Python interpreter với dependencies đã cài đặt
- Thử cài đặt lại: `pip install -r requirements.txt`

**Vấn đề**: Run configurations không hiển thị
**Giải pháp**:
- Vào **Run** → **Edit Configurations**
- Các configurations nên được liệt kê trong **Python**
- Nếu thiếu, các file `.idea/runConfigurations/*.xml` có thể chưa được load đúng

**Vấn đề**: "Python interpreter not configured"
**Giải pháp**:
- Làm theo bước 2 ở trên để cấu hình Python interpreter
- Khởi động lại PyCharm nếu cần

# Usage Examples / Ví dụ Sử dụng

## Example 1: Basic Search / Tìm kiếm Cơ bản

### Scenario / Kịch bản
You have 10,000 photos on Google Drive and want to find all photos containing your face.
/ Bạn có 10,000 ảnh trên Google Drive và muốn tìm tất cả ảnh có khuôn mặt của mình.

### Steps / Các bước

```bash
# 1. Install dependencies / Cài đặt thư viện
pip install -r requirements.txt

# 2. Run setup / Chạy thiết lập
python setup.py
# Enter your Google Drive folder ID when prompted
# Nhập Google Drive folder ID khi được yêu cầu

# 3. Add your target image / Thêm ảnh mẫu
# Place your photo as target_person.jpg
# Đặt ảnh của bạn với tên target_person.jpg

# 4. Run the search / Chạy tìm kiếm
python face_search.py
```

### Expected Output / Kết quả mong đợi
```
============================================================
🔎 FACE RECOGNITION SEARCH ENGINE
============================================================
✓ Đã kết nối Google Drive API
✓ Đã load ảnh mẫu: target_person.jpg
✓ Đã load 5432 encodings từ cache
📁 Đang quét thư mục Google Drive...
✓ Tìm thấy 10000 ảnh

🔍 Bắt đầu tìm kiếm với 4 threads...
Xử lý ảnh: 100%|████████████████████| 10000/10000 [15:23<00:00, 10.83ảnh/s]

✓ Đã lưu 10000 encodings vào cache
✓ Đã lưu kết quả vào thư mục: matched_results

🎉 Hoàn thành! Tìm thấy 127 ảnh khớp
```

---

## Example 2: Adjusting Tolerance / Điều chỉnh Độ chính xác

### Problem / Vấn đề
Too many false positives (wrong faces matched)
/ Quá nhiều kết quả sai (khuôn mặt không đúng được khớp)

### Solution / Giải pháp

Edit `config.py`:
```python
CONFIG = {
    # ... other settings ...
    'TOLERANCE': 0.5,  # Changed from 0.6 to 0.5 (stricter)
                       # Thay đổi từ 0.6 sang 0.5 (nghiêm ngặt hơn)
}
```

**Tolerance Guide / Hướng dẫn Tolerance:**
- `0.4`: Very strict - Only very similar faces / Rất nghiêm ngặt - Chỉ khuôn mặt rất giống
- `0.5`: Strict - Good for exact matches / Nghiêm ngặt - Tốt cho khớp chính xác
- `0.6`: Default - Balanced / Mặc định - Cân bằng
- `0.7`: Lenient - More results / Dễ dàng - Nhiều kết quả hơn
- `0.8`: Very lenient - Many results / Rất dễ dàng - Rất nhiều kết quả

---

## Example 3: Analyzing Results / Phân tích Kết quả

### After Search / Sau khi Tìm kiếm

```bash
# View detailed statistics / Xem thống kê chi tiết
python view_results.py
```

### Output / Kết quả
```
============================================================
SEARCH RESULTS STATISTICS
============================================================

Total matches: 127
Tolerance used: 0.6

------------------------------------------------------------
SIMILARITY SCORES
------------------------------------------------------------
Average: 82.45%
Highest: 97.23%
Lowest:  61.12%

------------------------------------------------------------
QUALITY DISTRIBUTION
------------------------------------------------------------
Excellent (≥90%): 23 images (18.1%)
Good (80-89%):    67 images (52.8%)
Fair (70-79%):    28 images (22.0%)
Poor (<70%):      9 images (7.1%)

============================================================
TOP 15 MATCHES
============================================================

Rank   Similarity   Distance    Filename
------------------------------------------------------------
1      97.23% 🟢   0.0277      vacation_beach_2023.jpg
2      95.88% 🟢   0.0412      birthday_party.jpg
3      94.56% 🟢   0.0544      wedding_photo.jpg
...
```

---

## Example 4: Downloading Matched Images / Tải Ảnh Khớp

### Scenario / Kịch bản
You want to download all matched images to your local machine
/ Bạn muốn tải tất cả ảnh khớp về máy của mình

```bash
python download_results.py
```

### Output / Kết quả
```
============================================================
DOWNLOAD MATCHED IMAGES
============================================================
✓ Loaded 127 matched images
✓ Download directory: matched_results/downloaded_images
✓ Connected to Google Drive API

📥 Downloading 127 images...
Downloading: 100%|████████████████████| 127/127 [02:45<00:00,  1.30s/image]

✓ Successfully downloaded 127/127 images
✓ Images saved to: matched_results/downloaded_images
```

**Downloaded Files / File đã Tải:**
```
matched_results/downloaded_images/
├── vacation_beach_2023_sim97.2.jpg
├── birthday_party_sim95.9.jpg
├── wedding_photo_sim94.6.jpg
└── ...
```

---

## Example 5: Large Dataset Processing / Xử lý Dataset Lớn

### Scenario / Kịch bản
You have 50,000+ images and want to optimize performance
/ Bạn có 50,000+ ảnh và muốn tối ưu hiệu suất

### Configuration / Cấu hình

Edit `config.py`:
```python
CONFIG = {
    # ... other settings ...
    'NUM_THREADS': 8,      # Increase if you have powerful CPU
                           # Tăng nếu bạn có CPU mạnh
    'BATCH_SIZE': 200,     # Larger batches for more memory
                           # Batch lớn hơn cho nhiều bộ nhớ hơn
    'ENABLE_CACHE': True,  # Essential for large datasets
                           # Quan trọng cho dataset lớn
}
```

### First Run / Lần chạy đầu
```bash
python face_search.py
# Will take longer (30-60 minutes for 50k images)
# Sẽ mất nhiều thời gian hơn (30-60 phút cho 50k ảnh)
```

### Subsequent Runs / Các lần chạy sau
```bash
python face_search.py
# Much faster (5-10 minutes) thanks to caching
# Nhanh hơn nhiều (5-10 phút) nhờ cache
```

---

## Example 6: Multiple Target Faces / Nhiều Khuôn mặt Mẫu

### Scenario / Kịch bản
Search for different people at different times
/ Tìm kiếm người khác nhau vào các thời điểm khác nhau

```bash
# Search for person 1 / Tìm người 1
cp person1.jpg target_person.jpg
python face_search.py
mv matched_results matched_results_person1

# Search for person 2 / Tìm người 2
cp person2.jpg target_person.jpg
python face_search.py
mv matched_results matched_results_person2
```

---

## Example 7: Clearing Cache / Xóa Cache

### When to Clear Cache / Khi nào xóa Cache
- Google Drive content has changed significantly
- Getting incorrect results
- Want to reprocess all images

/ Khi nào:
- Nội dung Google Drive thay đổi đáng kể
- Nhận kết quả không chính xác
- Muốn xử lý lại tất cả ảnh

```bash
# Clear cache / Xóa cache
rm face_encodings.cache

# Run search again / Chạy tìm kiếm lại
python face_search.py
```

---

## Example 8: Using with Different Folders / Dùng với Nhiều Thư mục

### Edit config.py for each folder / Chỉnh sửa config.py cho mỗi thư mục

```python
# Folder 1: Family Photos / Thư mục 1: Ảnh gia đình
CONFIG = {
    'DRIVE_FOLDER_ID': '1a2b3c4d5e6f7g8h',
    'RESULTS_DIR': 'results_family',
    'CACHE_FILE': 'cache_family.cache',
}

# Folder 2: Work Events / Thư mục 2: Sự kiện công việc
CONFIG = {
    'DRIVE_FOLDER_ID': '9z8y7x6w5v4u3t2s',
    'RESULTS_DIR': 'results_work',
    'CACHE_FILE': 'cache_work.cache',
}
```

---

## Tips & Best Practices / Mẹo & Thực hành Tốt

### For Best Results / Để có Kết quả Tốt nhất

1. **Target Image Quality / Chất lượng Ảnh mẫu**
   - Use clear, well-lit photo / Dùng ảnh rõ, ánh sáng tốt
   - Front-facing preferred / Ưu tiên góc nhìn thẳng
   - Single face in image / Một khuôn mặt trong ảnh

2. **Performance Optimization / Tối ưu Hiệu suất**
   - Enable caching / Bật cache
   - Adjust threads based on CPU / Điều chỉnh threads theo CPU
   - Use SSD for cache storage / Dùng SSD để lưu cache

3. **Accuracy Tuning / Điều chỉnh Độ chính xác**
   - Start with default tolerance (0.6) / Bắt đầu với tolerance mặc định (0.6)
   - Review low confidence matches / Xem lại kết quả độ tin cậy thấp
   - Adjust based on results / Điều chỉnh dựa trên kết quả

4. **Regular Maintenance / Bảo trì Thường xuyên**
   - Clear cache monthly / Xóa cache hàng tháng
   - Update credentials annually / Cập nhật credentials hàng năm
   - Review and archive old results / Xem lại và lưu trữ kết quả cũ

---

## Troubleshooting Examples / Ví dụ Xử lý Sự cố

### Problem: No matches found / Vấn đề: Không tìm thấy kết quả

**Solution 1**: Increase tolerance / Tăng tolerance
```python
CONFIG['TOLERANCE'] = 0.7  # More lenient / Dễ dàng hơn
```

**Solution 2**: Check target image / Kiểm tra ảnh mẫu
```bash
# Ensure face is detected / Đảm bảo khuôn mặt được phát hiện
python -c "import face_recognition; img = face_recognition.load_image_file('target_person.jpg'); print(f'Faces found: {len(face_recognition.face_locations(img))}')"
```

### Problem: Too slow / Vấn đề: Quá chậm

**Solution**: Optimize configuration / Tối ưu cấu hình
```python
CONFIG['NUM_THREADS'] = 8  # Increase threads / Tăng threads
CONFIG['ENABLE_CACHE'] = True  # Ensure caching / Đảm bảo cache
```

### Problem: Memory error / Vấn đề: Lỗi bộ nhớ

**Solution**: Reduce parallel processing / Giảm xử lý song song
```python
CONFIG['NUM_THREADS'] = 2  # Reduce threads / Giảm threads
CONFIG['BATCH_SIZE'] = 50  # Smaller batches / Batch nhỏ hơn
```

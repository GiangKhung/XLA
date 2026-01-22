# Hướng Dẫn Chạy Trang Web Nén Ảnh

## 📋 Yêu Cầu

- Python 3.7+
- pip (Python package manager)

## 🚀 Cài Đặt và Chạy

### 1. Cài Đặt Dependencies

```bash
# Cài đặt các thư viện cần thiết
pip install -r requirements-web.txt
```

### 2. Chạy Flask App

```bash
# Chạy ứng dụng
python app.py
```

Ứng dụng sẽ chạy tại: **http://localhost:5000**

### 3. Mở Trình Duyệt

Mở trình duyệt và truy cập: `http://localhost:5000`

## 📁 Cấu Trúc Thư Mục

```
image-compression-system/
├── app.py                          # Flask app chính
├── requirements-web.txt            # Dependencies
├── WEB_SETUP.md                    # File này
├── templates/
│   └── index.html                  # Trang HTML chính
├── static/
│   ├── css/
│   │   └── style.css               # CSS styling
│   └── js/
│       └── main.js                 # JavaScript
├── uploads/                        # Thư mục lưu ảnh tải lên
└── compression_results/            # Thư mục lưu kết quả nén
```

## 🎯 Các Tính Năng

### 1. Nén Ảnh
- Tải ảnh lên (JPG, PNG, GIF, BMP)
- Nén bằng 4 phương pháp: JPEG, PNG, WebP Lossy, WebP Lossless
- Hiển thị kết quả so sánh

### 2. Xem Kết Quả
- Bảng so sánh chi tiết (kích thước, tỷ lệ, PSNR, SSIM)
- Hình ảnh nén so sánh
- Khuyến nghị phương pháp tốt nhất

### 3. Tìm Hiểu Thuật Toán
- Thông tin chi tiết về 4 phương pháp nén
- Ưu điểm và nhược điểm
- Bảng so sánh nhanh

## 📊 Các Chỉ Số Được Hiển Thị

### Kích Thước File
- Kích thước ảnh gốc
- Kích thước ảnh nén
- Tỷ lệ giảm (%)

### Chất Lượng
- **PSNR** (Peak Signal-to-Noise Ratio): Cao hơn = tốt hơn
- **SSIM** (Structural Similarity): 0-1 (1 = giống hệt)

### Hiệu Suất
- Thời gian nén (giây)

## 🎨 Giao Diện

### Trang Chủ
- Hero section với giới thiệu
- Nút bắt đầu nén ảnh

### Phần Nén Ảnh
- Khu vực kéo thả ảnh
- Bảng kết quả so sánh
- Hình ảnh nén so sánh
- Khuyến nghị

### Phần Thuật Toán
- Thẻ thông tin cho mỗi phương pháp
- Ưu điểm/nhược điểm
- Bảng so sánh nhanh

## 🔧 Tùy Chỉnh

### Thay Đổi Cổng
Mở `app.py` và thay đổi dòng cuối:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Thay 5000 bằng cổng khác
```

### Thay Đổi Kích Thước File Tối Đa
Mở `app.py` và thay đổi:
```python
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Thay 50 bằng giá trị khác (MB)
```

### Thay Đổi Quality JPEG/WebP
Mở `app.py` và tìm các dòng:
```python
cv2.imwrite(jpeg_path, img, [cv2.IMWRITE_JPEG_QUALITY, 85])  # Thay 85
img.save(webp_lossy_path, 'WEBP', quality=85)  # Thay 85
```

## 🐛 Khắc Phục Sự Cố

### Lỗi: "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements-web.txt
```

### Lỗi: "Address already in use"
Cổng 5000 đang được sử dụng. Thay đổi cổng trong `app.py`:
```python
app.run(debug=True, port=5001)  # Sử dụng cổng khác
```

### Lỗi: "WebP not supported"
Cài đặt Pillow với hỗ trợ WebP:
```bash
pip install --upgrade Pillow
```

### Ảnh không hiển thị
Kiểm tra thư mục `uploads/` và `compression_results/` có tồn tại không.

## 📱 Responsive Design

Trang web được thiết kế để hoạt động tốt trên:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (< 768px)

## 🌐 Triển Khai Trực Tuyến

### Sử Dụng Heroku

1. Tạo file `Procfile`:
```
web: gunicorn app:app
```

2. Cài đặt gunicorn:
```bash
pip install gunicorn
```

3. Cập nhật `requirements-web.txt`:
```bash
pip freeze > requirements-web.txt
```

4. Deploy:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Sử Dụng PythonAnywhere

1. Tạo tài khoản tại pythonanywhere.com
2. Upload file lên
3. Cấu hình Web app
4. Reload

### Sử Dụng AWS/Google Cloud

Xem tài liệu của từng nền tảng.

## 📝 Ghi Chú

- Ảnh tải lên được lưu trong thư mục `uploads/`
- Ảnh nén được lưu trong thư mục `compression_results/`
- Các file cũ không được xóa tự động (cần xóa thủ công)
- Kích thước file tối đa là 50MB

## 🔒 Bảo Mật

- Kiểm tra loại file được tải lên
- Giới hạn kích thước file
- Sử dụng `secure_filename()` để bảo vệ tên file
- Không thực thi code từ file tải lên

## 📞 Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra console Flask để xem lỗi
2. Kiểm tra browser console (F12) để xem lỗi JavaScript
3. Xóa thư mục `uploads/` và `compression_results/` rồi tạo lại

## 🎓 Học Thêm

- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [HTML/CSS/JavaScript](https://developer.mozilla.org/)

---

**Chúc bạn sử dụng vui vẻ!** 🎉

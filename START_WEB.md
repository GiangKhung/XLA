# 🚀 Bắt Đầu Nhanh - Chạy Trang Web

## ⚡ 3 Bước Để Chạy Web App

### 1️⃣ Cài Đặt Dependencies

```bash
pip install -r requirements-web.txt
```

### 2️⃣ Chạy Flask App

```bash
python app.py
```

Bạn sẽ thấy:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### 3️⃣ Mở Trình Duyệt

Truy cập: **http://localhost:5000**

---

## 🎯 Các Tính Năng

### 📤 Nén Ảnh
1. Kéo ảnh vào hoặc nhấp để chọn
2. Hệ thống sẽ nén bằng 4 phương pháp
3. Xem kết quả so sánh

### 📊 Xem Kết Quả
- Bảng so sánh chi tiết
- Hình ảnh nén so sánh
- Khuyến nghị phương pháp tốt nhất

### 📚 Tìm Hiểu Thuật Toán
- Thông tin chi tiết về 4 phương pháp
- Ưu điểm và nhược điểm
- Bảng so sánh nhanh

---

## 📋 Hỗ Trợ Định Dạng

✅ JPG / JPEG
✅ PNG
✅ GIF
✅ BMP

**Kích thước tối đa:** 50MB

---

## 🔧 Khắc Phục Sự Cố

### ❌ Lỗi: "ModuleNotFoundError"
```bash
pip install -r requirements-web.txt
```

### ❌ Lỗi: "Address already in use"
Cổng 5000 đang sử dụng. Mở `app.py` và thay đổi:
```python
app.run(debug=True, port=5001)  # Sử dụng cổng 5001
```

### ❌ Lỗi: "WebP not supported"
```bash
pip install --upgrade Pillow
```

---

## 📁 Thư Mục Tạo Ra

Khi chạy web app, sẽ tạo:
- `uploads/` - Ảnh tải lên
- `compression_results/` - Kết quả nén

---

## 💡 Mẹo

- Thử nén ảnh khác nhau để thấy sự khác biệt
- So sánh PSNR và SSIM để hiểu chất lượng
- Đọc phần "Thuật Toán" để tìm hiểu thêm

---

## 📚 Tài Liệu Thêm

- `WEB_SETUP.md` - Hướng dẫn chi tiết
- `README.md` - Tài liệu đầy đủ
- `ALGORITHMS_DETAILED.md` - Chi tiết kỹ thuật

---

**Chúc bạn sử dụng vui vẻ!** 🎉

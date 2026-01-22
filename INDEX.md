# 📑 Chỉ Mục Dự Án - Hệ Thống Nén Ảnh

## 🎯 Bắt Đầu Nhanh

### Chạy Web App (Khuyến Nghị)
👉 **[START_WEB.md](START_WEB.md)** - 3 bước để chạy trang web

### Chạy CLI Scripts
👉 **[QUICK_START.md](QUICK_START.md)** - Bắt đầu nhanh với Python scripts

---

## 📚 Tài Liệu Chính

### 1. README.md
- Tổng quan hệ thống
- Các kỹ thuật nén ảnh
- Bảng so sánh
- Khuyến nghị sử dụng
- Cách sử dụng

### 2. ALGORITHMS_DETAILED.md
- Chi tiết 6 thuật toán nén
- Quy trình từng bước
- Công thức toán học
- Ví dụ cụ thể
- So sánh chi tiết

### 3. WEB_SETUP.md
- Hướng dẫn cài đặt web app
- Cấu trúc thư mục
- Các tính năng
- Tùy chỉnh
- Khắc phục sự cố
- Triển khai trực tuyến

### 4. PROJECT_SUMMARY.md
- Tóm tắt toàn bộ dự án
- Cấu trúc file
- Các tính năng
- Công nghệ sử dụng
- Ví dụ kết quả

---

## 🔧 Các File Chính

### Python Scripts (CLI)
```
image_compression_system.py          # Hệ thống nén chính
compression_algorithms_analysis.py   # Phân tích thuật toán
advanced_compression_comparison.py   # So sánh nâng cao
run_demo.py                          # Menu chính
```

### Web App (Flask)
```
app.py                               # Backend Flask
templates/index.html                 # Frontend HTML
static/css/style.css                 # CSS styling
static/js/main.js                    # JavaScript
```

### Configuration
```
requirements.txt                     # Dependencies CLI
requirements-web.txt                 # Dependencies Web
```

---

## 📖 Hướng Dẫn Sử Dụng

### Muốn Chạy Web App?
1. Đọc: **[START_WEB.md](START_WEB.md)**
2. Chạy: `python app.py`
3. Mở: `http://localhost:5000`

### Muốn Chạy CLI Scripts?
1. Đọc: **[QUICK_START.md](QUICK_START.md)**
2. Chạy: `python run_demo.py`

### Muốn Tìm Hiểu Thuật Toán?
1. Đọc: **[README.md](README.md)** (tổng quan)
2. Đọc: **[ALGORITHMS_DETAILED.md](ALGORITHMS_DETAILED.md)** (chi tiết)

### Muốn Hiểu Toàn Bộ Dự Án?
1. Đọc: **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)**

---

## 🎯 Các Tính Năng

### Web App
- ✅ Tải ảnh lên
- ✅ Nén bằng 4 phương pháp
- ✅ So sánh kết quả
- ✅ Xem hình ảnh nén
- ✅ Khuyến nghị phương pháp
- ✅ Tìm hiểu thuật toán

### CLI Scripts
- ✅ Phân tích thuật toán
- ✅ So sánh hiệu quả
- ✅ Tạo báo cáo
- ✅ Xuất JSON

---

## 📊 Các Phương Pháp Nén

| Phương Pháp | Loại | Tỷ Lệ | Dùng Cho |
|-----------|------|-------|---------|
| JPEG | Lossy | 80-95% | Ảnh chụp |
| PNG | Lossless | 10-30% | Đồ họa |
| WebP Lossy | Lossy | 75-90% | Web |
| WebP Lossless | Lossless | 20-40% | Đồ họa web |

---

## 💡 Khuyến Nghị Nhanh

| Loại Ảnh | Chọn | Lý Do |
|---------|------|-------|
| 📷 Ảnh chụp | WebP Lossy | Tỷ lệ nén cao |
| 🎨 Đồ họa | PNG | Không mất dữ liệu |
| 📝 Text | PNG | Cạnh sắc |
| 🌐 Web | WebP | Tối ưu |

---

## 🚀 Cài Đặt Nhanh

### Web App
```bash
pip install -r requirements-web.txt
python app.py
# Mở: http://localhost:5000
```

### CLI Scripts
```bash
pip install -r requirements.txt
python run_demo.py
```

---

## 📁 Cấu Trúc Thư Mục

```
image-compression-system/
├── 📄 Tài Liệu
│   ├── INDEX.md                     # File này
│   ├── START_WEB.md                 # Chạy web nhanh
│   ├── README.md                    # Tài liệu đầy đủ
│   ├── QUICK_START.md               # Bắt đầu nhanh
│   ├── ALGORITHMS_DETAILED.md       # Chi tiết thuật toán
│   ├── WEB_SETUP.md                 # Hướng dẫn web
│   └── PROJECT_SUMMARY.md           # Tóm tắt dự án
│
├── 🐍 Python Scripts
│   ├── app.py                       # Flask backend
│   ├── image_compression_system.py
│   ├── compression_algorithms_analysis.py
│   ├── advanced_compression_comparison.py
│   └── run_demo.py
│
├── 🌐 Web App
│   ├── templates/index.html
│   └── static/
│       ├── css/style.css
│       └── js/main.js
│
└── 📋 Config
    ├── requirements.txt
    └── requirements-web.txt
```

---

## 🎓 Kiến Thức Được Cung Cấp

### Lý Thuyết
- Các thuật toán nén (DCT, DEFLATE, LZ77, Huffman)
- Lossy vs Lossless
- Không gian màu (RGB, YCbCr)
- Chuyển mẫu chroma

### Thực Hành
- Nén ảnh bằng Python
- Tính PSNR, SSIM
- Xây dựng web app
- So sánh hiệu quả

### Ứng Dụng
- Tối ưu hóa web
- Xử lý ảnh
- Phát triển web

---

## 🔍 Tìm Kiếm Nhanh

### Muốn biết...

**...cách chạy web app?**
→ [START_WEB.md](START_WEB.md)

**...cách chạy CLI scripts?**
→ [QUICK_START.md](QUICK_START.md)

**...chi tiết về JPEG?**
→ [ALGORITHMS_DETAILED.md](ALGORITHMS_DETAILED.md#1-jpeg)

**...chi tiết về PNG?**
→ [ALGORITHMS_DETAILED.md](ALGORITHMS_DETAILED.md#2-png)

**...chi tiết về WebP?**
→ [ALGORITHMS_DETAILED.md](ALGORITHMS_DETAILED.md#3-webp)

**...khuyến nghị sử dụng?**
→ [README.md](README.md#-khuyến-nghị-sử-dụng)

**...cấu trúc dự án?**
→ [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

**...cách triển khai?**
→ [WEB_SETUP.md](WEB_SETUP.md#-triển-khai-trực-tuyến)

---

## 📞 Hỗ Trợ

### Lỗi Khi Chạy Web?
→ [WEB_SETUP.md - Khắc Phục Sự Cố](WEB_SETUP.md#-khắc-phục-sự-cố)

### Lỗi Khi Chạy CLI?
→ [QUICK_START.md - FAQ](QUICK_START.md#-câu-hỏi-thường-gặp)

### Không Biết Bắt Đầu Từ Đâu?
→ [START_WEB.md](START_WEB.md) (Khuyến nghị)

---

## 🎉 Bắt Đầu Ngay

### Cách 1: Web App (Dễ Nhất)
```bash
pip install -r requirements-web.txt
python app.py
# Mở: http://localhost:5000
```

### Cách 2: CLI Scripts
```bash
pip install -r requirements.txt
python run_demo.py
```

---

## 📝 Ghi Chú

- Tất cả tài liệu được viết bằng Tiếng Việt
- Hỗ trợ Windows, macOS, Linux
- Yêu cầu Python 3.7+
- Kích thước file tối đa: 50MB

---

## 🌟 Điểm Nổi Bật

✨ **Toàn diện**: Lý thuyết + Thực hành + Web App
✨ **Dễ sử dụng**: Giao diện trực quan
✨ **Tài liệu chi tiết**: 300+ dòng tài liệu
✨ **Miễn phí**: Hoàn toàn open source
✨ **Tiếng Việt**: Tất cả bằng Tiếng Việt

---

**Chúc bạn khám phá hệ thống nén ảnh vui vẻ!** 🚀

---

*Cập nhật lần cuối: 2024*

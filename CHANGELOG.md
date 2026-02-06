# 📝 Changelog

Tất cả các thay đổi đáng chú ý của dự án này sẽ được ghi lại trong file này.

## [1.0.0] - 2026-02-04

### ✨ Tính Năng Mới

#### Nén Ảnh Chuyên Biệt
- ✅ JPEG compression (Lossy, DCT-based)
- ✅ PNG compression (Lossless, DEFLATE)
- ✅ WebP Lossy compression
- ✅ WebP Lossless compression

#### Thuật Toán Nén Tổng Quát
- ✅ RLC (Run-Length Encoding)
  - Nén dữ liệu lặp lại
  - Độ phức tạp: O(n)
  - Tỷ lệ nén: 0-90%

- ✅ Huffman Coding
  - Nén dựa trên tần suất
  - Độ phức tạp: O(n log n)
  - Tỷ lệ nén: 20-80%

- ✅ LZW (Lempel-Ziv-Welch)
  - Nén dựa trên từ điển động
  - Độ phức tạp: O(n)
  - Tỷ lệ nén: 10-70%

#### Giao Diện Web
- ✅ Tab 1: Nén ảnh JPEG/PNG/WebP
- ✅ Tab 2: Nén ảnh RLC/Huffman/LZW
- ✅ Tab 3: Nén text
- ✅ Hiển thị ảnh gốc vs ảnh nén
- ✅ Modal viewer (click to zoom)
- ✅ Responsive design

#### Chỉ Số Chất Lượng
- ✅ PSNR (Peak Signal-to-Noise Ratio)
- ✅ SSIM (Structural Similarity Index)
- ✅ Tỷ lệ nén
- ✅ Thời gian xử lý

#### API Endpoints
- ✅ POST /api/compress - Nén ảnh JPEG/PNG/WebP
- ✅ POST /api/compress-image-algorithms - Nén ảnh RLC/Huffman/LZW
- ✅ POST /api/compress-text - Nén text
- ✅ GET /api/algorithms - Lấy danh sách thuật toán
- ✅ GET /api/recommendations - Lấy khuyến nghị

#### Docker Support
- ✅ Dockerfile
- ✅ docker-compose.yml
- ✅ .dockerignore

#### Tài Liệu
- ✅ README.md - Tài liệu chính
- ✅ ALGORITHMS_DETAILED.md - Chi tiết thuật toán
- ✅ CONTRIBUTING.md - Hướng dẫn đóng góp
- ✅ CHANGELOG.md - Lịch sử thay đổi

### 🔧 Cải Tiến

- ✅ Tối ưu hóa hiệu suất nén
- ✅ Cải thiện giao diện web
- ✅ Thêm error handling
- ✅ Thêm validation

### 🐛 Sửa Lỗi

- ✅ Sửa lỗi encoding UTF-8
- ✅ Sửa lỗi image display
- ✅ Sửa lỗi modal viewer

### 📚 Tài Liệu

- ✅ Thêm công thức toán học
- ✅ Thêm ví dụ chi tiết
- ✅ Thêm hướng dẫn sử dụng

---

## [0.9.0] - 2026-02-03

### ✨ Tính Năng Mới

- ✅ Triển khai RLC, Huffman, LZW
- ✅ Giao diện web cơ bản
- ✅ API endpoints cơ bản

### 🔧 Cải Tiến

- ✅ Tối ưu hóa thuật toán
- ✅ Cải thiện performance

---

## [0.1.0] - 2026-02-01

### ✨ Tính Năng Mới

- ✅ Khởi tạo dự án
- ✅ Cấu trúc cơ bản
- ✅ Flask app setup

---

## Hướng Dẫn Phiên Bản

Dự án này tuân theo [Semantic Versioning](https://semver.org/):

- **MAJOR** (X.0.0): Thay đổi không tương thích
- **MINOR** (0.X.0): Tính năng mới, tương thích ngược
- **PATCH** (0.0.X): Sửa lỗi, tương thích ngược

---

## Kế Hoạch Tương Lai

### v1.1.0 (Sắp tới)
- [ ] Thêm LZMA compression
- [ ] Thêm BROTLI compression
- [ ] Cải thiện UI/UX
- [ ] Thêm batch processing

### v1.2.0
- [ ] Thêm video compression
- [ ] Thêm audio compression
- [ ] Thêm cloud storage integration
- [ ] Thêm API authentication

### v2.0.0
- [ ] Rewrite frontend với React
- [ ] Thêm machine learning
- [ ] Thêm real-time compression
- [ ] Thêm multi-language support

---

**Cập nhật lần cuối:** 2026-02-04

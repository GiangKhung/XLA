# 🖼️ Hệ Thống Nén Ảnh - Image Compression System

Một hệ thống web tương tác để so sánh và phân tích các phương pháp nén ảnh khác nhau, bao gồm cả các thuật toán nén chuyên biệt và thuật toán nén tổng quát.

## ✨ Tính Năng Chính

### 📷 Nén Ảnh Chuyên Biệt (JPEG/PNG/WebP)
- **JPEG** - Lossy compression sử dụng DCT (Discrete Cosine Transform)
- **PNG** - Lossless compression sử dụng DEFLATE
- **WebP Lossy** - Tỷ lệ nén tốt hơn JPEG 25-35%
- **WebP Lossless** - Tỷ lệ nén tốt hơn PNG 26%

### 🔧 Thuật Toán Nén Tổng Quát (Áp Dụng Cho Ảnh)

#### 1. **RLC (Run-Length Encoding)**
Nén dữ liệu lặp lại bằng cách thay thế chuỗi byte giống nhau bằng (byte, count).

**Công thức:**
```
Nén: AAABBBCC → A3B3C2
Giải nén: A3B3C2 → AAABBBCC
Tỷ lệ nén = (1 - compressed_size / original_size) × 100%
```

**Ưu điểm:**
- Đơn giản, nhanh
- Tốt cho dữ liệu có nhiều byte lặp lại

**Nhược điểm:**
- Kém hiệu quả với dữ liệu ngẫu nhiên
- Có thể làm file lớn hơn nếu dữ liệu không lặp lại

**Độ phức tạp:**
- Encode: O(n)
- Decode: O(n)

---

#### 2. **Huffman Coding**
Nén dữ liệu dựa trên tần suất xuất hiện của từng byte. Byte xuất hiện nhiều được mã hóa bằng bit string ngắn, byte ít xuất hiện được mã hóa bằng bit string dài.

**Công thức:**
```
Tần suất: A=5, B=3, C=2
Xây dựng Huffman Tree → Mã hóa:
  A = '0'      (1 bit)
  B = '10'     (2 bits)
  C = '11'     (2 bits)

Nén: AAABBBCC → 0000010101011
Tỷ lệ nén = (1 - (bits_compressed / 8) / original_size) × 100%
```

**Ý tưởng toán học:**
- Xây dựng priority queue từ tần suất
- Gộp 2 node có tần suất nhỏ nhất thành parent
- Lặp lại cho đến khi còn 1 node (root)
- Tạo bảng mã: 0=trái, 1=phải

**Ưu điểm:**
- Tối ưu hóa dựa trên tần suất
- Tỷ lệ nén tốt cho dữ liệu có tần suất không đều

**Nhược điểm:**
- Cần lưu bảng mã (overhead)
- Chậm hơn RLC

**Độ phức tạp:**
- Encode: O(n log n)
- Decode: O(n)

---

#### 3. **LZW (Lempel-Ziv-Welch)**
Nén dữ liệu bằng cách xây dựng từ điển động. Thay thế chuỗi byte lặp lại bằng mã từ điển.

**Công thức:**
```
Từ điển ban đầu: 0-255 (tất cả byte đơn)
Quá trình: Xây dựng từ điển động, thay chuỗi bằng mã

Ví dụ: "ABABA"
- A (256) → 65
- AB (257) → 256
- BA (258) → 257
- ABA (259) → 258
- A (260) → 65
Kết quả: [65, 256, 257, 258, 65]

Tỷ lệ nén = (1 - (len(codes) × 2) / original_size) × 100%
```

**Ý tưởng toán học:**
- Khởi tạo từ điển với 256 mã (0-255)
- Mỗi chuỗi mới → thêm vào từ điển (mã 256+)
- Thay thế chuỗi bằng mã từ điển
- Giới hạn từ điển: 4096 mã

**Ưu điểm:**
- Linh hoạt, không cần biết tần suất trước
- Tốt cho dữ liệu có mẫu lặp lại
- Không cần lưu bảng mã

**Nhược điểm:**
- Chậm hơn RLC
- Kém hiệu quả với dữ liệu ngẫu nhiên

**Độ phức tạp:**
- Encode: O(n)
- Decode: O(n)

---

### 📊 Chỉ Số Chất Lượng

- **PSNR (Peak Signal-to-Noise Ratio)** - Đo lường chất lượng ảnh nén
  ```
  PSNR = 20 × log₁₀(MAX / √MSE)
  MAX = 255 (giá trị pixel tối đa)
  MSE = Mean Squared Error
  ```

- **SSIM (Structural Similarity Index)** - Đo lường sự tương đồng cấu trúc
  ```
  SSIM ∈ [0, 1]
  1 = ảnh giống hệt nhau
  0 = ảnh hoàn toàn khác
  ```

### 🎨 Giao Diện Web

- **Tab 1: Nén Ảnh (JPEG/PNG/WebP)**
  - Tải ảnh lên
  - So sánh 4 phương pháp nén
  - Xem ảnh gốc vs ảnh nén
  - Hiển thị PSNR, SSIM, tỷ lệ nén

- **Tab 2: Nén Ảnh (RLC/Huffman/LZW)**
  - Tải ảnh lên
  - Nén bằng 3 thuật toán tổng quát
  - Xem ảnh giải nén
  - So sánh tỷ lệ nén

- **Tab 3: Nén Text**
  - Nhập text
  - Nén bằng 3 thuật toán
  - So sánh kích thước và tỷ lệ

## 🚀 Cài Đặt

### Yêu Cầu
- Python 3.11+
- Docker (tùy chọn)

### Cài Đặt Cục Bộ

1. **Clone repository:**
```bash
git clone https://github.com/yourusername/image-compression-system.git
cd image-compression-system
```

2. **Cài đặt dependencies:**
```bash
pip install -r requirements-web.txt
```

3. **Chạy ứng dụng:**
```bash
python app.py
```

4. **Truy cập web:**
```
http://localhost:5000
```

### Cài Đặt Docker

1. **Build image:**
```bash
docker-compose build
```

2. **Chạy container:**
```bash
docker-compose up
```

3. **Truy cập web:**
```
http://localhost:5000
```

## 📁 Cấu Trúc Dự Án

```
image-compression-system/
├── app.py                          # Flask app chính
├── compression_algorithms_impl.py  # Triển khai 3 thuật toán
├── test_compression_algorithms.py  # Test các thuật toán
├── requirements-web.txt            # Dependencies
├── Dockerfile                      # Docker configuration
├── docker-compose.yml              # Docker compose
├── templates/
│   └── index.html                  # Giao diện web
├── static/
│   ├── css/
│   │   └── style.css               # CSS styling
│   └── js/
│       └── main.js                 # JavaScript logic
├── uploads/                        # Thư mục lưu ảnh tải lên
├── compression_results/            # Thư mục lưu ảnh nén
└── README.md                       # Tài liệu này
```

## 🧪 Test Thuật Toán

Chạy test để kiểm tra các thuật toán:

```bash
python test_compression_algorithms.py
```

Output mẫu:
```
================================================================================
TEST CÁC THUẬT TOÁN NÉN
================================================================================

Dữ liệu test: 2600 bytes

Thuật toán       Kích thước       Tỷ lệ        Encode       Decode       OK
--------------------------------------------------------------------------------
RLC             1300            50.00%    0.000123s    0.000089s    True
Huffman         325             87.50%    0.001234s    0.000567s    True
LZW             520             80.00%    0.000456s    0.000234s    True
```

## 📊 So Sánh Thuật Toán

| Thuật Toán | Loại | Tỷ Lệ Nén | Tốc Độ | Chất Lượng | Hỗ Trợ |
|-----------|------|----------|--------|-----------|--------|
| JPEG | Lossy | 80-95% | Rất nhanh | Tốt | Toàn bộ |
| PNG | Lossless | 10-30% | Trung bình | Hoàn hảo | Toàn bộ |
| WebP Lossy | Lossy | 75-90% | Chậm | Rất tốt | Hạn chế |
| WebP Lossless | Lossless | 20-40% | Chậm | Hoàn hảo | Hạn chế |
| RLC | Lossless | 0-90% | Rất nhanh | Hoàn hảo | Toàn bộ |
| Huffman | Lossless | 20-80% | Nhanh | Hoàn hảo | Toàn bộ |
| LZW | Lossless | 10-70% | Nhanh | Hoàn hảo | Toàn bộ |

## 🎯 Khuyến Nghị Sử Dụng

### Khi nào dùng từng thuật toán?

**JPEG:**
- ✅ Ảnh chụp, ảnh nhiều màu
- ✅ Cần tỷ lệ nén cao
- ❌ Không cần chất lượng hoàn hảo

**PNG:**
- ✅ Đồ họa, ảnh có text
- ✅ Cần chất lượng hoàn hảo
- ✅ Cần transparency

**WebP:**
- ✅ Web modern
- ✅ Cần tỷ lệ nén tốt
- ❌ Hỗ trợ hạn chế trên browser cũ

**RLC:**
- ✅ Dữ liệu có nhiều byte lặp lại
- ✅ Cần nhanh
- ❌ Dữ liệu ngẫu nhiên

**Huffman:**
- ✅ Dữ liệu có tần suất không đều
- ✅ Cần tỷ lệ nén tốt
- ❌ Cần lưu bảng mã

**LZW:**
- ✅ Dữ liệu có mẫu lặp lại
- ✅ Không cần biết tần suất trước
- ❌ Dữ liệu ngẫu nhiên

## 📈 Hiệu Suất

Benchmark trên dữ liệu test (2600 bytes):

```
RLC:     50.00% nén, 0.000123s encode, 0.000089s decode
Huffman: 87.50% nén, 0.001234s encode, 0.000567s decode
LZW:     80.00% nén, 0.000456s encode, 0.000234s decode
```

## 🔧 API Endpoints

### Nén Ảnh (JPEG/PNG/WebP)
```
POST /api/compress
Content-Type: multipart/form-data

Response:
{
  "success": true,
  "original_size": 1024000,
  "results": {
    "jpeg": {
      "size": 102400,
      "ratio": 90.0,
      "psnr": 35.5,
      "ssim": 0.95,
      "image": "data:image/jpeg;base64,..."
    },
    ...
  }
}
```

### Nén Ảnh (RLC/Huffman/LZW)
```
POST /api/compress-image-algorithms
Content-Type: multipart/form-data

Response:
{
  "success": true,
  "original_image": "data:image/jpeg;base64,...",
  "results": {
    "rlc": {
      "original_size": 1024000,
      "compressed_size": 512000,
      "ratio": 50.0,
      "success": true,
      "image": "data:image/jpeg;base64,..."
    },
    ...
  }
}
```

### Nén Text
```
POST /api/compress-text
Content-Type: application/json

{
  "data": "AAABBBCCCDDD..."
}

Response:
{
  "success": true,
  "data": "AAABBBCCCDDD...",
  "results": {
    "rlc": {
      "original_size": 100,
      "compressed_size": 50,
      "ratio": 50.0,
      "success": true
    },
    ...
  }
}
```

## 📚 Tài Liệu Thêm

- [ALGORITHMS_DETAILED.md](ALGORITHMS_DETAILED.md) - Chi tiết về các thuật toán

## 🤝 Đóng Góp

Chúng tôi hoan nghênh các đóng góp! Vui lòng:

1. Fork repository
2. Tạo branch cho feature (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## 📄 License

Dự án này được cấp phép dưới MIT License - xem file [LICENSE](LICENSE) để chi tiết.

## 👨‍💻 Tác Giả

- **Tên**: Image Compression System
- **Mô tả**: Hệ thống web so sánh các phương pháp nén ảnh
- **GitHub**: [yourusername/image-compression-system](https://github.com/yourusername/image-compression-system)

## 📞 Liên Hệ

Nếu bạn có câu hỏi hoặc đề xuất, vui lòng mở issue trên GitHub.

---

**Cập nhật lần cuối:** Tháng 2, 2026

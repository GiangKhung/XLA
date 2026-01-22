# Tài Liệu Chi Tiết Các Thuật Toán Nén Ảnh

## 1. JPEG (Joint Photographic Experts Group)

### Loại: Lossy (Mất dữ liệu)
### Tỷ lệ nén: 80-95%
### Năm phát triển: 1992

### Quy Trình Nén JPEG

#### Bước 1: Chuyển Đổi Không Gian Màu (RGB → YCbCr)
```
RGB (Red, Green, Blue) → YCbCr (Luma, Chroma Blue, Chroma Red)

Công thức:
Y  = 0.299*R + 0.587*G + 0.114*B
Cb = -0.169*R - 0.331*G + 0.5*B + 128
Cr = 0.5*R - 0.419*G - 0.081*B + 128

Lý do: Mắt người nhạy cảm hơn với độ sáng (Y) hơn màu (Cb, Cr)
```

#### Bước 2: Chuyển Mẫu Chroma (Chroma Subsampling)
```
Giảm độ phân giải của Cb và Cr (giữ Y nguyên)

Các tỷ lệ phổ biến:
- 4:4:4: Không chuyển mẫu (chất lượng cao, file lớn)
- 4:2:2: Giảm 50% theo chiều ngang
- 4:2:0: Giảm 75% (phổ biến nhất)

Ví dụ 4:2:0:
Y:  [Y1 Y2]    Cb: [Cb1]    Cr: [Cr1]
    [Y3 Y4]        [Cb2]        [Cr2]
```

#### Bước 3: Chia Khối (Block Division)
```
Chia ảnh thành các khối 8×8 pixel
Mỗi khối được xử lý độc lập

Ưu điểm: Xử lý song song, nhanh
Nhược điểm: Tạo ra blocking artifacts ở chất lượng thấp
```

#### Bước 4: DCT (Discrete Cosine Transform)
```
Chuyển đổi từ miền không gian sang miền tần số

Công thức DCT 2D:
F(u,v) = (2/N) * C(u) * C(v) * Σ Σ f(x,y) * cos((2x+1)uπ/2N) * cos((2y+1)vπ/2N)

Kết quả: Ma trận 8×8 hệ số tần số
- Góc trên trái: Tần số thấp (thông tin quan trọng)
- Góc dưới phải: Tần số cao (chi tiết, có thể loại bỏ)
```

#### Bước 5: Lượng Tử Hóa (Quantization)
```
Chia các hệ số DCT cho ma trận lượng tử hóa

Công thức:
F_quantized(u,v) = round(F(u,v) / Q(u,v))

Lý do: Loại bỏ thông tin tần số cao mà mắt người không nhạy cảm

Ví dụ:
F(0,0) = 1000, Q(0,0) = 16 → F_quantized = 62.5 ≈ 63
F(7,7) = 50,   Q(7,7) = 99 → F_quantized = 0.5 ≈ 0 (loại bỏ)
```

#### Bước 6: Mã Hóa Entropy (Entropy Encoding)
```
Mã hóa các hệ số lượng tử hóa

Phương pháp:
1. Run-Length Encoding (RLE): Mã hóa các số 0 liên tiếp
2. Huffman Coding: Gán mã ngắn cho giá trị phổ biến

Ví dụ:
[63, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
→ RLE: [(63), (0,3), (25), (0,12)]
→ Huffman: Mã hóa với bảng Huffman
```

#### Bước 7: Lưu Trữ JPEG
```
Cấu trúc file JPEG:
- SOI (Start of Image): FFD8
- APP0 (JFIF header): FFE0
- DQT (Quantization Table): FFDB
- SOF (Start of Frame): FFC0
- DHT (Huffman Table): FFC4
- SOS (Start of Scan): FFDA
- Dữ liệu nén
- EOI (End of Image): FFD9
```

### Ưu Điểm JPEG
- Tỷ lệ nén rất cao (80-95%)
- Nhanh (xử lý song song)
- Phổ biến, hỗ trợ rộng rãi
- Chất lượng tốt ở mức nén cao

### Nhược Điểm JPEG
- Mất dữ liệu (không thể khôi phục hoàn toàn)
- Blocking artifacts ở chất lượng thấp
- Không hỗ trợ transparency
- Không tốt cho đồ họa với cạnh sắc

### Khi Nào Sử Dụng JPEG
- Ảnh chụp
- Ảnh phức tạp với nhiều màu
- Web (phổ biến)
- Khi cần tỷ lệ nén cao

---

## 2. PNG (Portable Network Graphics)

### Loại: Lossless (Không mất dữ liệu)
### Tỷ lệ nén: 10-30%
### Năm phát triển: 1996

### Quy Trình Nén PNG

#### Bước 1: Filtering
```
Áp dụng bộ lọc để tìm mẫu trong dữ liệu

5 loại bộ lọc:
1. None: Không lọc
   Filtered = Original

2. Sub: Hiệu với pixel bên trái
   Filtered = Original - Left

3. Up: Hiệu với pixel phía trên
   Filtered = Original - Up

4. Average: Hiệu với trung bình
   Filtered = Original - (Left + Up) / 2

5. Paeth: Dự đoán Paeth
   Filtered = Original - Paeth(Left, Up, LeftUp)

Lý do: Dữ liệu lọc có entropy thấp hơn, nén tốt hơn

Ví dụ:
Original: [100, 102, 101, 103, 105]
Sub:      [100, 2, -1, 2, 2]  (nhỏ hơn, nén tốt hơn)
```

#### Bước 2: DEFLATE Compression
```
Kết hợp LZ77 + Huffman coding

LZ77 (Lempel-Ziv-Welch):
- Tìm chuỗi lặp lại
- Thay thế bằng tham chiếu (offset, length)

Ví dụ:
Original: "ABCABCABC"
LZ77:     "ABC" + (3, 3) + (6, 3)
          (3 bytes + 2 tham chiếu = 7 bytes)

Huffman Coding:
- Gán mã ngắn cho ký tự phổ biến
- Gán mã dài cho ký tự hiếm

Ví dụ:
'A': 01 (2 bits)
'B': 10 (2 bits)
'C': 11 (2 bits)
```

### Ưu Điểm PNG
- Không mất dữ liệu (lossless)
- Hỗ trợ transparency (alpha channel)
- Tốt cho đồ họa, logo, ảnh cần chất lượng cao
- Phổ biến, hỗ trợ rộng rãi

### Nhược Điểm PNG
- Tỷ lệ nén thấp hơn JPEG (10-30%)
- File lớn hơn JPEG
- Chậm hơn JPEG
- Không tốt cho ảnh chụp phức tạp

### Khi Nào Sử Dụng PNG
- Đồ họa, logo
- Ảnh cần transparency
- Ảnh cần chất lượng hoàn hảo
- Ảnh với cạnh sắc

---

## 3. WebP

### Loại: Lossy/Lossless
### Tỷ lệ nén: 75-90% (lossy), 20-40% (lossless)
### Năm phát triển: 2010 (Google)

### WebP Lossy

#### Quy Trình
```
1. Prediction: Dự đoán pixel từ lân cận
2. Transform: DCT hoặc Walsh-Hadamard
3. Quantization: Lượng tử hóa
4. Entropy Coding: Arithmetic coding

Sử dụng VP8 codec (video codec)
```

#### Ưu Điểm
- Tỷ lệ nén tốt hơn JPEG 25-35%
- Chất lượng tốt hơn JPEG
- Hiện đại
- Hỗ trợ animation

#### Nhược Điểm
- Hỗ trợ trình duyệt chưa toàn bộ (cần fallback)
- Mất dữ liệu
- Chậm hơn JPEG

### WebP Lossless

#### Quy Trình
```
1. Prediction: Dự đoán pixel
2. Transform: Chuyển đổi không gian
3. Color Cache: Lưu cache màu
4. Entropy Coding: Huffman + LZ77
```

#### Ưu Điểm
- Không mất dữ liệu
- Tỷ lệ nén tốt hơn PNG 26%
- Hiện đại

#### Nhược Điểm
- Hỗ trợ trình duyệt chưa toàn bộ
- Chậm hơn PNG

### Khi Nào Sử Dụng WebP
- Web (tối ưu cho web)
- Mobile (file nhỏ)
- Ảnh chụp (lossy)
- Đồ họa (lossless)
- Animation

---

## 4. GIF (Graphics Interchange Format)

### Loại: Lossless
### Tỷ lệ nén: 5-20%
### Năm phát triển: 1987

### Quy Trình Nén GIF

#### Bước 1: Palette
```
Giới hạn 256 màu
Mỗi pixel được lưu trữ bằng 1 byte (0-255)

Ưu điểm: File nhỏ
Nhược điểm: Chất lượng kém cho ảnh phức tạp
```

#### Bước 2: LZW (Lempel-Ziv-Welch)
```
Nén dữ liệu palette

Ví dụ:
Original: [1, 2, 3, 1, 2, 3, 1, 2, 3]
LZW:      [1, 2, 3, 256, 256, 256]
          (256 = mã cho "1, 2, 3")
```

### Ưu Điểm GIF
- Hỗ trợ animation
- Phổ biến
- Đơn giản

### Nhược Điểm GIF
- Tối đa 256 màu
- Tỷ lệ nén thấp
- Lỗi thời

### Khi Nào Sử Dụng GIF
- Animation (nhưng WebP tốt hơn)
- Đồ họa đơn giản
- Ảnh cũ

---

## 5. Wavelet Compression

### Loại: Lossy/Lossless
### Tỷ lệ nén: Tùy thuộc
### Ứng dụng: JPEG2000, ảnh y tế

### Quy Trình

#### Bước 1: Wavelet Transform
```
Phân tích ảnh thành các thành phần tần số

Ưu điểm so với DCT:
- Ít blocking artifacts
- Tốt ở bitrate thấp
- Phân tích đa độ phân giải

Ví dụ:
LL (Low-Low): Thông tin chính
LH (Low-High): Chi tiết ngang
HL (High-Low): Chi tiết dọc
HH (High-High): Chi tiết đường chéo
```

#### Bước 2: Quantization
```
Lượng tử hóa các hệ số wavelet
```

#### Bước 3: Entropy Coding
```
Mã hóa entropy
```

### Ưu Điểm Wavelet
- Chất lượng tốt ở bitrate thấp
- Ít blocking artifacts
- Hỗ trợ cả lossy và lossless
- Tốt cho ảnh y tế

### Nhược Điểm Wavelet
- Chậm
- Phức tạp
- Hỗ trợ hạn chế

### Khi Nào Sử Dụng Wavelet
- Ảnh y tế
- Ảnh khoa học
- JPEG2000
- Khi cần chất lượng cao ở bitrate thấp

---

## So Sánh Các Thuật Toán

### Tỷ Lệ Nén
```
WebP Lossy (89%) > JPEG (87%) > WebP Lossless (83%) > PNG (20%) > GIF (10%)
```

### Chất Lượng
```
PNG (100%) = WebP Lossless (100%) > Wavelet (95%) > WebP Lossy (90%) > JPEG (85%) > GIF (70%)
```

### Tốc Độ
```
GIF (Nhanh) > JPEG (Nhanh) > PNG (Trung bình) > WebP (Chậm) > Wavelet (Rất chậm)
```

### Hỗ Trợ
```
JPEG (100%) = PNG (100%) = GIF (100%) > WebP (80%) > Wavelet (20%)
```

---

## Các Chỉ Số Chất Lượng

### PSNR (Peak Signal-to-Noise Ratio)
```
Công thức:
PSNR = 20 * log10(MAX / sqrt(MSE))

Giá trị điển hình:
- < 20 dB: Chất lượng kém
- 20-30 dB: Chất lượng trung bình
- 30-40 dB: Chất lượng tốt
- > 40 dB: Chất lượng rất tốt

Ưu điểm: Dễ tính toán
Nhược điểm: Không phản ánh chất lượng nhận thức tốt
```

### SSIM (Structural Similarity Index)
```
Công thức:
SSIM = (2*μx*μy + C1) * (2*σxy + C2) / ((μx² + μy² + C1) * (σx² + σy² + C2))

Giá trị:
- -1 đến 1 (1 = giống hệt)
- > 0.9: Rất tốt
- 0.8-0.9: Tốt
- 0.7-0.8: Trung bình
- < 0.7: Kém

Ưu điểm: Phản ánh chất lượng nhận thức tốt hơn PSNR
Nhược điểm: Tính toán phức tạp hơn
```

---

## Khuyến Nghị Chọn Định Dạng

| Loại Ảnh | Tốt Nhất | Thay Thế | Lý Do |
|---------|---------|---------|-------|
| Ảnh chụp | WebP Lossy | JPEG | Tỷ lệ nén tốt hơn 25-35% |
| Đồ họa | PNG | WebP Lossless | Không mất dữ liệu |
| Animation | WebP | GIF | File nhỏ hơn, chất lượng tốt hơn |
| Ảnh y tế | Wavelet | PNG | Chất lượng cao ở bitrate thấp |
| Web | WebP | JPEG + PNG | Tối ưu cho web |

---

## Tài Liệu Tham Khảo

- [JPEG Standard](https://en.wikipedia.org/wiki/JPEG)
- [PNG Specification](http://www.libpng.org/pub/png/)
- [WebP Format](https://developers.google.com/speed/webp)
- [Image Compression](https://en.wikipedia.org/wiki/Image_compression)
- [DCT Transform](https://en.wikipedia.org/wiki/Discrete_cosine_transform)
- [Wavelet Transform](https://en.wikipedia.org/wiki/Wavelet_transform)

# Hướng Dẫn Nhanh - Hệ Thống Nén Ảnh

## 🚀 Bắt Đầu Nhanh

### 1. Cài Đặt

```bash
# Clone hoặc tải project
cd image-compression-system

# Cài đặt dependencies
pip install -r requirements.txt
```

### 2. Chạy Demo

```bash
# Chạy menu chính
python run_demo.py

# Hoặc chạy từng script riêng
python compression_algorithms_analysis.py      # Phân tích thuật toán
python image_compression_system.py             # So sánh hiệu quả
python advanced_compression_comparison.py      # So sánh nâng cao
```

## 📊 Kết Quả Nhanh

### Ảnh Chụp (Photo)
```
✓ JPEG: 87.50% giảm
✓ PNG: 68.75% giảm
✓ WebP Lossy: 89.58% giảm ⭐ (Tốt nhất)
✓ WebP Lossless: 73.61% giảm
```

### Ảnh Đồ Họa (Graphic)
```
✓ JPEG: 77.78% giảm
✓ PNG: 80.56% giảm ⭐ (Tốt nhất)
✓ WebP Lossy: 82.64% giảm
✓ WebP Lossless: 83.33% giảm
```

### Ảnh Text
```
✓ JPEG: 72.22% giảm
✓ PNG: 86.11% giảm ⭐ (Tốt nhất)
✓ WebP Lossy: 75.69% giảm
✓ WebP Lossless: 87.50% giảm
```

## 💡 Khuyến Nghị Nhanh

| Loại Ảnh | Chọn | Lý Do |
|---------|------|-------|
| 📷 Ảnh chụp | WebP Lossy | Tỷ lệ nén cao, chất lượng tốt |
| 🎨 Đồ họa | PNG | Không mất dữ liệu, cạnh sắc |
| 📝 Text | PNG | Cạnh sắc, không mất dữ liệu |
| 🌐 Web | WebP | Tối ưu, file nhỏ |
| 🎬 Animation | WebP | Hỗ trợ animation, file nhỏ |

## 📁 Cấu Trúc Project

```
image-compression-system/
├── image_compression_system.py          # Hệ thống nén chính
├── compression_algorithms_analysis.py   # Phân tích thuật toán
├── advanced_compression_comparison.py   # So sánh nâng cao
├── run_demo.py                          # Menu chính
├── requirements.txt                     # Dependencies
├── README.md                            # Tài liệu đầy đủ
├── ALGORITHMS_DETAILED.md               # Chi tiết thuật toán
├── QUICK_START.md                       # File này
└── compression_results/                 # Kết quả nén
    ├── compressed_jpeg.jpg
    ├── compressed_png.png
    ├── compressed_webp_lossy.webp
    ├── compressed_webp_lossless.webp
    ├── compression_report.txt
    └── compression_results.json
```

## 🔍 Các Chỉ Số Chất Lượng

### PSNR (Peak Signal-to-Noise Ratio)
- Cao hơn = chất lượng tốt hơn
- Giá trị điển hình: 30-50 dB
- > 40 dB: Rất tốt

### SSIM (Structural Similarity)
- Giá trị từ -1 đến 1 (1 = giống hệt)
- > 0.9: Rất tốt
- 0.8-0.9: Tốt

## 🎯 Các Thuật Toán Chính

### JPEG (Lossy)
- Tỷ lệ nén: 80-95%
- Tốc độ: Rất nhanh
- Dùng cho: Ảnh chụp

### PNG (Lossless)
- Tỷ lệ nén: 10-30%
- Tốc độ: Trung bình
- Dùng cho: Đồ họa, logo

### WebP (Lossy/Lossless)
- Tỷ lệ nén: 75-90% (lossy), 20-40% (lossless)
- Tốc độ: Chậm
- Dùng cho: Web, mobile

### Wavelet (Lossy/Lossless)
- Tỷ lệ nén: Tùy thuộc
- Tốc độ: Rất chậm
- Dùng cho: Ảnh y tế, khoa học

## 📈 Hiệu Suất So Sánh

```
Tỷ lệ nén:
WebP Lossy (89%) > JPEG (87%) > WebP Lossless (83%) > PNG (20%)

Chất lượng:
PNG (100%) = WebP Lossless (100%) > WebP Lossy (90%) > JPEG (85%)

Tốc độ:
JPEG (Nhanh) > PNG (Trung bình) > WebP (Chậm)

Hỗ trợ:
JPEG (100%) = PNG (100%) > WebP (80%)
```

## 🛠️ Sử Dụng Trong Code

### Nén Ảnh
```python
from image_compression_system import ImageCompressionSystem

system = ImageCompressionSystem()
results = system.compress_all("image.jpg")
print(system.generate_report())
```

### Phân Tích Thuật Toán
```python
from compression_algorithms_analysis import CompressionAlgorithmsAnalysis

analysis = CompressionAlgorithmsAnalysis()
analysis.print_algorithms_comparison()
analysis.create_comparison_table()
```

### So Sánh Nâng Cao
```python
from advanced_compression_comparison import AdvancedCompressionComparison

comparison = AdvancedCompressionComparison()
comparison.run_comparison()
```

## ⚠️ Lưu Ý

- WebP cần hỗ trợ từ trình duyệt/ứng dụng
- Kết quả phụ thuộc vào loại ảnh
- Thời gian nén phụ thuộc vào kích thước ảnh
- Thử nghiệm nhiều mức nén để tìm cân bằng tốt nhất

## 📚 Tài Liệu Thêm

- `README.md`: Tài liệu đầy đủ
- `ALGORITHMS_DETAILED.md`: Chi tiết các thuật toán
- `compression_results/`: Kết quả nén

## ❓ Câu Hỏi Thường Gặp

**Q: Định dạng nào tốt nhất?**
A: Không có định dạng tốt nhất cho tất cả. Chọn dựa trên loại ảnh:
- Ảnh chụp: WebP Lossy
- Đồ họa: PNG
- Web: WebP

**Q: Làm sao để cân bằng chất lượng và kích thước?**
A: Sử dụng quality level 75-85 cho lossy, kiểm tra PSNR/SSIM.

**Q: WebP có được hỗ trợ rộng rãi không?**
A: Hầu hết trình duyệt hiện đại hỗ trợ, nhưng cần fallback cho cũ.

**Q: Nên sử dụng Wavelet khi nào?**
A: Cho ảnh y tế, khoa học, hoặc khi cần chất lượng cao ở bitrate thấp.

---

**Bắt đầu ngay:** `python run_demo.py`

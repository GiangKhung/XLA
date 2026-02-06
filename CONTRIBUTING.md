# 🤝 Hướng Dẫn Đóng Góp

Cảm ơn bạn đã quan tâm đến dự án này! Chúng tôi hoan nghênh các đóng góp từ cộng đồng.

## 📋 Quy Trình Đóng Góp

### 1. Fork Repository
```bash
# Truy cập GitHub và click "Fork"
# Hoặc sử dụng GitHub CLI
gh repo fork yourusername/image-compression-system
```

### 2. Clone Repository
```bash
git clone https://github.com/yourusername/image-compression-system.git
cd image-compression-system
```

### 3. Tạo Branch Mới
```bash
# Tạo branch cho feature hoặc bug fix
git checkout -b feature/your-feature-name
# hoặc
git checkout -b bugfix/your-bug-name
```

### 4. Thực Hiện Thay Đổi
- Viết code theo chuẩn PEP 8
- Thêm comments và docstrings
- Cập nhật tests nếu cần

### 5. Test Code
```bash
# Chạy tests
python test_compression_algorithms.py

# Hoặc chạy Flask app
python app.py
```

### 6. Commit Changes
```bash
git add .
git commit -m "Add feature: description of changes"
```

### 7. Push to GitHub
```bash
git push origin feature/your-feature-name
```

### 8. Tạo Pull Request
- Truy cập GitHub
- Click "Compare & pull request"
- Mô tả thay đổi của bạn
- Submit PR

## 📝 Hướng Dẫn Viết Code

### Python Style Guide
- Tuân theo PEP 8
- Sử dụng 4 spaces cho indentation
- Tối đa 79 ký tự mỗi dòng
- Thêm docstrings cho tất cả functions

### Ví Dụ:
```python
def compress_data(data: bytes) -> bytes:
    """
    Nén dữ liệu sử dụng RLC.
    
    Args:
        data: Dữ liệu cần nén
        
    Returns:
        Dữ liệu đã nén
        
    Raises:
        ValueError: Nếu dữ liệu rỗng
    """
    if not data:
        raise ValueError("Dữ liệu không được rỗng")
    
    # Thực hiện nén
    return compressed_data
```

### JavaScript Style Guide
- Sử dụng 2 spaces cho indentation
- Sử dụng const/let thay vì var
- Thêm comments cho logic phức tạp

### CSS Style Guide
- Sử dụng kebab-case cho class names
- Tổ chức properties theo thứ tự: layout, display, color, font, etc.

## 🐛 Báo Cáo Bug

### Tạo Issue
1. Truy cập GitHub Issues
2. Click "New Issue"
3. Chọn "Bug report"
4. Điền thông tin:
   - **Title**: Mô tả ngắn gọn
   - **Description**: Chi tiết bug
   - **Steps to Reproduce**: Cách tái hiện
   - **Expected Behavior**: Hành vi mong đợi
   - **Actual Behavior**: Hành vi thực tế
   - **Environment**: OS, Python version, etc.

### Ví Dụ:
```
Title: RLC compression fails with empty data

Description:
RLC compression throws an error when given empty bytes.

Steps to Reproduce:
1. Call RLCCompression.encode(b'')
2. Observe error

Expected Behavior:
Should return empty bytes

Actual Behavior:
Throws IndexError

Environment:
- OS: Windows 10
- Python: 3.11
```

## 💡 Đề Xuất Tính Năng

### Tạo Feature Request
1. Truy cập GitHub Issues
2. Click "New Issue"
3. Chọn "Feature request"
4. Điền thông tin:
   - **Title**: Tên tính năng
   - **Description**: Mô tả chi tiết
   - **Use Case**: Trường hợp sử dụng
   - **Proposed Solution**: Giải pháp đề xuất

### Ví Dụ:
```
Title: Add LZMA compression algorithm

Description:
LZMA is a modern compression algorithm with better ratio than LZW.

Use Case:
Users want to compress large files with better ratio.

Proposed Solution:
Add LZMACompression class similar to LZWCompression.
```

## 📚 Cấu Trúc Dự Án

```
image-compression-system/
├── app.py                          # Flask app chính
├── compression_algorithms_impl.py  # Triển khai thuật toán
├── test_compression_algorithms.py  # Tests
├── requirements-web.txt            # Dependencies
├── Dockerfile                      # Docker config
├── docker-compose.yml              # Docker compose
├── templates/
│   └── index.html                  # Giao diện web
├── static/
│   ├── css/
│   │   └── style.css               # CSS
│   └── js/
│       └── main.js                 # JavaScript
├── uploads/                        # Ảnh tải lên
├── compression_results/            # Ảnh nén
├── README.md                       # Tài liệu
├── ALGORITHMS_DETAILED.md          # Chi tiết thuật toán
└── CONTRIBUTING.md                 # Hướng dẫn này
```

## 🧪 Chạy Tests

```bash
# Chạy tất cả tests
python test_compression_algorithms.py

# Chạy Flask app
python app.py

# Chạy với Docker
docker-compose up
```

## 📖 Tài Liệu

- [README.md](README.md) - Tài liệu chính
- [ALGORITHMS_DETAILED.md](ALGORITHMS_DETAILED.md) - Chi tiết thuật toán

## 🎯 Các Lĩnh Vực Cần Đóng Góp

- ✅ Thêm thuật toán nén mới
- ✅ Cải thiện hiệu suất
- ✅ Cải thiện giao diện web
- ✅ Thêm tests
- ✅ Cải thiện tài liệu
- ✅ Sửa bugs
- ✅ Tối ưu hóa code

## 📞 Liên Hệ

Nếu bạn có câu hỏi, vui lòng:
- Mở issue trên GitHub
- Gửi email cho maintainers
- Tham gia discussions

## 📄 License

Bằng cách đóng góp, bạn đồng ý rằng các đóng góp của bạn sẽ được cấp phép dưới MIT License.

---

**Cảm ơn bạn đã đóng góp!** 🎉

# Hướng Dẫn Đóng Góp

Cảm ơn bạn quan tâm đến dự án này! Dưới đây là hướng dẫn để đóng góp.

## 🚀 Cách Bắt Đầu

### 1. Fork Repository
Nhấp nút "Fork" trên GitHub

### 2. Clone Repository
```bash
git clone https://github.com/your-username/image-compression-system.git
cd image-compression-system
```

### 3. Tạo Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Cài Đặt Dependencies
```bash
python -m pip install -r requirements-web.txt
```

### 5. Thực Hiện Thay Đổi
- Sửa code
- Thêm tính năng
- Cải thiện tài liệu

### 6. Commit Changes
```bash
git add .
git commit -m "Add: mô tả thay đổi"
```

### 7. Push to GitHub
```bash
git push origin feature/your-feature-name
```

### 8. Tạo Pull Request
- Vào GitHub
- Nhấp "New Pull Request"
- Mô tả thay đổi của bạn

## 📝 Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

### Types
- **feat**: Tính năng mới
- **fix**: Sửa lỗi
- **docs**: Cập nhật tài liệu
- **style**: Định dạng code
- **refactor**: Tái cấu trúc code
- **test**: Thêm test
- **chore**: Cập nhật dependencies

### Ví Dụ
```
feat: Add AVIF compression support

- Implement AVIF compression algorithm
- Add AVIF to comparison table
- Update documentation

Closes #123
```

## 🎯 Các Lĩnh Vực Cần Đóng Góp

### Code
- [ ] Thêm định dạng nén mới (AVIF, HEIF)
- [ ] Tối ưu hóa hiệu suất
- [ ] Sửa lỗi
- [ ] Cải thiện UI/UX

### Tài Liệu
- [ ] Dịch sang ngôn ngữ khác
- [ ] Cải thiện hướng dẫn
- [ ] Thêm ví dụ
- [ ] Sửa lỗi chính tả

### Testing
- [ ] Viết unit tests
- [ ] Viết integration tests
- [ ] Kiểm tra trên nhiều trình duyệt

## 📋 Checklist Trước Khi Submit PR

- [ ] Code tuân theo style guide
- [ ] Tài liệu được cập nhật
- [ ] Tests pass
- [ ] Không có lỗi lint
- [ ] Commit messages rõ ràng

## 🐛 Báo Cáo Lỗi

### Tạo Issue
1. Vào "Issues"
2. Nhấp "New Issue"
3. Chọn template phù hợp
4. Điền thông tin chi tiết

### Thông Tin Cần Cung Cấp
- Mô tả lỗi
- Cách tái hiện
- Kết quả mong đợi
- Kết quả thực tế
- Môi trường (OS, Python version, etc.)

## 💡 Gợi Ý Tính Năng

### Tạo Discussion
1. Vào "Discussions"
2. Nhấp "New Discussion"
3. Mô tả ý tưởng của bạn

## 📚 Tài Liệu Phát Triển

### Cấu Trúc Dự Án
```
image-compression-system/
├── app.py                    # Flask app
├── templates/                # HTML templates
├── static/                   # CSS, JS
├── *.py                      # Python scripts
└── docs/                     # Tài liệu
```

### Chạy Locally
```bash
python app.py
# Mở http://localhost:5000
```

### Chạy Tests
```bash
python -m pytest
```

## 🎓 Học Thêm

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)

## 📞 Liên Hệ

- Tạo Issue cho câu hỏi
- Tạo Discussion cho thảo luận
- Email: [your-email@example.com]

## 📄 Giấy Phép

Bằng cách đóng góp, bạn đồng ý rằng đóng góp của bạn sẽ được cấp phép dưới MIT License.

---

Cảm ơn bạn đã đóng góp! 🙏

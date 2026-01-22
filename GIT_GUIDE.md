# 📚 Hướng Dẫn Push Lên Git

## 🚀 Bước 1: Tạo Repository Trên GitHub

1. Truy cập [GitHub](https://github.com)
2. Nhấp **"New"** để tạo repository mới
3. Điền thông tin:
   - **Repository name**: `image-compression-system`
   - **Description**: `A comprehensive image compression system with web interface`
   - **Public** hoặc **Private** (tùy chọn)
   - ✅ Không chọn "Initialize with README" (vì đã có)
4. Nhấp **"Create repository"**

---

## 🔧 Bước 2: Cấu Hình Git Locally

### Nếu Chưa Cài Git

Tải từ: https://git-scm.com/download/win

### Cấu Hình Git

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@gmail.com"
```

---

## 📤 Bước 3: Push Lên GitHub

### Cách 1: Từ Thư Mục Dự Án (Khuyến Nghị)

```bash
# 1. Vào thư mục dự án
cd D:\NENANH

# 2. Khởi tạo Git repository
git init

# 3. Thêm tất cả file
git add .

# 4. Commit
git commit -m "Initial commit: Add image compression system"

# 5. Thêm remote repository
git remote add origin https://github.com/your-username/image-compression-system.git

# 6. Đổi tên branch (nếu cần)
git branch -M main

# 7. Push lên GitHub
git push -u origin main
```

### Cách 2: Sử Dụng GitHub Desktop

1. Tải [GitHub Desktop](https://desktop.github.com)
2. Mở GitHub Desktop
3. Nhấp **"File"** → **"Clone Repository"**
4. Chọn repository vừa tạo
5. Chọn thư mục lưu
6. Nhấp **"Clone"**
7. Copy file dự án vào thư mục
8. Commit và Push

---

## 📝 Bước 4: Commit Messages

### Format Chuẩn

```
<type>: <subject>

<body>

<footer>
```

### Ví Dụ

```bash
git commit -m "feat: Add image compression system

- Implement Flask web app
- Add 4 compression methods (JPEG, PNG, WebP)
- Add detailed documentation
- Add responsive UI

Closes #1"
```

### Types
- **feat**: Tính năng mới
- **fix**: Sửa lỗi
- **docs**: Cập nhật tài liệu
- **style**: Định dạng code
- **refactor**: Tái cấu trúc
- **test**: Thêm test
- **chore**: Cập nhật dependencies

---

## 🔄 Bước 5: Cập Nhật Sau Này

### Thêm Thay Đổi

```bash
# 1. Xem trạng thái
git status

# 2. Thêm file
git add .

# 3. Commit
git commit -m "fix: Update compression algorithm"

# 4. Push
git push origin main
```

### Tạo Branch Mới

```bash
# 1. Tạo branch
git checkout -b feature/new-feature

# 2. Thực hiện thay đổi
# ... edit files ...

# 3. Commit
git add .
git commit -m "feat: Add new feature"

# 4. Push
git push origin feature/new-feature

# 5. Tạo Pull Request trên GitHub
```

---

## 🎯 Các File Quan Trọng Để Push

✅ **Bắt buộc**
- `app.py` - Flask app
- `templates/index.html` - HTML
- `static/css/style.css` - CSS
- `static/js/main.js` - JavaScript
- `requirements-web.txt` - Dependencies
- `README.md` - Tài liệu
- `.gitignore` - Git ignore

✅ **Khuyến Nghị**
- `LICENSE` - Giấy phép
- `CONTRIBUTING.md` - Hướng dẫn đóng góp
- `CHANGELOG.md` - Lịch sử thay đổi
- `INSTALLATION.md` - Hướng dẫn cài đặt
- `Dockerfile` - Docker config
- `docker-compose.yml` - Docker compose
- `.env.example` - Ví dụ biến môi trường
- `.github/workflows/` - CI/CD

❌ **Không Push** (trong .gitignore)
- `uploads/` - Ảnh tải lên
- `compression_results/` - Kết quả nén
- `venv/` - Virtual environment
- `__pycache__/` - Python cache
- `.env` - Biến môi trường thực

---

## 🔐 Xác Thực GitHub

### Sử Dụng HTTPS (Dễ Nhất)

```bash
git push origin main
# Nhập username và password (hoặc token)
```

### Sử Dụng SSH (An Toàn Hơn)

1. Tạo SSH key:
```bash
ssh-keygen -t ed25519 -C "your-email@gmail.com"
```

2. Thêm vào GitHub:
   - Vào Settings → SSH and GPG keys
   - Nhấp "New SSH key"
   - Paste public key

3. Push:
```bash
git push origin main
```

---

## 📊 Kiểm Tra Trên GitHub

1. Vào repository trên GitHub
2. Xem file đã push
3. Xem commit history
4. Xem README

---

## 🆘 Khắc Phục Sự Cố

### Lỗi: "fatal: not a git repository"

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/image-compression-system.git
git push -u origin main
```

### Lỗi: "fatal: The current branch main has no upstream branch"

```bash
git push -u origin main
```

### Lỗi: "Permission denied (publickey)"

Sử dụng HTTPS thay vì SSH:
```bash
git remote set-url origin https://github.com/your-username/image-compression-system.git
```

### Lỗi: "fatal: remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/your-username/image-compression-system.git
```

---

## 📋 Checklist Trước Push

- [ ] Tất cả file đã thêm
- [ ] Commit message rõ ràng
- [ ] .gitignore đúng
- [ ] README.md cập nhật
- [ ] LICENSE thêm
- [ ] CONTRIBUTING.md thêm
- [ ] Không có file nhạy cảm

---

## 🎉 Hoàn Thành!

Sau khi push thành công:

1. ✅ Repository trên GitHub
2. ✅ Tất cả file đã push
3. ✅ Sẵn sàng chia sẻ
4. ✅ Sẵn sàng nhận đóng góp

---

## 📚 Tài Liệu Thêm

- [GitHub Docs](https://docs.github.com)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

---

**Chúc bạn push thành công!** 🚀

# 🚀 Hướng Dẫn Push Lên GitHub

Hướng dẫn chi tiết để push dự án lên GitHub.

## 📋 Chuẩn Bị

### 1. Kiểm Tra Git Configuration

```bash
# Kiểm tra user name
git config --global user.name

# Kiểm tra email
git config --global user.email

# Nếu chưa cấu hình
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2. Kiểm Tra Repository

```bash
# Xem status
git status

# Xem log
git log --oneline -5

# Xem remote
git remote -v
```

## 🔧 Cấu Hình Repository

### 1. Tạo Repository Trên GitHub

1. Truy cập https://github.com/new
2. Điền thông tin:
   - **Repository name:** image-compression-system
   - **Description:** Interactive web system for comparing image compression algorithms
   - **Public/Private:** Public
   - **Initialize with:** Không chọn (vì đã có local repo)
3. Click "Create repository"

### 2. Thêm Remote

```bash
# Thêm remote origin
git remote add origin https://github.com/yourusername/image-compression-system.git

# Hoặc nếu đã có
git remote set-url origin https://github.com/yourusername/image-compression-system.git

# Kiểm tra
git remote -v
```

## 📝 Commit Changes

### 1. Kiểm Tra Status

```bash
git status
```

### 2. Thêm Tất Cả Files

```bash
# Thêm tất cả files
git add .

# Hoặc thêm từng file
git add README.md
git add app.py
# ...

# Kiểm tra
git status
```

### 3. Commit

```bash
# Commit với message chi tiết
git commit -m "Initial commit: Image Compression System v1.0.0

- Implement 4 image compression algorithms (JPEG, PNG, WebP Lossy, WebP Lossless)
- Implement 3 general-purpose compression algorithms (RLC, Huffman, LZW)
- Create interactive web interface with 3 tabs
- Add API endpoints for compression
- Add Docker support (Dockerfile, docker-compose.yml)
- Add comprehensive documentation (README, ALGORITHMS_DETAILED, CONTRIBUTING, INSTALL, CHANGELOG)
- Add tests for all compression algorithms
- Add responsive web design with emoji icons
- Add PSNR and SSIM quality metrics"

# Hoặc commit đơn giản
git commit -m "Initial commit: Image Compression System v1.0.0"
```

## 🚀 Push Lên GitHub

### 1. Push Branch Main

```bash
# Push lần đầu tiên
git push -u origin main

# Hoặc nếu branch là master
git push -u origin master

# Lần sau chỉ cần
git push
```

### 2. Kiểm Tra Trên GitHub

1. Truy cập https://github.com/yourusername/image-compression-system
2. Kiểm tra:
   - ✅ Tất cả files đã được push
   - ✅ README.md hiển thị đúng
   - ✅ Commit message hiển thị

## 📌 Tạo Release

### 1. Tạo Tag

```bash
# Tạo tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag
git push origin v1.0.0

# Hoặc push tất cả tags
git push origin --tags
```

### 2. Tạo Release Trên GitHub

1. Truy cập https://github.com/yourusername/image-compression-system/releases
2. Click "Create a new release"
3. Điền thông tin:
   - **Tag version:** v1.0.0
   - **Release title:** Image Compression System v1.0.0
   - **Description:**
     ```
     ## Features
     - 4 image compression algorithms (JPEG, PNG, WebP)
     - 3 general-purpose compression algorithms (RLC, Huffman, LZW)
     - Interactive web interface
     - API endpoints
     - Docker support
     - Comprehensive documentation
     
     ## Installation
     See [INSTALL.md](INSTALL.md) for detailed instructions.
     
     ## Documentation
     - [README.md](README.md) - Main documentation
     - [ALGORITHMS_DETAILED.md](ALGORITHMS_DETAILED.md) - Algorithm details
     - [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guide
     ```
4. Click "Publish release"

## 🔐 Cấu Hình SSH (Tùy Chọn)

### 1. Tạo SSH Key

```bash
# Tạo SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Hoặc RSA
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Nhấn Enter để chấp nhận vị trí mặc định
# Nhập passphrase (tùy chọn)
```

### 2. Thêm SSH Key Vào GitHub

1. Copy SSH key:
   ```bash
   # macOS
   pbcopy < ~/.ssh/id_ed25519.pub
   
   # Linux
   cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard
   
   # Windows
   type %USERPROFILE%\.ssh\id_ed25519.pub | clip
   ```

2. Truy cập https://github.com/settings/keys
3. Click "New SSH key"
4. Paste key và click "Add SSH key"

### 3. Sử Dụng SSH

```bash
# Thay đổi remote từ HTTPS sang SSH
git remote set-url origin git@github.com:yourusername/image-compression-system.git

# Kiểm tra
git remote -v
```

## 🔄 Cập Nhật Repository

### 1. Thêm Changes

```bash
# Xem changes
git status

# Thêm files
git add .

# Commit
git commit -m "Update: description of changes"

# Push
git push
```

### 2. Tạo Branch Mới

```bash
# Tạo branch
git checkout -b feature/new-feature

# Thực hiện changes
# ...

# Commit
git add .
git commit -m "Add new feature"

# Push
git push -u origin feature/new-feature

# Tạo Pull Request trên GitHub
```

## 📊 Kiểm Tra Repository

### 1. Xem Commit History

```bash
# Xem log
git log --oneline

# Xem log chi tiết
git log --pretty=format:"%h - %an, %ar : %s"

# Xem graph
git log --graph --oneline --all
```

### 2. Xem Files

```bash
# Liệt kê files
git ls-files

# Xem size
git ls-files -s
```

### 3. Xem Remote

```bash
# Xem remote
git remote -v

# Xem chi tiết remote
git remote show origin
```

## 🐛 Khắc Phục Sự Cố

### Lỗi: "fatal: not a git repository"

```bash
# Giải pháp: Khởi tạo git
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/image-compression-system.git
git push -u origin main
```

### Lỗi: "fatal: The current branch main has no upstream branch"

```bash
# Giải pháp: Đặt upstream
git push -u origin main
```

### Lỗi: "fatal: Authentication failed"

```bash
# Giải pháp 1: Kiểm tra credentials
git config --global user.name
git config --global user.email

# Giải pháp 2: Sử dụng SSH
git remote set-url origin git@github.com:yourusername/image-compression-system.git

# Giải pháp 3: Cập nhật token
# Truy cập https://github.com/settings/tokens
# Tạo personal access token
# Sử dụng token làm password
```

### Lỗi: "fatal: refusing to merge unrelated histories"

```bash
# Giải pháp: Cho phép merge
git pull origin main --allow-unrelated-histories
git push origin main
```

## ✅ Checklist Trước Push

- [x] Tất cả files đã được thêm
- [x] Commit message rõ ràng
- [x] Git config đúng
- [x] Remote URL đúng
- [x] Không có uncommitted changes
- [x] README.md đầy đủ
- [x] .gitignore cấu hình đúng
- [x] LICENSE file có sẵn
- [x] Tài liệu đầy đủ
- [x] Tests chạy thành công

## 📚 Tài Liệu Thêm

- [GitHub Docs](https://docs.github.com)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub CLI](https://cli.github.com)

## 🎉 Hoàn Thành

Sau khi push thành công:

1. ✅ Repository đã được tạo trên GitHub
2. ✅ Tất cả files đã được push
3. ✅ README.md hiển thị đúng
4. ✅ Sẵn sàng cho collaborators
5. ✅ Sẵn sàng cho pull requests

---

**Chúc mừng! Dự án của bạn đã được push lên GitHub!** 🎉

Bây giờ bạn có thể:
- Chia sẻ link repository
- Mời collaborators
- Nhận pull requests
- Theo dõi issues
- Tạo releases

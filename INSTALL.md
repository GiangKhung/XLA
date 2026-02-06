# 📦 Hướng Dẫn Cài Đặt

Hướng dẫn chi tiết để cài đặt và chạy Image Compression System.

## 📋 Yêu Cầu Hệ Thống

### Tối Thiểu
- Python 3.11+
- pip (Python package manager)
- 2GB RAM
- 500MB disk space

### Khuyến Nghị
- Python 3.12+
- 4GB RAM
- 1GB disk space
- Docker (tùy chọn)

## 🖥️ Cài Đặt Cục Bộ

### 1. Cài Đặt Python

#### Windows
```bash
# Tải từ https://www.python.org/downloads/
# Hoặc sử dụng Chocolatey
choco install python

# Kiểm tra
python --version
```

#### macOS
```bash
# Sử dụng Homebrew
brew install python@3.11

# Kiểm tra
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
# Cập nhật package manager
sudo apt update

# Cài đặt Python
sudo apt install python3.11 python3-pip

# Kiểm tra
python3 --version
```

### 2. Clone Repository

```bash
# Sử dụng Git
git clone https://github.com/yourusername/image-compression-system.git
cd image-compression-system

# Hoặc tải ZIP
# Giải nén và mở terminal trong thư mục
```

### 3. Tạo Virtual Environment

#### Windows
```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt
venv\Scripts\activate
```

#### macOS/Linux
```bash
# Tạo virtual environment
python3 -m venv venv

# Kích hoạt
source venv/bin/activate
```

### 4. Cài Đặt Dependencies

```bash
# Cập nhật pip
pip install --upgrade pip

# Cài đặt requirements
pip install -r requirements-web.txt
```

### 5. Cấu Hình Ứng Dụng

```bash
# Tạo file .env từ .env.example
cp .env.example .env

# Chỉnh sửa .env nếu cần
# Mở .env và cập nhật các giá trị
```

### 6. Chạy Ứng Dụng

```bash
# Chạy Flask app
python app.py

# Hoặc sử dụng Flask CLI
flask run

# Hoặc chạy với Gunicorn (production)
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### 7. Truy Cập Web

Mở trình duyệt và truy cập:
```
http://localhost:5000
```

## 🐳 Cài Đặt Docker

### 1. Cài Đặt Docker

#### Windows
```bash
# Tải Docker Desktop từ https://www.docker.com/products/docker-desktop
# Hoặc sử dụng Chocolatey
choco install docker-desktop
```

#### macOS
```bash
# Sử dụng Homebrew
brew install docker

# Hoặc tải Docker Desktop
# https://www.docker.com/products/docker-desktop
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install docker.io docker-compose

# Thêm user vào docker group
sudo usermod -aG docker $USER
```

### 2. Build Docker Image

```bash
# Build image
docker-compose build

# Hoặc build manual
docker build -t image-compression-system .
```

### 3. Chạy Docker Container

```bash
# Chạy container
docker-compose up

# Hoặc chạy background
docker-compose up -d

# Hoặc chạy manual
docker run -p 5000:5000 -v $(pwd)/uploads:/app/uploads image-compression-system
```

### 4. Truy Cập Web

```
http://localhost:5000
```

### 5. Dừng Container

```bash
# Dừng container
docker-compose down

# Hoặc
docker stop <container-id>
```

## 🧪 Test Cài Đặt

### Chạy Tests

```bash
# Chạy test compression algorithms
python test_compression_algorithms.py

# Output mẫu:
# ================================================================================
# TEST CÁC THUẬT TOÁN NÉN
# ================================================================================
# 
# Dữ liệu test: 2600 bytes
# 
# Thuật toán       Kích thước       Tỷ lệ        Encode       Decode       OK
# --------------------------------------------------------------------------------
# RLC             1300            50.00%    0.000123s    0.000089s    True
# Huffman         325             87.50%    0.001234s    0.000567s    True
# LZW             520             80.00%    0.000456s    0.000234s    True
```

### Kiểm Tra Web App

```bash
# Mở trình duyệt
# Truy cập http://localhost:5000

# Kiểm tra:
# 1. Trang chủ tải được
# 2. Có thể tải ảnh lên
# 3. Có thể nén ảnh
# 4. Có thể xem kết quả
```

## 🔧 Cấu Hình Nâng Cao

### Thay Đổi Port

```bash
# Trong .env
PORT=8000

# Hoặc chạy trực tiếp
python app.py --port 8000
```

### Thay Đổi Thư Mục Upload

```bash
# Trong .env
UPLOAD_FOLDER=/path/to/uploads
RESULTS_FOLDER=/path/to/results

# Hoặc tạo thư mục
mkdir -p uploads compression_results
```

### Cấu Hình HTTPS

```bash
# Tạo certificate
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

# Chạy với HTTPS
python app.py --ssl-context=adhoc
```

## 🐛 Khắc Phục Sự Cố

### Lỗi: "ModuleNotFoundError: No module named 'flask'"

```bash
# Giải pháp: Cài đặt dependencies
pip install -r requirements-web.txt
```

### Lỗi: "Port 5000 already in use"

```bash
# Giải pháp 1: Sử dụng port khác
python app.py --port 8000

# Giải pháp 2: Tìm process sử dụng port
# Windows
netstat -ano | findstr :5000

# macOS/Linux
lsof -i :5000

# Giết process
# Windows
taskkill /PID <PID> /F

# macOS/Linux
kill -9 <PID>
```

### Lỗi: "Permission denied" (Linux/macOS)

```bash
# Giải pháp: Cấp quyền
chmod +x app.py
chmod -R 755 uploads compression_results
```

### Lỗi: "Docker daemon not running"

```bash
# Giải pháp: Khởi động Docker
# Windows/macOS: Mở Docker Desktop

# Linux
sudo systemctl start docker
```

## 📊 Kiểm Tra Cài Đặt

```bash
# Kiểm tra Python
python --version

# Kiểm tra pip
pip --version

# Kiểm tra Flask
python -c "import flask; print(flask.__version__)"

# Kiểm tra OpenCV
python -c "import cv2; print(cv2.__version__)"

# Kiểm tra Pillow
python -c "import PIL; print(PIL.__version__)"

# Kiểm tra Docker
docker --version
docker-compose --version
```

## 🚀 Chạy Production

### Sử dụng Gunicorn

```bash
# Cài đặt Gunicorn
pip install gunicorn

# Chạy với 4 workers
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Hoặc với Nginx
# Xem hướng dẫn Nginx configuration
```

### Sử dụng Docker

```bash
# Build production image
docker build -t image-compression-system:latest .

# Chạy container
docker run -d -p 5000:5000 \
  -v $(pwd)/uploads:/app/uploads \
  -v $(pwd)/compression_results:/app/compression_results \
  image-compression-system:latest
```

## 📚 Tài Liệu Thêm

- [README.md](README.md) - Tài liệu chính
- [ALGORITHMS_DETAILED.md](ALGORITHMS_DETAILED.md) - Chi tiết thuật toán
- [CONTRIBUTING.md](CONTRIBUTING.md) - Hướng dẫn đóng góp

## 💬 Hỗ Trợ

Nếu bạn gặp vấn đề:

1. Kiểm tra [Troubleshooting](#-khắc-phục-sự-cố) section
2. Mở issue trên GitHub
3. Liên hệ với maintainers

---

**Cập nhật lần cuối:** 2026-02-04

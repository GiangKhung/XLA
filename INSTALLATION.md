# Hướng Dẫn Cài Đặt

## 📋 Yêu Cầu

- Python 3.7+
- pip (Python package manager)
- Git (để clone repository)

## 🚀 Cài Đặt Cơ Bản

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/image-compression-system.git
cd image-compression-system
```

### 2. Tạo Virtual Environment (Khuyến Nghị)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Cài Đặt Dependencies

```bash
pip install -r requirements-web.txt
```

### 4. Chạy Web App

```bash
python app.py
```

Mở trình duyệt: **http://localhost:5000**

---

## 🐳 Cài Đặt Với Docker

### 1. Cài Đặt Docker

- [Docker Desktop](https://www.docker.com/products/docker-desktop)

### 2. Build Image

```bash
docker build -t image-compression-system .
```

### 3. Chạy Container

```bash
docker run -p 5000:5000 image-compression-system
```

Mở trình duyệt: **http://localhost:5000**

### 4. Sử Dụng Docker Compose

```bash
docker-compose up
```

---

## 🔧 Cài Đặt Nâng Cao

### Tạo File .env

```bash
cp .env.example .env
```

Chỉnh sửa `.env` theo nhu cầu của bạn.

### Cài Đặt Development Dependencies

```bash
pip install -r requirements-web.txt
pip install pytest pytest-cov flake8 black
```

### Chạy Tests

```bash
pytest
```

### Chạy Linter

```bash
flake8 .
```

### Format Code

```bash
black .
```

---

## 🌐 Triển Khai Trực Tuyến

### Heroku

1. Cài đặt [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

2. Tạo Procfile:
```
web: gunicorn app:app
```

3. Deploy:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### PythonAnywhere

1. Tạo tài khoản tại [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload file lên
3. Cấu hình Web app
4. Reload

### AWS

1. Tạo EC2 instance
2. SSH vào instance
3. Clone repository
4. Cài đặt dependencies
5. Chạy app

### Google Cloud

1. Tạo Cloud Run service
2. Deploy container
3. Cấu hình domain

---

## 🐛 Khắc Phục Sự Cố

### Lỗi: "ModuleNotFoundError"

```bash
pip install -r requirements-web.txt
```

### Lỗi: "Address already in use"

Cổng 5000 đang sử dụng. Thay đổi cổng:

```bash
python app.py --port 5001
```

### Lỗi: "WebP not supported"

```bash
pip install --upgrade Pillow
```

### Lỗi: "OpenCV not found"

```bash
pip install opencv-python
```

---

## 📝 Cấu Hình

### Thay Đổi Cổng

Mở `app.py` và thay đổi:

```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Thay 5001 bằng cổng khác
```

### Thay Đổi Kích Thước File Tối Đa

Mở `app.py` và thay đổi:

```python
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB
```

### Thay Đổi Quality Nén

Mở `app.py` và tìm:

```python
cv2.imwrite(jpeg_path, img, [cv2.IMWRITE_JPEG_QUALITY, 85])  # Thay 85
img.save(webp_lossy_path, 'WEBP', quality=85)  # Thay 85
```

---

## 📚 Tài Liệu Thêm

- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Docker Documentation](https://docs.docker.com/)

---

## 🆘 Hỗ Trợ

- Tạo Issue trên GitHub
- Tạo Discussion
- Email: your-email@example.com

---

**Chúc bạn cài đặt thành công!** 🎉

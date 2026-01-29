"""
Flask app cho hệ thống nén ảnh web
"""

from flask import Flask, render_template, request, jsonify, send_file, url_for, send_from_directory
import os
import cv2
import numpy as np
from PIL import Image
import time
import json
from pathlib import Path
from io import BytesIO
import base64
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULTS_FOLDER'] = 'compression_results'

# Tạo thư mục
Path(app.config['UPLOAD_FOLDER']).mkdir(exist_ok=True)
Path(app.config['RESULTS_FOLDER']).mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def calculate_psnr(original, compressed):
    """Tính PSNR"""
    mse = np.mean((original.astype(float) - compressed.astype(float)) ** 2)
    if mse == 0:
        return 100.0
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

def calculate_ssim(original, compressed):
    """Tính SSIM"""
    try:
        from skimage.metrics import structural_similarity as ssim
        
        if len(original.shape) == 3:
            original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
            compressed_gray = cv2.cvtColor(compressed, cv2.COLOR_BGR2GRAY)
        else:
            original_gray = original
            compressed_gray = compressed
        
        return ssim(original_gray, compressed_gray, data_range=255)
    except:
        return 0.0

def get_file_size(file_path):
    """Lấy kích thước file"""
    return os.path.getsize(file_path)

def image_to_base64(image_path):
    """Chuyển ảnh thành base64"""
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

@app.route('/')
def index():
    """Trang chủ"""
    return render_template('index.html')

@app.route('/api/algorithms')
def get_algorithms():
    """Lấy danh sách thuật toán"""
    algorithms = [
        {
            'id': 'jpeg',
            'name': 'JPEG',
            'type': 'Lossy',
            'ratio': '80-95%',
            'speed': 'Rất nhanh',
            'quality': 'Tốt',
            'support': 'Toàn bộ',
            'description': 'Sử dụng DCT, tốt cho ảnh chụp',
            'advantages': ['Tỷ lệ nén cao', 'Nhanh', 'Phổ biến'],
            'disadvantages': ['Mất dữ liệu', 'Blocking artifacts']
        },
        {
            'id': 'png',
            'name': 'PNG',
            'type': 'Lossless',
            'ratio': '10-30%',
            'speed': 'Trung bình',
            'quality': 'Hoàn hảo',
            'support': 'Toàn bộ',
            'description': 'Sử dụng DEFLATE, tốt cho đồ họa',
            'advantages': ['Không mất dữ liệu', 'Transparency', 'Lossless'],
            'disadvantages': ['File lớn', 'Chậm hơn JPEG']
        },
        {
            'id': 'webp_lossy',
            'name': 'WebP Lossy',
            'type': 'Lossy',
            'ratio': '75-90%',
            'speed': 'Chậm',
            'quality': 'Rất tốt',
            'support': 'Hạn chế',
            'description': 'Tỷ lệ nén tốt hơn JPEG 25-35%',
            'advantages': ['Tỷ lệ nén cao', 'Chất lượng tốt', 'Hiện đại'],
            'disadvantages': ['Hỗ trợ hạn chế', 'Chậm']
        },
        {
            'id': 'webp_lossless',
            'name': 'WebP Lossless',
            'type': 'Lossless',
            'ratio': '20-40%',
            'speed': 'Chậm',
            'quality': 'Hoàn hảo',
            'support': 'Hạn chế',
            'description': 'Tỷ lệ nén tốt hơn PNG 26%',
            'advantages': ['Không mất dữ liệu', 'Tỷ lệ nén tốt', 'Hiện đại'],
            'disadvantages': ['Hỗ trợ hạn chế', 'Chậm']
        }
    ]
    return jsonify(algorithms)

@app.route('/api/compress', methods=['POST'])
def compress_image():
    """Nén ảnh"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Không có file'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Không chọn file'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Định dạng file không hỗ trợ'}), 400
        
        # Lưu file gốc
        filename = secure_filename(file.filename)
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(original_path)
        
        # Tải ảnh
        img = cv2.imread(original_path)
        if img is None:
            img_pil = Image.open(original_path)
            img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        
        original_size = get_file_size(original_path)
        
        # Nén ảnh
        results = {}
        
        # JPEG
        jpeg_path = os.path.join(app.config['RESULTS_FOLDER'], 'compressed_jpeg.jpg')
        start = time.time()
        cv2.imwrite(jpeg_path, img, [cv2.IMWRITE_JPEG_QUALITY, 85])
        jpeg_time = time.time() - start
        jpeg_size = get_file_size(jpeg_path)
        jpeg_decompressed = cv2.imread(jpeg_path)
        
        results['jpeg'] = {
            'size': jpeg_size,
            'ratio': (1 - jpeg_size / original_size) * 100,
            'time': jpeg_time,
            'psnr': calculate_psnr(img, jpeg_decompressed),
            'ssim': calculate_ssim(img, jpeg_decompressed),
            'image': 'data:image/jpeg;base64,' + image_to_base64(jpeg_path),
            'download': url_for('download_result', filename=os.path.basename(jpeg_path))
        }
        
        # PNG
        png_path = os.path.join(app.config['RESULTS_FOLDER'], 'compressed_png.png')
        start = time.time()
        cv2.imwrite(png_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
        png_time = time.time() - start
        png_size = get_file_size(png_path)
        png_decompressed = cv2.imread(png_path)
        
        results['png'] = {
            'size': png_size,
            'ratio': (1 - png_size / original_size) * 100,
            'time': png_time,
            'psnr': calculate_psnr(img, png_decompressed),
            'ssim': calculate_ssim(img, png_decompressed),
            'image': 'data:image/png;base64,' + image_to_base64(png_path),
            'download': url_for('download_result', filename=os.path.basename(png_path))
        }
        
        # WebP Lossy
        try:
            img_pil = Image.open(original_path)
            webp_lossy_path = os.path.join(app.config['RESULTS_FOLDER'], 'compressed_webp_lossy.webp')
            start = time.time()
            img_pil.save(webp_lossy_path, 'WEBP', quality=85)
            webp_lossy_time = time.time() - start
            webp_lossy_size = get_file_size(webp_lossy_path)
            webp_lossy_decompressed = cv2.cvtColor(np.array(Image.open(webp_lossy_path)), cv2.COLOR_RGB2BGR)
            
            results['webp_lossy'] = {
                'size': webp_lossy_size,
                'ratio': (1 - webp_lossy_size / original_size) * 100,
                'time': webp_lossy_time,
                'psnr': calculate_psnr(img, webp_lossy_decompressed),
                'ssim': calculate_ssim(img, webp_lossy_decompressed),
                'image': 'data:image/webp;base64,' + image_to_base64(webp_lossy_path),
                'download': url_for('download_result', filename=os.path.basename(webp_lossy_path))
            }
        except Exception as e:
            results['webp_lossy'] = {'error': str(e)}
        
        # WebP Lossless
        try:
            img_pil = Image.open(original_path)
            webp_lossless_path = os.path.join(app.config['RESULTS_FOLDER'], 'compressed_webp_lossless.webp')
            start = time.time()
            img_pil.save(webp_lossless_path, 'WEBP', lossless=True)
            webp_lossless_time = time.time() - start
            webp_lossless_size = get_file_size(webp_lossless_path)
            webp_lossless_decompressed = cv2.cvtColor(np.array(Image.open(webp_lossless_path)), cv2.COLOR_RGB2BGR)
            
            results['webp_lossless'] = {
                'size': webp_lossless_size,
                'ratio': (1 - webp_lossless_size / original_size) * 100,
                'time': webp_lossless_time,
                'psnr': calculate_psnr(img, webp_lossless_decompressed),
                'ssim': calculate_ssim(img, webp_lossless_decompressed),
                'image': 'data:image/webp;base64,' + image_to_base64(webp_lossless_path),
                'download': url_for('download_result', filename=os.path.basename(webp_lossless_path))
            }
        except Exception as e:
            results['webp_lossless'] = {'error': str(e)}
        
        return jsonify({
            'success': True,
            'original_size': original_size,
            'results': results
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/recommendations')
def get_recommendations():
    """Lấy khuyến nghị"""
    recommendations = {
        'photo': {
            'best': 'WebP Lossy',
            'reason': 'Tỷ lệ nén cao, chất lượng tốt'
        },
        'graphic': {
            'best': 'PNG',
            'reason': 'Không mất dữ liệu, cạnh sắc'
        },
        'text': {
            'best': 'PNG',
            'reason': 'Cạnh sắc, không mất dữ liệu'
        },
        'web': {
            'best': 'WebP',
            'reason': 'Tối ưu cho web, file nhỏ'
        }
    }
    return jsonify(recommendations)


@app.route('/download/<path:filename>')
def download_result(filename):
    """Serve a compressed result file as an attachment."""
    # Use secure filename to avoid path traversal
    safe_name = secure_filename(filename)
    file_path = os.path.join(app.config['RESULTS_FOLDER'], safe_name)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    # send_from_directory is safer and sets appropriate headers
    return send_from_directory(app.config['RESULTS_FOLDER'], safe_name, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

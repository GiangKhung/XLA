"""
Flask app cho hệ thống nén ảnh web
"""

from flask import Flask, render_template, request, jsonify, send_file
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
from compression_algorithms_impl import (
    RLCCompression, HuffmanCompression, LZWCompression, CompressionBenchmark
)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULTS_FOLDER'] = 'compression_results'

Path(app.config['UPLOAD_FOLDER']).mkdir(exist_ok=True)
Path(app.config['RESULTS_FOLDER']).mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def calculate_psnr(original, compressed):
    mse = np.mean((original.astype(float) - compressed.astype(float)) ** 2)
    if mse == 0:
        return 100.0
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

def calculate_ssim(original, compressed):
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
    return os.path.getsize(file_path)

def image_to_base64(image_path):
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/algorithms')
def get_algorithms():
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
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Không có file'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Không chọn file'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Định dạng file không hỗ trợ'}), 400
        
        filename = secure_filename(file.filename)
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(original_path)
        
        img = cv2.imread(original_path)
        if img is None:
            img_pil = Image.open(original_path)
            img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        
        original_size = get_file_size(original_path)
        results = {}
        
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
            'image': 'data:image/jpeg;base64,' + image_to_base64(jpeg_path)
        }
        
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
            'image': 'data:image/png;base64,' + image_to_base64(png_path)
        }
        
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
                'image': 'data:image/webp;base64,' + image_to_base64(webp_lossy_path)
            }
        except Exception as e:
            results['webp_lossy'] = {'error': str(e)}
        
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
                'image': 'data:image/webp;base64,' + image_to_base64(webp_lossless_path)
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

@app.route('/api/compress-text', methods=['POST'])
def compress_text():
    try:
        data = request.json.get('data', '')
        if not data:
            return jsonify({'error': 'Không có dữ liệu'}), 400
        
        data_bytes = data.encode('utf-8')
        results = {}
        
        try:
            rlc_compressed = RLCCompression.encode(data_bytes)
            rlc_decompressed = RLCCompression.decode(rlc_compressed)
            rlc_ratio = RLCCompression.get_compression_ratio(len(data_bytes), len(rlc_compressed))
            
            results['rlc'] = {
                'original_size': len(data_bytes),
                'compressed_size': len(rlc_compressed),
                'ratio': rlc_ratio,
                'success': rlc_decompressed == data_bytes
            }
        except Exception as e:
            results['rlc'] = {'error': str(e)}
        
        try:
            huffman_encoded, huffman_codes = HuffmanCompression.encode(data_bytes)
            huffman_decompressed = HuffmanCompression.decode(huffman_encoded, huffman_codes)
            huffman_compressed_size = (len(huffman_encoded) + 7) // 8
            huffman_ratio = (1 - huffman_compressed_size / len(data_bytes)) * 100 if len(data_bytes) > 0 else 0
            
            results['huffman'] = {
                'original_size': len(data_bytes),
                'compressed_size': huffman_compressed_size,
                'ratio': huffman_ratio,
                'success': huffman_decompressed == data_bytes
            }
        except Exception as e:
            results['huffman'] = {'error': str(e)}
        
        try:
            lzw_encoded = LZWCompression.encode(data_bytes)
            lzw_decompressed = LZWCompression.decode(lzw_encoded)
            lzw_compressed_size = len(lzw_encoded) * 2
            lzw_ratio = (1 - lzw_compressed_size / len(data_bytes)) * 100 if len(data_bytes) > 0 else 0
            
            results['lzw'] = {
                'original_size': len(data_bytes),
                'compressed_size': lzw_compressed_size,
                'ratio': lzw_ratio,
                'success': lzw_decompressed == data_bytes
            }
        except Exception as e:
            results['lzw'] = {'error': str(e)}
        
        return jsonify({
            'success': True,
            'data': data,
            'results': results
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/compress-image-algorithms', methods=['POST'])
def compress_image_algorithms():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Không có file'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Không chọn file'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Định dạng file không hỗ trợ'}), 400
        
        filename = secure_filename(file.filename)
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(original_path)
        
        img = cv2.imread(original_path)
        if img is None:
            img_pil = Image.open(original_path)
            img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        
        img_bytes = img.tobytes()
        original_size = len(img_bytes)
        results = {}
        
        try:
            rlc_compressed = RLCCompression.encode(img_bytes)
            rlc_decompressed = RLCCompression.decode(rlc_compressed)
            rlc_ratio = RLCCompression.get_compression_ratio(original_size, len(rlc_compressed))
            
            rlc_img = np.frombuffer(rlc_decompressed, dtype=np.uint8).reshape(img.shape)
            rlc_path = os.path.join(app.config['RESULTS_FOLDER'], 'rlc_decompressed.jpg')
            cv2.imwrite(rlc_path, rlc_img)
            
            results['rlc'] = {
                'original_size': original_size,
                'compressed_size': len(rlc_compressed),
                'ratio': rlc_ratio,
                'success': rlc_decompressed == img_bytes,
                'image': 'data:image/jpeg;base64,' + image_to_base64(rlc_path)
            }
        except Exception as e:
            results['rlc'] = {'error': str(e)}
        
        try:
            huffman_encoded, huffman_codes = HuffmanCompression.encode(img_bytes)
            huffman_decompressed = HuffmanCompression.decode(huffman_encoded, huffman_codes)
            huffman_compressed_size = (len(huffman_encoded) + 7) // 8
            huffman_ratio = (1 - huffman_compressed_size / original_size) * 100 if original_size > 0 else 0
            
            huffman_img = np.frombuffer(huffman_decompressed, dtype=np.uint8).reshape(img.shape)
            huffman_path = os.path.join(app.config['RESULTS_FOLDER'], 'huffman_decompressed.jpg')
            cv2.imwrite(huffman_path, huffman_img)
            
            results['huffman'] = {
                'original_size': original_size,
                'compressed_size': huffman_compressed_size,
                'ratio': huffman_ratio,
                'success': huffman_decompressed == img_bytes,
                'image': 'data:image/jpeg;base64,' + image_to_base64(huffman_path)
            }
        except Exception as e:
            results['huffman'] = {'error': str(e)}
        
        try:
            lzw_encoded = LZWCompression.encode(img_bytes)
            lzw_decompressed = LZWCompression.decode(lzw_encoded)
            lzw_compressed_size = len(lzw_encoded) * 2
            lzw_ratio = (1 - lzw_compressed_size / original_size) * 100 if original_size > 0 else 0
            
            lzw_img = np.frombuffer(lzw_decompressed, dtype=np.uint8).reshape(img.shape)
            lzw_path = os.path.join(app.config['RESULTS_FOLDER'], 'lzw_decompressed.jpg')
            cv2.imwrite(lzw_path, lzw_img)
            
            results['lzw'] = {
                'original_size': original_size,
                'compressed_size': lzw_compressed_size,
                'ratio': lzw_ratio,
                'success': lzw_decompressed == img_bytes,
                'image': 'data:image/jpeg;base64,' + image_to_base64(lzw_path)
            }
        except Exception as e:
            results['lzw'] = {'error': str(e)}
        
        original_image = 'data:image/jpeg;base64,' + image_to_base64(original_path)
        
        return jsonify({
            'success': True,
            'filename': filename,
            'original_image': original_image,
            'results': results
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

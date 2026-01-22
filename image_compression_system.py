"""
Hệ thống nén ảnh và so sánh hiệu quả các phương pháp nén
"""

import os
import cv2
import numpy as np
from PIL import Image
import time
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Tuple
import json
from datetime import datetime


@dataclass
class CompressionResult:
    """Lưu trữ kết quả nén ảnh"""
    method: str
    original_size: int
    compressed_size: int
    compression_ratio: float
    quality_loss: float
    compression_time: float
    decompression_time: float
    psnr: float = 0.0
    ssim: float = 0.0


class ImageCompressionSystem:
    """Hệ thống nén ảnh với nhiều phương pháp"""
    
    def __init__(self, output_dir: str = "compression_results"):
        self.output_dir = output_dir
        Path(output_dir).mkdir(exist_ok=True)
        self.results: List[CompressionResult] = []
    
    def load_image(self, image_path: str) -> np.ndarray:
        """Tải ảnh từ file"""
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Không thể tải ảnh: {image_path}")
        return img
    
    def get_file_size(self, file_path: str) -> int:
        """Lấy kích thước file"""
        return os.path.getsize(file_path)
    
    def calculate_psnr(self, original: np.ndarray, compressed: np.ndarray) -> float:
        """Tính PSNR (Peak Signal-to-Noise Ratio)"""
        mse = np.mean((original.astype(float) - compressed.astype(float)) ** 2)
        if mse == 0:
            return 100.0
        max_pixel = 255.0
        psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
        return psnr
    
    def calculate_ssim(self, original: np.ndarray, compressed: np.ndarray) -> float:
        """Tính SSIM (Structural Similarity Index)"""
        from skimage.metrics import structural_similarity as ssim
        
        # Chuyển sang grayscale nếu cần
        if len(original.shape) == 3:
            original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
            compressed_gray = cv2.cvtColor(compressed, cv2.COLOR_BGR2GRAY)
        else:
            original_gray = original
            compressed_gray = compressed
        
        return ssim(original_gray, compressed_gray, data_range=255)
    
    def compress_jpeg(self, image_path: str, quality: int = 85) -> CompressionResult:
        """Nén JPEG (Lossy)"""
        img = self.load_image(image_path)
        original_size = self.get_file_size(image_path)
        
        output_path = os.path.join(self.output_dir, "compressed_jpeg.jpg")
        
        # Nén
        start_time = time.time()
        cv2.imwrite(output_path, img, [cv2.IMWRITE_JPEG_QUALITY, quality])
        compression_time = time.time() - start_time
        
        # Giải nén
        start_time = time.time()
        decompressed = cv2.imread(output_path)
        decompression_time = time.time() - start_time
        
        compressed_size = self.get_file_size(output_path)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        psnr = self.calculate_psnr(img, decompressed)
        ssim = self.calculate_ssim(img, decompressed)
        
        return CompressionResult(
            method="JPEG (Quality=85)",
            original_size=original_size,
            compressed_size=compressed_size,
            compression_ratio=compression_ratio,
            quality_loss=100 - psnr,
            compression_time=compression_time,
            decompression_time=decompression_time,
            psnr=psnr,
            ssim=ssim
        )
    
    def compress_png(self, image_path: str) -> CompressionResult:
        """Nén PNG (Lossless)"""
        img = self.load_image(image_path)
        original_size = self.get_file_size(image_path)
        
        output_path = os.path.join(self.output_dir, "compressed_png.png")
        
        # Nén
        start_time = time.time()
        cv2.imwrite(output_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
        compression_time = time.time() - start_time
        
        # Giải nén
        start_time = time.time()
        decompressed = cv2.imread(output_path)
        decompression_time = time.time() - start_time
        
        compressed_size = self.get_file_size(output_path)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        psnr = self.calculate_psnr(img, decompressed)
        ssim = self.calculate_ssim(img, decompressed)
        
        return CompressionResult(
            method="PNG (Lossless)",
            original_size=original_size,
            compressed_size=compressed_size,
            compression_ratio=compression_ratio,
            quality_loss=100 - psnr,
            compression_time=compression_time,
            decompression_time=decompression_time,
            psnr=psnr,
            ssim=ssim
        )
    
    def compress_webp_lossy(self, image_path: str, quality: int = 85) -> CompressionResult:
        """Nén WebP Lossy"""
        img = Image.open(image_path)
        original_size = self.get_file_size(image_path)
        
        output_path = os.path.join(self.output_dir, "compressed_webp_lossy.webp")
        
        # Nén
        start_time = time.time()
        img.save(output_path, 'WEBP', quality=quality)
        compression_time = time.time() - start_time
        
        # Giải nén
        start_time = time.time()
        decompressed_pil = Image.open(output_path)
        decompressed = cv2.cvtColor(np.array(decompressed_pil), cv2.COLOR_RGB2BGR)
        decompression_time = time.time() - start_time
        
        compressed_size = self.get_file_size(output_path)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        original_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        psnr = self.calculate_psnr(original_cv, decompressed)
        ssim = self.calculate_ssim(original_cv, decompressed)
        
        return CompressionResult(
            method="WebP Lossy (Quality=85)",
            original_size=original_size,
            compressed_size=compressed_size,
            compression_ratio=compression_ratio,
            quality_loss=100 - psnr,
            compression_time=compression_time,
            decompression_time=decompression_time,
            psnr=psnr,
            ssim=ssim
        )
    
    def compress_webp_lossless(self, image_path: str) -> CompressionResult:
        """Nén WebP Lossless"""
        img = Image.open(image_path)
        original_size = self.get_file_size(image_path)
        
        output_path = os.path.join(self.output_dir, "compressed_webp_lossless.webp")
        
        # Nén
        start_time = time.time()
        img.save(output_path, 'WEBP', lossless=True)
        compression_time = time.time() - start_time
        
        # Giải nén
        start_time = time.time()
        decompressed_pil = Image.open(output_path)
        decompressed = cv2.cvtColor(np.array(decompressed_pil), cv2.COLOR_RGB2BGR)
        decompression_time = time.time() - start_time
        
        compressed_size = self.get_file_size(output_path)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        original_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        psnr = self.calculate_psnr(original_cv, decompressed)
        ssim = self.calculate_ssim(original_cv, decompressed)
        
        return CompressionResult(
            method="WebP Lossless",
            original_size=original_size,
            compressed_size=compressed_size,
            compression_ratio=compression_ratio,
            quality_loss=100 - psnr,
            compression_time=compression_time,
            decompression_time=decompression_time,
            psnr=psnr,
            ssim=ssim
        )
    
    def compress_all(self, image_path: str) -> List[CompressionResult]:
        """Nén ảnh bằng tất cả các phương pháp"""
        print(f"Đang nén ảnh: {image_path}")
        print("-" * 80)
        
        results = []
        
        try:
            result = self.compress_jpeg(image_path)
            results.append(result)
            print(f"✓ JPEG: {result.compressed_size} bytes ({result.compression_ratio:.2f}% giảm)")
        except Exception as e:
            print(f"✗ JPEG: {e}")
        
        try:
            result = self.compress_png(image_path)
            results.append(result)
            print(f"✓ PNG: {result.compressed_size} bytes ({result.compression_ratio:.2f}% giảm)")
        except Exception as e:
            print(f"✗ PNG: {e}")
        
        try:
            result = self.compress_webp_lossy(image_path)
            results.append(result)
            print(f"✓ WebP Lossy: {result.compressed_size} bytes ({result.compression_ratio:.2f}% giảm)")
        except Exception as e:
            print(f"✗ WebP Lossy: {e}")
        
        try:
            result = self.compress_webp_lossless(image_path)
            results.append(result)
            print(f"✓ WebP Lossless: {result.compressed_size} bytes ({result.compression_ratio:.2f}% giảm)")
        except Exception as e:
            print(f"✗ WebP Lossless: {e}")
        
        self.results.extend(results)
        return results
    
    def generate_report(self) -> str:
        """Tạo báo cáo so sánh"""
        if not self.results:
            return "Không có kết quả nén"
        
        report = []
        report.append("\n" + "=" * 100)
        report.append("BÁO CÁO SO SÁNH HIỆU QUẢ NÉN ẢNH")
        report.append("=" * 100)
        report.append(f"Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Bảng so sánh
        report.append(f"{'Phương pháp':<25} {'Kích thước':<15} {'Tỷ lệ':<12} {'PSNR':<10} {'SSIM':<10} {'Thời gian':<12}")
        report.append("-" * 100)
        
        for result in self.results:
            report.append(
                f"{result.method:<25} {result.compressed_size:<15} "
                f"{result.compression_ratio:>10.2f}% {result.psnr:>9.2f} "
                f"{result.ssim:>9.4f} {result.compression_time:>10.4f}s"
            )
        
        report.append("\n" + "-" * 100)
        
        # Thống kê
        report.append("\nTHỐNG KÊ:")
        best_ratio = max(self.results, key=lambda x: x.compression_ratio)
        best_quality = max(self.results, key=lambda x: x.psnr)
        fastest = min(self.results, key=lambda x: x.compression_time)
        
        report.append(f"• Tỷ lệ nén tốt nhất: {best_ratio.method} ({best_ratio.compression_ratio:.2f}%)")
        report.append(f"• Chất lượng tốt nhất: {best_quality.method} (PSNR: {best_quality.psnr:.2f})")
        report.append(f"• Nhanh nhất: {fastest.method} ({fastest.compression_time:.4f}s)")
        
        report.append("\n" + "=" * 100 + "\n")
        
        return "\n".join(report)
    
    def save_report(self, filename: str = "compression_report.txt"):
        """Lưu báo cáo vào file"""
        report = self.generate_report()
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Báo cáo đã lưu: {filepath}")
        return filepath
    
    def save_json_report(self, filename: str = "compression_results.json"):
        """Lưu kết quả dưới dạng JSON"""
        data = {
            "timestamp": datetime.now().isoformat(),
            "results": [
                {
                    "method": r.method,
                    "original_size": r.original_size,
                    "compressed_size": r.compressed_size,
                    "compression_ratio": r.compression_ratio,
                    "psnr": r.psnr,
                    "ssim": r.ssim,
                    "compression_time": r.compression_time,
                    "decompression_time": r.decompression_time
                }
                for r in self.results
            ]
        }
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Kết quả JSON đã lưu: {filepath}")
        return filepath


def create_test_image(width: int = 800, height: int = 600) -> str:
    """Tạo ảnh test"""
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Vẽ các hình dạng
    cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), -1)
    cv2.circle(img, (400, 300), 100, (255, 0, 0), -1)
    cv2.ellipse(img, (600, 400), (80, 120), 45, 0, 360, (0, 255, 255), -1)
    
    # Thêm gradient
    for i in range(height):
        img[i, :] = [i % 256, (i * 2) % 256, (i * 3) % 256]
    
    # Lưu ảnh test
    test_path = "test_image.jpg"
    cv2.imwrite(test_path, img)
    return test_path


if __name__ == "__main__":
    # Tạo ảnh test
    print("Tạo ảnh test...")
    test_image = create_test_image()
    
    # Khởi tạo hệ thống
    system = ImageCompressionSystem()
    
    # Nén ảnh
    results = system.compress_all(test_image)
    
    # In báo cáo
    print(system.generate_report())
    
    # Lưu báo cáo
    system.save_report()
    system.save_json_report()
    
    print("✓ Hoàn thành!")

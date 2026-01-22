"""
So sánh nâng cao: Hiệu quả nén với các loại ảnh khác nhau
"""

import numpy as np
import cv2
from PIL import Image
import os
import time
from typing import Dict, List, Tuple
import json
from pathlib import Path


class AdvancedCompressionComparison:
    """So sánh nâng cao các phương pháp nén"""
    
    def __init__(self, output_dir: str = "advanced_results"):
        self.output_dir = output_dir
        Path(output_dir).mkdir(exist_ok=True)
    
    def create_photo_image(self) -> str:
        """Tạo ảnh giống ảnh chụp (nhiều chi tiết, gradient)"""
        img = np.zeros((600, 800, 3), dtype=np.uint8)
        
        # Gradient phức tạp
        for i in range(600):
            for j in range(800):
                img[i, j] = [
                    int(255 * i / 600),
                    int(255 * j / 800),
                    int(255 * (i + j) / 1400)
                ]
        
        # Thêm nhiễu
        noise = np.random.normal(0, 10, img.shape).astype(np.uint8)
        img = cv2.add(img, noise)
        
        # Thêm chi tiết
        for _ in range(50):
            x, y = np.random.randint(0, 800), np.random.randint(0, 600)
            r = np.random.randint(10, 50)
            color = tuple(np.random.randint(0, 256, 3).tolist())
            cv2.circle(img, (x, y), r, color, -1)
        
        path = os.path.join(self.output_dir, "photo_image.jpg")
        cv2.imwrite(path, img)
        return path
    
    def create_graphic_image(self) -> str:
        """Tạo ảnh đồ họa (màu đơn, cạnh sắc)"""
        img = np.zeros((600, 800, 3), dtype=np.uint8)
        
        # Vẽ các hình dạng với màu đơn
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
        
        cv2.rectangle(img, (50, 50), (250, 250), colors[0], -1)
        cv2.circle(img, (400, 150), 80, colors[1], -1)
        cv2.ellipse(img, (600, 300), (100, 50), 45, 0, 360, colors[2], -1)
        cv2.polygon(img, np.array([[100, 400], [200, 350], [250, 450], [150, 500]]), colors[3])
        
        # Thêm text
        cv2.putText(img, "GRAPHIC", (300, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, colors[4], 3)
        
        path = os.path.join(self.output_dir, "graphic_image.png")
        cv2.imwrite(path, img)
        return path
    
    def create_text_image(self) -> str:
        """Tạo ảnh chứa text (cạnh sắc, ít màu)"""
        img = np.ones((600, 800, 3), dtype=np.uint8) * 255
        
        # Thêm text
        texts = ["COMPRESSION", "COMPARISON", "ANALYSIS", "2024"]
        y_pos = 100
        for text in texts:
            cv2.putText(img, text, (50, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 
                       2, (0, 0, 0), 3)
            y_pos += 120
        
        # Thêm các đường
        cv2.line(img, (50, 550), (750, 550), (0, 0, 0), 2)
        cv2.rectangle(img, (50, 50), (750, 550), (0, 0, 0), 2)
        
        path = os.path.join(self.output_dir, "text_image.png")
        cv2.imwrite(path, img)
        return path
    
    def compress_and_analyze(self, image_path: str, image_type: str) -> Dict:
        """Nén ảnh và phân tích"""
        original_size = os.path.getsize(image_path)
        results = {
            "image_type": image_type,
            "original_size": original_size,
            "methods": {}
        }
        
        # JPEG
        jpeg_path = os.path.join(self.output_dir, f"{image_type}_jpeg.jpg")
        cv2.imwrite(jpeg_path, cv2.imread(image_path), [cv2.IMWRITE_JPEG_QUALITY, 85])
        jpeg_size = os.path.getsize(jpeg_path)
        results["methods"]["JPEG"] = {
            "size": jpeg_size,
            "ratio": (1 - jpeg_size / original_size) * 100
        }
        
        # PNG
        png_path = os.path.join(self.output_dir, f"{image_type}_png.png")
        cv2.imwrite(png_path, cv2.imread(image_path), [cv2.IMWRITE_PNG_COMPRESSION, 9])
        png_size = os.path.getsize(png_path)
        results["methods"]["PNG"] = {
            "size": png_size,
            "ratio": (1 - png_size / original_size) * 100
        }
        
        # WebP Lossy
        try:
            img = Image.open(image_path)
            webp_lossy_path = os.path.join(self.output_dir, f"{image_type}_webp_lossy.webp")
            img.save(webp_lossy_path, 'WEBP', quality=85)
            webp_lossy_size = os.path.getsize(webp_lossy_path)
            results["methods"]["WebP Lossy"] = {
                "size": webp_lossy_size,
                "ratio": (1 - webp_lossy_size / original_size) * 100
            }
        except:
            results["methods"]["WebP Lossy"] = {"size": 0, "ratio": 0}
        
        # WebP Lossless
        try:
            img = Image.open(image_path)
            webp_lossless_path = os.path.join(self.output_dir, f"{image_type}_webp_lossless.webp")
            img.save(webp_lossless_path, 'WEBP', lossless=True)
            webp_lossless_size = os.path.getsize(webp_lossless_path)
            results["methods"]["WebP Lossless"] = {
                "size": webp_lossless_size,
                "ratio": (1 - webp_lossless_size / original_size) * 100
            }
        except:
            results["methods"]["WebP Lossless"] = {"size": 0, "ratio": 0}
        
        return results
    
    def run_comparison(self):
        """Chạy so sánh đầy đủ"""
        print("\n" + "=" * 100)
        print("SO SÁNH HIỆU QUẢ NÉN VỚI CÁC LOẠI ẢNH KHÁC NHAU")
        print("=" * 100 + "\n")
        
        # Tạo ảnh test
        print("Tạo ảnh test...")
        photo_path = self.create_photo_image()
        graphic_path = self.create_graphic_image()
        text_path = self.create_text_image()
        
        # Nén và phân tích
        print("Đang nén ảnh...\n")
        
        results = []
        
        # Ảnh chụp
        print("1. Ảnh chụp (Photo):")
        photo_result = self.compress_and_analyze(photo_path, "photo")
        results.append(photo_result)
        self._print_results(photo_result)
        
        # Ảnh đồ họa
        print("\n2. Ảnh đồ họa (Graphic):")
        graphic_result = self.compress_and_analyze(graphic_path, "graphic")
        results.append(graphic_result)
        self._print_results(graphic_result)
        
        # Ảnh text
        print("\n3. Ảnh text (Text):")
        text_result = self.compress_and_analyze(text_path, "text")
        results.append(text_result)
        self._print_results(text_result)
        
        # Tóm tắt
        self._print_summary(results)
        
        # Lưu kết quả
        self._save_results(results)
    
    def _print_results(self, result: Dict):
        """In kết quả nén"""
        print(f"   Kích thước gốc: {result['original_size']:,} bytes")
        print(f"   {'Phương pháp':<20} {'Kích thước':<15} {'Tỷ lệ nén':<15}")
        print(f"   {'-' * 50}")
        
        for method, data in result['methods'].items():
            if data['size'] > 0:
                print(f"   {method:<20} {data['size']:<15,} {data['ratio']:>13.2f}%")
    
    def _print_summary(self, results: List[Dict]):
        """In tóm tắt"""
        print("\n" + "=" * 100)
        print("TÓM TẮT VÀ KHUYẾN NGHỊ")
        print("=" * 100 + "\n")
        
        for result in results:
            image_type = result['image_type'].upper()
            best_method = max(result['methods'].items(), 
                            key=lambda x: x[1]['ratio'] if x[1]['size'] > 0 else 0)
            
            print(f"📌 {image_type}:")
            print(f"   • Phương pháp tốt nhất: {best_method[0]} ({best_method[1]['ratio']:.2f}% giảm)")
            
            if image_type == "PHOTO":
                print(f"   → Khuyến nghị: WebP Lossy (chất lượng cao, file nhỏ)")
            elif image_type == "GRAPHIC":
                print(f"   → Khuyến nghị: PNG hoặc WebP Lossless (không mất dữ liệu)")
            elif image_type == "TEXT":
                print(f"   → Khuyến nghị: PNG (cạnh sắc, không mất dữ liệu)")
            print()
    
    def _save_results(self, results: List[Dict]):
        """Lưu kết quả"""
        filepath = os.path.join(self.output_dir, "comparison_results.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"✓ Kết quả đã lưu: {filepath}")


class CompressionBestPractices:
    """Các thực hành tốt nhất trong nén ảnh"""
    
    @staticmethod
    def print_best_practices():
        """In các thực hành tốt nhất"""
        practices = {
            "Chuẩn bị ảnh": [
                "Resize ảnh đến kích thước cần thiết",
                "Loại bỏ metadata không cần thiết",
                "Chuyển đổi sang không gian màu phù hợp (RGB, YCbCr)"
            ],
            "Chọn định dạng": [
                "Ảnh chụp: WebP Lossy hoặc JPEG",
                "Đồ họa: PNG hoặc WebP Lossless",
                "Animation: WebP hoặc GIF",
                "Web: WebP (với fallback JPEG/PNG)"
            ],
            "Tối ưu hóa": [
                "Sử dụng quality level phù hợp (75-85 cho lossy)",
                "Thử nghiệm nhiều mức nén",
                "So sánh kích thước và chất lượng",
                "Sử dụng công cụ tối ưu hóa"
            ],
            "Kiểm tra chất lượng": [
                "Kiểm tra PSNR (Peak Signal-to-Noise Ratio)",
                "Kiểm tra SSIM (Structural Similarity)",
                "Xem trực quan ảnh nén",
                "Kiểm tra trên nhiều thiết bị"
            ],
            "Triển khai": [
                "Sử dụng responsive images",
                "Lazy load ảnh không quan trọng",
                "Sử dụng CDN cho ảnh",
                "Caching ảnh nén"
            ]
        }
        
        print("\n" + "=" * 100)
        print("CÁC THỰC HÀNH TỐT NHẤT TRONG NÉN ẢNH")
        print("=" * 100 + "\n")
        
        for category, items in practices.items():
            print(f"📋 {category}:")
            for item in items:
                print(f"   • {item}")
            print()


def main():
    """Chạy so sánh"""
    comparison = AdvancedCompressionComparison()
    comparison.run_comparison()
    
    # In thực hành tốt nhất
    CompressionBestPractices.print_best_practices()


if __name__ == "__main__":
    main()

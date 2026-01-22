"""
Phân tích chi tiết các thuật toán nén ảnh
"""

import numpy as np
from typing import Tuple, List
import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass
class AlgorithmInfo:
    """Thông tin về thuật toán nén"""
    name: str
    type: str  # Lossy hoặc Lossless
    compression_ratio: str
    use_cases: List[str]
    advantages: List[str]
    disadvantages: List[str]
    technical_details: str


class CompressionAlgorithmsAnalysis:
    """Phân tích các thuật toán nén ảnh"""
    
    @staticmethod
    def get_algorithms_info() -> List[AlgorithmInfo]:
        """Lấy thông tin chi tiết về các thuật toán"""
        return [
            AlgorithmInfo(
                name="JPEG (DCT - Discrete Cosine Transform)",
                type="Lossy",
                compression_ratio="80-95%",
                use_cases=["Ảnh chụp", "Ảnh phức tạp", "Web"],
                advantages=[
                    "Tỷ lệ nén rất cao",
                    "Phổ biến, hỗ trợ rộng rãi",
                    "Nhanh",
                    "Chất lượng tốt ở mức nén cao"
                ],
                disadvantages=[
                    "Mất dữ liệu",
                    "Hiện tượng blocking ở chất lượng thấp",
                    "Không hỗ trợ transparency"
                ],
                technical_details="""
JPEG sử dụng 7 bước:
1. Chuyển đổi không gian màu: RGB → YCbCr
2. Chuyển mẫu chroma: Giảm độ phân giải màu
3. Chia khối: Chia ảnh thành khối 8×8 pixel
4. DCT: Chuyển đổi từ miền không gian sang miền tần số
5. Lượng tử hóa: Loại bỏ dữ liệu tần số cao
6. Mã hóa entropy: Huffman hoặc arithmetic coding
7. Lưu trữ: Định dạng JPEG
                """
            ),
            AlgorithmInfo(
                name="PNG (DEFLATE + Filtering)",
                type="Lossless",
                compression_ratio="10-30%",
                use_cases=["Đồ họa", "Logo", "Ảnh cần chất lượng cao", "Transparency"],
                advantages=[
                    "Không mất dữ liệu",
                    "Hỗ trợ transparency",
                    "Tốt cho đồ họa",
                    "Phổ biến"
                ],
                disadvantages=[
                    "Tỷ lệ nén thấp hơn JPEG",
                    "File lớn hơn JPEG",
                    "Chậm hơn JPEG"
                ],
                technical_details="""
PNG sử dụng 2 bước:
1. Filtering: Áp dụng bộ lọc để tìm mẫu
   - None: Không lọc
   - Sub: Hiệu với pixel bên trái
   - Up: Hiệu với pixel phía trên
   - Average: Hiệu với trung bình
   - Paeth: Dự đoán Paeth
2. DEFLATE: Kết hợp LZ77 + Huffman coding
                """
            ),
            AlgorithmInfo(
                name="WebP Lossy",
                type="Lossy",
                compression_ratio="75-90%",
                use_cases=["Web", "Mobile", "Ảnh chụp"],
                advantages=[
                    "Tỷ lệ nén tốt hơn JPEG 25-35%",
                    "Chất lượng tốt hơn JPEG",
                    "Hiện đại",
                    "Hỗ trợ animation"
                ],
                disadvantages=[
                    "Hỗ trợ trình duyệt chưa toàn bộ",
                    "Mất dữ liệu",
                    "Chậm hơn JPEG"
                ],
                technical_details="""
WebP Lossy sử dụng:
1. VP8 codec (video codec)
2. Prediction: Dự đoán pixel từ lân cận
3. Transform: DCT hoặc Walsh-Hadamard
4. Quantization: Lượng tử hóa
5. Entropy coding: Arithmetic coding
                """
            ),
            AlgorithmInfo(
                name="WebP Lossless",
                type="Lossless",
                compression_ratio="20-40%",
                use_cases=["Đồ họa", "Logo", "Web"],
                advantages=[
                    "Không mất dữ liệu",
                    "Tỷ lệ nén tốt hơn PNG 26%",
                    "Hiện đại"
                ],
                disadvantages=[
                    "Hỗ trợ trình duyệt chưa toàn bộ",
                    "Chậm hơn PNG"
                ],
                technical_details="""
WebP Lossless sử dụng:
1. Prediction: Dự đoán pixel
2. Transform: Chuyển đổi không gian
3. Color cache: Lưu cache màu
4. Entropy coding: Huffman + LZ77
                """
            ),
            AlgorithmInfo(
                name="GIF (LZW)",
                type="Lossless",
                compression_ratio="5-20%",
                use_cases=["Animation", "Đồ họa đơn giản"],
                advantages=[
                    "Hỗ trợ animation",
                    "Phổ biến",
                    "Đơn giản"
                ],
                disadvantages=[
                    "Tối đa 256 màu",
                    "Tỷ lệ nén thấp",
                    "Lỗi thời"
                ],
                technical_details="""
GIF sử dụng:
1. Palette: Giới hạn 256 màu
2. LZW (Lempel-Ziv-Welch): Nén dữ liệu
3. Interlacing: Hiển thị dần
                """
            ),
            AlgorithmInfo(
                name="Wavelet Compression",
                type="Lossy/Lossless",
                compression_ratio="Tùy thuộc",
                use_cases=["Ảnh y tế", "Ảnh khoa học", "JPEG2000"],
                advantages=[
                    "Chất lượng tốt ở bitrate thấp",
                    "Ít hiện tượng blocking",
                    "Hỗ trợ cả lossy và lossless"
                ],
                disadvantages=[
                    "Chậm",
                    "Phức tạp",
                    "Hỗ trợ hạn chế"
                ],
                technical_details="""
Wavelet sử dụng:
1. Wavelet Transform: Phân tích tần số
2. Quantization: Lượng tử hóa hệ số
3. Entropy Coding: Mã hóa entropy
Ưu điểm: Ít blocking artifacts, tốt ở bitrate thấp
                """
            )
        ]
    
    @staticmethod
    def print_algorithms_comparison():
        """In so sánh các thuật toán"""
        algorithms = CompressionAlgorithmsAnalysis.get_algorithms_info()
        
        print("\n" + "=" * 120)
        print("PHÂN TÍCH CHI TIẾT CÁC THUẬT TOÁN NÉN ẢNH")
        print("=" * 120 + "\n")
        
        for i, algo in enumerate(algorithms, 1):
            print(f"\n{i}. {algo.name}")
            print("-" * 120)
            print(f"   Loại: {algo.type}")
            print(f"   Tỷ lệ nén: {algo.compression_ratio}")
            
            print(f"\n   Trường hợp sử dụng:")
            for use_case in algo.use_cases:
                print(f"   • {use_case}")
            
            print(f"\n   Ưu điểm:")
            for adv in algo.advantages:
                print(f"   ✓ {adv}")
            
            print(f"\n   Nhược điểm:")
            for dis in algo.disadvantages:
                print(f"   ✗ {dis}")
            
            print(f"\n   Chi tiết kỹ thuật:{algo.technical_details}")
    
    @staticmethod
    def create_comparison_table():
        """Tạo bảng so sánh"""
        algorithms = CompressionAlgorithmsAnalysis.get_algorithms_info()
        
        print("\n" + "=" * 150)
        print("BẢNG SO SÁNH NHANH")
        print("=" * 150)
        
        header = f"{'Thuật toán':<25} {'Loại':<12} {'Tỷ lệ':<15} {'Tốc độ':<10} {'Chất lượng':<12} {'Hỗ trợ':<15}"
        print(header)
        print("-" * 150)
        
        speed_map = {
            "JPEG": "Rất nhanh",
            "PNG": "Trung bình",
            "WebP Lossy": "Chậm",
            "WebP Lossless": "Chậm",
            "GIF": "Nhanh",
            "Wavelet": "Rất chậm"
        }
        
        quality_map = {
            "JPEG": "Tốt",
            "PNG": "Hoàn hảo",
            "WebP Lossy": "Rất tốt",
            "WebP Lossless": "Hoàn hảo",
            "GIF": "Kém",
            "Wavelet": "Rất tốt"
        }
        
        support_map = {
            "JPEG": "Toàn bộ",
            "PNG": "Toàn bộ",
            "WebP Lossy": "Hạn chế",
            "WebP Lossless": "Hạn chế",
            "GIF": "Toàn bộ",
            "Wavelet": "Rất hạn chế"
        }
        
        for algo in algorithms:
            name = algo.name.split("(")[0].strip()
            print(f"{name:<25} {algo.type:<12} {algo.compression_ratio:<15} "
                  f"{speed_map.get(name, 'N/A'):<10} {quality_map.get(name, 'N/A'):<12} "
                  f"{support_map.get(name, 'N/A'):<15}")
        
        print("=" * 150 + "\n")
    
    @staticmethod
    def get_recommendations():
        """Lấy khuyến nghị sử dụng"""
        recommendations = {
            "Ảnh chụp": {
                "Tốt nhất": "WebP Lossy (chất lượng cao, file nhỏ)",
                "Thay thế": "JPEG (phổ biến, hỗ trợ rộng)",
                "Lý do": "WebP cho tỷ lệ nén tốt hơn 25-35% so với JPEG"
            },
            "Đồ họa/Logo": {
                "Tốt nhất": "PNG (lossless, transparency)",
                "Thay thế": "WebP Lossless (file nhỏ hơn 26%)",
                "Lý do": "PNG không mất dữ liệu, WebP hiện đại hơn"
            },
            "Animation": {
                "Tốt nhất": "WebP (hỗ trợ animation, file nhỏ)",
                "Thay thế": "GIF (phổ biến nhưng lỗi thời)",
                "Lý do": "WebP hỗ trợ animation với file nhỏ hơn"
            },
            "Ảnh y tế/Khoa học": {
                "Tốt nhất": "Wavelet/JPEG2000 (chất lượng cao)",
                "Thay thế": "PNG (lossless)",
                "Lý do": "Wavelet tốt ở bitrate thấp, ít artifacts"
            },
            "Web": {
                "Tốt nhất": "WebP (tất cả loại ảnh)",
                "Thay thế": "JPEG + PNG (phổ biến)",
                "Lý do": "WebP tối ưu cho web, file nhỏ hơn"
            }
        }
        
        print("\n" + "=" * 100)
        print("KHUYẾN NGHỊ SỬ DỤNG")
        print("=" * 100 + "\n")
        
        for use_case, rec in recommendations.items():
            print(f"📌 {use_case}:")
            print(f"   ✓ Tốt nhất: {rec['Tốt nhất']}")
            print(f"   • Thay thế: {rec['Thay thế']}")
            print(f"   → Lý do: {rec['Lý do']}\n")


def main():
    """Chạy phân tích"""
    analysis = CompressionAlgorithmsAnalysis()
    
    # In so sánh chi tiết
    analysis.print_algorithms_comparison()
    
    # Bảng so sánh nhanh
    analysis.create_comparison_table()
    
    # Khuyến nghị
    analysis.get_recommendations()


if __name__ == "__main__":
    main()

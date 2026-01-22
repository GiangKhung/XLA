"""
Script demo chạy toàn bộ hệ thống nén ảnh
"""

import sys
import os

def print_header(title):
    """In header"""
    print("\n" + "=" * 100)
    print(f"  {title}")
    print("=" * 100 + "\n")

def main():
    """Chạy demo"""
    print_header("HỆ THỐNG NÉN ẢNH VÀ SO SÁNH HIỆU QUẢ")
    
    print("Chọn chế độ chạy:")
    print("1. Phân tích các thuật toán nén")
    print("2. So sánh hiệu quả nén (ảnh test)")
    print("3. So sánh nâng cao (các loại ảnh khác nhau)")
    print("4. Chạy tất cả")
    print("0. Thoát")
    
    choice = input("\nNhập lựa chọn (0-4): ").strip()
    
    if choice == "1":
        print_header("PHÂN TÍCH CÁC THUẬT TOÁN NÉN ẢNH")
        try:
            from compression_algorithms_analysis import CompressionAlgorithmsAnalysis
            analysis = CompressionAlgorithmsAnalysis()
            analysis.print_algorithms_comparison()
            analysis.create_comparison_table()
            analysis.get_recommendations()
        except Exception as e:
            print(f"Lỗi: {e}")
    
    elif choice == "2":
        print_header("SO SÁNH HIỆU QUẢ NÉN")
        try:
            from image_compression_system import ImageCompressionSystem, create_test_image
            
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
        except Exception as e:
            print(f"Lỗi: {e}")
    
    elif choice == "3":
        print_header("SO SÁNH NÂNG CAO")
        try:
            from advanced_compression_comparison import (
                AdvancedCompressionComparison,
                CompressionBestPractices
            )
            
            comparison = AdvancedCompressionComparison()
            comparison.run_comparison()
            
            # In thực hành tốt nhất
            CompressionBestPractices.print_best_practices()
            
            print("✓ Hoàn thành!")
        except Exception as e:
            print(f"Lỗi: {e}")
    
    elif choice == "4":
        print_header("CHẠY TẤT CẢ")
        
        # 1. Phân tích thuật toán
        print("\n[1/3] Phân tích các thuật toán nén ảnh...")
        try:
            from compression_algorithms_analysis import CompressionAlgorithmsAnalysis
            analysis = CompressionAlgorithmsAnalysis()
            analysis.print_algorithms_comparison()
            analysis.create_comparison_table()
            analysis.get_recommendations()
        except Exception as e:
            print(f"Lỗi: {e}")
        
        # 2. So sánh hiệu quả nén
        print("\n[2/3] So sánh hiệu quả nén...")
        try:
            from image_compression_system import ImageCompressionSystem, create_test_image
            
            test_image = create_test_image()
            system = ImageCompressionSystem()
            results = system.compress_all(test_image)
            print(system.generate_report())
            system.save_report()
            system.save_json_report()
        except Exception as e:
            print(f"Lỗi: {e}")
        
        # 3. So sánh nâng cao
        print("\n[3/3] So sánh nâng cao...")
        try:
            from advanced_compression_comparison import (
                AdvancedCompressionComparison,
                CompressionBestPractices
            )
            
            comparison = AdvancedCompressionComparison()
            comparison.run_comparison()
            CompressionBestPractices.print_best_practices()
        except Exception as e:
            print(f"Lỗi: {e}")
        
        print("\n✓ Hoàn thành tất cả!")
    
    elif choice == "0":
        print("Thoát.")
        sys.exit(0)
    
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBị gián đoạn bởi người dùng.")
    except Exception as e:
        print(f"\nLỗi: {e}")

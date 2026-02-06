"""
Script test các thuật toán nén: RLC, Huffman, LZW
"""

from compression_algorithms_impl import (
    RLCCompression, HuffmanCompression, LZWCompression, CompressionBenchmark
)


def test_rlc():
    """Test RLC"""
    print("\n" + "=" * 80)
    print("TEST RLC (Run-Length Encoding)")
    print("=" * 80)
    
    test_cases = [
        b'AAABBBCCCDDD',
        b'AAAAAAAABBBBBBBBCCCCCCCC',
        b'ABCDEFGHIJKLMNOP',
        b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    ]
    
    for i, data in enumerate(test_cases, 1):
        print(f"\nTest {i}: {data}")
        compressed = RLCCompression.encode(data)
        decompressed = RLCCompression.decode(compressed)
        ratio = RLCCompression.get_compression_ratio(len(data), len(compressed))
        
        print(f"  Gốc: {len(data)} bytes")
        print(f"  Nén: {len(compressed)} bytes")
        print(f"  Tỷ lệ: {ratio:.2f}%")
        print(f"  OK: {decompressed == data}")


def test_huffman():
    """Test Huffman"""
    print("\n" + "=" * 80)
    print("TEST HUFFMAN CODING")
    print("=" * 80)
    
    test_cases = [
        b'AAABBBCCCDDD',
        b'AAAAAAAABBBBBBBBCCCCCCCC',
        b'ABCDEFGHIJKLMNOP',
        b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    ]
    
    for i, data in enumerate(test_cases, 1):
        print(f"\nTest {i}: {data}")
        encoded, codes = HuffmanCompression.encode(data)
        decompressed = HuffmanCompression.decode(encoded, codes)
        
        compressed_size = (len(encoded) + 7) // 8
        ratio = (1 - compressed_size / len(data)) * 100 if len(data) > 0 else 0
        
        print(f"  Gốc: {len(data)} bytes")
        print(f"  Nén: {compressed_size} bytes (ước tính)")
        print(f"  Tỷ lệ: {ratio:.2f}%")
        print(f"  OK: {decompressed == data}")
        print(f"  Bảng mã: {codes}")


def test_lzw():
    """Test LZW"""
    print("\n" + "=" * 80)
    print("TEST LZW (Lempel-Ziv-Welch)")
    print("=" * 80)
    
    test_cases = [
        b'AAABBBCCCDDD',
        b'AAAAAAAABBBBBBBBCCCCCCCC',
        b'ABCDEFGHIJKLMNOP',
        b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    ]
    
    for i, data in enumerate(test_cases, 1):
        print(f"\nTest {i}: {data}")
        encoded = LZWCompression.encode(data)
        decompressed = LZWCompression.decode(encoded)
        
        compressed_size = len(encoded) * 2
        ratio = (1 - compressed_size / len(data)) * 100 if len(data) > 0 else 0
        
        print(f"  Gốc: {len(data)} bytes")
        print(f"  Nén: {compressed_size} bytes")
        print(f"  Tỷ lệ: {ratio:.2f}%")
        print(f"  OK: {decompressed == data}")
        print(f"  Mã: {encoded[:20]}..." if len(encoded) > 20 else f"  Mã: {encoded}")


def benchmark_comparison():
    """So sánh hiệu suất"""
    print("\n" + "=" * 80)
    print("SO SÁNH HIỆU SUẤT CÁC THUẬT TOÁN")
    print("=" * 80)
    
    # Test với dữ liệu khác nhau
    test_data_sets = {
        'Dữ liệu lặp lại': b'AAABBBCCCDDD' * 100,
        'Dữ liệu ngẫu nhiên': b'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 100,
        'Dữ liệu hỗn hợp': (b'AAAA' + b'BCDE' + b'FFFF' + b'GHIJ') * 100,
    }
    
    for dataset_name, data in test_data_sets.items():
        print(f"\n{dataset_name} ({len(data)} bytes):")
        print("-" * 80)
        
        results = CompressionBenchmark.benchmark_all(data)
        
        print(f"{'Thuật toán':<15} {'Kích thước':<15} {'Tỷ lệ':<12} {'Encode':<12} {'Decode':<12}")
        print("-" * 80)
        
        for result in results:
            if 'error' not in result:
                print(f"{result['name']:<15} {result['compressed_size']:<15} "
                      f"{result['ratio']:>10.2f}% {result['encode_time']:>10.6f}s "
                      f"{result['decode_time']:>10.6f}s")
            else:
                print(f"{result['name']:<15} Error: {result['error']}")


def main():
    """Chạy tất cả test"""
    print("\n" + "=" * 80)
    print("KIỂM TRA CÁC THUẬT TOÁN NÉN: RLC, HUFFMAN, LZW")
    print("=" * 80)
    
    # Test từng thuật toán
    test_rlc()
    test_huffman()
    test_lzw()
    
    # So sánh hiệu suất
    benchmark_comparison()
    
    print("\n" + "=" * 80)
    print("HOÀN THÀNH!")
    print("=" * 80)


if __name__ == '__main__':
    main()

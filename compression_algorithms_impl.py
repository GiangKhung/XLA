"""
Triển khai 3 thuật toán nén: RLC, Huffman, LZW
"""

import heapq
from collections import defaultdict, Counter
from typing import Tuple, Dict, List
import time


class RLCCompression:
    """Run-Length Encoding (RLC) - Nén dữ liệu lặp lại"""
    
    @staticmethod
    def encode(data: bytes) -> bytes:
        """
        Nén RLC
        
        Ý tưởng: Thay thế các byte lặp lại bằng (byte, count)
        
        Ví dụ: AAABBBCC → A3B3C2
        """
        if not data:
            return b''
        
        encoded = bytearray()
        i = 0
        
        while i < len(data):
            current_byte = data[i]
            count = 1
            
            # Đếm số lần lặp lại
            while i + count < len(data) and data[i + count] == current_byte and count < 255:
                count += 1
            
            # Lưu byte và count
            encoded.append(current_byte)
            encoded.append(count)
            
            i += count
        
        return bytes(encoded)
    
    @staticmethod
    def decode(data: bytes) -> bytes:
        """Giải nén RLC"""
        if not data:
            return b''
        
        decoded = bytearray()
        
        for i in range(0, len(data), 2):
            if i + 1 < len(data):
                byte_val = data[i]
                count = data[i + 1]
                decoded.extend([byte_val] * count)
        
        return bytes(decoded)
    
    @staticmethod
    def get_compression_ratio(original_size: int, compressed_size: int) -> float:
        """Tính tỷ lệ nén"""
        if original_size == 0:
            return 0
        return (1 - compressed_size / original_size) * 100


class HuffmanCompression:
    """Huffman Coding - Nén dữ liệu dựa trên tần suất"""
    
    class Node:
        """Node cho Huffman tree"""
        def __init__(self, byte_val=None, freq=0, left=None, right=None):
            self.byte_val = byte_val
            self.freq = freq
            self.left = left
            self.right = right
        
        def __lt__(self, other):
            return self.freq < other.freq
    
    @staticmethod
    def build_huffman_tree(data: bytes) -> Tuple[Dict[int, str], 'HuffmanCompression.Node']:
        """Xây dựng Huffman tree"""
        if not data:
            return {}, None
        
        # Tính tần suất
        freq = Counter(data)
        
        # Tạo priority queue
        heap = [HuffmanCompression.Node(byte_val=byte_val, freq=count) 
                for byte_val, count in freq.items()]
        heapq.heapify(heap)
        
        # Xây dựng tree
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            
            parent = HuffmanCompression.Node(freq=left.freq + right.freq, 
                                            left=left, right=right)
            heapq.heappush(heap, parent)
        
        root = heap[0] if heap else None
        
        # Tạo bảng mã
        codes = {}
        HuffmanCompression._build_codes(root, '', codes)
        
        return codes, root
    
    @staticmethod
    def _build_codes(node: 'HuffmanCompression.Node', code: str, codes: Dict):
        """Xây dựng bảng mã từ tree"""
        if node is None:
            return
        
        if node.byte_val is not None:
            codes[node.byte_val] = code if code else '0'
        
        HuffmanCompression._build_codes(node.left, code + '0', codes)
        HuffmanCompression._build_codes(node.right, code + '1', codes)
    
    @staticmethod
    def encode(data: bytes) -> Tuple[str, Dict[int, str]]:
        """Nén Huffman"""
        if not data:
            return '', {}
        
        codes, _ = HuffmanCompression.build_huffman_tree(data)
        
        # Mã hóa dữ liệu
        encoded = ''.join(codes[byte_val] for byte_val in data)
        
        return encoded, codes
    
    @staticmethod
    def decode(encoded: str, codes: Dict[int, str]) -> bytes:
        """Giải nén Huffman"""
        if not encoded or not codes:
            return b''
        
        # Tạo reverse mapping
        reverse_codes = {v: k for k, v in codes.items()}
        
        decoded = bytearray()
        current_code = ''
        
        for bit in encoded:
            current_code += bit
            if current_code in reverse_codes:
                decoded.append(reverse_codes[current_code])
                current_code = ''
        
        return bytes(decoded)


class LZWCompression:
    """LZW (Lempel-Ziv-Welch) - Nén dữ liệu dựa trên từ điển"""
    
    @staticmethod
    def encode(data: bytes) -> List[int]:
        """
        Nén LZW
        
        Ý tưởng: Xây dựng từ điển động và thay thế chuỗi bằng mã
        """
        if not data:
            return []
        
        # Khởi tạo từ điển với tất cả byte đơn
        dict_size = 256
        dictionary = {bytes([i]): i for i in range(dict_size)}
        
        encoded = []
        current_string = b''
        
        for byte_val in data:
            current_byte = bytes([byte_val])
            combined = current_string + current_byte
            
            if combined in dictionary:
                current_string = combined
            else:
                # Lưu mã của chuỗi hiện tại
                encoded.append(dictionary[current_string])
                
                # Thêm chuỗi mới vào từ điển
                if dict_size < 4096:  # Giới hạn kích thước từ điển
                    dictionary[combined] = dict_size
                    dict_size += 1
                
                current_string = current_byte
        
        # Lưu mã cuối cùng
        if current_string:
            encoded.append(dictionary[current_string])
        
        return encoded
    
    @staticmethod
    def decode(encoded: List[int]) -> bytes:
        """Giải nén LZW"""
        if not encoded:
            return b''
        
        # Khởi tạo từ điển
        dict_size = 256
        dictionary = {i: bytes([i]) for i in range(dict_size)}
        
        decoded = bytearray()
        
        # Lấy chuỗi đầu tiên
        current_string = dictionary[encoded[0]]
        decoded.extend(current_string)
        
        for code in encoded[1:]:
            if code in dictionary:
                entry = dictionary[code]
            elif code == dict_size:
                entry = current_string + bytes([current_string[0]])
            else:
                raise ValueError(f'Mã không hợp lệ: {code}')
            
            decoded.extend(entry)
            
            # Thêm vào từ điển
            if dict_size < 4096:
                dictionary[dict_size] = current_string + bytes([entry[0]])
                dict_size += 1
            
            current_string = entry
        
        return bytes(decoded)


class CompressionBenchmark:
    """So sánh hiệu suất các thuật toán"""
    
    @staticmethod
    def benchmark_rlc(data: bytes) -> Dict:
        """Benchmark RLC"""
        start = time.time()
        compressed = RLCCompression.encode(data)
        encode_time = time.time() - start
        
        start = time.time()
        decompressed = RLCCompression.decode(compressed)
        decode_time = time.time() - start
        
        original_size = len(data)
        compressed_size = len(compressed)
        ratio = RLCCompression.get_compression_ratio(original_size, compressed_size)
        
        return {
            'name': 'RLC',
            'original_size': original_size,
            'compressed_size': compressed_size,
            'ratio': ratio,
            'encode_time': encode_time,
            'decode_time': decode_time,
            'success': decompressed == data
        }
    
    @staticmethod
    def benchmark_huffman(data: bytes) -> Dict:
        """Benchmark Huffman"""
        start = time.time()
        encoded, codes = HuffmanCompression.encode(data)
        encode_time = time.time() - start
        
        start = time.time()
        decompressed = HuffmanCompression.decode(encoded, codes)
        decode_time = time.time() - start
        
        original_size = len(data)
        # Ước tính kích thước nén (bits → bytes)
        compressed_size = (len(encoded) + 7) // 8
        ratio = (1 - compressed_size / original_size) * 100 if original_size > 0 else 0
        
        return {
            'name': 'Huffman',
            'original_size': original_size,
            'compressed_size': compressed_size,
            'ratio': ratio,
            'encode_time': encode_time,
            'decode_time': decode_time,
            'success': decompressed == data
        }
    
    @staticmethod
    def benchmark_lzw(data: bytes) -> Dict:
        """Benchmark LZW"""
        start = time.time()
        encoded = LZWCompression.encode(data)
        encode_time = time.time() - start
        
        start = time.time()
        decompressed = LZWCompression.decode(encoded)
        decode_time = time.time() - start
        
        original_size = len(data)
        # Mỗi mã là 2 bytes (16 bits)
        compressed_size = len(encoded) * 2
        ratio = (1 - compressed_size / original_size) * 100 if original_size > 0 else 0
        
        return {
            'name': 'LZW',
            'original_size': original_size,
            'compressed_size': compressed_size,
            'ratio': ratio,
            'encode_time': encode_time,
            'decode_time': decode_time,
            'success': decompressed == data
        }
    
    @staticmethod
    def benchmark_all(data: bytes) -> List[Dict]:
        """So sánh tất cả thuật toán"""
        results = []
        
        try:
            results.append(CompressionBenchmark.benchmark_rlc(data))
        except Exception as e:
            results.append({'name': 'RLC', 'error': str(e)})
        
        try:
            results.append(CompressionBenchmark.benchmark_huffman(data))
        except Exception as e:
            results.append({'name': 'Huffman', 'error': str(e)})
        
        try:
            results.append(CompressionBenchmark.benchmark_lzw(data))
        except Exception as e:
            results.append({'name': 'LZW', 'error': str(e)})
        
        return results


if __name__ == '__main__':
    # Test
    test_data = b'AAABBBCCCDDDEEEEAAABBBCCC' * 100
    
    print("=" * 80)
    print("TEST CÁC THUẬT TOÁN NÉN")
    print("=" * 80)
    print(f"\nDữ liệu test: {len(test_data)} bytes\n")
    
    results = CompressionBenchmark.benchmark_all(test_data)
    
    print(f"{'Thuật toán':<15} {'Kích thước':<15} {'Tỷ lệ':<12} {'Encode':<12} {'Decode':<12} {'OK':<5}")
    print("-" * 80)
    
    for result in results:
        if 'error' not in result:
            print(f"{result['name']:<15} {result['compressed_size']:<15} "
                  f"{result['ratio']:>10.2f}% {result['encode_time']:>10.6f}s "
                  f"{result['decode_time']:>10.6f}s {str(result['success']):<5}")
        else:
            print(f"{result['name']:<15} Error: {result['error']}")
    
    print("\n" + "=" * 80)

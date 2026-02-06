# 📚 Chi Tiết Các Thuật Toán Nén

## 1. RLC (Run-Length Encoding)

### Định Nghĩa
Run-Length Encoding là một phương pháp nén dữ liệu đơn giản, thay thế các chuỗi byte giống nhau bằng một cặp (byte, count).

### Công Thức Toán Học

```
Nén:
  Input:  AAABBBCCCDDD
  Output: A3B3C3D3

Giải nén:
  Input:  A3B3C3D3
  Output: AAABBBCCCDDD

Tỷ lệ nén:
  Ratio = (1 - compressed_size / original_size) × 100%
```

### Thuật Toán

**Encode:**
```
1. Khởi tạo output rỗng
2. Duyệt qua từng byte trong input
3. Đếm số lần byte hiện tại lặp lại
4. Lưu (byte, count) vào output
5. Tiếp tục với byte tiếp theo
```

**Decode:**
```
1. Khởi tạo output rỗng
2. Duyệt qua output theo cặp (byte, count)
3. Thêm byte vào output count lần
4. Tiếp tục với cặp tiếp theo
```

### Ví Dụ Chi Tiết

```
Input:  AAABBBCCCDDD (12 bytes)
Step 1: A lặp 3 lần → A3
Step 2: B lặp 3 lần → B3
Step 3: C lặp 3 lần → C3
Step 4: D lặp 3 lần → D3
Output: A3B3C3D3 (8 bytes)

Tỷ lệ nén = (1 - 8/12) × 100% = 33.33%
```

### Độ Phức Tạp

- **Encode:** O(n) - duyệt qua mỗi byte một lần
- **Decode:** O(n) - duyệt qua mỗi cặp một lần
- **Space:** O(n) - trong trường hợp xấu nhất

### Ưu Điểm

✅ Đơn giản, dễ hiểu
✅ Rất nhanh (O(n))
✅ Không cần overhead (bảng mã, tree)
✅ Tốt cho dữ liệu có nhiều byte lặp lại

### Nhược Điểm

❌ Kém hiệu quả với dữ liệu ngẫu nhiên
❌ Có thể làm file lớn hơn nếu không có byte lặp lại
❌ Tỷ lệ nén phụ thuộc vào dữ liệu

### Trường Hợp Sử Dụng

- Ảnh đơn sắc (monochrome)
- Dữ liệu có nhiều byte lặp lại
- Cần nén nhanh

---

## 2. Huffman Coding

### Định Nghĩa
Huffman Coding là một phương pháp nén dữ liệu dựa trên tần suất xuất hiện của từng byte. Byte xuất hiện nhiều được mã hóa bằng bit string ngắn, byte ít xuất hiện được mã hóa bằng bit string dài.

### Công Thức Toán Học

```
Tần suất:
  A: 5 lần
  B: 3 lần
  C: 2 lần

Xây dựng Huffman Tree:
  Bước 1: Tạo node cho mỗi byte với tần suất
  Bước 2: Gộp 2 node có tần suất nhỏ nhất
  Bước 3: Lặp lại cho đến khi còn 1 node

Mã hóa:
  A = '0'      (1 bit)
  B = '10'     (2 bits)
  C = '11'     (2 bits)

Nén:
  Input:  AAABBBCC
  Output: 0000101011 (10 bits = 1.25 bytes)

Tỷ lệ nén:
  Ratio = (1 - (bits_compressed / 8) / original_size) × 100%
```

### Thuật Toán

**Build Huffman Tree:**
```
1. Tính tần suất của mỗi byte
2. Tạo priority queue với các node
3. Lặp lại:
   a. Pop 2 node có tần suất nhỏ nhất
   b. Tạo parent node với tần suất = left.freq + right.freq
   c. Push parent vào queue
4. Node còn lại là root
```

**Encode:**
```
1. Xây dựng Huffman tree
2. Tạo bảng mã từ tree (0=trái, 1=phải)
3. Thay thế mỗi byte bằng mã của nó
4. Lưu bảng mã + dữ liệu nén
```

**Decode:**
```
1. Đọc bảng mã
2. Duyệt qua bit string
3. Theo dõi đường đi trong tree (0=trái, 1=phải)
4. Khi đến leaf node, lưu byte và reset
```

### Ví Dụ Chi Tiết

```
Input: AAABBBCC (8 bytes = 64 bits)

Bước 1: Tính tần suất
  A: 3
  B: 3
  C: 2

Bước 2: Xây dựng tree
  Tạo node: A(3), B(3), C(2)
  Gộp C(2) + B(3) = CB(5)
  Gộp A(3) + CB(5) = ACB(8)
  
  Tree:
       ACB(8)
      /      \
    A(3)    CB(5)
           /    \
         C(2)  B(3)

Bước 3: Tạo bảng mã
  A = '0'
  B = '11'
  C = '10'

Bước 4: Nén
  A A A B B B C C
  0 0 0 11 11 11 10 10
  = 00011111110 10 (14 bits)

Tỷ lệ nén = (1 - (14/8)/8) × 100% = 78.125%
```

### Độ Phức Tạp

- **Encode:** O(n log n) - xây dựng tree
- **Decode:** O(n) - duyệt qua bit string
- **Space:** O(n) - lưu bảng mã

### Ưu Điểm

✅ Tối ưu hóa dựa trên tần suất
✅ Tỷ lệ nén tốt cho dữ liệu có tần suất không đều
✅ Không cần biết dữ liệu trước
✅ Lossless (không mất dữ liệu)

### Nhược Điểm

❌ Cần lưu bảng mã (overhead)
❌ Chậm hơn RLC
❌ Phức tạp hơn RLC

### Trường Hợp Sử Dụng

- Dữ liệu có tần suất không đều
- Cần tỷ lệ nén tốt
- Dữ liệu text, log files

---

## 3. LZW (Lempel-Ziv-Welch)

### Định Nghĩa
LZW là một phương pháp nén dữ liệu dựa trên từ điển động. Thay thế chuỗi byte lặp lại bằng mã từ điển.

### Công Thức Toán Học

```
Từ điển ban đầu:
  0-255: tất cả byte đơn

Quá trình:
  1. Khởi tạo từ điển
  2. Duyệt qua input
  3. Tìm chuỗi dài nhất trong từ điển
  4. Lưu mã của chuỗi
  5. Thêm chuỗi mới vào từ điển
  6. Tiếp tục

Nén:
  Input:  ABABA
  Output: [65, 256, 257, 258, 65]

Tỷ lệ nén:
  Ratio = (1 - (len(codes) × 2) / original_size) × 100%
```

### Thuật Toán

**Encode:**
```
1. Khởi tạo từ điển với 256 mã (0-255)
2. current_string = ''
3. Duyệt qua mỗi byte:
   a. combined = current_string + byte
   b. Nếu combined trong từ điển:
      - current_string = combined
   c. Nếu không:
      - Lưu mã của current_string
      - Thêm combined vào từ điển
      - current_string = byte
4. Lưu mã của current_string cuối cùng
```

**Decode:**
```
1. Khởi tạo từ điển với 256 mã (0-255)
2. current_string = dictionary[code[0]]
3. Lưu current_string
4. Duyệt qua code[1:]:
   a. Nếu code trong từ điển:
      - entry = dictionary[code]
   b. Nếu không:
      - entry = current_string + current_string[0]
   c. Lưu entry
   d. Thêm (current_string + entry[0]) vào từ điển
   e. current_string = entry
```

### Ví Dụ Chi Tiết

```
Input: ABABA (5 bytes)

Encode:
  Từ điển ban đầu: 0-255 (A=65, B=66)
  
  Bước 1: A
    - current_string = ''
    - combined = '' + A = A
    - A trong từ điển → current_string = A
  
  Bước 2: B
    - combined = A + B = AB
    - AB không trong từ điển
    - Lưu mã của A = 65
    - Thêm AB vào từ điển (mã 256)
    - current_string = B
  
  Bước 3: A
    - combined = B + A = BA
    - BA không trong từ điển
    - Lưu mã của B = 66
    - Thêm BA vào từ điển (mã 257)
    - current_string = A
  
  Bước 4: B
    - combined = A + B = AB
    - AB trong từ điển (mã 256)
    - current_string = AB
  
  Bước 5: A
    - combined = AB + A = ABA
    - ABA không trong từ điển
    - Lưu mã của AB = 256
    - Thêm ABA vào từ điển (mã 258)
    - current_string = A
  
  Cuối: Lưu mã của A = 65
  
  Output: [65, 66, 256, 65] (4 mã = 8 bytes)

Tỷ lệ nén = (1 - 8/5) × 100% = -60% (không nén được)
```

### Độ Phức Tạp

- **Encode:** O(n) - duyệt qua mỗi byte một lần
- **Decode:** O(n) - duyệt qua mỗi mã một lần
- **Space:** O(dictionary_size) - lưu từ điển

### Ưu Điểm

✅ Linh hoạt, không cần biết tần suất trước
✅ Tốt cho dữ liệu có mẫu lặp lại
✅ Không cần lưu bảng mã
✅ Nhanh (O(n))

### Nhược Điểm

❌ Kém hiệu quả với dữ liệu ngẫu nhiên
❌ Cần lưu từ điển (overhead)
❌ Giới hạn kích thước từ điển (4096 mã)

### Trường Hợp Sử Dụng

- Dữ liệu có mẫu lặp lại
- Không cần biết tần suất trước
- Dữ liệu nén (GIF, TIFF)

---

## So Sánh Chi Tiết

| Tiêu Chí | RLC | Huffman | LZW |
|---------|-----|---------|-----|
| **Độ phức tạp Encode** | O(n) | O(n log n) | O(n) |
| **Độ phức tạp Decode** | O(n) | O(n) | O(n) |
| **Tỷ lệ nén** | 0-90% | 20-80% | 10-70% |
| **Tốc độ** | Rất nhanh | Nhanh | Nhanh |
| **Overhead** | Không | Bảng mã | Từ điển |
| **Lossless** | Có | Có | Có |
| **Tốt cho** | Dữ liệu lặp | Tần suất không đều | Mẫu lặp |

---

## Công Thức Tính Tỷ Lệ Nén

```
Tỷ lệ nén = (1 - compressed_size / original_size) × 100%

Ví dụ:
  Original: 1000 bytes
  Compressed: 300 bytes
  Ratio = (1 - 300/1000) × 100% = 70%
```

## Công Thức Tính PSNR

```
PSNR = 20 × log₁₀(MAX / √MSE)

Trong đó:
  MAX = 255 (giá trị pixel tối đa)
  MSE = (1/N) × Σ(original[i] - compressed[i])²
  N = số pixel

Ví dụ:
  MSE = 10
  PSNR = 20 × log₁₀(255 / √10) = 28.1 dB
```

## Công Thức Tính SSIM

```
SSIM = (2μₓμᵧ + c₁)(2σₓᵧ + c₂) / ((μₓ² + μᵧ² + c₁)(σₓ² + σᵧ² + c₂))

Trong đó:
  μₓ, μᵧ = trung bình của x, y
  σₓ², σᵧ² = phương sai của x, y
  σₓᵧ = hiệp phương sai
  c₁, c₂ = hằng số ổn định

Kết quả:
  SSIM ∈ [0, 1]
  1 = ảnh giống hệt nhau
  0 = ảnh hoàn toàn khác
```

---

**Cập nhật lần cuối:** Tháng 2, 2026

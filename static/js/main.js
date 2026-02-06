// DOM Elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const resultsDiv = document.getElementById('results');
const loadingDiv = document.getElementById('loading');
const resultsTable = document.getElementById('resultsTable');
const comparisonGrid = document.getElementById('comparisonGrid');
const algorithmsGrid = document.getElementById('algorithmsGrid');
const comparisonTableBody = document.getElementById('comparisonTableBody');

// Event Listeners
uploadArea.addEventListener('click', () => fileInput.click());
uploadArea.addEventListener('dragover', handleDragOver);
uploadArea.addEventListener('drop', handleDrop);
fileInput.addEventListener('change', handleFileSelect);

// Drag and Drop
function handleDragOver(e) {
    e.preventDefault();
    uploadArea.style.borderColor = 'var(--secondary-color)';
    uploadArea.style.backgroundColor = '#f0fff4';
}

function handleDrop(e) {
    e.preventDefault();
    uploadArea.style.borderColor = 'var(--primary-color)';
    uploadArea.style.backgroundColor = '#f0f7ff';

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        handleFileSelect();
    }
}

// File Selection
function handleFileSelect() {
    const file = fileInput.files[0];
    if (file) {
        compressImage(file);
    }
}

// Compress Image
async function compressImage(file) {
    const formData = new FormData();
    formData.append('file', file);

    // Show loading
    uploadArea.style.display = 'none';
    resultsDiv.style.display = 'none';
    loadingDiv.style.display = 'block';

    try {
        const response = await fetch('/api/compress', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Lỗi nén ảnh');
        }

        const data = await response.json();

        if (data.success) {
            displayResults(data, file);
        } else {
            alert('Lỗi: ' + data.error);
        }
    } catch (error) {
        alert('Lỗi: ' + error.message);
    } finally {
        loadingDiv.style.display = 'none';
    }
}

// Display Results
function displayResults(data, file) {
    // Original Info
    document.getElementById('originalSize').textContent = formatBytes(data.original_size);
    document.getElementById('originalFormat').textContent = file.type || 'Unknown';

    // Results Table
    resultsTable.innerHTML = '';
    const methods = ['jpeg', 'png', 'webp_lossy', 'webp_lossless'];
    const methodNames = {
        'jpeg': 'JPEG',
        'png': 'PNG',
        'webp_lossy': 'WebP Lossy',
        'webp_lossless': 'WebP Lossless'
    };

    let bestRatio = 0;
    let bestMethod = '';

    methods.forEach(method => {
        const result = data.results[method];
        if (result && !result.error) {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><strong>${methodNames[method]}</strong></td>
                <td>${formatBytes(result.size)}</td>
                <td>${result.ratio.toFixed(2)}%</td>
                <td>${result.psnr.toFixed(2)} dB</td>
                <td>${result.ssim.toFixed(4)}</td>
                <td>${result.time.toFixed(4)}s</td>
            `;
            resultsTable.appendChild(row);

            if (result.ratio > bestRatio) {
                bestRatio = result.ratio;
                bestMethod = methodNames[method];
            }
        }
    });

    // Comparison Grid
    comparisonGrid.innerHTML = '';
    methods.forEach(method => {
        const result = data.results[method];
        if (result && !result.error) {
            const item = document.createElement('div');
            item.className = 'comparison-item';
            item.innerHTML = `
                <img src="${result.image}" alt="${methodNames[method]}">
                <div class="comparison-item-info">
                    <h4>${methodNames[method]}</h4>
                    <div class="metric">
                        <span>Kích thước:</span>
                        <strong>${formatBytes(result.size)}</strong>
                    </div>
                    <div class="metric">
                        <span>Tỷ lệ:</span>
                        <strong>${result.ratio.toFixed(2)}%</strong>
                    </div>
                    <div class="metric">
                        <span>PSNR:</span>
                        <strong>${result.psnr.toFixed(2)} dB</strong>
                    </div>
                    <div class="metric">
                        <span>SSIM:</span>
                        <strong>${result.ssim.toFixed(4)}</strong>
                    </div>
                    <div class="metric">
                        <a class="btn btn-download" href="${result.download}" target="_blank" rel="noopener">Tải xuống</a>
                    </div>
                </div>
            `;
            comparisonGrid.appendChild(item);
        }
    });

    // Recommendation
    const recommendationText = document.getElementById('recommendationText');
    recommendationText.innerHTML = `
        <p><strong>Phương pháp tốt nhất:</strong> ${bestMethod}</p>
        <p><strong>Tỷ lệ nén:</strong> ${bestRatio.toFixed(2)}%</p>
        <p>Phương pháp này cung cấp tỷ lệ nén cao nhất cho ảnh của bạn.</p>
    `;

    // Show results
    resultsDiv.style.display = 'block';
}

// Reset Compress
function resetCompress() {
    uploadArea.style.display = 'block';
    resultsDiv.style.display = 'none';
    fileInput.value = '';
}

// Format Bytes
function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

// Load Algorithms
async function loadAlgorithms() {
    try {
        const response = await fetch('/api/algorithms');
        const algorithms = await response.json();

        algorithmsGrid.innerHTML = '';
        algorithms.forEach(algo => {
            const card = document.createElement('div');
            card.className = 'algorithm-card';

            const badgeClass = algo.type === 'Lossy' ? 'badge-lossy' : 'badge-lossless';

            card.innerHTML = `
                <h3>${algo.name}</h3>
                <span class="algorithm-badge ${badgeClass}">${algo.type}</span>
                <div class="algorithm-info">
                    <p><strong>Tỷ lệ nén:</strong> ${algo.ratio}</p>
                    <p><strong>Tốc độ:</strong> ${algo.speed}</p>
                    <p><strong>Chất lượng:</strong> ${algo.quality}</p>
                    <p><strong>Hỗ trợ:</strong> ${algo.support}</p>
                </div>
                <p style="margin-bottom: 15px; color: #7f8c8d;">${algo.description}</p>
                <h4 style="margin-top: 15px; margin-bottom: 10px;">Ưu điểm:</h4>
                <ul class="algorithm-list">
                    ${algo.advantages.map(adv => `<li>${adv}</li>`).join('')}
                </ul>
                <h4 style="margin-bottom: 10px;">Nhược điểm:</h4>
                <ul class="algorithm-list">
                    ${algo.disadvantages.map(dis => `<li>${dis}</li>`).join('')}
                </ul>
            `;

            algorithmsGrid.appendChild(card);
        });

        // Populate comparison table
        comparisonTableBody.innerHTML = '';
        algorithms.forEach(algo => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><strong>${algo.name}</strong></td>
                <td>${algo.type}</td>
                <td>${algo.ratio}</td>
                <td>${algo.speed}</td>
                <td>${algo.quality}</td>
                <td>${algo.support}</td>
            `;
            comparisonTableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Lỗi tải thuật toán:', error);
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadAlgorithms();
});

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Image Modal
const modal = document.getElementById('imageModal');
const modalImg = document.getElementById('modalImage');
const captionText = document.getElementById('caption');
const closeBtn = document.querySelector('.close');

// Mở modal khi nhấp vào ảnh
document.addEventListener('click', function (e) {
    if (e.target.tagName === 'IMG' && e.target.closest('.comparison-item img')) {
        modal.style.display = 'block';
        modalImg.src = e.target.src;
        captionText.innerHTML = e.target.closest('.comparison-item').querySelector('h4').textContent;
    }
});

// Đóng modal khi nhấp vào nút close
closeBtn.addEventListener('click', function () {
    modal.style.display = 'none';
});

// Đóng modal khi nhấp vào ngoài ảnh
modal.addEventListener('click', function (e) {
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});

// Đóng modal khi nhấp phím Escape
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        modal.style.display = 'none';
    }
});

// Tab Switching
function switchTab(tabName) {
    // Ẩn tất cả tab
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));

    // Bỏ active từ tất cả button
    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(btn => btn.classList.remove('active'));

    // Hiển thị tab được chọn
    document.getElementById(tabName).classList.add('active');

    // Thêm active vào button được chọn
    event.target.classList.add('active');
}

// Compress Text
async function compressText() {
    const textInput = document.getElementById('textInput').value;

    if (!textInput) {
        alert('Vui lòng nhập dữ liệu text');
        return;
    }

    const textLoading = document.getElementById('textLoading');
    const textResults = document.getElementById('textResults');

    textLoading.style.display = 'block';
    textResults.style.display = 'none';

    try {
        const response = await fetch('/api/compress-text', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: textInput })
        });

        if (!response.ok) {
            throw new Error('Lỗi nén dữ liệu');
        }

        const data = await response.json();

        if (data.success) {
            displayTextResults(data);
        } else {
            alert('Lỗi: ' + data.error);
        }
    } catch (error) {
        alert('Lỗi: ' + error.message);
    } finally {
        textLoading.style.display = 'none';
    }
}

// Display Text Results
function displayTextResults(data) {
    const textOriginalSize = document.getElementById('textOriginalSize');
    const textCharCount = document.getElementById('textCharCount');
    const textResultsTable = document.getElementById('textResultsTable');
    const textResults = document.getElementById('textResults');

    // Original Info
    textOriginalSize.textContent = data.results.rlc.original_size + ' bytes';
    textCharCount.textContent = data.data.length + ' ký tự';

    // Results Table
    textResultsTable.innerHTML = '';
    const algorithms = ['rlc', 'huffman', 'lzw'];
    const algorithmNames = {
        'rlc': 'RLC (Run-Length Encoding)',
        'huffman': 'Huffman Coding',
        'lzw': 'LZW (Lempel-Ziv-Welch)'
    };

    algorithms.forEach(algo => {
        const result = data.results[algo];
        if (result && !result.error) {
            const row = document.createElement('tr');
            const status = result.success ? '✅ OK' : '❌ Lỗi';
            row.innerHTML = `
                <td><strong>${algorithmNames[algo]}</strong></td>
                <td>${result.compressed_size} bytes</td>
                <td>${result.ratio.toFixed(2)}%</td>
                <td>${status}</td>
            `;
            textResultsTable.appendChild(row);
        } else if (result && result.error) {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><strong>${algorithmNames[algo]}</strong></td>
                <td colspan="3">❌ Lỗi: ${result.error}</td>
            `;
            textResultsTable.appendChild(row);
        }
    });

    textResults.style.display = 'block';
}

// Reset Text Compress
function resetTextCompress() {
    document.getElementById('textInput').value = '';
    document.getElementById('textResults').style.display = 'none';
}

// Compress Image with Algorithms (RLC, Huffman, LZW)
const uploadAreaAlgo = document.getElementById('uploadAreaAlgo');
const fileInputAlgo = document.getElementById('fileInputAlgo');

uploadAreaAlgo.addEventListener('click', () => fileInputAlgo.click());
uploadAreaAlgo.addEventListener('dragover', handleDragOver);
uploadAreaAlgo.addEventListener('drop', handleDropAlgo);
fileInputAlgo.addEventListener('change', handleFileSelectAlgo);

function handleDropAlgo(e) {
    e.preventDefault();
    uploadAreaAlgo.style.borderColor = 'var(--secondary-color)';
    uploadAreaAlgo.style.backgroundColor = '#f0fff4';

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInputAlgo.files = files;
        handleFileSelectAlgo();
    }
}

function handleFileSelectAlgo() {
    const file = fileInputAlgo.files[0];
    if (file) {
        compressImageAlgo(file);
    }
}

async function compressImageAlgo(file) {
    const formData = new FormData();
    formData.append('file', file);

    uploadAreaAlgo.style.display = 'none';
    document.getElementById('resultsAlgo').style.display = 'none';
    document.getElementById('loadingAlgo').style.display = 'block';

    try {
        const response = await fetch('/api/compress-image-algorithms', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Lỗi nén ảnh');
        }

        const data = await response.json();

        if (data.success) {
            displayResultsAlgo(data, file);
        } else {
            alert('Lỗi: ' + data.error);
        }
    } catch (error) {
        alert('Lỗi: ' + error.message);
    } finally {
        document.getElementById('loadingAlgo').style.display = 'none';
    }
}

function displayResultsAlgo(data, file) {
    document.getElementById('originalSizeAlgo').textContent = formatBytes(data.results.rlc.original_size);
    document.getElementById('originalFormatAlgo').textContent = file.type || 'Unknown';

    const resultsTableAlgo = document.getElementById('resultsTableAlgo');
    resultsTableAlgo.innerHTML = '';

    const methods = ['rlc', 'huffman', 'lzw'];
    const methodNames = {
        'rlc': 'RLC (Run-Length Encoding)',
        'huffman': 'Huffman Coding',
        'lzw': 'LZW (Lempel-Ziv-Welch)'
    };

    methods.forEach(method => {
        const result = data.results[method];
        if (result && !result.error) {
            const row = document.createElement('tr');
            const status = result.success ? '✅ OK' : '❌ Lỗi';
            row.innerHTML = `
                <td><strong>${methodNames[method]}</strong></td>
                <td>${formatBytes(result.compressed_size)}</td>
                <td>${result.ratio.toFixed(2)}%</td>
                <td>${status}</td>
            `;
            resultsTableAlgo.appendChild(row);
        } else if (result && result.error) {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><strong>${methodNames[method]}</strong></td>
                <td colspan="3">❌ Lỗi: ${result.error}</td>
            `;
            resultsTableAlgo.appendChild(row);
        }
    });

    // Display image comparison grid
    const comparisonGridAlgo = document.createElement('div');
    comparisonGridAlgo.className = 'image-comparison';
    comparisonGridAlgo.innerHTML = '<h3>So Sánh Hình Ảnh</h3>';

    const imageGrid = document.createElement('div');
    imageGrid.className = 'comparison-grid';

    // Add original image
    const originalItem = document.createElement('div');
    originalItem.className = 'comparison-item';
    originalItem.innerHTML = `
        <img src="${data.original_image}" alt="Ảnh Gốc">
        <div class="comparison-item-info">
            <h4>Ảnh Gốc</h4>
            <div class="metric">
                <span>Kích thước:</span>
                <strong>${formatBytes(data.results.rlc.original_size)}</strong>
            </div>
        </div>
    `;
    imageGrid.appendChild(originalItem);

    // Add decompressed images
    methods.forEach(method => {
        const result = data.results[method];
        if (result && !result.error && result.image) {
            const item = document.createElement('div');
            item.className = 'comparison-item';
            item.innerHTML = `
                <img src="${result.image}" alt="${methodNames[method]}">
                <div class="comparison-item-info">
                    <h4>${methodNames[method]}</h4>
                    <div class="metric">
                        <span>Kích thước:</span>
                        <strong>${formatBytes(result.compressed_size)}</strong>
                    </div>
                    <div class="metric">
                        <span>Tỷ lệ:</span>
                        <strong>${result.ratio.toFixed(2)}%</strong>
                    </div>
                    <div class="metric">
                        <span>Trạng thái:</span>
                        <strong>${result.success ? '✅ OK' : '❌ Lỗi'}</strong>
                    </div>
                </div>
            `;
            imageGrid.appendChild(item);
        }
    });

    comparisonGridAlgo.appendChild(imageGrid);

    // Insert image comparison after the table
    const resultsAlgoDiv = document.getElementById('resultsAlgo');
    const existingComparison = resultsAlgoDiv.querySelector('.image-comparison');
    if (existingComparison) {
        existingComparison.remove();
    }
    resultsAlgoDiv.insertBefore(comparisonGridAlgo, resultsAlgoDiv.querySelector('.btn-secondary'));

    document.getElementById('resultsAlgo').style.display = 'block';
}

function resetCompressAlgo() {
    uploadAreaAlgo.style.display = 'block';
    document.getElementById('resultsAlgo').style.display = 'none';
    fileInputAlgo.value = '';
}

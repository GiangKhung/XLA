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

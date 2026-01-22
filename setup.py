"""
Setup script for Image Compression System
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="image-compression-system",
    version="1.0.0",
    author="Image Compression Team",
    author_email="your-email@example.com",
    description="A comprehensive image compression system with web interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/image-compression-system",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Flask>=3.0.0",
        "Werkzeug>=3.0.1",
        "opencv-python>=4.8.1.78",
        "Pillow>=11.0.0",
        "numpy>=1.24.3",
        "scikit-image>=0.22.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "flake8>=5.0",
            "black>=22.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "image-compression=app:app",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

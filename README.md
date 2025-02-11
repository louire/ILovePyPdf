# ILovePyPdf

A Python utility for compressing PDF files while maintaining reasonable quality. This tool provides a simple yet effective way to reduce PDF file sizes for easier sharing and storage.

## Features
* Compress PDF files with customizable quality settings
* Maintain reasonable document quality
* Track compression progress
* Generate detailed compression statistics
* Error handling and logging
* Support for both high-quality and maximum compression modes

## Requirements
* Python 3.6 or higher
* PyPDF2 library

## Installation

### 1. Clone this repository:
```bash
git clone https://github.com/louire/ILovePyPdf.git`
cd ILovePyPdf`
```
### 2. Install required dependencies:
```bash
pip install PyPDF2`
```
## Usage

### Basic Usage
```bash
`from pdf_compressor import compress_pdf`

`# Compress with high quality (default)`
`compress_pdf("input.pdf", "output_compressed.pdf")`

`# Compress with lower quality for smaller file size`
`compress_pdf("input.pdf", "output_compressed.pdf", high_quality=False)`
```
### Command Line Usage

`python pdf_compressor.py`

### Example Output
```bash
Processing 5 pages...`
Compressed page 1/5`
Compressed page 2/5`
Compressed page 3/5`
Compressed page 4/5`
Compressed page 5/5`
Saving compressed file...`

Compression completed successfully!`
Original size: 1024.55 KB`
Compressed size: 428.73 KB`
Reduction: 58.2%`
Processing time: 2.34 seconds`
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Author
[@louire](https://github.com/louire)

## Acknowledgments
* PyPDF2 library and its contributors
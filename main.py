"""
I Love PyPDF

This script provides functionality to compress PDF files while maintaining reasonable quality.
It uses PyPDF2 library to handle PDF compression with different quality settings.

Features:
- Compress PDF files with customizable quality settings
- Display compression statistics
- Error handling and detailed logging
- Progress tracking for large files

Dependencies:
- PyPDF2
- os (built-in)

Author: Loui Recio
"""

from PyPDF2 import PdfReader, PdfWriter
import os
from datetime import datetime

def compress_pdf(input_file, output_file, high_quality=True):
    """
    Compress a PDF file while attempting to maintain reasonable quality.
    
    Args:
        input_file (str): Path to the input PDF file
        output_file (str): Path where the compressed PDF will be saved
        high_quality (bool): If True, uses higher quality compression settings
                           If False, uses more aggressive compression
    
    Returns:
        dict: Dictionary containing compression statistics:
              - original_size: Size of original file in KB
              - compressed_size: Size of compressed file in KB
              - reduction_percent: Percentage of size reduction
              - processing_time: Time taken to compress
    
    Raises:
        FileNotFoundError: If input file doesn't exist
        PermissionError: If script lacks permission to read/write files
        Exception: For other unexpected errors
    """
    try:
        # Record start time for performance metrics
        start_time = datetime.now()
        
        # Validate input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")
        
        # Initialize PDF reader and writer
        reader = PdfReader(input_file)
        writer = PdfWriter()
        
        # Get total number of pages for progress tracking
        total_pages = len(reader.pages)
        print(f"Processing {total_pages} pages...")
        
        # Process each page
        for page_number, page in enumerate(reader.pages, 1):
            # Set compression parameters based on quality setting
            if high_quality:
                # High quality: Use standard compression
                page.compress_content_streams()  # Default compression
            else:
                # Lower quality: Use maximum compression
                page.compress_content_streams(level=9)
            
            # Add compressed page to output PDF
            writer.add_page(page)
            
            # Show progress
            print(f"Compressed page {page_number}/{total_pages}")
        
        # Save the compressed PDF
        print("Saving compressed file...")
        with open(output_file, 'wb') as output:
            writer.write(output)
        
        # Calculate compression statistics
        original_size = os.path.getsize(input_file) / 1024  # Convert to KB
        compressed_size = os.path.getsize(output_file) / 1024  # Convert to KB
        reduction = ((original_size - compressed_size) / original_size) * 100
        processing_time = (datetime.now() - start_time).total_seconds()
        
        # Prepare statistics dictionary
        stats = {
            'original_size': round(original_size, 2),
            'compressed_size': round(compressed_size, 2),
            'reduction_percent': round(reduction, 1),
            'processing_time': round(processing_time, 2)
        }
        
        # Print compression results
        print("\nCompression completed successfully!")
        print(f"Original size: {stats['original_size']} KB")
        print(f"Compressed size: {stats['compressed_size']} KB")
        print(f"Reduction: {stats['reduction_percent']}%")
        print(f"Processing time: {stats['processing_time']} seconds")
        
        return stats
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except PermissionError:
        print("Error: Permission denied when trying to read/write files")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        raise

def main():
    """
    Main function to demonstrate PDF compression usage.
    """
    # Example usage
    try:
        input_file = "example.pdf"
        output_file = "example_compressed.pdf"
        
        # Compress with high quality (default)
        stats = compress_pdf(input_file, output_file)
        
        # Alternative: Compress with lower quality for smaller file size
        # stats = compress_pdf(input_file, output_file, high_quality=False)
        
    except Exception as e:
        print(f"Compression failed: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
#!/usr/bin/env python3
import os
import sys
import argparse
from typing import Optional
import PyPDF2
import re

class PDFToMarkdownConverter:
    def __init__(self, input_file: str, output_file: Optional[str] = None):
        """
        Initialize the converter with input and output files.
        
        Args:
            input_file (str): Path to the input PDF file
            output_file (str, optional): Path to the output Markdown file
        """
        self.input_file = input_file
        self.output_file = output_file or self._generate_output_filename()
        
    def _generate_output_filename(self) -> str:
        """Generate output filename by replacing .pdf extension with .md"""
        base_name = os.path.splitext(self.input_file)[0]
        return f"{base_name}.md"
    
    def _clean_text(self, text: str) -> str:
        """
        Clean extracted text by:
        - Removing multiple spaces
        - Converting multiple newlines to double newlines
        - Adding proper markdown formatting
        """
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Convert common PDF artifacts
        text = text.replace('•', '-')  # Convert bullets
        
        # Handle basic formatting
        # Note: This is a simple implementation. For more complex documents,
        # you might need more sophisticated formatting detection
        
        # Detect and format headers (lines ending with colon)
        text = re.sub(r'^(.+):(\s*)$', r'### \1', text, flags=re.MULTILINE)
        
        # Add paragraph breaks
        text = re.sub(r'\n\s*\n', '\n\n', text)
        
        return text.strip()
    
    def convert(self) -> bool:
        """
        Convert PDF to Markdown format
        
        Returns:
            bool: True if conversion was successful, False otherwise
        """
        try:
            # Open PDF file
            with open(self.input_file, 'rb') as file:
                # Create PDF reader object
                pdf_reader = PyPDF2.PdfReader(file)
                
                # Extract text from all pages
                markdown_content = []
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    cleaned_text = self._clean_text(text)
                    markdown_content.append(cleaned_text)
                
                # Join all pages with double newlines
                final_content = '\n\n'.join(markdown_content)
                
                # Write to output file
                with open(self.output_file, 'w', encoding='utf-8') as md_file:
                    md_file.write(final_content)
                
                return True
                
        except Exception as e:
            print(f"Error during conversion: {str(e)}", file=sys.stderr)
            return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert PDF files to Markdown format')
    parser.add_argument('input_file', help='Path to the input PDF file')
    parser.add_argument('-o', '--output', help='Path to the output Markdown file (optional)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create converter instance
    converter = PDFToMarkdownConverter(args.input_file, args.output)
    
    # Perform conversion
    if args.verbose:
        print(f"Converting {args.input_file} to Markdown...")
    
    success = converter.convert()
    
    if success:
        if args.verbose:
            print(f"Conversion completed successfully. Output saved to: {converter.output_file}")
        sys.exit(0)
    else:
        if args.verbose:
            print("Conversion failed.", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

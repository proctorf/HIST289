#!/usr/bin/env python3

import PyPDF2
import sys

def extract_pdf_text(pdf_path):
    """Extract text from PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get number of pages
            num_pages = len(pdf_reader.pages)
            print(f"PDF has {num_pages} pages")
            
            # Extract text from all pages
            full_text = ""
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                full_text += f"\n\n--- PAGE {page_num + 1} ---\n\n"
                full_text += text
                
            return full_text
            
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

if __name__ == "__main__":
    pdf_path = "/Users/proctorf/Documents/GitHub/HIST289/Tableau-Power-Start-Workbook-2020-Week-1.pdf"
    
    text = extract_pdf_text(pdf_path)
    if text:
        # Save to file
        output_file = "/Users/proctorf/Documents/GitHub/HIST289/tableau-workbook-extracted.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Text extracted and saved to: {output_file}")
    else:
        print("Failed to extract text from PDF")
import PyPDF2
# need following pip to run
# pip install PyPDF2
import sys
import os

def extract_text_from_pdf(pdf_path):
    try:
        # Get PDF file location and file name
        dir_name, pdf_file_name = os.path.split(pdf_path)
        base_name, _ = os.path.splitext(pdf_file_name)
        
        # Create path for output
        txt_file_name = os.path.join(dir_name, f"{base_name}.txt")
        
        # Open PDF file
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            
            # Get number of pages
            num_pages = len(reader.pages)
            
            # Declare variable to store text
            text = ""
            
            # Extract text from each pages
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text() + "\n"
            
            # Save test for designated file name
            with open(txt_file_name, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
        
        print(f"Text saved as '{txt_file_name}' successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python yubaba.py <PDF filepath>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    extract_text_from_pdf(pdf_path)

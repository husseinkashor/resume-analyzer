from pdfminer.high_level import extract_text as extract_pdf_text

def extract_text(pdf_path):
    return extract_pdf_text(pdf_path)

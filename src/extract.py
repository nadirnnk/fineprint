import PyPDF2

def extract_text_from_pdf(pdf_file, max_chars=3000):
    """
    Extracts text from the first page of the PDF and truncates.
    """
    reader = PyPDF2.PdfReader(pdf_file)
    if len(reader.pages) == 0:
        raise ValueError("PDF has no pages")
    text = reader.pages[0].extract_text()
    if not text:
        raise ValueError("No text extracted from PDF")
    return text[:max_chars]
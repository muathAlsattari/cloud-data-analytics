from PyPDF2 import PdfReader
from docx import Document

def extract_title_pdf(path):
    reader = PdfReader(path)
    return reader.metadata.title if reader.metadata else "Unknown"

def extract_title_docx(path):
    doc = Document(path)
    return doc.core_properties.title or "Unknown"

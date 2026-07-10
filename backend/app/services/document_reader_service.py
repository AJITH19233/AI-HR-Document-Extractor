import os
import fitz
import pytesseract
from PIL import Image
from docx import Document
from app.services.ocr_service import extract_text as image_ocr
def extract_text(file_path: str):
    extension = os.path.splitext(file_path)[1].lower()
    if extension in [".png", ".jpg", ".jpeg"]:
        return image_ocr(file_path)
    elif extension == ".pdf":
        pdf = fitz.open(file_path)
        text = ""
        for page in pdf:
            text += page.get_text()
        pdf.close()
        return text
    elif extension == ".docx":
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    else:
        raise ValueError("Unsupported file type.")
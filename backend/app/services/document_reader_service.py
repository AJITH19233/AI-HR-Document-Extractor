import os
import fitz
import pytesseract
from PIL import Image
from docx import Document
from app.services.ocr_service import perform_ocr, perform_pdf_page_ocr
def extract_text(file_path: str) -> str:
    extension = os.path.splitext(file_path)[1].lower()
    if extension in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(file_path)
    elif extension == ".pdf":
        return extract_text_from_pdf(file_path)
    elif extension == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {extension}")
def extract_text_from_image(file_path: str) -> str:
    ocr_text = perform_pdf_page_ocr(page)
    extracted_text += ocr_text + "\n"
def extract_text_from_pdf(file_path: str) -> str:
    pdf = fitz.open(file_path)
    extracted_text = ""
    for page in pdf:
        page_text = page.get_text().strip()
        if page_text:
            extracted_text += page_text + "\n"
        else:
            pix = page.get_pixmap(dpi=300)
            image = Image.frombytes(
                "RGB",
                [pix.width, pix.height],
                pix.samples
            )
            ocr_text = pytesseract.image_to_string(image)
            extracted_text += ocr_text + "\n"
    pdf.close()
    return extracted_text.strip()
def extract_text_from_docx(file_path: str) -> str:
    """
    Extract text from DOCX.
    """
    document = Document(file_path)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text.strip()
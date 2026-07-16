import pytesseract
from PIL import Image
def perform_ocr(image: Image.Image) -> str:
    text = pytesseract.image_to_string(image)
    return text.strip()
def perform_ocr_from_path(image_path: str) -> str:
    image = Image.open(image_path)
    return perform_ocr(image)
def perform_pdf_page_ocr(page) -> str:
    pix = page.get_pixmap(dpi=300)
    image = Image.frombytes(
        "RGB",
        (pix.width, pix.height),
        pix.samples
    )
    return perform_ocr(image)
from PIL import Image
def perform_ocr(image: Image.Image) -> str:
    text = pytesseract.image_to_string(image)
    return text.strip()
def perform_ocr_from_path(image_path: str) -> str:
    image = Image.open(image_path)
    return perform_ocr(image)
def perform_pdf_page_ocr(page) -> str:
    pix = page.get_pixmap(dpi=300)
    image = Image.frombytes(
        "RGB",
        (pix.width, pix.height),
        pix.samples
    )
    return perform_ocr(image)
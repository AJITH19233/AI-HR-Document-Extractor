import pytesseract
from PIL import Image

def extract_text(file_path: str):
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        raise Exception(f"OCR failed: {str(e)}")
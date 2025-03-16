from PIL import Image
import pytesseract

class OCRExtractor:
    def __init__(self, tesseract_cmd=None):
        # Установите путь к Tesseract OCR, если он не задан по умолчанию.
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def extract_text(self, image_path):
        """Извлекает текст из изображения."""
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            raise RuntimeError(f"Ошибка при извлечении текста: {e}")

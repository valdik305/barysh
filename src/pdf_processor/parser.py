
from PIL import Image
import pytesseract


class PDFParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self):
        """Определяет тип файла и парсит его."""
        if self.file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            return self._parse_image()
        elif self.file_path.lower().endswith('.pdf'):
            return self._parse_pdf()
        else:
            raise ValueError("Неподдерживаемый формат файла")

    def _parse_image(self):
        """Парсинг изображения с использованием OCR."""
        image = Image.open(self.file_path)
        text = pytesseract.image_to_string(image)
        return {"text": text.strip()}

    def _parse_pdf(self):
        """Парсинг PDF (реализовано ранее)."""
        # Путь к изображению
        image_path = 'D:/foto'  # Замените на путь к вашему изображению

        # Открытие изображения
        image = Image.open(image_path)

        # Извлечение текста из изображения
        extracted_text = pytesseract.image_to_string(image)

        # Вывод извлеченного текста
        print("Извлеченный текст:")
        print(extracted_text)
        # Ваш существующий код для PDF-парсинга.
        pass

from pdf_processor.pdf_processor import PDFParser, PDFValidator

from pdf_processor.ocr_extractor import OCRExtractor
def main():
    parser = PDFParser("tests/test_data/test_sample.pdf")
    data = parser.parse()

    validator = PDFValidator()
    if validator.validate(data):
        print("Документ валиден:")
        print(f"Дата: {data['date']}")
        print(f"Сумма: {data['amount']}")
    else:
        print("Ошибки валидации:")
        for error in validator.errors:
            print(f"- {error}")


if __name__ == "__main__":
    main()




def main():
    ocr = OCRExtractor(tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe')
    extracted_text = ocr.extract_text("tests/test_data/image.jpg")

    print("Извлеченный текст:")
    print(extracted_text)


if __name__ == "__main__":
    main()

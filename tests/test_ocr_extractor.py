import pytest
from pdf_processor.ocr_extractor import OCRExtractor

@pytest.fixture
def ocr():
    return OCRExtractor(tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe')

def test_extract_text(ocr):
    text = ocr.extract_text("tests/test_data/image.jpg")
    assert "GRIFFON AVIATION SERVICES LLC" in text
    assert "EXP DATE: 13.04.2022" in text

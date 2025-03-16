import pytest
from src.pdf_processor.parser import PDFParser

@pytest.fixture
def sample_patterns():
    return {
        "PO": re.compile(r"PO:\s*(P\d+)")
    }

def test_po_extraction(sample_patterns):
    parser = PDFParser(sample_patterns)
    result = parser.extract_data("tests/test_data/reference.pdf")
    assert result["PO"] == "P101"
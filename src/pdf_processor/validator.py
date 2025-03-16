from dataclasses import dataclass
from typing import List, Dict, re


@dataclass
class ValidationRule:
    field: str
    pattern: re.Pattern
    position: tuple = None  # (x0, y0, x1, y1)


class PDFValidator:
    def __init__(self, rules: List[ValidationRule]):
        self.rules = rules

    def validate(self, file_path: str) -> Dict:
# ... логика валидации ...
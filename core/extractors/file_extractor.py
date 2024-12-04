from PyPDF2 import PdfReader
from core.types import Extractor

__all__ = ["get_file_extractor"]


def get_file_extractor(file_name: str) -> Extractor:
    def extractor(_):
        reader = PdfReader(file_name)
        return "".join([page.extract_text() for page in reader.pages])

    return extractor

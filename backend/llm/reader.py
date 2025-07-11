import base64
from io import BytesIO
from pypdf import PdfReader
from fastapi import UploadFile


def read_pdf_file(file_contents: BytesIO) -> str:
    reader = PdfReader(file_contents)
    text = ""
    for page in reader.pages:
        try:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        except Exception as e:
            print(f"Warning: Could not extract text from a page in the PDF: {e}")
            continue
    return text


def encode_image_file(file: UploadFile) -> str:
    return base64.b64encode(file.file.read()).decode("utf-8")

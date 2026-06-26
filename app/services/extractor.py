from pathlib import Path
from pypdf import PdfReader
from docx import Document
from bs4 import BeautifulSoup
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io


def requires_ocr_for_pdf(file_path: str, min_text_chars: int = 100) -> bool:
    """
    Detect whether a PDF likely needs OCR.
    If very little text is extractable from first few pages,
    it is probably a scanned PDF.
    """
    reader = PdfReader(file_path)
    extracted_text = ""

    for page in reader.pages[:3]:
        text = page.extract_text()
        if text:
            extracted_text += text.strip()

    return len(extracted_text) < min_text_chars


def extract_text_with_ocr(file_path: str) -> str:
    """
    Convert PDF pages to images and run OCR.
    """
    doc = fitz.open(file_path)
    all_text = []

    for page_number in range(len(doc)):
        page = doc[page_number]

        pix = page.get_pixmap(dpi=300)

        image = Image.open(io.BytesIO(pix.tobytes("png")))

        text = pytesseract.image_to_string(image)

        if text.strip():
            all_text.append(f"\n--- Page {page_number + 1} ---\n{text}")

    return "\n".join(all_text)


def extract_text_from_pdf(file_path: str) -> dict:
    """
    Extract PDF text normally.
    If text is too low, run OCR.
    """
    ocr_required = requires_ocr_for_pdf(file_path)

    if ocr_required:
        text = extract_text_with_ocr(file_path)
        return {
            "text": text,
            "ocr_required": True,
            "ocr_used": True
        }

    reader = PdfReader(file_path)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    return {
        "text": text,
        "ocr_required": False,
        "ocr_used": False
    }


def extract_text(file_path: str) -> dict:
    path = Path(file_path)
    ext = path.suffix.lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)

    if ext == ".docx":
        doc = Document(file_path)
        text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
        return {
            "text": text,
            "ocr_required": False,
            "ocr_used": False
        }

    if ext in [".html", ".htm"]:
        soup = BeautifulSoup(
            path.read_text(encoding="utf-8", errors="ignore"),
            "html.parser"
        )
        text = soup.get_text(separator="\n")
        return {
            "text": text,
            "ocr_required": False,
            "ocr_used": False
        }

    if ext in [".txt", ".md", ".json", ".csv", ".py", ".js", ".ts"]:
        text = path.read_text(encoding="utf-8", errors="ignore")
        return {
            "text": text,
            "ocr_required": False,
            "ocr_used": False
        }

    return {
        "text": "",
        "ocr_required": False,
        "ocr_used": False
    }
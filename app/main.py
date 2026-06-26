import shutil
from pathlib import Path
from fastapi import FastAPI, UploadFile, File

from app.models import ClassificationResponse
from app.services.extractor import extract_text
from app.services.classifier import classify_document
from app.services.classifier import classify_with_llm
from app.services.recommender import recommend

app = FastAPI(title="Document Classifier Service")

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.post("/classify", response_model=ClassificationResponse)
async def classify(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    #text = extract_text(str(file_path))
    extraction_result = extract_text(str(file_path))
    text = extraction_result["text"]

    # classification = classify_document(file.filename, text)
    # recommendation = recommend(classification["document_type"])
    try:
        classification = classify_with_llm(file.filename, text)
    except Exception:
        classification = classify_document(file.filename, text)

    recommendation = recommend(classification["document_type"])

    return ClassificationResponse(
    filename=file.filename,
    file_type=Path(file.filename).suffix,
    document_type=classification["document_type"],
    confidence=classification["confidence"],
    recommended_chunking=recommendation["chunking"],
    requires_ocr=extraction_result["ocr_required"],
    ocr_used=extraction_result["ocr_used"],
    extract_tables=recommendation["tables"],
    metadata_fields=recommendation["metadata"],
    processing_pipeline=recommendation["pipeline"],
)
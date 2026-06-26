from pydantic import BaseModel
from typing import List


class ClassificationResponse(BaseModel):
    filename: str
    file_type: str
    document_type: str
    confidence: float
    recommended_chunking: str
    requires_ocr: bool
    extract_tables: bool
    metadata_fields: List[str]
    processing_pipeline: List[str]


from pydantic import BaseModel
from typing import List


class ClassificationResponse(BaseModel):
    filename: str
    file_type: str
    document_type: str
    confidence: float
    recommended_chunking: str
    requires_ocr: bool
    ocr_used: bool
    extract_tables: bool
    metadata_fields: List[str]
    processing_pipeline: List[str]
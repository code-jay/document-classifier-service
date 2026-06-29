# 📄 Enterprise Document Classifier Service

An enterprise-ready document classification service built with
**FastAPI** that automatically classifies uploaded documents and
recommends the optimal processing strategy for Enterprise AI and RAG
applications.

## Features

-   Upload documents through REST API
-   Automatic document classification
-   Rule-based classifier
-   Optional LLM-powered classifier
-   OCR detection
-   Chunking strategy recommendation
-   Metadata recommendation
-   Processing pipeline recommendation
-   Table extraction recommendation
-   Enterprise AI ready

## Supported Document Types

-   HR Policies
-   Legal Contracts
-   Technical Documentation
-   Research Papers
-   Source Code
-   FAQ / Knowledge Base
-   Invoices
-   General Documents

## Recommended Chunking Strategies

  Document Type             Recommended Strategy
  ------------------------- -----------------------------
  Policy Documents          Section-based Chunking
  Legal Contracts           Section + Semantic Chunking
  Technical Documentation   Heading-based Chunking
  Source Code               Function/Class Chunking
  Research Papers           Semantic Chunking
  FAQ Documents             Question-Answer Chunking
  CSV / Excel               Table Chunking
  General Documents         Fixed-size Chunking

## Processing Pipeline

``` text
Enterprise Documents
        │
        ▼
Text Extraction
        │
        ▼
OCR Detection
        │
        ▼
Document Classification
        │
        ▼
Metadata Recommendation
        │
        ▼
Chunking Strategy Recommendation
        │
        ▼
Table Extraction Decision
        │
        ▼
Chunk Generation
        │
        ▼
Embedding Generation
        │
        ▼
Vector Database
```

## Tech Stack

-   FastAPI
-   Python
-   OpenAI API (optional)
-   Pydantic

## Installation

``` bash
git clone https://github.com/<your-username>/document-classifier.git
cd document-classifier
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

``` bash
uvicorn app.main:app --reload
```

Open:

    http://127.0.0.1:8000/docs

## Sample Response

``` json
{
  "document_type": "Policy / HR Document",
  "recommended_chunking": "Section-based Chunking",
  "requires_ocr": false,
  "extract_tables": false
}
```

## Roadmap

-   Layout Detection
-   Table Detection
-   Local LLM Support
-   Batch Processing
-   Vector Database Integration
-   Evaluation Dashboard

## License

MIT

## Author

**Jay Ram Singh**

Building Enterprise AI Platforms, RAG Systems, Document Intelligence,
and LLMOps.

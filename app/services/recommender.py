def recommend(document_type: str) -> dict:
    mapping = {
        "Source Code": {
            "chunking": "Code-Aware Chunking",
            "ocr": False,
            "tables": False,
            "metadata": ["language", "functions", "classes", "file_path"],
            "pipeline": ["Extract Code", "Parse Structure", "Code Chunking", "Embed"]
        },
        "Legal Contract": {
            "chunking": "Parent-Child + LLM-Assisted Chunking",
            "ocr": False,
            "tables": True,
            "metadata": ["parties", "effective_date", "clauses", "risk_level"],
            "pipeline": ["Extract Text", "Detect Clauses", "Extract Metadata", "Chunk", "Embed"]
        },
        "Policy / HR Document": {
            "chunking": "Structural / Parent-Child Chunking",
            "ocr": False,
            "tables": False,
            "metadata": ["department", "policy_type", "version", "owner"],
            "pipeline": ["Extract Text", "Detect Sections", "Metadata Enrichment", "Chunk", "Embed"]
        },
        "Technical Documentation": {
            "chunking": "Markdown/Header + Semantic Chunking",
            "ocr": False,
            "tables": True,
            "metadata": ["product", "version", "section", "topic"],
            "pipeline": ["Extract Text", "Detect Headings", "Semantic Chunking", "Embed"]
        },
        "FAQ / Knowledge Base": {
            "chunking": "Semantic Chunking",
            "ocr": False,
            "tables": False,
            "metadata": ["topic", "category", "intent", "audience"],
            "pipeline": ["Extract Text", "Detect Q&A", "Semantic Chunking", "Embed"]
        },
    }

    default = {
        "chunking": "Recursive Chunking",
        "ocr": False,
        "tables": False,
        "metadata": ["title", "author", "created_date", "document_type"],
        "pipeline": ["Extract Text", "Clean Text", "Recursive Chunking", "Embed"]
    }

    return mapping.get(document_type, default)
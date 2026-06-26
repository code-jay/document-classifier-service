import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DOCUMENT_TYPES = [
    "Policy / HR Document",
    "Legal Contract",
    "Invoice / Financial Document",
    "Technical Documentation",
    "FAQ / Knowledge Base",
    "Source Code",
    "Research Paper",
    "General Document"
]


def classify_with_llm(filename: str, text: str) -> dict:
    sample_text = text[:4000]

    prompt = f"""
You are an enterprise document classification engine.

Classify the uploaded document into one of these types:
{DOCUMENT_TYPES}

Return ONLY valid JSON in this format:
{{
  "document_type": "...",
  "confidence": 0.0,
  "reason": "...",
  "recommended_metadata": ["..."],
  "recommended_chunking": "..."
}}

Filename: {filename}

Document Content:
{sample_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {"role": "system", "content": "You classify enterprise documents and return valid JSON only."},
            {"role": "user", "content": prompt}
        ],
    )

    result = response.choices[0].message.content
    return json.loads(result)

def classify_document(filename: str, text: str) -> dict:
    name = filename.lower()
    content = text.lower()

    if name.endswith((".py", ".js", ".ts")) or "def " in content or "function " in content:
        return {"document_type": "Source Code", "confidence": 0.95}

    if "agreement" in content or "party" in content or "terms and conditions" in content:
        return {"document_type": "Legal Contract", "confidence": 0.85}

    if "invoice" in content or "amount due" in content or "gst" in content:
        return {"document_type": "Invoice / Financial Document", "confidence": 0.85}

    if "policy" in content or "leave" in content or "employee" in content:
        return {"document_type": "Policy / HR Document", "confidence": 0.80}

    if "api" in content or "endpoint" in content or "request" in content:
        return {"document_type": "Technical Documentation", "confidence": 0.82}

    if "question" in content or "faq" in content:
        return {"document_type": "FAQ / Knowledge Base", "confidence": 0.78}

    return {"document_type": "General Document", "confidence": 0.60}
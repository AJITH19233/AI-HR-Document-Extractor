import re
def classify_document(extracted_text: str) -> str:
    if not extracted_text:
        return "UNKNOWN"
    text = extracted_text.upper()
    if (
        "UNIQUE IDENTIFICATION AUTHORITY OF INDIA" in text
        or "AADHAAR" in text
        or "UIDAI" in text
        or re.search(r"\b\d{4}\s\d{4}\s\d{4}\b", text)
    ):
        return "AADHAAR"
    if (
        "INCOME TAX DEPARTMENT" in text
        or "PERMANENT ACCOUNT NUMBER" in text
        or re.search(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b", text)
    ):
        return "PAN"
    if (
        "PASSPORT" in text
        or "REPUBLIC OF INDIA" in text
        or "PASSPORT NO" in text
        or "NATIONALITY" in text
    ):
        return "PASSPORT"
    resume_keywords = [
        "EDUCATION",
        "EXPERIENCE",
        "WORK EXPERIENCE",
        "PROFESSIONAL EXPERIENCE",
        "PROJECTS",
        "SKILLS",
        "TECHNICAL SKILLS",
        "CERTIFICATIONS",
        "SUMMARY",
        "PROFILE",
        "CAREER OBJECTIVE",
        "PROFESSIONAL SUMMARY",
        "INTERNSHIP"

    ]
    score = 0
    for keyword in resume_keywords:
        if keyword in text:
            score += 1
    if score >= 3:
        return "RESUME"
    return "UNKNOWN"
def classify_document(text: str):
    text = text.lower()
    # Resume
    if (
        "education" in text
        and "experience" in text
        and (
            "technical skills" in text
            or "skills" in text
        )
    ):
        return "RESUME"
    # Aadhaar
    elif (
        "aadhaar" in text
        or "government of india" in text
        or "uidai" in text
    ):
        return "AADHAAR"
    # PAN
    elif (
        "income tax department" in text
        or "permanent account number" in text
    ):
        return "PAN"
    # Passport
    elif (
        "passport" in text
        or "republic of india" in text
    ):
        return "PASSPORT"
    # Driving License
    elif (
        "driving licence" in text
        or "driving license" in text
    ):
        return "DRIVING_LICENSE"

    return "UNKNOWN"
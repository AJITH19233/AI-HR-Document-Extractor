def calculate_resume_score(document_info):
    score = 0
    if document_info["name"]:
        score += 10
    if document_info["email"]:
        score += 10
    if document_info["phone"]:
        score += 10
    if document_info["skills"]:
        score += 20
    if document_info["education"]:
        score += 15
    if document_info["experience"]:
        score += 15
    if document_info["projects"]:
        score += 10
    if document_info["certifications"]:
        score += 5
    if document_info["languages"]:
        score += 5
    return score
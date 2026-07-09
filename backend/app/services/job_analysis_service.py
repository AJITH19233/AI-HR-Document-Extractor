import json
from sqlalchemy.orm import Session
from app.models.document import Document
from app.models.job_analysis import JobAnalysis
from app.services.jd_matching_service import analyze_resume
from fastapi import HTTPException
def create_job_analysis(
    document_id: int,
    job_description: str,
    db: Session
):
    # Fetch document
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )
    if document is None:
        raise HTTPException(status_code=404,
        detail="Document not found."
    )
    # Build document_info
    document_info = {
    "name": document.name,
    "email": document.email,
    "phone": document.phone,

    "skills": [
        skill.skill
        for skill in document.skills
    ],

    "education": [
        {
            "degree": education.degree,
            "institution": education.institution,
            "year": education.year
        }
        for education in document.education_records
    ],

    "experience": [
        {
            "designation": experience.designation,
            "company": experience.company,
            "duration": experience.duration
        }
        for experience in document.experiences
    ],

    "projects": [
        {
            "project_name": project.project_name,
            "description": project.description
        }
        for project in document.projects
    ],

    "certifications": [
        {
            "certification_name": certification.certification_name,
            "issuer": certification.issuer,
            "year": certification.year
        }
        for certification in document.certifications
    ],

    "languages": [
        language.language
        for language in document.languages
    ]
}
    # Gemini Analysis
    analysis = analyze_resume(
        document_info,
        job_description
    )
    # Save to Database
    new_analysis = JobAnalysis(
        document_id=document.id,
        job_description=job_description,
        match_score=analysis["match_score"],
        matching_skills=json.dumps(
            analysis["matching_skills"]
        ),
        missing_skills=json.dumps(
            analysis["missing_skills"]
        ),
        strengths=json.dumps(
            analysis["strengths"]
        ),
        recommendations=json.dumps(
            analysis["recommendations"]
        )
    )
    db.add(new_analysis)
    db.commit()
    db.refresh(new_analysis)
    return analysis
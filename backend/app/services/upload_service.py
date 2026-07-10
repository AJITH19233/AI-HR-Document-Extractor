import os
import shutil
import uuid

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from app.core.config import (
    UPLOAD_DIR,
    MAX_FILE_SIZE,
    ALLOWED_EXTENSIONS,
)
from app.models.document import Document
from app.services.extractor_service import extract_information
from app.models.skill import Skill
from app.models.education import Education
from app.models.experience import Experience
from app.models.project import Project
from app.models.certification import Certification
from app.models.language import Language
from app.services.classifier_service import classify_document
from app.services.scoring_service import calculate_resume_score
from app.services.ai_summary_service import generate_ai_summary
from app.services.document_reader_service import extract_text


os.makedirs(UPLOAD_DIR, exist_ok=True)


def validate_file(file: UploadFile):
    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}"
        )


def validate_file_size(file: UploadFile):
    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)

    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 10 MB."
        )

    return file_size


def save_uploaded_file(file: UploadFile, db: Session):

    # Step 1: Validate file
    validate_file(file)
    file_size = validate_file_size(file)

    # Step 2: Get extension
    extension = os.path.splitext(file.filename)[1].lower()

    # Step 3: Generate UUID filename
    unique_filename = f"{uuid.uuid4()}{extension}"

    # Step 4: Create full file path
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Step 5: Save file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Step 6: Create database record
    document = Document(
        original_filename=file.filename,
        stored_filename=unique_filename,
        file_path=file_path,
        file_size=file_size,
        file_type=extension,
        status="UPLOADED",
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    # Step 7: OCR Processing
    try:
        extracted_text = extract_text(file_path)
        document_type = classify_document(extracted_text)
        document_info = extract_information(extracted_text)
        resume_score = calculate_resume_score(document_info)
        ai_summary = generate_ai_summary(document_info)

        print(f"Resume Score: {resume_score}")
        print(document_type)
        document.name = document_info["name"]
        document.email = document_info["email"]
        document.phone = document_info["phone"]
        print(document_info["languages"])
        document.extracted_text = extracted_text
        print(document_info)
        print(extracted_text)
        print(document_info["skills"])
        print(document_info["experience"])
        print(document_info["projects"])
        document.status = "EXTRACTED"
        document.document_type = document_type
        document.resume_score = resume_score
        document.ai_summary = ai_summary

        db.commit()
        db.refresh(document)

    except Exception as e:

        document.status = "OCR_FAILED"

        db.commit()
        db.refresh(document)
        raise HTTPException(
            status_code=500,
            detail=f"OCR failed: {str(e)}"
        )

    for skill_name in document_info["skills"]:

        if not skill_name:
            continue

        new_skill = Skill(
            document_id=document.id,
        skill=skill_name
        )

        db.add(new_skill)
    db.commit()
    for education in document_info["education"]:

        if not education.get("degree"):
            continue

        education_record = Education(
        document_id=document.id,
        degree=education["degree"],
        institution=education["institution"],
        year=education["year"]
    )

        db.add(education_record)

    db.commit()


    #save the experience extracted to the db
    for exp in document_info["experience"]:

        new_experience = Experience(
        document_id=document.id,
        designation=exp["designation"],
        company=exp["company"],
        duration=exp["duration"]
    )

        db.add(new_experience)

    db.commit()
    
    #projects extraction and saving to the db
    for project in document_info["projects"]:

        new_project = Project(
        document_id=document.id,
        project_name=project["project_name"],
        description=project["description"]
        )

        db.add(new_project)

    db.commit()

    #add certifications to the db
    for certification in document_info["certifications"]:

        new_certification = Certification(
        document_id=document.id,
        certification_name=certification["certification_name"],
        issuer=certification["issuer"],
        year=certification["year"]
    )

        db.add(new_certification)

    db.commit()

    #add languages to the db
    for language in document_info["languages"]:
        new_language = Language(
        document_id=document.id,
        language=language["language"]
    )

        db.add(new_language)

    db.commit()
    # Step 8: Return response
    return {
        "original_filename": document.original_filename,
        "stored_filename": document.stored_filename,
        "file_path": document.file_path,
        "file_size": document.file_size,
        "status": document.status,
        
    }
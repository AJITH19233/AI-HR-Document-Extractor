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

    # Validate
    validate_file(file)
    file_size = validate_file_size(file)

    # Extension
    extension = os.path.splitext(file.filename)[1].lower()

    # UUID filename
    unique_filename = f"{uuid.uuid4()}{extension}"

    # Full path
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Database object
    document = Document(
        original_filename=file.filename,
        stored_filename=unique_filename,
        file_path=file_path,
        file_size=file_size,
        file_type=extension,
        status="UPLOADED"
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "original_filename": document.original_filename,
        "stored_filename": document.stored_filename,
        "file_path": document.file_path,
        "file_size": document.file_size,
    }
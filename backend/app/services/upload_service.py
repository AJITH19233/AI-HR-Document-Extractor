import os
import shutil
import uuid

from fastapi import UploadFile, HTTPException

from app.core.config import (
    UPLOAD_DIR,
    MAX_FILE_SIZE,
    ALLOWED_EXTENSIONS,
)
os.makedirs(UPLOAD_DIR, exist_ok=True)


def validate_file(file: UploadFile):
    """
    Validate uploaded file extension.
    """
    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}"
        )

def validate_file_size(file: UploadFile):
    # Move pointer to the end of the file
    file.file.seek(0, 2)

    # Get file size
    file_size = file.file.tell()

    # Move pointer back to the beginning
    file.file.seek(0)

    # Check size
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 10 MB."
        )


def save_uploaded_file(file: UploadFile):
    """
    Validate and save uploaded file with a UUID filename.
    """

    # Step 1: Validate
    validate_file(file)

    #size = len(file.file.read())
    validate_file_size(file)
    
    # Step 2: Get file extension
    extension = os.path.splitext(file.filename)[1].lower()

    # Step 3: Generate unique filename
    unique_filename = f"{uuid.uuid4()}{extension}"

    # Step 4: Create full path
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Step 5: Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Step 6: Return metadata
    return {
        "original_filename": file.filename,
        "stored_filename": unique_filename,
        "file_path": file_path
    }
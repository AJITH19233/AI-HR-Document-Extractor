from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import save_uploaded_file

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
def upload_document(file: UploadFile = File(...)):
    file_path = save_uploaded_file(file)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "path": file_path
    }
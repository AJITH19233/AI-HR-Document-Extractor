from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.document_schema import UploadResponse
from app.services.upload_service import save_uploaded_file

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/", response_model=UploadResponse)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    document = save_uploaded_file(file, db)

    return UploadResponse(
        message="File uploaded successfully",
        document=document
    )
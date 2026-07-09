from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.job_analysis import (
    JobAnalysisRequest,
    JobAnalysisResponse
)
from app.services.job_analysis_service import create_job_analysis

router = APIRouter(
    prefix="/job-analysis",
    tags=["Job Analysis"]
)
@router.post(
    "/",
    response_model=JobAnalysisResponse
)
def analyze_job(
    request: JobAnalysisRequest,
    db: Session = Depends(get_db)
):
    return create_job_analysis(
        request.document_id,
        request.job_description,
        db
    )
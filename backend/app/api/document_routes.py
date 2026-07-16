from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.document_schema import (
    DocumentListResponse,
    DocumentDetailResponse,
    DashboardStatsResponse
)

from app.services.document_service import (
    get_all_documents,
    get_document_by_id,
    delete_document,
    search_documents,
    filter_documents,
    get_dashboard_stats,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

@router.get(
    "/",
    response_model=list[DocumentListResponse]
)
def get_documents(
    page: int = 1,
    size: int = 10,
    sort: str = "uploaded_at",
    db: Session = Depends(get_db)
):

    return get_all_documents(
        db=db,
        page=page,
        size=size,
        sort=sort
    )

@router.get(
    "/search",
    response_model=list[DocumentListResponse]
)
def search_resume(
    query: str = Query(...),
    db: Session = Depends(get_db)
):

    return search_documents(
        query=query,
        db=db
    )
@router.get(
    "/filter",
    response_model=list[DocumentListResponse]
)
def filter_resume(
    skill: Optional[str] = None,
    document_type: Optional[str] = None,
    min_score: Optional[int] = None,
    max_score: Optional[int] = None,
    db: Session = Depends(get_db)
):

    return filter_documents(
        db=db,
        skill=skill,
        document_type=document_type,
        min_score=min_score,
        max_score=max_score
    )
@router.get(
    "/stats",
    response_model=DashboardStatsResponse
)
def dashboard_statistics(
    db: Session = Depends(get_db)
):

    return get_dashboard_stats(db)
@router.get(
    "/{document_id}",
    response_model=DocumentDetailResponse
)
def get_document(
    document_id: int,
    db: Session = Depends(get_db)
):

    return get_document_by_id(
        document_id=document_id,
        db=db
    )

@router.delete("/{document_id}")
def delete_resume(
    document_id: int,
    db: Session = Depends(get_db)
):

    return delete_document(
        document_id=document_id,
        db=db
    )
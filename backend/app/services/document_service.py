from fastapi import HTTPException
from sqlalchemy import func, or_
from sqlalchemy.orm import Session
from app.models.document import Document
from app.models.skill import Skill
def get_all_documents(
    db: Session,
    page: int = 1,
    size: int = 10,
    sort: str = "uploaded_at"
):
    offset = (page - 1) * size
    query = db.query(Document)
    if sort == "resume_score":
        query = query.order_by(Document.resume_score.desc())

    elif sort == "name":
        query = query.order_by(Document.name.asc())

    elif sort == "uploaded_at":
        query = query.order_by(Document.uploaded_at.desc())

    else:
        query = query.order_by(Document.uploaded_at.desc())

    documents = (
        query
        .offset(offset)
        .limit(size)
        .all()
    )
    return documents
def get_document_by_id(
    document_id: int,
    db: Session
):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )
    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )
    return document
def delete_document(
    document_id: int,
    db: Session
):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )
    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )
    db.delete(document)
    db.commit()
    return {
        "message": "Document deleted successfully.",
        "document_id": document_id
    }
def search_documents(
    query: str,
    db: Session
):

    documents = (
        db.query(Document)
        .filter(
            or_(
                Document.name.ilike(f"%{query}%"),
                Document.email.ilike(f"%{query}%"),
                Document.phone.ilike(f"%{query}%"),
                Document.original_filename.ilike(f"%{query}%")
            )
        )
        .order_by(Document.uploaded_at.desc())
        .all()
    )

    return documents
def filter_documents(
    db: Session,
    skill: str | None = None,
    document_type: str | None = None,
    min_score: int | None = None,
    max_score: int | None = None,
):

    query = db.query(Document)

    if skill:

        query = (
            query.join(Skill)
            .filter(
                Skill.skill.ilike(f"%{skill}%")
            )
        )

    if document_type:

        query = query.filter(
            Document.document_type == document_type
        )

    if min_score is not None:

        query = query.filter(
            Document.resume_score >= min_score
        )

    if max_score is not None:

        query = query.filter(
            Document.resume_score <= max_score
        )

    documents = (
        query
        .order_by(Document.uploaded_at.desc())
        .all()
    )

    return documents
def get_dashboard_stats(
    db: Session
):

    total_resumes = db.query(Document).count()

    average_resume_score = (
        db.query(
            func.avg(Document.resume_score)
        )
        .scalar()
    )

    highest_resume_score = (
        db.query(
            func.max(Document.resume_score)
        )
        .scalar()
    )

    lowest_resume_score = (
        db.query(
            func.min(Document.resume_score)
        )
        .scalar()
    )
    return {
        "total_resumes": total_resumes,
        "average_resume_score": round(
            average_resume_score or 0,
            2
        ),
        "highest_resume_score": highest_resume_score or 0,
        "lowest_resume_score": lowest_resume_score or 0
    }
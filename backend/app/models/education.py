from app.database.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Education(Base):
    __tablename__="education"

    id=Column(Integer, primary_key=True, index=True)
    document_id=Column(Integer, ForeignKey("documents.id"), nullable=False)
    document = relationship( "Document",back_populates="education_records")
    degree=Column(String, nullable=False)
    institution=Column(String, nullable=False)
    year=Column(String, nullable=False)


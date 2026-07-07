from app.database.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
class Certification(Base):
    __tablename__ = "certifications"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer,ForeignKey("documents.id"),nullable=False)
    document = relationship("Document",back_populates="certifications")
    certification_name = Column(String, nullable=False)
    issuer = Column(String, nullable=False)
    year = Column(String, nullable=False)
    
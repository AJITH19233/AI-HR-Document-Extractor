from app.database.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
class Experience(Base):
    __tablename__ = "experience"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer,ForeignKey("documents.id"),nullable=False)
    document = relationship("Document",back_populates="experiences")
    designation = Column(String, nullable=False)
    company = Column(String, nullable=False)
    duration = Column(String, nullable=False)
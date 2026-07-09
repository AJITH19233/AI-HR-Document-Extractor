from app.database.base import Base
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
class JobAnalysis(Base):
    __tablename__ = "job_analysis"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer,ForeignKey("documents.id"),nullable=False)
    document = relationship("Document",back_populates="job_analyses")
    job_description = Column(Text, nullable=False)
    match_score = Column(Integer, nullable=False)
    matching_skills = Column(Text)
    missing_skills = Column(Text)
    strengths = Column(Text)
    recommendations = Column(Text)
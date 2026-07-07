from app.database.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
class Project(Base):
    __tablename__="projects"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    document = relationship("Document", back_populates="projects")
    project_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
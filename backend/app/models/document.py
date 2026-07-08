from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy import Text
from app.database.base import Base
from sqlalchemy.orm import relationship

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String, nullable=False)
    stored_filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)
    file_type = Column(String, nullable=False)
    document_type = Column(String, default="UNKNOWN")
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    skills = relationship("Skill",back_populates="document",cascade="all, delete-orphan")
    education_records = relationship("Education",back_populates="document",cascade="all, delete-orphan")
    experiences = relationship("Experience",back_populates="document",cascade="all, delete-orphan")
    projects = relationship("Project",back_populates="document",cascade="all, delete-orphan")
    certifications = relationship("Certification",back_populates="document",cascade="all, delete-orphan")
    languages = relationship("Language",back_populates="document",cascade="all, delete-orphan")
    extracted_text = Column(Text, nullable=True)
    status = Column(
        String,
        nullable=False,
        default="UPLOADED"
    )
    uploaded_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
    
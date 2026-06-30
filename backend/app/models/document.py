from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy import Text
from app.database.base import Base


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String, nullable=False)
    stored_filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)
    file_type = Column(String, nullable=False)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
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
    
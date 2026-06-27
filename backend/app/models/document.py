from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class Document(Base):
    __tablename__ = "documents"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Original filename uploaded by the user
    original_filename = Column(String, nullable=False)

    # UUID filename stored on the server
    stored_filename = Column(String, nullable=False)

    # Path where the file is stored
    file_path = Column(String, nullable=False)

    # File size in bytes
    file_size = Column(Integer, nullable=False)

    # File extension (pdf, png, jpg, jpeg)
    file_type = Column(String, nullable=False)

    # Processing status
    status = Column(
        String,
        nullable=False,
        default="UPLOADED"
    )

    # Upload timestamp
    uploaded_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
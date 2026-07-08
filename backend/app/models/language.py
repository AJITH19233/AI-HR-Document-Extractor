from app.database.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer,ForeignKey("documents.id"),nullable=False)
    language=Column(String, nullable=False)
    document = relationship("Document",back_populates="languages")

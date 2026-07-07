from app.database.base import Base
from app.database.session import engine

# Import ALL models
from app.models.document import Document
from app.models.education import Education
from app.models.skill import Skill
from app.models.experience import Experience
from app.models.project import Project


def init_db():
    Base.metadata.create_all(bind=engine)
from app.database.base import Base
from app.database.session import engine

# Import all models
from app.models.document import Document


def init_db():
    Base.metadata.create_all(bind=engine)
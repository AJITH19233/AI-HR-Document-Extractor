from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to HR Document Extraction API",
        "status": "Running"
    }
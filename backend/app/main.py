from fastapi import FastAPI
from app.api.routes import router
from app.api.upload_routes import router as upload_router

app = FastAPI(
    title="HR Document Extraction API",
    description="AI Powered HR Document Extraction System",
    version="1.0.0"
)

app.include_router(router)
app.include_router(upload_router)
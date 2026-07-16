from fastapi import FastAPI
from app.api.routes import router
from app.api.upload_routes import router as upload_router
from app.api.job_analysis_routes import router as job_analysis_router
from app.database.init_db import init_db
from app.api.document_routes import router as document_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="HR Document Extraction API",
    description="AI Powered HR Document Extraction System",
    version="1.0.0"
)
init_db()
app.include_router(router)
app.include_router(upload_router)
app.include_router(job_analysis_router)
app.include_router(document_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
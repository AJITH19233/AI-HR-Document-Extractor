from pydantic import BaseModel
class DocumentResponse(BaseModel):
    original_filename: str
    stored_filename: str
    file_path: str
    file_size: int
class UploadResponse(BaseModel):
    message: str
    document: DocumentResponse
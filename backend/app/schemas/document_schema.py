from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    original_filename: str
    stored_filename: str
    file_path: str
    file_size: int
    status: str
class UploadResponse(BaseModel):
    message: str
    document: DocumentResponse
class DocumentListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    original_filename: str
    document_type: str
    resume_score: int
    status: str
    uploaded_at: datetime
class SkillResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    skill: str
class EducationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    degree: str
    institution: Optional[str] = None
    year: Optional[str] = None
class ExperienceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    designation: Optional[str] = None
    company: Optional[str] = None
    duration: Optional[str] = None
class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    project_name: str
    description: Optional[str] = None
class CertificationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    certification_name: str
    issuer: Optional[str] = None
    year: Optional[str] = None
class LanguageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    language: str
class DocumentDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    original_filename: str
    document_type: str
    resume_score: int
    ai_summary: Optional[str] = None
    status: str
    uploaded_at: datetime
    skills: list[SkillResponse]
    education_records: list[EducationResponse]
    experiences: list[ExperienceResponse]
    projects: list[ProjectResponse]
    certifications: list[CertificationResponse]
    languages: list[LanguageResponse]
class DashboardStatsResponse(BaseModel):
    total_resumes: int
    average_resume_score: float
    highest_resume_score: int
    lowest_resume_score: int
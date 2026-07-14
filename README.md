# AI HR Document Extractor

An AI-powered HR Resume Analysis Platform built with FastAPI, PostgreSQL, OCR, and Google Gemini to automate resume parsing, candidate analysis, and recruiter workflows.

---

## Features

### Resume Processing

- Upload Resume (PNG, JPG, JPEG, PDF, DOCX)
- OCR-based Text Extraction
- Resume Information Extraction
- PostgreSQL Storage

### AI Features

- AI Resume Summary
- Resume Score Generation
- Automatic Document Classification
- Job Description Matching
- Match Score Calculation
- Missing Skills Detection
- Candidate Strength Analysis
- AI Recommendations

### Recruiter APIs

- Get All Resumes
- Get Resume Details
- Delete Resume
- Search Candidates
- Filter Candidates
- Dashboard Statistics
- Pagination
- Sorting

### Batch Processing

- Upload Multiple Resumes
- Individual Processing Status
- Error Handling
- Batch Response

---

# Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

## AI

- Google Gemini 2.5 Flash

## OCR

- Tesseract OCR
- PyMuPDF
- python-docx

## Tools

- Git
- GitHub
- Postman

---

# Project Structure

```
backend
│
├── app
│   ├── api
│   ├── core
│   ├── database
│   ├── models
│   ├── routes
│   ├── schemas
│   ├── services
│   └── utils
│
├── uploads
│
└── requirements.txt
```

---

# Current Workflow

```
Resume Upload
        │
        ▼
Universal Document Reader
(Image / PDF / DOCX)
        │
        ▼
OCR Extraction
        │
        ▼
Information Extraction
        │
        ▼
Database Storage
        │
        ▼
Document Classification
        │
        ▼
Resume Score
        │
        ▼
AI Summary
        │
        ▼
Job Matching
        │
        ▼
Recruiter Management APIs
```

---

# API Endpoints

## Upload

```
POST /upload
POST /upload/batch
```

## Documents

```
GET    /documents
GET    /documents/{id}
DELETE /documents/{id}
GET    /documents/search
GET    /documents/filter
GET    /documents/stats
```

## Job Analysis

```
POST /job-analysis
```

---

# Implemented Features

- Universal Resume Reader
- OCR Processing
- Resume Parsing
- AI Resume Summary
- Resume Score
- Job Matching
- Batch Upload
- Search API
- Filter API
- Dashboard Statistics
- Pagination
- Sorting

---

# Upcoming Features

- React Recruiter Dashboard
- Authentication
- Role-Based Access Control
- Docker
- Jenkins
- GitHub Actions
- AWS Deployment
- Terraform
- Prometheus
- Grafana

---

# Future Enhancements

- Gemini-based Resume Parsing
- Background Job Processing
- Resume Comparison
- Candidate Ranking
- Interview Recommendation Engine
- Email Notifications

---

# Author

**Ajith Chandran G**

MCA Graduate

Backend Developer | Python | FastAPI | PostgreSQL | AI | DevOps

GitHub:
https://github.com/AJITH19233/AI-HR-Document-Extractor
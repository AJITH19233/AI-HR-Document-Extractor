# 🤖 AI HR Document Extractor

An AI-powered HR Document Processing System built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Tesseract OCR**, and **Google Gemini AI**.

The application extracts structured information from resumes, classifies uploaded documents, calculates resume scores, generates AI-powered candidate summaries, and analyzes resumes against Job Descriptions using Generative AI.

---

## 🚀 Features

### 📄 Resume Processing

- Upload Resume Images
- OCR-based Text Extraction using Tesseract
- Automatic Document Classification
- Resume Information Extraction
- Resume Score Generation
- AI-powered Resume Summary
- Store Extracted Information in PostgreSQL

---

### 📊 Resume Information Extraction

The system extracts:

- Name
- Email
- Phone Number
- Skills
- Education
- Experience
- Projects
- Certifications
- Languages

---

### 🤖 AI Features

#### ✅ Document Classification

Automatically classifies uploaded documents into:

- Resume
- Aadhaar
- PAN
- Passport
- Unknown Document

---

#### ✅ Resume Score

Calculates a resume score based on:

- Personal Information
- Skills
- Education
- Experience
- Projects
- Certifications
- Languages

---

#### ✅ AI Resume Summary

Uses **Google Gemini 2.5 Flash** to generate a recruiter-friendly professional summary.

Example:

> Ajith Chandran G is a Python Backend Developer with knowledge of FastAPI, PostgreSQL, SQLAlchemy, Docker, and AWS. He completed his MCA and has internship experience in backend development and OCR-based document processing.

---

#### ✅ AI Job Description Matching

Compare a candidate's resume against any Job Description.

Returns:

- Match Score
- Matching Skills
- Missing Skills
- Candidate Strengths
- Improvement Recommendations

Example:

```
Overall Match : 86%

Matching Skills
✔ Python
✔ FastAPI
✔ PostgreSQL
✔ Docker
✔ Git
✔ AWS

Missing Skills
✘ Terraform
```

---

## 🏗 Tech Stack

### Backend

- FastAPI
- Python

### Database

- PostgreSQL
- SQLAlchemy ORM

### AI

- Google Gemini 2.5 Flash
- Prompt Engineering

### OCR

- Tesseract OCR

### Image Processing

- Pillow

### Validation

- Pydantic

---

# 📂 Project Structure

```
backend/
│
├── app/
│   ├── api/
│   │   ├── upload_routes.py
│   │   └── job_analysis_routes.py
│   │
│   ├── database/
│   │
│   ├── models/
│   │   ├── document.py
│   │   ├── skill.py
│   │   ├── education.py
│   │   ├── experience.py
│   │   ├── project.py
│   │   ├── certification.py
│   │   ├── language.py
│   │   └── job_analysis.py
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │   ├── upload_service.py
│   │   ├── extractor_service.py
│   │   ├── classifier_service.py
│   │   ├── scoring_service.py
│   │   ├── ai_summary_service.py
│   │   ├── jd_matching_service.py
│   │   └── job_analysis_service.py
│   │
│   └── main.py
│
└── requirements.txt
```

---

# 🔄 System Workflow

```
Resume Upload
        │
        ▼
File Validation
        │
        ▼
OCR (Tesseract)
        │
        ▼
Document Classification
        │
        ▼
Resume Information Extraction
        │
        ▼
Resume Score Generation
        │
        ▼
AI Resume Summary (Gemini)
        │
        ▼
Store in PostgreSQL
```

---

## 📈 Job Analysis Workflow

```
Stored Resume
        │
        ▼
Job Description
        │
        ▼
Google Gemini AI
        │
        ▼
──────────────────────────
Match Score
Matching Skills
Missing Skills
Strengths
Recommendations
──────────────────────────
        │
        ▼
Store Analysis in PostgreSQL
```

---

# 🗄 Database Design

### Tables

- documents
- skills
- education
- experience
- projects
- certifications
- languages
- job_analysis

---

# 📸 API Endpoints

### Resume Upload

```
POST /upload
```

Uploads a resume and performs:

- OCR
- Resume Parsing
- Resume Scoring
- AI Resume Summary

---

### Job Analysis

```
POST /job-analysis
```

Compares a stored resume against a Job Description using Google Gemini AI.

---

# 🎯 Current Project Status

## ✅ Phase 1

- OCR Integration
- Resume Parsing
- PostgreSQL Integration

---

## ✅ Phase 2

- Document Classification
- Resume Score
- AI Resume Summary
- Job Description Matching
- Missing Skills Analysis
- AI Recommendations

---

## 🚀 Upcoming Features (Phase 3)

- PDF Resume Upload
- DOCX Resume Upload
- Scanned PDF OCR
- Batch Resume Processing
- Recruiter Dashboard
- Resume Ranking
- Candidate Search

---

## ☁ Phase 4

- Docker
- Docker Compose
- Jenkins
- GitHub Actions
- Terraform
- AWS Deployment
- Prometheus
- Grafana

---

# 📷 Screenshots

Add screenshots here:

- Swagger API
- Resume Upload
- Resume Score
- AI Summary
- Job Analysis
- PostgreSQL Tables

---

# 👨‍💻 Author

**Ajith Chandran G**

MCA Graduate

Python Backend Developer

Open to opportunities in Backend Development, AI, and DevOps.

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
# AI HR Document Extractor

An AI-powered Resume Parsing application built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Tesseract OCR**. The application extracts structured information from resumes and stores it in a normalized PostgreSQL database using a production-style backend architecture.

---

# Features

## Resume Upload
- Upload resume images (.png, .jpg, .jpeg)
- UUID-based file storage
- File size validation
- File type validation

## OCR Processing
- Text extraction using Tesseract OCR
- Image-based resume processing
- Stores extracted text in PostgreSQL

## Resume Information Extraction

### Personal Information
- Name
- Email Address
- Phone Number

### Skills Extraction
- Detects Technical Skills section
- Extracts multiple skills
- Stores skills in a separate table

### Education Extraction
- Degree
- Institution
- Academic Year
- Stores multiple education records

### Experience Extraction
- Designation
- Company
- Duration
- Stores multiple experience records

---

# Tech Stack

## Backend
- Python
- FastAPI

## Database
- PostgreSQL
- SQLAlchemy ORM

## OCR
- Tesseract OCR

## Tools
- Git
- GitHub
- VS Code

---

# Project Structure

```
HR-DOCUMENT-EXTRACTOR
│
├── backend
│   ├── app
│   │   ├── models
│   │   │   ├── document.py
│   │   │   ├── skill.py
│   │   │   ├── education.py
│   │   │   └── experience.py
│   │   │
│   │   ├── services
│   │   │   ├── upload_service.py
│   │   │   ├── extractor_service.py
│   │   │   ├── ocr_service.py
│   │   │   └── classifier_service.py
│   │   │
│   │   ├── schemas
│   │   ├── database
│   │   ├── utils
│   │   └── main.py
│   │
│   ├── uploads
│   └── requirements.txt
│
├── docker-compose.yml
├── Jenkinsfile
└── terraform
```

---

# Application Workflow

```
Resume Image
      │
      ▼
FastAPI Upload API
      │
      ▼
OCR (Tesseract)
      │
      ▼
Text Extraction
      │
      ▼
Resume Information Extraction
      │
 ┌────┼────────┬────────────┬─────────────┬─────────────┐
 ▼    ▼        ▼            ▼             ▼             ▼
Name Email Phone Skills Education Experience
      │
      ▼
PostgreSQL Database
```

---

# Database Schema

## Documents

| Column |
|----------|
| id |
| original_filename |
| stored_filename |
| file_path |
| file_size |
| file_type |
| name |
| email |
| phone |
| extracted_text |
| status |
| uploaded_at |

---

## Skills

| Column |
|----------|
| id |
| document_id |
| skill |

---

## Education

| Column |
|----------|
| id |
| document_id |
| degree |
| institution |
| year |

---

## Experience

| Column |
|----------|
| id |
| document_id |
| designation |
| company |
| duration |

---

# Database Relationships

```
documents
    │
    ├──────── skills
    │
    ├──────── education
    │
    └──────── experience
```

All tables are connected using **One-to-Many Relationships** with SQLAlchemy ORM.

---

# API Endpoint

## Upload Resume

```
POST /upload/
```

Uploads a resume image, performs OCR, extracts structured information, and stores the data in PostgreSQL.

---

# Current Capabilities

✔ Resume Upload

✔ OCR Text Extraction

✔ Name Extraction

✔ Email Extraction

✔ Phone Number Extraction

✔ Skills Extraction

✔ Education Extraction

✔ Experience Extraction

✔ PostgreSQL Integration

✔ SQLAlchemy ORM Relationships

---

# Upcoming Features

- Project Extraction
- Certification Extraction
- Languages Extraction
- Resume Classification
- AI-powered Resume Parsing (LLM)
- PDF Resume OCR
- Confidence Score Generation
- Docker Deployment
- CI/CD Pipeline with Jenkins
- AWS Deployment
- Terraform Infrastructure
- Prometheus & Grafana Monitoring

---

# Future Architecture

```
Resume
    │
    ▼
OCR
    │
    ▼
Resume Parser
│
├── Name
├── Email
├── Phone
├── Skills
├── Education
├── Experience
├── Projects
├── Certifications
├── Languages
└── AI Resume Analysis
    │
    ▼
PostgreSQL
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/AJITH19233/AI-HR-Document-Extractor.git
```

## Navigate to Project

```bash
cd AI-HR-Document-Extractor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start FastAPI

```bash
uvicorn app.main:app --reload
```

---

# Author

**Ajith Chandran G**

GitHub: https://github.com/AJITH19233

LinkedIn: https://www.linkedin.com/in/ajithchandrang

---

# Project Status

## Version

**Day 8**

### Completed

- Resume Upload
- OCR Integration
- Name Extraction
- Email Extraction
- Phone Extraction
- Skills Extraction
- Education Extraction
- Experience Extraction
- PostgreSQL Integration
- SQLAlchemy ORM
- One-to-Many Relationships

### Next Milestone

- Project Extraction

---

⭐ This project is being built step by step to understand how production-ready AI-powered HR Document Processing and Resume Parsing systems are designed using Python, FastAPI, SQLAlchemy, PostgreSQL, and OCR technologies.
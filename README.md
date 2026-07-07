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

---

# Resume Information Extraction

### Personal Information
- Name
- Email Address
- Phone Number

### Skills Extraction
- Detects Technical Skills section
- Extracts multiple technical skills
- Stores skills in a dedicated table

### Education Extraction
- Degree
- Institution
- Academic Year
- Supports multiple education records

### Experience Extraction
- Designation
- Company
- Duration
- Supports multiple experience records

### Project Extraction
- Project Name
- Project Description
- Supports multiple projects

### Certification Extraction
- Certification Name
- Issuer
- Year
- Supports multiple certifications

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
│   │   ├── api
│   │   ├── core
│   │   ├── database
│   │   ├── models
│   │   │   ├── document.py
│   │   │   ├── skill.py
│   │   │   ├── education.py
│   │   │   ├── experience.py
│   │   │   ├── project.py
│   │   │   └── certification.py
│   │   │
│   │   ├── schemas
│   │   ├── services
│   │   │   ├── upload_service.py
│   │   │   ├── extractor_service.py
│   │   │   ├── ocr_service.py
│   │   │   └── classifier_service.py
│   │   │
│   │   ├── utils
│   │   └── main.py
│   │
│   └── uploads
│
├── docker-compose.yml
├── Jenkinsfile
├── terraform
└── README.md
```

---

# Application Workflow

```
Resume Upload
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
 ├──────── Name
 ├──────── Email
 ├──────── Phone
 ├──────── Skills
 ├──────── Education
 ├──────── Experience
 ├──────── Projects
 └──────── Certifications
      │
      ▼
PostgreSQL Database
```

---

# Database Schema

## Documents

- id
- original_filename
- stored_filename
- file_path
- file_size
- file_type
- name
- email
- phone
- extracted_text
- status
- uploaded_at

---

## Skills

- id
- document_id
- skill

---

## Education

- id
- document_id
- degree
- institution
- year

---

## Experience

- id
- document_id
- designation
- company
- duration

---

## Projects

- id
- document_id
- project_name
- description

---

## Certifications

- id
- document_id
- certification_name
- issuer
- year

---

# Database Relationships

```
documents
│
├──────── skills
├──────── education
├──────── experience
├──────── projects
└──────── certifications
```

All entities are connected using **One-to-Many Relationships** through SQLAlchemy ORM.

---

# API Endpoint

## Upload Resume

```
POST /upload/
```

Uploads a resume, performs OCR, extracts structured information, and stores the results in PostgreSQL.

---

# Current Features

✅ Resume Upload

✅ OCR Integration

✅ Name Extraction

✅ Email Extraction

✅ Phone Extraction

✅ Skills Extraction

✅ Education Extraction

✅ Experience Extraction

✅ Project Extraction

✅ Certification Extraction

✅ PostgreSQL Integration

✅ SQLAlchemy ORM Relationships

---

# Upcoming Features

- Languages Extraction
- Resume Classification
- AI-powered Resume Parsing (LLM)
- PDF Resume Processing
- Confidence Score Generation
- Docker Deployment
- CI/CD Pipeline (Jenkins)
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

## Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

# Author

**Ajith Chandran G**

GitHub: https://github.com/AJITH19233/AI-HR-Document-Extractor

LinkedIn: https://www.linkedin.com/in/ajithchandrang

---

# Project Status

## Version

**Day 10**

### Completed

- Resume Upload
- OCR Integration
- Name Extraction
- Email Extraction
- Phone Extraction
- Skills Extraction
- Education Extraction
- Experience Extraction
- Project Extraction
- Certification Extraction
- PostgreSQL Integration
- SQLAlchemy ORM
- One-to-Many Relationships

### Next Milestone

- Languages Extraction

---

⭐ This project is being built step by step to understand how production-ready AI-powered HR Document Processing and Resume Parsing systems are designed using Python, FastAPI, SQLAlchemy, PostgreSQL, and OCR technologies.
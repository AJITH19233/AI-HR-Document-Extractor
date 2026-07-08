# AI HR Document Extractor

An AI-powered HR Document Processing System built using **FastAPI**, **Python**, **PostgreSQL**, **SQLAlchemy**, and **Tesseract OCR**.

The application automatically processes uploaded documents, classifies document types, extracts structured information from resumes, and stores the extracted data in a normalized PostgreSQL database following production-ready backend architecture.

---

# Features

## Document Upload
- Upload document images (.png, .jpg, .jpeg)
- UUID-based file storage
- File size validation
- File type validation

## OCR Processing
- Text extraction using Tesseract OCR
- Image-based document processing
- Extracted text stored in PostgreSQL

## Document Classification (Phase 2)
- Resume
- Aadhaar Card
- PAN Card
- Passport
- Driving License
- Unknown Document

## Resume Information Extraction

### Personal Information
- Name
- Email Address
- Phone Number

### Skills
- Technical Skills Extraction

### Education
- Degree
- Institution
- Academic Year

### Experience
- Designation
- Company
- Duration

### Projects
- Project Name
- Project Description

### Certifications
- Certification Name
- Issuer
- Year

### Languages
- Multiple Language Extraction

---

# Technology Stack

## Backend
- Python
- FastAPI

## Database
- PostgreSQL
- SQLAlchemy ORM

## OCR
- Tesseract OCR

## Version Control
- Git
- GitHub

## Development Tools
- VS Code

---

# Project Workflow

```text
Document Upload
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
        ├──────── Resume
        │             │
        │             ▼
        │     Resume Information Extraction
        │             │
        │             ▼
        │      PostgreSQL Database
        │
        ├──────── Aadhaar
        ├──────── PAN
        ├──────── Passport
        ├──────── Driving License
        └──────── Unknown
```

---

# Database Design

```
documents
│
├── skills
├── education
├── experience
├── projects
├── certifications
└── languages
```

All tables are connected using **One-to-Many Relationships** through SQLAlchemy ORM.

---

# Resume Information Extracted

✅ Name

✅ Email

✅ Phone Number

✅ Technical Skills

✅ Education

✅ Experience

✅ Projects

✅ Certifications

✅ Languages

---

# API

## Upload Document

```
POST /upload/
```

Performs:

- File Upload
- OCR
- Document Classification
- Resume Parsing
- Database Storage

---

# Current Features

✅ Document Upload

✅ OCR Processing

✅ Document Classification

✅ Name Extraction

✅ Email Extraction

✅ Phone Extraction

✅ Skills Extraction

✅ Education Extraction

✅ Experience Extraction

✅ Project Extraction

✅ Certification Extraction

✅ Language Extraction

✅ PostgreSQL Integration

✅ SQLAlchemy ORM Relationships

---

# Upcoming Features

- Resume Score Generation
- AI Resume Summary
- Job Description Matching
- Skill Gap Analysis
- Resume Recommendation Engine
- PDF Resume Processing
- Confidence Score Generation
- Docker
- Jenkins CI/CD
- GitHub Actions
- Terraform
- AWS Deployment
- Prometheus
- Grafana

---

# Project Architecture

```text
                    Upload
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
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
   Resume         Aadhaar          Passport
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
 └── Languages
      │
      ▼
 PostgreSQL Database
```

---

# Roadmap

## ✅ Phase 1 - Resume Parser (Completed)

- OCR Integration
- Resume Upload
- Name Extraction
- Email Extraction
- Phone Extraction
- Skills Extraction
- Education Extraction
- Experience Extraction
- Projects Extraction
- Certifications Extraction
- Languages Extraction
- PostgreSQL Integration

---

## 🚀 Phase 2 - AI Document Processing (In Progress)

- ✅ Document Classification
- Resume Score
- AI Resume Summary
- Job Description Matching
- Skill Gap Analysis
- Resume Recommendation

---

## ☁️ Phase 3 - Production Deployment

- Docker
- Docker Compose
- Jenkins
- GitHub Actions
- Terraform
- AWS
- Prometheus
- Grafana

---

# Author

**Ajith Chandran G**

Backend Developer | Python | FastAPI | PostgreSQL | OCR | AI Document Processing

GitHub:
https://github.com/AJITH19233/AI-HR-Document-Extractor

LinkedIn:
https://www.linkedin.com/in/ajithchandran1923
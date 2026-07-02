# AI HR Document Extractor

An AI-powered Resume Parsing application built with FastAPI, PostgreSQL, SQLAlchemy, and Tesseract OCR.

The application extracts structured information from uploaded resumes and stores it in a normalized PostgreSQL database using production-style backend architecture.

---

## Features

### File Upload
- Upload resume images (.png, .jpg, .jpeg)
- UUID-based file storage
- File size validation
- File type validation

### OCR Processing
- Text extraction using Tesseract OCR
- Supports image-based resumes
- Stores extracted text in PostgreSQL

### Resume Information Extraction
- Candidate Name
- Email Address
- Phone Number

### Skills Extraction
- Detects the Technical Skills section
- Extracts multiple skills
- Stores skills in a separate table
- One-to-Many relationship with Document

### Education Extraction
- Detects the Education section
- Extracts:
  - Degree
  - Institution
  - Year
- Stores education records in a separate table
- One-to-Many relationship with Document

---

## Tech Stack

### Backend
- Python
- FastAPI

### Database
- PostgreSQL
- SQLAlchemy ORM

### OCR
- Tesseract OCR

### Tools
- Git
- GitHub
- VS Code

---

## Project Structure

```
backend/
│
├── app/
│   ├── models/
│   │   ├── document.py
│   │   ├── skill.py
│   │   └── education.py
│   │
│   ├── services/
│   │   ├── upload_service.py
│   │   ├── extractor_service.py
│   │   ├── ocr_service.py
│   │   └── classifier_service.py
│   │
│   ├── schemas/
│   ├── database/
│   ├── utils/
│   └── main.py
│
├── uploads/
├── .env
├── docker-compose.yml
└── requirements.txt
```

---

## Current Workflow

```
Resume Image
      │
      ▼
Upload API
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
 ┌────┼────────┬──────────┬─────────────┐
 ▼    ▼        ▼          ▼             ▼
Name Email Phone Skills Education
      │
      ▼
PostgreSQL Database
```

---

## Database Schema

### Documents

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

### Skills

| Column |
|----------|
| id |
| document_id |
| skill |

### Education

| Column |
|----------|
| id |
| document_id |
| degree |
| institution |
| year |

---

## Relationships

```
documents
    │
    ├──────── skills
    │
    └──────── education
```

Both Skills and Education have a **One-to-Many** relationship with Documents using SQLAlchemy ORM.

---

## API Endpoint

### Upload Resume

```
POST /upload/
```

Uploads a resume image, performs OCR, extracts resume information, and stores the results in PostgreSQL.

---

## Current Output

Currently the application extracts:

- Name
- Email
- Phone Number
- Skills
- Education

---

## Upcoming Features

- Experience Extraction
- Project Extraction
- Certifications Extraction
- PDF OCR Support
- Resume Classification
- AI/LLM-powered Resume Parsing
- Confidence Score Generation
- REST API Documentation Improvements
- Docker Deployment
- CI/CD Pipeline
- AWS Deployment
- Prometheus & Grafana Monitoring

---

## Future Architecture

```
Resume
   │
   ▼
Upload API
   │
   ▼
OCR
   │
   ▼
Information Extraction
   ├── Name
   ├── Email
   ├── Phone
   ├── Skills
   ├── Education
   ├── Experience
   ├── Projects
   └── Certifications
   │
   ▼
PostgreSQL
```

---

## Author

**Ajith Chandran G**

GitHub: https://github.com/AJITH19233

LinkedIn: https://www.linkedin.com/in/ajithchandrang

---

## Project Status

**Current Version:** Day 7

### Completed

- File Upload
- OCR Integration
- Name Extraction
- Email Extraction
- Phone Extraction
- Skills Extraction
- Education Extraction
- PostgreSQL Integration
- SQLAlchemy ORM
- One-to-Many Relationships

### In Progress

- Experience Extraction

---

⭐ This project is being built step by step to understand how production-ready AI-powered HR Document Processing systems are designed.
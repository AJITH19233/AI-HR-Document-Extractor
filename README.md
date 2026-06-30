# 🤖 AI HR Document Extractor

A production-style AI-powered HR Document Extractor built with **FastAPI**, **PostgreSQL**, and **Tesseract OCR**. The application processes uploaded resume images, extracts text using OCR, identifies important candidate information, and stores the extracted data in PostgreSQL.

---

## 🚀 Features

### 📄 Document Upload
- Upload resume images (PNG, JPG, JPEG)
- File type validation
- File size validation (Max: 10 MB)
- UUID-based file storage

### 🔍 OCR Processing
- Optical Character Recognition (OCR) using Tesseract
- Extract text from uploaded documents
- OCR error handling
- Document status tracking

### 📑 Resume Information Extraction
- Extract Candidate Name
- Extract Email Address
- Extract Phone Number
- Regex-based information extraction
- Automatic fallback for resumes without a "Name:" field

### 🗄 Database Integration
Stores:

- Original filename
- Stored filename
- File path
- File size
- File type
- Candidate Name
- Email Address
- Phone Number
- Extracted OCR text
- Processing status
- Upload timestamp

---

## 🛠 Tech Stack

### Backend
- FastAPI
- Python 3.13

### Database
- PostgreSQL
- SQLAlchemy ORM

### OCR
- Tesseract OCR
- Pillow (PIL)

### Others
- Pydantic
- Uvicorn

---

## 📁 Project Structure

```text
backend/
│
├── app/
│   ├── core/
│   │   └── config.py
│   │
│   ├── database/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   │
│   ├── models/
│   │   └── document.py
│   │
│   ├── schemas/
│   │   └── document_schema.py
│   │
│   ├── services/
│   │   ├── upload_service.py
│   │   ├── ocr_service.py
│   │   └── extractor_service.py
│   │
│   ├── api/
│   │   └── upload_routes.py
│   │
│   └── main.py
│
├── uploads/
├── requirements.txt
└── README.md
```

---

## ⚙️ Processing Workflow

```text
Upload Resume
        │
        ▼
Validate File
        │
        ▼
Save File
        │
        ▼
Create Database Record
(Status = UPLOADED)
        │
        ▼
OCR Processing
        │
        ▼
Extract Text
        │
        ▼
Extract Candidate Information
(Name, Email, Phone)
        │
        ▼
Update Database
(Status = EXTRACTED)
```

---

## 📌 Current Extraction

Currently the system extracts:

- ✅ Name
- ✅ Email Address
- ✅ Phone Number

---

## 🔄 Document Status

| Status | Description |
|---------|-------------|
| UPLOADED | File uploaded successfully |
| EXTRACTED | OCR and information extraction completed |
| OCR_FAILED | OCR processing failed |

---

## 🚀 Upcoming Features

- Resume Skills Extraction
- Education Extraction
- Experience Extraction
- Resume Classification
- AI-powered Information Extraction using LLMs
- Confidence Scores
- PDF OCR Support
- Docker Deployment
- AWS Deployment
- CI/CD Pipeline
- Prometheus & Grafana Monitoring

---

## 📸 Sample Workflow

```
Resume Image
      │
      ▼
OCR
      │
      ▼
Extracted Text
      │
      ▼
Resume Information
      │
      ├── Name
      ├── Email
      └── Phone
      │
      ▼
PostgreSQL
```

---

## 👨‍💻 Author

**Ajith Chandran G**

Backend Developer | Python | FastAPI | PostgreSQL | SQLAlchemy | OCR | AI
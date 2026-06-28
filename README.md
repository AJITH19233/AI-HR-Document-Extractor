# 🤖 AI HR Document Extractor

An AI-powered HR Document Extraction System built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. This project is designed to automate the extraction of structured information from HR documents such as resumes, Aadhaar cards, PAN cards, passports, and other documents using OCR and AI.

---

## 🚀 Features Completed

- ✅ Upload HR documents (PDF, PNG, JPG, JPEG)
- ✅ File type validation
- ✅ File size validation (Max 10 MB)
- ✅ Unique UUID filename generation
- ✅ Store uploaded files securely
- ✅ Store document metadata in PostgreSQL
- ✅ SQLAlchemy ORM integration
- ✅ FastAPI dependency injection
- ✅ Pydantic response validation
- ✅ Clean project architecture

---

## 🔄 Current Workflow

```
Upload File
      │
      ▼
Validate File
      │
      ▼
Generate UUID Filename
      │
      ▼
Save File
      │
      ▼
Store Metadata in PostgreSQL
```

---

## 🛠 Tech Stack

### Backend
- FastAPI
- Python 3.13

### Database
- PostgreSQL
- SQLAlchemy ORM

### Validation
- Pydantic

### Utilities
- UUID
- Python Multipart
- Dotenv

---

## 📂 Project Structure

```
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── uploads/
├── .env
├── requirements.txt
└── README.md
```

---

## 📌 Database Schema

| Column | Type |
|----------|------|
| id | Integer |
| original_filename | String |
| stored_filename | String |
| file_path | String |
| file_size | Integer |
| file_type | String |
| status | String |
| uploaded_at | DateTime |

---

## 🧪 API Endpoint

### Upload Document

```
POST /upload/
```

Response

```json
{
    "message": "File uploaded successfully",
    "document": {
        "original_filename": "resume.pdf",
        "stored_filename": "3ab21c8d.pdf",
        "file_path": "uploads/3ab21c8d.pdf",
        "file_size": 152364
    }
}
```

---

## 🎯 Upcoming Features

- OCR using Tesseract
- Resume Information Extraction
- Aadhaar/PAN Detection
- AI-powered Field Extraction
- Confidence Scoring
- Document Classification
- Docker
- AWS Deployment
- CI/CD Pipeline
- Monitoring with Prometheus & Grafana

---

## 📈 Current Status

✅ Upload Module Completed

🚧 OCR Module In Progress

---

## 👨‍💻 Author

**Ajith Chandran G**

MCA Graduate | Backend Developer | FastAPI | Python | PostgreSQL | DevOps Enthusiast
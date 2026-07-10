# 🤖 AI HR Document Extractor

An AI-powered HR Document Processing Platform built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Tesseract OCR**, and **Google Gemini AI**.

The platform automates resume processing by extracting structured information, generating AI-powered summaries, scoring resumes, and matching candidates against job descriptions.

---

## 🚀 Features

### 📄 Universal Resume Upload

Supports multiple resume formats:

- ✅ PNG
- ✅ JPG
- ✅ JPEG
- ✅ PDF
- ✅ DOCX

---

## 📑 Resume Processing Pipeline

- File Validation
- OCR Text Extraction (Images)
- PDF Text Extraction
- DOCX Text Extraction
- Resume Information Extraction
- Resume Classification
- Resume Score Generation
- AI Resume Summary
- Store Data in PostgreSQL

---

## 🤖 AI Features

### AI Resume Summary

Generates recruiter-friendly professional summaries using Google Gemini.

### Resume Scoring

Evaluates resumes based on:

- Personal Information
- Skills
- Education
- Experience
- Projects
- Certifications
- Languages

### Job Description Matching

Compares resumes against job descriptions and generates:

- Match Score
- Matching Skills
- Missing Skills
- Candidate Strengths
- Improvement Recommendations

---

## 📊 Extracted Resume Information

- Name
- Email
- Phone
- Skills
- Education
- Experience
- Projects
- Certifications
- Languages

---

## 🏗️ Architecture

```
Resume Upload
      │
      ▼
File Validation
      │
      ▼
Universal Document Reader
      │
 ┌────┼────┬─────┐
 ▼    ▼    ▼
OCR  PDF DOCX
      │
      ▼
Information Extraction
      │
      ▼
Document Classification
      │
      ▼
Resume Score
      │
      ▼
AI Resume Summary
      │
      ▼
PostgreSQL
      │
      ▼
Job Description Matching
```

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI

### Database
- PostgreSQL
- SQLAlchemy

### AI
- Google Gemini 2.5 Flash

### OCR
- Tesseract OCR

### Document Processing
- PyMuPDF
- python-docx
- Pillow

### Validation
- Pydantic

---

## 📌 Current Status

### ✅ Phase 1
- Resume Upload
- OCR
- Resume Parsing
- PostgreSQL Integration

### ✅ Phase 2
- AI Resume Summary
- Resume Score
- Document Classification
- Job Description Matching
- AI Recommendations

### ✅ Phase 3 (Current)
- Universal Document Reader
- PNG Support
- JPG/JPEG Support
- PDF Support
- DOCX Support

---

## 🚀 Upcoming Features

- Smart OCR for Scanned PDFs
- Recruiter Dashboard
- Resume Search & Filtering
- Batch Resume Upload
- Docker
- Jenkins
- GitHub Actions
- Terraform
- AWS Deployment
- Prometheus
- Grafana

---

## 👨‍💻 Author

**Ajith Chandran G**

Python Backend Developer | AI Enthusiast | Open to Opportunities

GitHub:
https://github.com/AJITH19233/AI-HR-Document-Extractor
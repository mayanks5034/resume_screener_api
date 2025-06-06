# resume_screener_api
# AI-Powered Resume Screening – Internship Assessment Project

🚀 **Submitted for:** AI/ML Internship at Unstop (Flive Consulting Pvt. Ltd.)  
👨‍💻 **Candidate:** Mayank Singh  
📅 **Date:** June 2025

---

## 🧠 Project Objective

This project aims to automate the resume screening process for a **Software Engineer** role using **AI/LLMs**. It reads job descriptions and resumes, compares them using prompt-engineered instructions, and returns:
- A **relevance score (0–10)**
- Candidate **strengths and weaknesses**
- A **recommendation summary** for hiring managers

---

## ⚙️ Tech Stack

| Area              | Tool/Tech Used                       |
|-------------------|--------------------------------------|
| Language          | Python 3                             |
| AI Engine         | OpenAI GPT-3.5 Turbo (via API)       |
| Backend Framework | FastAPI                              |
| Deployment        | Render (free cloud hosting)          |
| Prompt Interface  | Google AI Studio (Gemini 2.5 Pro)    |

---

## 🏗️ Project Structure
resume_screener_api/
├── main.py # FastAPI app entry point
├── resume_matcher.py # LLM interaction & prompt logic
├── requirements.txt # Python dependencies
├── render.yaml # Render deployment configuration
└── README.md # Project overview


---

## 🔧 How It Works

1. **Input:** Job description & resume (plain text)
2. **LLM Prompt:** Crafted to extract JD keywords, match with resume, and analyze gaps
3. **Output:**
   - Relevance Score (0–10)
   - Strength/Weakness table
   - Recommendation (fit or not)

---

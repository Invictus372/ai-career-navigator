# 🧭 AI Career Navigator

### NLP-Based Resume Intelligence, Job Recommendation & Career Path Optimization

AI Career Navigator is an NLP-based Data Science project that analyzes a candidate's resume, extracts technical skills, recommends suitable job roles, identifies skill gaps, and explores possible career transitions.

## 🚀 Project Overview

The system takes a resume in PDF or DOCX format and processes it through an NLP pipeline. It identifies technical skills, compares the resume with predefined job descriptions, calculates an approximate match score, recommends suitable roles, and analyzes possible career paths using graph algorithms.

## 🔄 Project Workflow

Resume Upload  
↓  
Text Extraction  
↓  
NLP Preprocessing  
↓  
Skill Extraction  
↓  
TF-IDF + Cosine Similarity  
↓  
Skill Coverage  
↓  
Match Score  
↓  
Job Recommendation  
↓  
Skill Gap Analysis  
↓  
Career Graph  
↓  
BFS / DFS / Dijkstra  
↓  
Career Path Recommendation

## ✨ Features

- 📄 PDF and DOCX resume processing
- 🧠 NLP-based text preprocessing using spaCy
- 🔎 Technical skill extraction and normalization
- 📊 TF-IDF and Cosine Similarity based job matching
- 🎯 Approximate resume-job match score
- 🏆 Top 5 job recommendations
- ✅ Matched and missing skill analysis
- 🗺️ Career graph and career transition analysis
- 🔵 BFS career path search
- 🟢 DFS career path exploration
- 🟠 Dijkstra minimum-cost career path
- 💻 Interactive Streamlit dashboard

## 🧠 NLP Pipeline

The resume text is processed using spaCy through:

- Lowercasing
- Number removal
- Punctuation removal
- Stopword removal
- Lemmatization

Technical skills are then identified using a predefined skill dataset.

## 📊 Resume-Job Matching

The system uses TF-IDF to convert resume and job-description text into numerical vectors.

Cosine Similarity is then used to measure the similarity between the resume and job description.

### Match Score

Final Match Score =

40% × Text Similarity + 60% × Skill Coverage

The score is an approximate educational score and is not intended to represent a commercial ATS score.

## 🧩 Skill Gap Analysis

For the recommended role, the system compares the candidate's detected skills with the skills required for that role.

It displays:

- Matched Skills
- Missing Skills

This helps identify areas where the candidate can improve.

## 🗺️ Career Path Optimization

Career roles are represented as nodes in a directed graph, while possible career transitions are represented as edges.

The project uses:

### BFS
Finds a career path with fewer transitions.

### DFS
Explores possible career paths using depth-first traversal.

### Dijkstra
Finds a minimum-cost career path based on the defined skill-gap cost.

## 📈 Example Result

For one tested resume:

- Recommended Role: **Backend Developer**
- Match Score: **75.69%**
- Text Similarity: **39.22%**
- Skill Coverage: **100%**
- Skills Detected: **22**

Example career path:

**Backend Developer → Data Engineer → Data Scientist → Data Analyst**

Dijkstra Skill Gap Cost: **12**

## 🛠️ Technology Stack

- Python
- Streamlit
- spaCy
- Pandas
- NumPy
- Scikit-learn
- pdfplumber
- python-docx
- Matplotlib
- WordCloud

## 📁 Project Structure

```text
ai-career-navigator/
│
├── app.py
├── test.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── jobs.csv
│   ├── roles.csv
│   └── skills.csv
│
├── resumes/
│   └── sample_resume.pdf
│
└── utils/
    ├── career_graph.py
    ├── extract_text.py
    ├── match_score.py
    ├── preprocess.py
    ├── recommendation.py
    └── skill_match.py

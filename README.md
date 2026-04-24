# AI Resume Critiquer
AI Resume Critiquer is a simple web application that analyzes resumes and provides AI-powered feedback to help improve them. The app allows users to upload their resume and receive structured suggestions on how to enhance content, skills presentation, and overall impact.
The application is built using **Streamlit** for the interface and **Google Gemini AI** for generating intelligent resume feedback.

---

## Features

* Upload resumes in **PDF or TXT format**
* Extracts and reads resume content automatically
* Provides **AI-powered feedback and suggestions**
* Allows users to specify a **target job role**
* Generates **structured improvement recommendations**

---

## Technologies Used

* Python
* Streamlit
* PyPDF2
* Google Gemini API
* python-dotenv

---

## How It Works

1. The user uploads a resume file.
2. The application extracts text from the file.
3. The user can optionally specify a job role they are targeting.
4. The resume content is sent to the Gemini AI model.
5. The AI analyzes the resume and returns feedback with improvement suggestions.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aliza-imran25/AI-Resume-Critiquer.git
cd AI-Resume-Critiquer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Google Gemini API key:

```
GOOGLE_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run main.py
```

---

## Usage

1. Upload your resume in **PDF or TXT format**.
2. Enter the **job role** you are targeting (optional).
3. Click **Analyze Resume**.
4. View the **AI-generated feedback and improvement suggestions**.

---

## Project Purpose

This project demonstrates how AI models can be integrated into web applications to provide intelligent document analysis and feedback.
It is an AI project showcasing the integration of **Streamlit and generative AI models**.

---

## Author

**Aliza Imran**

GitHub: https://github.com/aliza-imran25



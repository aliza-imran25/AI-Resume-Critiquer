import streamlit as st
import PyPDF2
import io
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Streamlit page setup
st.set_page_config(page_title="AI Resume Critiquer", page_icon="📄", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs.")

# Get API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])

# Job role input
job_role = st.text_input("Enter the job you are targeting (optional)")

# Analyze button
analyze = st.button("Analyze Resume")


# -------- PDF TEXT EXTRACTION --------
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


# -------- FILE TEXT EXTRACTION --------
def extract_text_from_file(uploaded_file):

    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))

    else:
        return uploaded_file.read().decode("utf-8")


# -------- MAIN ANALYSIS --------
if analyze and uploaded_file:

    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not contain readable content.")
            st.stop()

        prompt = f"""
You are an expert resume reviewer with years of experience.

Please analyze this resume and provide constructive feedback.

Focus on the following:

1. Content clarity and impact
2. Skills presentation
3. Experience descriptions
4. Improvements for {job_role if job_role else "general job applications"}

Resume Content:
{file_content}

Provide your analysis in a clear structured format with actionable recommendations.
"""

        # Gemini model
        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(prompt)

        st.markdown("### Analysis Results")
        st.write(response.text)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
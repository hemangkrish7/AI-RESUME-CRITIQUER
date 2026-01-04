import streamlit as st
import PyPDF2
import os
import io
import google.generativeai as genai

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="AI Resume Critiquer",
    page_icon="📝",
    layout="centered"
)

st.title("AI Resume Critiquer 📝")
st.markdown("Upload your resume in PDF or TXT format and get instant feedback!")

# ------------------ GEMINI SETUP ------------------
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.0-pro")


# ------------------ FILE UPLOAD ------------------
uploaded_file = st.file_uploader(
    "Upload your Resume file (PDF or TXT)",
    type=["pdf", "txt"]
)

job_role = st.text_input("Enter the job role you are applying for:")
analyze = st.button("Analyze Resume")

# ------------------ HELPERS ------------------
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

def extract_text_from_file(file):
    if file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(file.read()))
    else:
        return file.read().decode("utf-8")

# ------------------ ANALYSIS ------------------
if analyze and uploaded_file:
    try:
        resume_text = extract_text_from_file(uploaded_file)

        if not resume_text.strip():
            st.error("The uploaded file is empty. Please upload a valid resume.")
            st.stop()

        prompt = f"""
You are an expert career advisor and ATS specialist.

Analyze the resume below and provide **clear, actionable feedback** focusing on:
1. Content clarity and impact
2. Skills presentation
3. Experience & project descriptions
4. ATS optimization tips
5. Specific improvements for the role: {job_role if job_role else "general job applications"}

Resume:
{resume_text}

Respond in a structured format with bullet points.
"""

        response = model.generate_content(prompt)

        st.markdown("## 📊 Resume Analysis & Feedback")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred: {e}")

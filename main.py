import streamlit as st
import PyPDF2
import os
import io
from dotenv import load_dotenv
from google import genai  # ✅ updated import

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon=":memo:", layout="centered")    
st.title("AI Resume Critiquer :memo:")
st.markdown("Upload your resume in PDF format and get instant feedback to improve it!")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

uploaded_file = st.file_uploader("Upload your Resume file (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are applying for:")
analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)
        if not file_content.strip():
            st.error("The uploaded file is empty. Please upload a valid resume.")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback.
        Focus on:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience description
        4. Specific improvements for {job_role if job_role else 'general job applications'}

        Resume Content:
        {file_content}

        Please provide your analysis in a clear and structured format with actionable recommendations."""

        response = client.models.generate_content(
            model="gemini-2.0-flash",  # You can also try "gemini-2.5-flash"
            contents=f"You are an expert career advisor.\n\n{prompt}"
        )

        st.markdown("### Resume Analysis and Feedback:")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")

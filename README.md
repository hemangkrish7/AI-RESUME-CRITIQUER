# 🧠 AI Resume Critiquer

An intelligent, Gemini-powered Streamlit app that analyzes resumes and provides actionable feedback on content clarity, skill presentation, and experience alignment — all within seconds!

![App Screenshot](https://drive.google.com/uc?export=view&id=1unDpEWEiK1g0Xlgh9IXxSYwYdRFH10Rp
)

---

## 🚀 Features

* ✅ **AI-Powered Feedback** — Uses Google’s Gemini API to provide smart, human-like suggestions.
* ✅ **PDF/Text Upload** — Supports both `.pdf` and `.txt` resume formats.
* ✅ **Job Role Context** — Customizes feedback based on the job role you’re targeting.
* ✅ **Instant Insights** — Highlights areas to improve formatting, phrasing, or technical impact.
* ✅ **Streamlit UI** — Clean, interactive interface built with `streamlit`.

---

## 🧩 Tech Stack

* **Frontend/UI:** Streamlit
* **AI Model:** Google Gemini (via `google-genai` SDK)
* **Backend Logic:** Python
* **File Parsing:** PyPDF2
* **Environment Management:** python-dotenv

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-resume-critiquer.git
cd ai-resume-critiquer
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

> **Note:** The `.venv` folder contains your project’s virtual environment. Do **not** push it to GitHub; it will be ignored via `.gitignore`.

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variable

Create a `.env` file in your root directory:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### 5️⃣ Run the App Locally

```bash
streamlit run main.py
```

Then open your browser at **[http://localhost:8501](http://localhost:8501)** 🎉

---

## 🧱 Project Structure

```
AI-Resume-Critiquer/
│
├── main.py                 # Streamlit application entry point
├── requirements.txt        # Dependencies for deployment
├── .env                    # Stores GEMINI_API_KEY (not committed)
├── .gitignore              # Ignores venv and sensitive files
├── .venv/                  # Virtual environment folder (ignored by git)
└── README.md               # Project documentation
```

---

## 🤖 Deployment (Streamlit Cloud)

1. Push your code to GitHub.
2. Go to [https://share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app** and select your repository.
4. Set `main.py` as the entry file.
5. Under **Advanced Settings → Secrets**, add:

   ```
   GEMINI_API_KEY = your_actual_api_key_here
   ```
6. Deploy and share your app link ✨

---

## 🔄 Troubleshooting

* **App not loading:** Check `requirements.txt` and logs on Streamlit Cloud.
* **Invalid API key:** Ensure your key is set in secrets, not in `.env`.
* **Large resumes:** Consider summarizing before sending full text to Gemini.

---

## 🚀 Future Enhancements

* Resume score grading system.
* Option to export feedback as PDF.
* Auto-detection of weak bullet points using NLP.
* Integration with LinkedIn-style formatting suggestions.

---

## ❤️ Acknowledgments

Built by **Hemang Krish** using [Streamlit](https://streamlit.io/) and [Google Gemini AI](https://ai.google.dev/).
Special thanks to open-source contributors and Streamlit Cloud for free hosting!



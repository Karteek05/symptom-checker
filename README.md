# 🩺 Healthcare Symptom Checker

**🎯 Live Demo:** [https://karteek05-symptom-checker.streamlit.app](https://karteek05-symptom-checker.streamlit.app)

An AI-powered educational tool that analyzes symptoms and suggests possible conditions using LLMs.
Built with FastAPI, Streamlit, and OpenRouter.

> ⚠️ For educational purposes only — not a diagnostic tool.

An AI-powered educational symptom analysis tool that helps users understand possible medical conditions and safe next steps based on their entered symptoms.
Built using FastAPI, Streamlit, and OpenRouter (GPT-OSS-20B) — this project demonstrates how large language models can assist in health awareness and decision support while maintaining strict safety and ethical disclaimers.

⚠️ Disclaimer: This application is for educational and informational purposes only. It is not a medical diagnostic tool and should not replace professional consultation or treatment.

🚀 Features

🧠 LLM-Powered Reasoning – Uses OpenRouter’s GPT-OSS-20B model for intelligent, contextual symptom analysis

⚙️ FastAPI Backend – Provides a secure and structured API for symptom queries

🎨 Streamlit Frontend – Simple, elegant interface for users to input and view results

🔄 One-Click Launcher – run.py automatically starts both backend and frontend together

💾 Offline Safety Fallback – Returns example responses when API is unreachable

🛡️ Educational Compliance – Built with responsible AI principles and clear disclaimers

🧰 Tech Stack
Component	Technology
Backend	FastAPI
Frontend	Streamlit
Model Provider	OpenRouter (GPT-OSS-20B)
Language	Python 3.10+
Environment	.env for API key management
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Karteek05/symptom-checker.git
cd symptom-checker

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment

Create a .env file in the project root:

OPENAI_API_KEY=sk-or-v1-your-openrouter-key-here

4️⃣ Run the App
python run.py


This will:

Start the FastAPI backend on port 8000

Launch the Streamlit GUI on port 8501

Automatically open the app in your browser

🧠 Example Usage

Input:

fever, sore throat, headache


Output:

Possible conditions:
1. Flu or viral infection
2. Strep throat
3. Sinusitis

Next Steps:
• Rest and hydrate
• Use OTC fever reducers
• Consult a doctor if symptoms persist

⚠️ Educational use only – not a substitute for professional medical advice

🧩 Project Structure
symptom-checker/
│
├── main.py            # FastAPI backend
├── app.py             # Streamlit frontend
├── run.py             # Combined launcher script
├── requirements.txt   # Dependencies
├── .env               # Environment variables (ignored in Git)
└── README.md          # Documentation

🧭 Future Enhancements

🧾 Symptom history tracking (per session)

🏥 Integration with open medical datasets for richer insights

🌐 Multi-language support (for rural accessibility)

📱 Deployable web version for smartphones

👤 Developed By

Cherukupalli Sai Sriram Karteek (22BCE7767)
Vellore Institute of Technology — Unthinkable 2026 Project
📅 October 2025


import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load your OpenRouter API key from environment variables or Streamlit secrets
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Healthcare Symptom Checker", page_icon="🩺", layout="centered")

st.markdown("""
    <style>
        .main-title {
            text-align: center;
            color: #2B6CB0;
            font-size: 2.2em;
            font-weight: bold;
        }
        .sub-title {
            text-align: center;
            color: #4A5568;
            font-size: 1.1em;
            margin-bottom: 20px;
        }
    </style>
    <h1 class='main-title'>🩺 Healthcare Symptom Checker</h1>
    <p class='sub-title'>AI-powered educational assistant that helps you understand your symptoms safely.</p>
""", unsafe_allow_html=True)
st.info("💡 This tool provides educational information only and should not replace a doctor’s consultation.")

# User input
symptoms = st.text_area("Describe your symptoms:", placeholder="e.g., fever, sore throat, headache")

if st.button("Analyze Symptoms"):
    if not symptoms.strip():
        st.warning("⚠️ Please enter your symptoms before submitting.")
    else:
        with st.spinner("Analyzing with AI..."):
            try:
                # --- Prepare OpenRouter API Request ---
                headers = {
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "HTTP-Referer": "https://github.com/Karteek05/symptom-checker",
                    "X-Title": "Healthcare Symptom Checker (Streamlit)",
                    "Content-Type": "application/json",
                }

                data = {
                    "model": "openai/gpt-oss-20b:free",
                    "messages": [{
                        "role": "user",
                        "content": f"""
                        You are a responsible medical assistant.
                        Based on these symptoms: "{symptoms}",
                        list 3–5 possible conditions (educational purposes only),
                        provide next steps,
                        and always include this disclaimer:
                        ⚠️ This is for educational purposes only and not a substitute for medical advice.
                        """
                    }],
                }

                # --- API Request to OpenRouter ---
                response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                         headers=headers, json=data)
                response.raise_for_status()
                result = response.json()["choices"][0]["message"]["content"]

                st.success("✅ Analysis Complete!")
                st.markdown(result)

            except Exception as e:
                st.error(f"⚠️ Could not reach OpenRouter API: {e}")
                st.info("Showing offline example response instead.")
                st.markdown("""
                **Possible conditions:** Common cold, Flu, or Viral infection  
                **Next steps:** Rest, hydrate, and consult a doctor if symptoms persist.  
                ⚠️ Educational purposes only — not medical advice.
                """)

st.markdown("---")
st.markdown("""
    <div style='text-align: center; font-size: 0.9em; color: grey;'>
        Developed by <b>Karteek Cherukupalli (22BCE7767)</b> <br>
        Vellore Institute of Technology | Unthinkable 2026 Project <br>
        <i>Powered by OpenRouter | Built with FastAPI + Streamlit</i>
    </div>
""", unsafe_allow_html=True)

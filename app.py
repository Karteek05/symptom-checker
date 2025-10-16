import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load your OpenRouter API key from environment variables or Streamlit secrets
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Healthcare Symptom Checker", page_icon="🩺", layout="centered")

st.title("🩺 Healthcare Symptom Checker")
st.markdown("Enter your symptoms below to get possible conditions and next steps (for educational use only).")

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
st.caption("Developed by Karteek Cherukupalli (22BCE7767) | VIT-AP | Unthinkable 2026 Project")

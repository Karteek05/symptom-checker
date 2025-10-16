import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")

# Page setup
st.set_page_config(page_title="Healthcare Symptom Checker", page_icon="🩺", layout="centered")

# Custom CSS
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
            margin-bottom: 25px;
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: grey;
            margin-top: 50px;
        }
        .disclaimer {
            background-color: #EBF8FF;
            border-left: 5px solid #2B6CB0;
            padding: 10px;
            margin-top: 20px;
            font-size: 0.9em;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-title'>🩺 Healthcare Symptom Checker</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>AI-powered educational assistant to help you understand your symptoms responsibly.</p>", unsafe_allow_html=True)

st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=100)

# Symptom input
st.markdown("### Describe your symptoms below:")
symptoms = st.text_area(" ", placeholder="e.g., fever, sore throat, headache")

st.info("💡 This tool provides educational information only and should not replace a doctor’s consultation.")

# Initialize history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Analyze button
if st.button("🔍 Analyze Symptoms"):
    if not symptoms.strip():
        st.warning("⚠️ Please enter your symptoms before submitting.")
    else:
        with st.spinner("Analyzing your symptoms using AI..."):
            try:
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

                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers=headers, json=data
                )
                response.raise_for_status()
                result = response.json()["choices"][0]["message"]["content"]

                st.success("✅ Analysis Complete!")
                st.markdown(result)

                # Save to history
                st.session_state.history.append({
                    "symptoms": symptoms,
                    "result": result
                })

            except Exception as e:
                st.error(f"⚠️ Could not reach OpenRouter API: {e}")
                st.info("Showing offline example response instead.")
                example_response = """
                **Possible conditions:** Common cold, Flu, or Viral infection  
                **Next steps:** Rest, hydrate, and consult a doctor if symptoms persist.  
                ⚠️ Educational purposes only — not medical advice.
                """
                st.markdown(example_response)
                st.session_state.history.append({
                    "symptoms": symptoms,
                    "result": example_response
                })

# Divider
st.markdown("---")

# History section
if st.session_state.history:
    st.markdown("### 🕒 Previous Queries")
    for entry in reversed(st.session_state.history[-5:]):
        st.markdown(f"**🩹 Symptoms:** {entry['symptoms']}")
        st.markdown(f"{entry['result']}")
        st.markdown("---")

# Disclaimer
st.markdown("<div class='disclaimer'>⚠️ This tool is for educational purposes only. Always consult a qualified healthcare professional for personalized medical advice.</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class='footer'>
        Developed by <b>Karteek C (22BCE7767)</b> <br>
        Vellore Institute of Technology | Unthinkable 2026 Project <br>
        <i>Powered by OpenRouter | Built with FastAPI + Streamlit</i>
    </div>
""", unsafe_allow_html=True)

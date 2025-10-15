import streamlit as st
import requests

st.set_page_config(page_title="Healthcare Symptom Checker", page_icon="🩺", layout="centered")

st.title("🩺 Healthcare Symptom Checker")
st.markdown("Enter your symptoms below to get possible conditions and next steps (educational use only).")

# Text input for symptoms
symptoms = st.text_area("Describe your symptoms:", placeholder="e.g., fever, sore throat, headache")

# Backend API URL (your local FastAPI app)
API_URL = "http://127.0.0.1:8000/check-symptoms"

if st.button("Analyze Symptoms"):
    if not symptoms.strip():
        st.warning("⚠️ Please enter your symptoms before submitting.")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(API_URL, json={"symptoms": symptoms})
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Analysis Complete!")
                    st.markdown(data["analysis"])
                else:
                    st.error(f"❌ Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"🚫 Could not connect to backend: {e}")

st.markdown("---")
st.caption("⚠️ This tool is for **educational purposes only** and not a substitute for professional medical advice.")
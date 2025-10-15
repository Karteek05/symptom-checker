from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Healthcare Symptom Checker",
    description="Educational symptom checker using OpenRouter (free GPT-OSS-20B model).",
    version="1.0.0",
)

class SymptomInput(BaseModel):
    symptoms: str


@app.post("/check-symptoms")
async def check_symptoms(input: SymptomInput):
    """Analyze symptoms and return possible conditions + next steps."""
    if not input.symptoms.strip():
        raise HTTPException(status_code=400, detail="Symptoms cannot be empty")

    prompt = f"""
    You are a responsible medical information assistant.
    Based on these symptoms: "{input.symptoms}",
    list 3–5 possible conditions (educational purposes only),
    provide practical next steps,
    and include this disclaimer:
    ⚠️ This is for educational purposes only and not a substitute for medical advice.
    """

    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "https://github.com/Karteek05/symptom-checker",  # required by OpenRouter
            "X-Title": "Healthcare Symptom Checker",
            "Content-Type": "application/json",
        }

        data = {
    "model": "openai/gpt-oss-20b:free",  # 👈 ensures it uses the free route
    "messages": [{"role": "user", "content": prompt}],
    }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
        )
        response.raise_for_status()
        result = response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        result = (
            f"⚠️ Could not connect to OpenRouter: {e}\n\n"
            "Possible conditions: Common cold, Flu, or Viral infection.\n"
            "Next steps: Rest, hydrate, and consult a doctor if fever persists.\n"
            "⚠️ Educational use only."
        )

    return {"input": input.symptoms, "analysis": result}


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Healthcare Symptom Checker API (OpenRouter-powered)",
        "usage": "POST /check-symptoms with {'symptoms': 'your symptoms here'}",
    }
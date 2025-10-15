from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

try:
    from openai import OpenAI
    USE_LLM = True
except ImportError:
    USE_LLM = False

# Load environment variables
load_dotenv()

app = FastAPI(title="Healthcare Symptom Checker")

# Initialize OpenAI client (if available)
if USE_LLM and os.getenv("OPENAI_API_KEY"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
else:
    client = None

# Input model
class SymptomInput(BaseModel):
    symptoms: str

@app.post("/check-symptoms")
async def check_symptoms(input: SymptomInput):
    """Takes symptom text and returns possible conditions + recommendations"""
    if not input.symptoms.strip():
        raise HTTPException(status_code=400, detail="Symptoms cannot be empty")

    # Create LLM prompt
    prompt = f"""
    You are a helpful medical assistant (for educational purposes only).
    Based on these symptoms: "{input.symptoms}",
    list 3–5 possible conditions and practical next steps.
    Always end with this disclaimer:
    ⚠️ This is for educational purposes only and not a substitute for medical advice.
    """

    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
            )
            result = response.choices[0].message.content
        except Exception as e:
            result = f"Error generating response: {e}"
    else:
        # Offline fallback
        result = (
            "Possible conditions: Common Cold, Influenza, or Viral Infection.\n"
            "Next steps: Rest, stay hydrated, and consult a doctor if fever persists.\n"
            "⚠️ This is for educational purposes only and not a substitute for medical advice."
        )

    return {"input": input.symptoms, "analysis": result}
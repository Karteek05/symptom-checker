# Healthcare Symptom Checker
Educational project that suggests possible conditions and next steps based on symptoms.
⚠️ Disclaimer: This tool is not a substitute for medical advice.

## Features
- Input symptoms (text)
- Returns possible conditions & recommendations
- Optional frontend + query history

## Tech Stack
- FastAPI / Flask
- OpenAI API
- (Optional) SQLite for storage

## Run Locally
pip install -r requirements.txt  
python main.py

## Example
Input: "fever, sore throat"
Output:
- Conditions: Common cold, Flu, Strep throat
- Next Steps: Rest, hydration, see doctor if symptoms persist >3 days

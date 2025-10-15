import subprocess
import time
import webbrowser
import threading

def run_fastapi():
    subprocess.run(["uvicorn", "main:app", "--reload"])

def run_streamlit():
    # Wait for FastAPI to start first
    time.sleep(2)
    webbrowser.open("http://localhost:8501")
    subprocess.run(["streamlit", "run", "app.py"])

if __name__ == "__main__":
    print("🚀 Launching Healthcare Symptom Checker...")
    print("Starting FastAPI backend and Streamlit frontend...")

    # Run both processes in parallel
    fastapi_thread = threading.Thread(target=run_fastapi)
    streamlit_thread = threading.Thread(target=run_streamlit)

    fastapi_thread.start()
    streamlit_thread.start()

    fastapi_thread.join()
    streamlit_thread.join()
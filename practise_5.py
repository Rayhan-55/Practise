import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

# Load the .env file
load_dotenv()

# Get your API key from .env
api_key = os.getenv("GROQ_API_KEY")  
Groq_MODEL = "llama-3.1-8b-instant"

ollama_groq = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)
Rayhan_Profile = {
    "name": "Rayhan",
    "skills": ["C++ problem solving", "Machine Learning", "LLM engineering", "Full-stack AI projects", "Streamlit", "GitHub","Python"],
    "experience": ["Worked on ML and AI projects", "Created Telco churn prediction project", "LLM-based chatbots"],
    "education": "studying cse at Northern University of Business and Technology",
    "projects": [
        {"name": "Telco Churn Prediction", "links": ["https://telcochurnprediction.streamlit.app/", "https://github.com/Rayhan-55/Telco_Churn_Prediction"]},
        {"name": "Full-stack AI restaurant chatbot project", "description": "AI + database + Q&A chatbot"}
    ],
    
    
}

Recruiter_System = (
    "You are a personal profile assistant chatbot for Rayhan. "
    "Use the following profile information to answer any recruiter questions accurately and professionally: "
    f"{Rayhan_Profile} "
    "Do NOT give opinions, personal advice, or unrelated content. "
    "Keep answers concise and focused on Rayhan's professional profile."
)

def chat(message, history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role": "system", "content": Recruiter_System}] + history + [{"role": "user", "content": message}]
    stream = ollama_groq.chat.completions.create(model=Groq_MODEL, messages=messages, stream=True)
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response

gr.ChatInterface(fn=chat, type="messages").launch()
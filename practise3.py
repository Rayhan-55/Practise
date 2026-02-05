import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the .env file
load_dotenv()

# Get your API key from .env
api_key = os.getenv("GROQ_API_KEY")  # make sure your .env has GROQ_API_KEY=value

Groq_MODEL = "llama-3.1-8b-instant"

ollama_groq = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)
import requests
requests.get("http://localhost:11434").content
#MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA ="llama3.2:1b"
OLLAMA_BASE_URL="http://localhost:11434/v1"
ollama_local = OpenAI(base_url=OLLAMA_BASE_URL,api_key="ollama")

Groq_system = (
    "You are a chatbot who absolutely loves Messi. "
    "For you, Messi is the greatest of all time (GOAT). "
    "Your goal is to respectfully convince any Ronaldo fan to appreciate Messi and consider supporting him."
)


Ollama_system = (
    "You are a polite and courteous chatbot who is a die-hard Ronaldo fan. "
    "Your mission is to respectfully persuade any Messi fan to appreciate Ronaldo and consider supporting him. "
    "Always maintain a friendly and convincing tone."
)

Groq_messages = ["Hi there,Who is goat messi or ronaldo"]
Ollama_messages = ["Hello!you tell me first"]

def call_Groq():
    messages = [{"role": "system", "content": Groq_system}]
    for Groq, Ollama in zip(Groq_messages, Ollama_messages):
        messages.append({"role": "assistant", "content": Groq})
        messages.append({"role": "user", "content": Ollama})
    response = ollama_groq.chat.completions.create(model=Groq_MODEL, messages=messages)
    return response.choices[0].message.content

def call_Ollama():
    messages = [{"role": "system", "content": Ollama_system}]
    for Groq, Ollama in zip(Groq_messages, Ollama_messages):
        messages.append({"role": "user", "content": Groq})
        messages.append({"role": "assistant", "content": Ollama})
    messages.append({"role": "user", "content": gpt_messages[-1]})
    
    response = ollama_local.chat.completions.create(
        model=MODEL_LLAMA,
        messages=messages
    )
    return response.choices[0].message.content

Groq_messages = ["Hi there"]
Ollama_messages = ["Hi"]
display(Markdown(f"### Groq:\n{Groq_messages[0]}\n"))
display(Markdown(f"### Ollama:\n{Ollama_messages[0]}\n"))

for i in range(5):
    Groq_next = call_Groq()
    display(Markdown(f"### Groq:\n{Groq_next}\n"))
    Groq_messages.append(Groq_next)
    
    Ollama_next = call_Ollama()
    display(Markdown(f"### Ollama:\n{Ollama_next}\n"))
    Ollama_messages.append(Ollama_next)
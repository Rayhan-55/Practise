import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

# Load the .env file
load_dotenv()

# Get your API key from .env
api_key = os.getenv("GROQ_API_KEY")  # make sure your .env has GROQ_API_KEY=value

Groq_MODEL = "llama-3.1-8b-instant"

ollama_groq = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)
Groq_system = (
    "You are a translator chatbot. Your only task is to translate English text into Bengali. "
    "Do NOT provide explanations, comments, or any other answers. Only output the translation."
)
def stream_gpt(prompt):
    messages = [
        {"role": "system", "content": Groq_system},
        {"role": "user", "content": prompt}
      ]
    stream = ollama_groq.chat.completions.create(
        model=Groq_MODEL,
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result

message_input = gr.Textbox(label="Your message:", info="Enter a message for Translation", lines=7)
message_output = gr.Markdown(label="Response:")

view = gr.Interface(
    fn=stream_gpt,
    title="LLMs Translator", 
    inputs=[message_input], 
    outputs=[message_output], 
    
    flagging_mode="never"
    )
view.launch()
import os
import gradio as gr
from dotenv import load_dotenv
import google.generativeai as genai

#  Load Gemini API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Check if key exists
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

# Configure Gemini API
genai.configure(api_key=api_key)

#  Use Gemini 1.5 Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

# Prompt Evaluation Logic
def evaluate_prompts(user_task):
    prompt_1 = f"""
You are a professional summarizer.
Summarize the following in 3 formal bullet points:

{user_task}
"""

    prompt_2 = f"""
You are a social media expert.
Convert the following into a 3-tweet thread using a casual, engaging tone:

{user_task}
"""

    try:
        response_1 = model.generate_content(prompt_1).text
        response_2 = model.generate_content(prompt_2).text

        return f"""###  Prompt 1: Formal Summary
{response_1}

---

###  Prompt 2: Tweet Thread Style
{response_2}

---

 Compare outputs. Which one better fits your use case?
"""
    except Exception as e:
        return f" Error: {e}"

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("##  Prompt Evaluation Tool – Gemini AI")
    gr.Markdown("Compare two prompt strategies on the same input using Gemini 1.5 Flash. Useful for analyzing tone, clarity, and hallucination.")

    input_box = gr.Textbox(label=" Input Task (e.g., news, resume, article)", lines=6)
    output_box = gr.Textbox(label=" Prompt Outputs", lines=16)
    generate_btn = gr.Button(" Run Prompt Evaluation")

    generate_btn.click(fn=evaluate_prompts, inputs=input_box, outputs=output_box)

    gr.Markdown("---")
    gr.Markdown(" Powered by Google Gemini 1.5 Flash")
    gr.Markdown("© 2025 **Mantasha Idrisi**. All rights reserved.", elem_id="footer")

if __name__ == "__main__":
    demo.launch()
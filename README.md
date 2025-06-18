#  Prompt Evaluation Tool – Gemini AI

This app allows you to compare how different prompt styles perform on the same input task using **Google Gemini 1.5 Flash**.

 It helps evaluate:
- Tone (Formal vs Casual)
- Response clarity
- Suitability for use case (summaries, tweets, etc.)
- Prompt effectiveness — side by side

---

##  Why I Built This

As part of my prompt engineering journey, I wanted to understand how AI behaves under different prompts for the same input.

This is **one of the core tasks done by Prompt Engineers** at companies like Google, OpenAI, Jasper, and Cohere.

---

##  Tech Stack

- [Google Generative AI](https://ai.google.dev/)
- `gradio` for UI
- `python-dotenv` for API key security
- Prompt chaining logic in Python

---

##  How It Works

### Input:
- A paragraph of text (news, resume, product description, etc.)

### Prompts:
- **Prompt 1:** Summarize the input in 3 formal bullet points  
- **Prompt 2:** Convert it into a casual, engaging tweet thread

### Output:
- Side-by-side responses to compare tone and quality

---

## Local Setup Instructions

1. **Clone this repo:**
```bash
git clone https://github.com/imantasha/prompt-evaluation-tool.git
cd prompt-evaluation-tool

Create .env file and add your Gemini API key:

GEMINI_API_KEY=your_real_key_here


Install dependencies:
pip install -r requirements.txt


Run the app:
python prompt_evaluator.py

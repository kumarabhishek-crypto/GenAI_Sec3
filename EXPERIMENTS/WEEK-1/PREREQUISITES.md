# Week 1 Lab: First LLM API Call

## Prerequisites
1. Visual Studio Code installed.
2. Python installed (3.14 or above).
3. Active virtual environment (`.venv`).
4. An OpenAI API key or Gemini API key.

## Setup Instructions
1. Activate virtual environment:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
3. Add your API key to `.env`:
   - For OpenAI: `OPENAI_API_KEY="your_api_key_here"`
   - For Gemini: `GEMINI_API_KEY="your_api_key_here"`
4. Run the code:
   - For OpenAI: `python main.py`
   - For Gemini: `python call.py`

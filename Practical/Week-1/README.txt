WEEK1-LLM-CALL — GEMINI API PYTHON STARTER

1. Open this folder in VS Code.
2. Open Terminal > New Terminal (PowerShell).
3. Create a virtual environment:
   python -m venv .venv
4. Activate it:
   .\.venv\Scripts\Activate.ps1
5. Install dependencies:
   python -m pip install --upgrade pip
   pip install -r requirements.txt
6. Open .env and replace YOUR_API_KEY_HERE with your own Gemini API key.
   Get a key from Google AI Studio: https://aistudio.google.com/apikey
7. Run:
   python main.py

The .venv folder is intentionally not packaged. Create it on your Windows
computer using step 3 so it matches your local Python installation.

Model: gemini-3.8-flash
Keep your API key private. Do not upload .env or share its contents.

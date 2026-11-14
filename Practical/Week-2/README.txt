WEEK 2 — PROVIDER-AGNOSTIC LLM CLIENT

This project lets you use Gemini through Google's hosted API or Llama 3.2
locally through Ollama.

FILES
- main.py: choose a provider and enter a prompt
- llm_client.py: shared interface and Gemini/Ollama providers
- test_client.py: unit test using a fake provider
- requirements.txt: Python dependencies
- .env: Gemini API key
- .gitignore: excludes secrets and local environment files

SETUP — WINDOWS POWERSHELL

1. Open this folder in VS Code and open Terminal > New Terminal.

2. Create and activate a virtual environment:
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   If activation is blocked, run:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   Then activate again.

3. Install Python dependencies:
   python -m pip install --upgrade pip
   pip install -r requirements.txt

4. To use Gemini:
   - Open .env and replace YOUR_API_KEY_HERE with your own key.
   - Get a key from https://aistudio.google.com/apikey
   - Keep the key private.

5. To use local Ollama:
   - Install Ollama from https://ollama.com/download
   - Start Ollama and wait for it to be ready.
   - In PowerShell run: ollama pull llama3.2
   - Keep Ollama running when selecting the ollama provider.

6. Run the app:
   python main.py
   Choose gemini or ollama, then enter your question.

7. Run the unit test:
   python -m unittest -v
   Or: pytest

NOTES
- The Python module is named llm_client.py (underscore), matching the
  import in main.py.
- The .venv folder is not included. Create it on your Windows computer.
- The Gemini model ID follows the supplied Week-2 guide. If Google reports
  it unavailable, check https://ai.google.dev/gemini-api/docs/models

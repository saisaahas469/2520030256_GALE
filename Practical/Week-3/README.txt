WEEK 3 - LLM MONITORING WITH MONGODB

WHAT THIS PROJECT DOES
- Calls Gemini or local Ollama through a common client.
- Tracks input/output/total tokens and request latency.
- Estimates Gemini API cost using configurable per-million-token rates.
- Stores successful and failed calls in MongoDB Atlas.
- Uses timeouts and up to three attempts for temporary errors.

REQUIREMENTS
- Python 3.10 or newer
- VS Code
- MongoDB Atlas account and a free cluster
- Gemini API key (for Gemini mode)
- Ollama installed and llama3.2 pulled (only for Ollama mode)

SETUP IN VS CODE (WINDOWS)
1. Extract this ZIP file.
2. Open VS Code -> File -> Open Folder -> select Week3_LLM_Monitoring.
3. Open Terminal -> New Terminal. Make sure the terminal is in this project folder.
4. Create a virtual environment:
   py -m venv .venv
5. Activate it in PowerShell:
   .venv\Scripts\Activate.ps1
   If PowerShell blocks activation, use Command Prompt terminal and run:
   .venv\Scripts\activate.bat
6. Install packages:
   python -m pip install -r requirements.txt
7. Copy .env.example to a new file named .env.
8. Edit .env and enter your Gemini API key and MongoDB Atlas connection string.
   Replace the database username, password, and cluster address with your own.
   Keep the two Gemini price values at 0 if using the free tier.
9. In MongoDB Atlas, create a free cluster, create a database user, and add your current IP
   under Network Access / IP Access List. Copy the Python/PyMongo connection string.
10. Run the offline unit test:
    python -m unittest -v test_client
11. Run the application:
    python main.py
12. Enter gemini or ollama, then enter a question.

OLLAMA ONLY
Install/start Ollama, then run once:
ollama pull llama3.2
Then run `python main.py` and choose `ollama`.

CHECK MONGODB
MongoDB Atlas -> Clusters -> Browse Collections ->
database `llm_monitoring` -> collection `api_usage`.

IMPORTANT SECURITY
- Never share your .env file, API key, or MongoDB password.
- Do not upload .env to GitHub.
- If a key/password is exposed, revoke/reset it.
- If your MongoDB password has special characters, URL-encode it.

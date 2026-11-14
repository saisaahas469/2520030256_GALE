import os
from dotenv import load_dotenv
from google import genai

# Load values from the .env file
load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "YOUR_API_KEY_HERE":
    raise ValueError(
        "Gemini API key not found. Add your key to the GEMINI_API_KEY "
        "value in the .env file."
    )

client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-3.5-flash-lite"


def main():
    try:
        print(f"Connecting to {MODEL_NAME}...")
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents="What is Artificial Intelligence? Explain it in simple words."
        )

        print("\nLLM Response:\n")
        print(response.text or "Gemini returned an empty response.")

    except Exception as error:
        print("\nAn error occurred:")
        print(error)


if __name__ == "__main__":
    main()

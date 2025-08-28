import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Use it with Google Generative AI
genai.configure(api_key=api_key)
def convert_to_structured_format(cobol_code):
    """
    Uses Gemini to convert COBOL code into structured format (e.g., JSON or pseudo-code).
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Convert the following COBOL business logic into structured format (JSON or pseudo-code):\n\n{cobol_code}"
    response = model.generate_content(prompt)
    return response.text

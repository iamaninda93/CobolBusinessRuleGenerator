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
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = (
        "Convert the following COBOL business logic into a structured format such as JSON or pseudo-code. "
        "Do not include any annotations or explanations: "
        + cobol_code
    )

    response = model.generate_content(prompt)
    return response.text




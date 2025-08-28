import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Use it with Google Generative AI
genai.configure(api_key=api_key)

def extract_business_rules(structured_logic):
    """
    Uses Gemini to extract business rules from structured COBOL logic.
    """
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    prompt = (
            "Extract business rules from the following structured COBOL logic. "
            "Please write the rules in simple, clear English that a business analyst can understand:\n\n"
        "Do not include any annotations or explanations: "
            + structured_logic
    )

    response = model.generate_content(prompt)
    return response.text.split("\n")




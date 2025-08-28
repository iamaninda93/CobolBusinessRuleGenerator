import google.generativeai as genai
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Use it with Google Generative AI
genai.configure(api_key=api_key)


def validate_rules(rules):
    """
    Uses Gemini to validate business rules for consistency and completeness.

    Args:
        rules (list): List of business rules as strings.

    Returns:
        list: Validated rules or feedback from Gemini.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = (
        "Review the following business rules written in simple English. "
        "Ensure they are clear, complete, and consistent. "
        "Rewrite them if needed, but do not include any annotations or explanations:

"
        + "
".join(rules)
    )

    response = model.generate_content(prompt)
    return response.text.split("\n")


#prompt = (
        #"Review the following business rules written in simple English. "
       # "Check for clarity, completeness, and consistency. "
       # "If needed, rewrite them in clearer language:\n\n"
        #+ "\n".join(rules)
   # )


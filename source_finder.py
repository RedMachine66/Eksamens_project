import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment variable
gemini_api_key = os.getenv('GOOGLE_GEMINI_KEY')

# Set your API key
client = genai.Client(api_key=gemini_api_key)

def get_gemini_response(user_message):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[user_message]
    )
    for candidate in response.candidates:
        return candidate.content.parts[0].text
import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
import re

# Indlæs miljøvariabler fra .env-filen
load_dotenv()

# Hent API-nøglen fra miljøvariablen
gemini_api_key = os.getenv('GOOGLE_GEMINI_KEY')

# Angiv din API-nøgle
if gemini_api_key:
    client = genai.Client(api_key=gemini_api_key)
else: client = None

def get_gemini_response_with_search(user_message, system_prompt_path="source_finder_system_prompt.txt"):
    if client is None:
        return "No genai client exists. This is likely because you're using a limited version of Dashcorp with secret API keys removed for security purposes. " \
        "Add your own key to the environment variables to unlock source finding, or keep using all other features of Dashcorp Student Tools without source finding."
    
    with open(system_prompt_path, 'r') as file:
        system_prompt = file.read()

    google_search_tool = Tool(google_search=GoogleSearch())

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_message,
        config=GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[google_search_tool],
            response_modalities=["TEXT"],
        )
    )
    for candidate in response.candidates:
        return candidate.content.parts[0].text

# # Eksempel
# print(get_gemini_response_with_search("hvornår er der næste solformørkelse i Danmark?"))
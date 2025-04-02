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
client = genai.Client(api_key=gemini_api_key)

def get_gemini_response_with_search(user_message, system_prompt_path="source_finder_system_prompt.txt"):
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
            max_output_tokens=500
        )
    )
    for candidate in response.candidates:
        return candidate.content.parts[0].text

# Eksempel på brug
print(get_gemini_response_with_search("hvornår er der næste solformørkelse i Danmark?"))





# import os
# from dotenv import load_dotenv
# from google import genai
# from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
# import re

# # Indlæs miljøvariabler fra .env-filen
# load_dotenv()

# # Hent API-nøglen fra miljøvariablen
# gemini_api_key = os.getenv('GOOGLE_GEMINI_KEY')

# # Angiv din API-nøgle
# client = genai.Client(api_key=gemini_api_key)

# def get_gemini_response_with_search(user_message, system_prompt_path="source_finder_system_prompt.txt"):
#     with open(system_prompt_path, 'r') as file:
#         system_prompt = file.read()

#     google_search_tool = Tool(google_search=GoogleSearch())

#     response = client.models.generate_content(
#         model="gemini-2.0-flash",
#         contents=user_message,
#         config=GenerateContentConfig(
#             system_instruction=system_prompt,
#             tools=[google_search_tool],
#             response_modalities=["TEXT"],
#             max_output_tokens=500
#         )
#     )
#     for candidate in response.candidates:
#         print("Svar:")
#         print(candidate.content.parts[0].text)

#         try:
#             print("\nKildehenvisninger:")
#             grounding_data = response.candidates[0].grounding_metadata.search_entry_point.rendered_content
#             urls = re.findall(r'href="([^"]+)"', grounding_data)
#             titles = re.findall(r'>([^<]+)</a>', grounding_data)
#             for url, title in zip(urls, titles):
#                 # Bestem kildetype (forenklet eksempel)
#                 if "http" in url:
#                     source_type = "Websted"
#                 else:
#                     source_type = "Andet" # Her vil det kræve yderligere kode, at finde kilde type.

#                 print(f"- Titel: {title}")
#                 print(f"  Webadresse: {url}")
#                 print(f"  Kildetype: {source_type}")
#         except:
#             print("\nIngen kildehenvisninger tilgængelige.")

# # Eksempel på brug
# get_gemini_response_with_search("hvornår er der næste solformørkelse i Danmark?")
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# response
def generate(parts):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[types.Content(parts=parts)])
    return response

# issue generator
def issue_generator(images):
    prompt = """You are a code mentor. Analyze the provided code.

    INSTRUCTIONS:
    1. If there are major issues, provide a clear text explanation of how to fix them.
    2. If the code is fine without major issues, say: "The code looks good. No major issues found."
    3. Do NOT provide code - only text explanation.

    FORMAT YOUR RESPONSE:
    [Provide text-based solution or say code is ok]"""

    parts = [types.Part(text=prompt)]

    for image in images:  
        parts.append(
            types.Part(
                inline_data=types.Blob(
                    mime_type=image.type,   
                    data=image.getvalue(),  
                )
            )
        )

    response = generate(parts)
    return response.text

def solution_generator(images,option):
    if option.lower() == "hints":
        prompt = """You are a code mentor. Analyze the provided code.

        INSTRUCTIONS:
        1. If there are major issues, provide a clear text explanation of how to fix them.
        2. If the code is fine without major issues, say: "The code looks good. No major issues found."
        3. Do NOT provide code - only text explanation.

        FORMAT YOUR RESPONSE:
        [Provide text-based solution or say code is ok]"""
    
    elif option.lower() == "solution with code":
        prompt = """You are a code expert. Analyze the provided code.

        INSTRUCTIONS:
        1. If there are major issues, provide the corrected code in a simple way.
        2. After the code, provide a brief explanation of what was fixed.
        3. If the code is fine without major issues, say: "The code looks good. No major issues found."
        4. Keep code simple and easy to understand.

        FORMAT YOUR RESPONSE:
        [Corrected code if needed, followed by brief explanation of changes made, or say code is ok]"""


    parts = [types.Part(text=prompt)]

    for image in images:  
        parts.append(
            types.Part(
                inline_data=types.Blob(
                    mime_type=image.type,   
                    data=image.getvalue(),  
                )
            )
        )

    response = generate(parts)
    return response.text


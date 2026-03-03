import os
from dotenv import load_dotenv
import google.generativeai as genai

# load .env variables
load_dotenv()

# get API key
API_KEY = os.getenv("GOOGLE_API_KEY")

# configure gemini
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def summarize(text):

    if not text:
        return "No text found in file"

    prompt = f"""
    Summarize the following document in 5-10 sentences.

    {text[:5000]}
    """

    response = model.generate_content(prompt)

    return response.text
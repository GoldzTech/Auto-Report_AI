import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_summary_ai(total, average, highest):
    prompt = f"""
    Create a short professional paragraph (3-5 sentences) summarizing a sales report.
    Total sales: ${total:.2f}, Average: ${average:.2f}, Highest sale: ${highest:.2f}.
    The text should be analyticol and professional.PermissionError
    """
    response = model.generate_content(prompt
    )
    return response.text.strip()

import json
import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def generate_ai_summary(document_info):
    try:
        resume_json = json.dumps(document_info, indent=2)
        prompt = f"""
You are an experienced HR Recruiter.

Analyze the structured resume information provided below.

Generate a professional candidate summary.

Rules:
- Use ONLY the provided information.
- Do NOT invent any skills, education, certifications, or experience.
- Write in third person.
- Keep the summary between 3 and 5 sentences.
- Mention the candidate's education.
- Mention technical skills.
- Mention work experience if available.
- Mention important projects if available.
- Keep the tone professional and suitable for recruiters.
-If the education information indicates the degree is completed, refer to the person as a graduate. Do not describe them as a candidate unless the data explicitly indicates they are currently pursuing the degree.
Resume Data:
{resume_json}
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return None
import json
import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def analyze_resume(document_info, job_description):
    try:
        resume_json = json.dumps(document_info, indent=2)
        prompt = f"""
You are an experienced HR Recruiter and ATS evaluator.

Analyze the candidate's resume against the provided Job Description.

Resume Information:
{resume_json}

Job Description:
{job_description}

Return ONLY valid JSON.

The JSON format MUST be:

{{
    "match_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "strengths": [],
    "recommendations": []
}}

Rules:

- Match score must be between 0 and 100.
- Only use the provided information.
- Do not invent skills, education or experience.
- Matching skills should contain only skills present in both resume and JD.
- Missing skills should contain skills present in JD but missing in resume.
- Strengths should explain why the candidate matches.
- Recommendations should suggest improvements.
- Return ONLY JSON.
- Do NOT wrap JSON inside markdown.
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        response_text = response.text.strip()
        # Remove markdown if Gemini accidentally returns it
        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "")
        response_text = response_text.strip()
        analysis = json.loads(response_text)
        required_keys = [
            "match_score",
            "matching_skills",
            "missing_skills",
            "strengths",
            "recommendations"
        ]
        for key in required_keys:
            if key not in analysis:
                raise ValueError(f"Missing key: {key}")
        return analysis
    except Exception as e:
        print(f"JD Matching Error: {e}")
        return {
            "match_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "strengths": [],
            "recommendations": []
        }
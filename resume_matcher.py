import openai

openai.api_key = "YOUR_API_KEY"  # Replace with your working key

def analyze_resume(jd_text, resume_text):
    prompt = f"""
You are an AI assistant that helps HR screen resumes.

Given the job description and a resume, match the candidate's skills, qualifications, and experiences.

1. Extract keywords from the job description.
2. Compare the resume against those keywords.
3. Score relevance from 0 to 10.
4. List strengths and weaknesses.
5. Provide a short hiring recommendation.

--- Job Description ---
{jd_text}

--- Resume ---
{resume_text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response["choices"][0]["message"]["content"]

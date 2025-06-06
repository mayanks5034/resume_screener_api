from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from resume_matcher import analyze_resume

app = FastAPI()

class ResumeRequest(BaseModel):
    job_description: str
    resume_text: str

@app.post("/analyze_resume/")
def analyze(resume_req: ResumeRequest):
    try:
        result = analyze_resume(resume_req.job_description, resume_req.resume_text)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

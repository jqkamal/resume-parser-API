from fastapi import FastAPI, UploadFile, File
from parser import extract_resume_data
from models import ResumeData

app = FastAPI(title="Resume Parser API")

@app.post("/parse-resume", response_model=ResumeData)
async def parse_resume(file: UploadFile = File(...)):
    contents = await file.read()
    text = contents.decode("utf-8", errors="ignore")
    result = extract_resume_data(text)
    return result

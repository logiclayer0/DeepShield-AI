from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from engines.image_engine import process_image_ela
from engines.audio_engine import process_audio_analysis
from engines.video_engine import process_video_analysis

app = FastAPI(title="DeepShield AI - Cyber Forensics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "DeepShield AI Engine Running", "version": "1.0.0"}

@app.post("/analyze/image")
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    heatmap_bytes, auth_score = process_image_ela(image_bytes)
    status = "Authentic" if auth_score > 75 else "Manipulated / Forged"
    return {
        "filename": file.filename,
        "authenticity_score": auth_score,
        "status": status,
        "details": f"Analysis complete. Found forgery probability: {round(100 - auth_score, 2)}%"
    }

@app.post("/analyze/audio")
async def analyze_audio(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    auth_score, status = process_audio_analysis(audio_bytes)
    return {
        "filename": file.filename,
        "authenticity_score": auth_score,
        "status": status,
        "details": f"Audio processing complete. Classification: {status}"
    }

@app.post("/analyze/video")
async def analyze_video(file: UploadFile = File(...)):
    video_bytes = await file.read()
    auth_score, status = process_video_analysis(video_bytes)
    return {
        "filename": file.filename,
        "authenticity_score": auth_score,
        "status": status,
        "details": f"Video analysis complete. Frame temporal status: {status}"
    }
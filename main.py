from fastapi import FastAPI, UploadFile, File, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from audio_analysis import analyze_audio
from video_analysis import analyze_video
import shutil
import os
import uuid
import uvicorn

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # غيّرها لاحقًا للدومين فقط
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "API is running 🚀"}

# =========================
# 🎧 Analyze Audio
# =========================
@app.post("/analyze/audio")
async def analyze_audio_api(
    file: UploadFile = File(...),
    user_id: int | None = Header(default=None)  # تجهيز للعملات
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    temp_path = f"temp_audio_{uuid.uuid4()}{os.path.splitext(file.filename)[1]}"

    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 🔒 هنا لاحقًا:
        # check_user_coins(user_id, cost=10)
        # deduct_coins(user_id, 10)

        result, confidence = analyze_audio(temp_path)

        return {
            "type": "audio",
            "result": result,
            "confidence": confidence
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

# =========================
# 🎥 Analyze Video
# =========================
@app.post("/analyze/video")
async def analyze_video_api(
    file: UploadFile = File(...),
    user_id: int | None = Header(default=None)  # تجهيز للعملات
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    temp_path = f"temp_video_{uuid.uuid4()}{os.path.splitext(file.filename)[1]}"

    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 🔒 هنا لاحقًا:
        # check_user_coins(user_id, cost=10)
        # deduct_coins(user_id, 10)

        result, confidence = analyze_video(temp_path)

        return {
            "type": "video",
            "result": result,
            "confidence": confidence
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

# =========================
# ▶️ Run Server
# =========================
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        reload=False
    )
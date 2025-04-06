from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
import PyPDF2
from gtts import gTTS

app = FastAPI()

# Allow requests from any frontend (e.g. http://localhost:8080)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create audio directory if it doesn't exist
UPLOAD_DIR = "audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/convert")
async def convert_pdf_to_audio(file: UploadFile = File(...)):
    pdf_text = ""
    temp_file = f"temp_{uuid.uuid4()}.pdf"

    # Save uploaded PDF temporarily
    with open(temp_file, "wb") as f:
        f.write(await file.read())

    # Extract text from PDF
    try:
        with open(temp_file, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    pdf_text += text
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"PDF read error: {str(e)}"})
    finally:
        os.remove(temp_file)

    if not pdf_text.strip():
        return JSONResponse(status_code=400, content={"error": "No text found in the PDF."})

    # Convert text to audio
    audio_filename = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.mp3")
    try:
        tts = gTTS(text=pdf_text, lang='en')
        tts.save(audio_filename)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"TTS error: {str(e)}"})

    return {"audio_file": os.path.basename(audio_filename)}

@app.get("/audio/{filename}")
async def get_audio(filename: str):
    path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(path):
        return JSONResponse(status_code=404, content={"error": "File not found"})
    return FileResponse(path, media_type="audio/mpeg", filename=filename)

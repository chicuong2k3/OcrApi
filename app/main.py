
from fastapi import FastAPI, File, UploadFile, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil
from .ocr_script import run_ocr
import os

# Config
VALID_API_KEY = os.environ.get("VALID_API_KEY", "my-secret-api-key")  

app = FastAPI(
    title="OCR API",
    description="API for OCR using EasyOCR with API key protection",
    version="1.0.0",
    docs_url="/swagger",       
    redoc_url="/redoc"       
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Key dependency
async def verify_api_key(request: Request):
    api_key = request.headers.get("X-API-KEY")
    if not api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API Key missing")
    if api_key != VALID_API_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid API Key")

# OCR endpoint
@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...), request: Request = None):
    await verify_api_key(request)

    # Save uploaded file temporarily
    temp_file = Path(f"/tmp/{file.filename}")
    with temp_file.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run OCR
    result = run_ocr(str(temp_file))

    # Delete temp file
    temp_file.unlink(missing_ok=True)

    return JSONResponse(content={"text": result})

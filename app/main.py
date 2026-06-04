from fastapi import FastAPI, UploadFile, File

from app.processing import process_csv
from app.db import save_report

app = FastAPI()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    result = process_csv(file.file)

    save_report(file.filename, result)

    return result
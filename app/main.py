from fastapi import FastAPI, UploadFile, File
from app.processing import process_csv

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Cloud Native Data Platform"}


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):

    result = process_csv(file.file)

    return result
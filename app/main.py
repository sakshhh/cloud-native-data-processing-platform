from fastapi import FastAPI, UploadFile, File

from app.processing import process_csv
from app.db import save_report
from contextlib import asynccontextmanager

from app.init_db import create_table

from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter

@asynccontextmanager

async def lifespan(app):

    create_table()

    yield

app = FastAPI(lifespan=lifespan)

Instrumentator().instrument(app).expose(app)

files_uploaded_total = Counter(
    "files_uploaded_total",
    "Total number of uploaded files"
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    result = process_csv(file.file)
    files_uploaded_total.inc()

    save_report(file.filename, result)

    return result
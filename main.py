from fastapi import FastAPI
from backend.api.v1.api import api_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Argus", version="0.0.1")

app.include_router(api_router, prefix="/api/v1")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@app.get("/")
def read_root():
    return {"message": "Hello From FastAPI from NVIM..."}

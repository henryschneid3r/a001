from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse
from backend.api.v1.api import api_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Argus", version="0.0.1")

app.include_router(api_router, prefix="/api/v1")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@app.get("/")
def read_root(request: Request):
    login_url = request.url_for("login")
    return RedirectResponse(url=login_url, status_code=status.HTTP_303_SEE_OTHER)

from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
TEMPLATES_DIR = BASE_DIR / "frontend" / "templates"


templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@router.get("/", name="login")
def login_page(request: Request):
    return templates.TemplateResponse(request, "pages/login.html", {"title": "Login"})


@router.post("/")
async def login_submit(request: Request):

    # deal with the request here
    form_data = await request.form()
    email = form_data.get("email")

    return "success"

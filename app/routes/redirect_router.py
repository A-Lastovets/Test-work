from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

redirect_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@redirect_router.get("/", include_in_schema=False)
def redirect_root(request: Request):
    return templates.TemplateResponse("redirect.html", {"request": request})

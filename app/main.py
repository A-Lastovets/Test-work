from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(router, prefix="/api/book")

app.mount("/static", StaticFiles(directory="static"), name="static")

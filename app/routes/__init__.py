from fastapi import APIRouter
from app.routes.book_routes import router as book_router
from app.routes.redirect_router import redirect_router

router = APIRouter()
router.include_router(redirect_router)
router.include_router(book_router, prefix="/api/book")
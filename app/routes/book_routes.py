from fastapi import APIRouter, Request, Form, Depends, Query
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_books, add_book, delete_book
from fastapi.templating import Jinja2Templates
from typing import Optional, Union
from decimal import Decimal

router = APIRouter()

BOOK_TAGS = ["Books"]

templates = Jinja2Templates(directory="templates")


@router.get("", tags=BOOK_TAGS)
def read_books(
    request: Request,
    year: Optional[Union[int, str]] = Query(None),
    author: Optional[str] = Query(None),
    price: Optional[Union[Decimal, str]] = Query(None),
    db: Session = Depends(get_db)
):
    filters = {}

    if year not in (None, ""):
        filters["year"] = int(year)
    if author not in (None, ""):
        filters["author"] = author
    if price not in (None, ""):
        filters["price"] = Decimal(price)

    books = get_books(db, filters)

    has_filters = any([
        year not in (None, ""),
        author not in (None, ""),
        price not in (None, "")
    ])

    return templates.TemplateResponse("index.html", {
        "request": request,
        "books": books,
        "filters": {"year": year, "author": author, "price": price},
        "has_filters": has_filters
    })

@router.post("", tags=BOOK_TAGS)
def create_book(
    name: str = Form(...),
    year: int = Form(...),
    author: str = Form(...),
    price: float = Form(...),
    db: Session = Depends(get_db)
):
    add_book(db, {"name": name, "year": year, "author": author, "price": price})
    return RedirectResponse("/", status_code=303)

@router.delete("/{book_id}", tags=BOOK_TAGS)
def remove_book(book_id: int, db: Session = Depends(get_db)):
    delete_book(db, book_id)
    return RedirectResponse("/", status_code=303)

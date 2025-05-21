from sqlalchemy.orm import Session
from .models import Book

def get_books(db: Session, filters: dict = {}):
    query = db.query(Book)
    if filters.get("year"):
        query = query.filter(Book.year == filters["year"])
    if filters.get("author"):
        query = query.filter(Book.author == filters["author"])
    if filters.get("price"):
        query = query.filter(Book.price == filters["price"])
    return query.all()

def add_book(db: Session, data: dict):
    book = Book(**data)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).get(book_id)
    if book:
        db.delete(book)
        db.commit()

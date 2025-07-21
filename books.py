"""
HTTP Request Methods
GET : Read Resource
POST : Create Resource
Put : Update /Replace Resource
Delete : Delete Resource

CRUD Create Read Update Delete
"""
from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel, Field
from uuid import UUID
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind = engine)
app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

BOOKS = []
@app.get("/books")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Books).all()

@app.post("/books")
def create_book(book:Book,db: Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db.add(book_model)
    db.commit()

    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)):

    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} : Does not exist"
        )
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    # db.add(book_model)
    db.commit()

    return book

@app.delete("/books/{book_id}")
def delete_book(book_id:int, db: Session = Depends(get_db)):

    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:

        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} : Does not exist"
        )
    db.query(models.Books).filter(models.Books.id == book_id).delete()

    db.commit()
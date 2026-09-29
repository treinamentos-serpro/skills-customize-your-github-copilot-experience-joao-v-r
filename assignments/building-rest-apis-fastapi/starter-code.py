from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Book API")

books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "price": 29.99},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho", "price": 39.99},
]


class Book(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Encontre o livro pelo id e retorne o item correspondente
    # Se não encontrar, retorne um erro 404
    pass


@app.post("/books", status_code=201)
def create_book(book: Book):
    # Crie um novo objeto com id incremental, adicione à lista e retorne o livro
    pass

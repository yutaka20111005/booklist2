from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "Booklist by FastAPI"}

@app.get("/books/{book_id}")
def read_book(book_id: int, q: Union[str, None] = None):
  return {"book_id": book_id, "q": q}

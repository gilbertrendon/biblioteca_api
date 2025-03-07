
from  models import Book
# from . import schemas, models
# from sqlalchemy.orm import Session
# Depends, HTTPException, status, APIRouter, Response, 
from fastapi import FastAPI   
# from .database import get_db
# librotest = Book()
app = FastAPI()
db = Book()

db.createTable()
#http://127.0.0.1:8000
@app.get("/{id}")
def index(id:int):
    libro = db.get_book(id)
    return {'status': 'success', 'libro': libro}

@app.post("/libro")
def create(bk:dict):
    libro = Book()
    libro.autor = bk["autor"]
    libro.title = bk["title"]
    libro.year = bk["year"]
    libro.isbn = bk["isbn"]
    Book.create_book(libro) 
    return "creado"

@app.post("/ulibro")
def create(bk:dict):
    libro = Book()
    libro.id = bk["id"]
    libro.autor = bk["autor"]
    libro.title = bk["title"]
    libro.year = bk["year"]
    libro.isbn = bk["isbn"]
    Book.update_book(libro) 
    return "actualizado"


# if __name__ == '__main__':
#     pass


from  models import Book
# from . import schemas, models
# from sqlalchemy.orm import Session
# Depends, HTTPException, status, APIRouter, Response, 
from fastapi import FastAPI   
# from .database import get_db
# librotest = Book()
app = FastAPI()
lib = Book(
    title="Harry potter y el caliz de fuego",
    autor="Jk rowling",
    year="2019-12-04",
    isbn="e5d4"
    )
lib.createTable()
lib.create_book(lib)    
#http://127.0.0.1:8000
@app.get("/")
def index():
    libro = lib.get_book(1)
    return {'status': 'success', 'libro': libro}


# if __name__ == '__main__':
#     pass

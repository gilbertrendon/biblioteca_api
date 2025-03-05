from fastapi import FastAPI
from  models.libro import Book

# librotest = Book()
app = FastAPI()

#http://127.0.0.1:8000
@app.get("/")
def index():
    return "hola asdfasdasdf"


if __name__ == '__main__':
    pass

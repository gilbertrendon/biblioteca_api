import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
# Definir una URL para una base de datos de prueba en memoria
from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models import Book
#  Cambia esto por la URL de tu base de datos
TEST_DATABASE_URL = 'postgresql://postgres:1234@localhost:5432/asdf'


# Crea el motor de la base de datos
engine = create_engine(TEST_DATABASE_URL, pool_pre_ping=True)

# Define la base para modelos declarativos
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
# Define tu modelo de datos
# class Book(Base):
#     __tablename__ = "books"

#     id = Column(Integer(), primary_key=True)
#     title = Column(String(50), nullable=True, unique=False)
#     autor = Column(String(50), nullable=True, unique=False)
#     isbn = Column(String(50), nullable=True, unique=False)
    
#     def __str__(self):
#         return f"Libro: {self.title} por {self.autor}" # Corregido
    
#     @staticmethod
#     def createTable():
#         Base.metadata.drop_all(engine)
#         Base.metadata.create_all(engine)




@pytest.fixture(scope='session')
def session():
    """Crea una sesión de base de datos para pruebas."""
    engine = create_engine(TEST_DATABASE_URL)
    Base = declarative_base()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
   
    

def test_create_table():
    """Prueba si la tabla de libros es creada correctamente."""
    book = Book()
    book.createTable()
    # book = Book(title="Test Title", autor="Test Author", isbn='123-456-789')
    # session.add(book)

def test_create_book(session):
    """Prueba si la tabla de libros es creada correctamente."""
    lib = Book(
        title="Harry potter y el caliz de qwer",
        autor="Jk asdf",
        year="2019-12-05",
        isbn="e5d4"
        )
    
    lib.create_book(lib)
    
#     # Verifica si la tabla fue creada comprobando si puedes consultar datos
    retrieved_book = session.query(Book).filter(Book.title == "Harry potter y el caliz de qwer").first()
    assert retrieved_book is not None
    assert retrieved_book.autor == "Jk asdf"
    assert retrieved_book.isbn == 'e5d4'
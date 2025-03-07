import pytest
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.models import Book
# Definir una URL para una base de datos de prueba en memoria
TEST_DATABASE_URL = 'postgresql://postgres:1234@localhost:5432/qwer'

# Obten el directorio que contiene el script actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obten el directorio padre
parent_dir = os.path.dirname(current_dir)

# Añade el directorio padre al path
sys.path.append(parent_dir)

@pytest.fixture(scope='session')
def session():
    """Crea una sesión de base de datos para pruebas."""
    engine = create_engine(TEST_DATABASE_URL)
    Base = declarative_base()
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)
    

def test_create_table(session):
    """Prueba si la tabla de libros es creada correctamente."""
    
    book = Book(title="Test Title", autor="Test Author", year=2023, isbn='123-456-789')
    session.add(book)
    session.commit()
    
    # Verifica si la tabla fue creada comprobando si puedes consultar datos
    retrieved_book = session.query(Book).filter(Book.title == "Test Title").first()
    assert retrieved_book is not None
    assert retrieved_book.autor == "Test Author"
    assert retrieved_book.year == 2023
    assert retrieved_book.isbn == '123-456-789'
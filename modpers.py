from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
#  Cambia esto por la URL de tu base de datos
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/asdf"

# Crea el motor de la base de datos
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Define la base para modelos declarativos
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
# Define tu modelo de datos
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=True, unique=False)
    autor = Column(String(50), nullable=True, unique=False)
    year = Column(DateTime(), default=datetime.now())
    isbn = Column(String(50), nullable=True, unique=False)
    
    def __str__(self):
        return self.title
    
        
    @staticmethod
    def createTable(testengine):
        # se borra la tabla por si existe 
        Base.metadata.drop_all(testengine)
        # Crea las tablas
        Base.metadata.create_all(testengine)
        # session.commit()
        # session.close()
        
    @staticmethod
    def create_book(lb):
        session.add(lb)
    
    @staticmethod
    def delete_book(idb):
        book_to_delete = session.query(Book).filter_by(id=idb).first()
        session.delete(book_to_delete)

    @staticmethod
    def get_book(idb):
        book= session.query(Book).filter_by(id=idb).first()
        print(book)
        return book
        
    @staticmethod
    def update_book(book):
        book_to_update = session.query(Book).filter_by(id=book.id).first()
        book_to_update.title = book.title
        book_to_update.author = book.autor
        book_to_update.year = book.year
        book_to_update.isbn = book.isbn
        session.add(book_to_update)
        session.commit()
        
if __name__ == '__main__':
        lib = Book(
        title="Harry potter y el caliz de fuego",
        autor="Jk rowling",
        year="2019-12-04",
        isbn="e5d4"
        )
    
        # SessionLocal = sessionmaker(bind=engine)
        # session = SessionLocal()
        # CREAR TABLA
        # lib.createTable(engine)
        # INSERTAR UN LIBRO
        # lib.create_book(lib)
        # BORRAR UN LIBRO
        # lib.delete_book(1)
        # CONSULTAR UN LIBRO POR ID
        # lib.get_book(2)
        # ACTUALIZAR UN LIBRO
        libro = lib.get_book(2)

    # MODIFICAR LOS ATRIBUTOS
        libro.title = 'Harry Potter y el cáliz de fuego'
        libro.autor = 'Jk Rowling2'
        libro.year = '2023-11-04'
        libro.isbn = 'isbn2'
        lib.update_book(libro)
        
        session.commit()
        session.close()  
  
    

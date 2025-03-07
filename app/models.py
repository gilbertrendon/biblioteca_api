from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String, DateTime
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
        return f"Libro: {self.title} por {self.autor} ({self.year})" # Corregido
    
        
    @staticmethod
    def createTable():
        # se borra la tabla por si existe 
        Base.metadata.drop_all(engine)
        # Crea las tablas
        Base.metadata.create_all(engine)
        session.commit()
        session.close()
        
    @staticmethod
    def create_book(lb):
        print("*************************************************")
        print(str(lb))
        session.add(lb)
        session.commit()
        session.close() 
    
    @staticmethod
    def delete_book(idb):
        book_to_delete = session.query(Book).filter_by(id=idb).first()
        session.delete(book_to_delete)
        session.commit()
        session.close() 

    @staticmethod
    def get_book(idb):
        book= session.query(Book).filter_by(id=idb).first()
        print(book)
        session.commit()
        # session.close()
        return {'status': 'success', 'libro': {
        'title': book.title,
        'author': book.autor,
        'year': book.year,
        'isbn': book.isbn
    }}
        
        
    @staticmethod
    def update_book(book):
        book_to_update = session.query(Book).filter_by(id=book.id).first()
        book_to_update.title = book.title
        book_to_update.author = book.autor
        book_to_update.year = book.year
        book_to_update.isbn = book.isbn
        session.add(book_to_update)
        session.commit()
        session.close()  
        
  
    

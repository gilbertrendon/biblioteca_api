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
    def createTable(asdf):
        SessionLocal = sessionmaker(bind=asdf)
        session = SessionLocal()
        # se borra la tabla por si existe 
        Base.metadata.drop_all(engine)
        # Crea las tablas
        Base.metadata.create_all(engine)
        session.commit()
        session.close()  


if __name__ == '__main__':
        lib = Book()
        lib.createTable(engine)
       
  
    

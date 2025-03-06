from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#  Cambia esto por la URL de tu base de datos
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/asdf"

# Crea el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Define la base para modelos declarativos
Base = declarative_base()

# Define tu modelo de datos
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    
# Crea las tablas
Base.metadata.create_all(engine)

# Crea una sesión (opcional, pero útil para interactuar con la DB)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


# Puedes realizar operaciones en la base de datos aquí (ej: agregar registros)

# Cierra la sesión cuando termines
session.close()
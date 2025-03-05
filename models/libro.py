from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
Base = declarative_base
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=True, unique=False)
    autor = Column(String(50), nullable=True, unique=False)
    year = Column(DateTime(), default=datetime.now())
    isbn = Column(String(50), nullable=True, unique=False)

    def __init__(self, id):
        self.id = id

    def title(self, title):
        self.title = title

    def autor(self, autor):
        self.autor = autor
    
    def year(self, year):
        self.year = year
    
    def isbn(self, isbn):
        self.isbn = isbn
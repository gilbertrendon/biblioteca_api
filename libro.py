from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:@serverOne/databaseOne')
class Book(engine):
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
Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    # Base.metada.drop_all(engine)
    # Base.metadata.create_all(engine)
    pass
from sqlalchemy.ext.declarative import declarative_base


class Book:
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
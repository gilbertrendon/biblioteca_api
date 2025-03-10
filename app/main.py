from  models import Book


if __name__ == '__main__':
        lib = Book(
        title="Harry potter y el caliz de iopiuopiopio",
        autor="Jkioupopuopiuoupop",
        year="2019-12-05",
        isbn="e5d4"
        )
    
        # SessionLocal = sessionmaker(bind=engine)
        # session = SessionLocal()
        # CREAR TABLA
        # lib.createTable()
        # INSERTAR UN LIBRO
        # lib.create_book(lib)
        # BORRAR UN LIBRO
        # lib.delete_book(1)
        # CONSULTAR UN LIBRO POR ID
        # lib.get_book(2)
        # ACTUALIZAR UN LIBRO
        # libro = lib.get_book(2)
        # libro.title = 'Harry Potter y el cáliz de fuego'
        # libro.autor = 'Jk Rowling7'
        # libro.year = '2023-11-04'
        # libro.isbn = 'isbn2'
        # lib.update_book(libro)
        asdf = lib.get_books_by_year('2019-12-05')
        # asdf = lib.get_books_by_author_and_year(author='Jkioupopuopiuoupop',year='2019-12-05')

        print(asdf)
        # session.commit()
        # session.close()  
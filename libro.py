from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine, MetaData
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import url, URL
from sqlalchemy import text

Base = declarative_base()

db_url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="1234",
    host="localhost",
    port=5432,
    database="asdf"
)

engine = create_engine(db_url,  connect_args={"options": "-c search_path=path"})
Session = sessionmaker(bind=engine)
session = Session()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=True, unique=False)
    autor = Column(String(50), nullable=True, unique=False)
    year = Column(DateTime(), default=datetime.now())
    isbn = Column(String(50), nullable=True, unique=False)




if __name__ == '__main__':
   try:
      metadata = MetaData()
    #   metadata.drop_all(engine)
    #   metadata.create_all(engine)
      print("metadata.create_all ejecutado")
      with sessionmaker(bind=engine)() as session:
          metadata.create_all(engine)
    #       session.execute(text("drop table if exists book"))
    #       session.execute(text('''
    #             CREATE TABLE BOOK (
    #             BID integer NOT NULL UNIQUE,
    #             TITLE varchar(40),
    #             AUTOR varchar(20),
    #             PUBYEAR varchar(20),
    #             ISBN varchar(20)
    #             )
    #   '''))
    #       session.execute(text('''
    #                            INSERT INTO BOOK VALUES (
    #                                4321,
    #                                'El señor de los anillos', 
    #                                'Joey',
    #                                '2000', 
    #                                '1234a')'''
    #                             ))
        #   session.execute(text(
        #                 '''
        #             UPDATE BOOK
        #             SET TITLE = 'El señor de los anillos', 
        #             AUTOR = "Joey",
        #             PUBYEAR = "2001",
        #             ISBN = "Joeyy"
        #             WHERE BID = 456789;
        #             '''
        #   ))
          
      session.commit()

   except UnicodeTranslateError as e:
           print(f"Error al crear las tablas: {e.reason}")
   except Exception as e:
       print(f"Error al crear las tablas: {str(e)}")
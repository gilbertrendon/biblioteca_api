import sqlite3

# establishing  a database connection asdfg
con = sqlite3.connect('D:\\TEST.db')
# preparing a cursor object
cursor = con.cursor()
# preparing sql statements
sql1 = 'DROP TABLE IF EXISTS BOOK'

sql2 = '''

       CREATE TABLE BOOK (
       BID INT(6) NOT NULL UNIQUE,
       TITLE varchar(20),
       AUTOR varchar(20),
       PUBYEAR varchar(20),
       ISBN varchar(20)
       )
      '''

# executing sql statements
cursor.execute(sql1)
cursor.execute(sql2)


# AGREGAR LIBRO
rec = (456789, 'El señor de los anillos', "Joey", '2000', "1234a")
sql = '''
      INSERT INTO BOOK VALUES ( ?, ?, ?, ?, ?)
      '''

try:

    cursor.execute(sql, rec)

    con.commit()

except Exception as e:

    print("Error Message :", str(e))

# ACTUALIZAR INFORMACIÓN DE UN LIBRO
sql = '''
     UPDATE BOOK
     SET TITLE = 'El señor de los anillos', 
     AUTOR = "Joey",
     PUBYEAR = "2001",
     ISBN = "Joeyy"
     WHERE BID == 456789;
      '''
try:

    cursor.execute(sql)

    con.commit()

except Exception as e:

    print("Error Message :", str(e))

# LISTAR LIBROS
sql = '''
       SELECT * FROM BOOK
      '''
try:
    cursor.execute(sql)
except  Exception as e:
    print('Unable to fetch data.', str(e))

# ELIMINAR LIBRO
sql = '''
       DELETE FROM BOOK WHERE BID == 456789;
      '''
try:
    cursor.execute(sql)
except  Exception as e:
    print('Unable to fetch data.', str(e))



records44 = cursor.fetchall()
print(records44)




#     con.rollback()

# records = [

#     (123456, 'John', 25, 'M', 50000.00),

#     (234651, 'Juli', 35, 'F', 75000.00),

#     (345121, 'Fred', 48, 'M', 125000.00),

#     (562412, 'Rosy', 28, 'F', 52000.00)

#     ]

# sql = '''

#        INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)

#       '''
# try:

#     cursor.executemany(sql, records)

#     con.commit()

# except Exception as e:

#     print("Error Message :", str(e))

#     con.rollback()

# sql = '''
#        SELECT * FROM EMPLOYEE
#       '''
# try:
#     cursor.execute(sql)
# except  Exception as e:
#     print('Unable to fetch data.', str(e))

# records = cursor.fetchall()

# sql44 = '''
#         SELECT * FROM EMPLOYEE 
#         '''
# try:
#     cursor.execute(sql44)
# except  Exception as e:
#     print('Unable to fetch data.', str(e))

# records44 = cursor.fetchall()
# print(records44)
con.close()
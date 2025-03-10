ENDPOINTS

PARA PROBAR CON SWAGER
http://127.0.0.1:8000/docs

obtenerlibro
http://127.0.0.1:8000/1

deletelibro
http://127.0.0.1:8000/1

createLibro
http://127.0.0.1:8000/libro

{
    "title": "Harry puerco y el caliz de fuegoasdfasd",
    "autor": "Jk rowlinaagaasdfasdfsadf",
    "year": "2019-12-05",
    "isbn": "e5d4aaa"
}

updateLibro
http://127.0.0.1:8000/ulibro
{
    "id": 1,
    "title": "Harry puerco y el caliz de fuegoasdfasd",
    "autor": "Jk rowlinaagaasdfasdfsadf",
    "year": "2019-12-05",
    "isbn": "e5d4aaa"
}

Para la instalación de pgadmin se instaló postgresqlcompleto

PARA MIRAR LAS TABLAS EN LA BD

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'; -- O el esquema que estés usando

Para ejecutar fastapi
uvicorn schemas:app --reload

 ¿Cómo manejarías la autenticación y autorización en la API?
Se pueden usar apis o servicios que usen tokens para mayor seguridad.
 ¿Qué estrategias utilizarías para escalar la aplicación?
Crear algo similar a las migraciones que se usan en otras tecnologías.
 ¿Cómo implementarías la paginación en los endpoints que devuelven listas
de libros?
 ¿Cómo asegurarías la seguridad de la aplicación (protección contra
inyecciones SQL, XSS, etc.)?
Evitar enviar datos por la url, como lo hago por ejemplo en la creación y el update 


REFERENCIAS:
https://www.youtube.com/watch?v=J0y2tjBz2Ao
Tuto entorno virtual

https://www.youtube.com/watch?v=XSAjQDM8ZS4
Creacion de tabla en el modelo con alchemy

https://www.youtube.com/watch?v=I8WTQGUUYHo
docker 

PRUEBAS UNITARIAS
parado en la carpeta app
pytest tests

Falta:
 Listar libros: Todos los libros o filtrados por autor o año.
Buscar libros por título o autor.
Pytest: Framework de pruebas unitarias y de integración.
        o Cobertura de código con pruebas unitarias y de integración.
        o Pruebas de los endpoints de la API.
        o Pruebas de la base de datos.
Docker: Para contenerizar la aplicación (opcional, pero recomendado).





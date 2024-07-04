import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "andymanuelreyes11",
    "database": "sakila"
}


# metodo para establecer la conexion a la base de datos

def get_connection() -> mysql.connector.MySQLConnection:
    return mysql.connector.connect(**config)  # type: ignore

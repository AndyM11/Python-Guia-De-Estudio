import mysql.connector as mysql

config = {
    # leer archivo de configuracion
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "sakila",
}


def get_client() -> mysql.MySQLConnection | None:
    try:
        print("Connecting to MySQL platform...")  # conexion a la base
        return mysql.connect(**config)  # conexion a la base de datos
    except mysql.Error as e:
        print(f"Error connecting to MySQL platform: {e}")  # error de conexion
        return None

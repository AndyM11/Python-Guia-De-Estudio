from typing import Any
from database import client
import prettytable as pt


get_client = client.get_client


def execute_query(query: str) -> list[dict[Any, Any]]:
    client = get_client()
    if client is not None:
        cursor = client.cursor(dictionary=True)
    else:
        # Handle the case when client is None
        # You can raise an exception, return a default value, or take any other appropriate action
        raise Exception("Client is None")
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    client.close()
    return [dict(row) for row in result]


# print(execute_query("SELECT actor_id, first_name, last_name FROM actor_info"))

table = pt.PrettyTable()  # Crear tabla

table.field_names = ["ID", "Nombre", "Aoellido"]  # Crear encabezado

for row in execute_query(
    "SELECT actor_id, first_name, last_name FROM actor_info"
):  # Recorrer la lista de actores
    table.add_row(
        [row["actor_id"], row["first_name"], row["last_name"]]
    )  # Agregar fila a la tabla

print(table)

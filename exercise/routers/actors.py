from fastapi import APIRouter
from db import client

router = APIRouter(prefix="/actors",
                   tags=["actors"],
                   responses={404: {"message": "Not found"}})


# conecta a la base de datos sakila y consultar la tabla actor.
def get_actors():
    connection = client.get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM actor_info")
    actors = cursor.fetchall()
    cursor.close()
    connection.close()
    return actors


@router.get("/")
async def actors():
    # conviente resultados de get_actors a un diccionario y retornar el resultado.
    actors: dict = get_actors()
    return actors


@router.get("/{id}")
async def actor(id: int):
    actors: dict = get_actors()
    return actors[id]

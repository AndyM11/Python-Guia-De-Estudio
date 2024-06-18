from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Inicializamos el server con el comando uvicorn users:router --reload

# Enttidad user


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [
    User(id=1, name="Andy", surname="Reyes", url="https://areyes.dev", age=25),
    User(id=2, name="MoureDev", surname="Developer",
         url="https://mouredev.com", age=35),
    User(id=3, name="Haakon", surname="Dahlberg",
         url="https://haakon.com", age=20)
]


@router.get("/usersjson")
async def usersjson():
    return [
        {"name": "Andy", "surname": "Reyes", "url": "https://areyes.dev", "age": 25},
        {"name": "MoureDev", "surname": "Developer",
            "url": "https://mouredev.com", "age": 35},
        {"name": "Haakon", "surname": "Dahlberg",
            "url": "https://haakon.com", "age": 20}
    ]


@router.get("/users")
async def users():
    return users_list

# Path


@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query


@router.get("/user/")
async def userquery(id: int):
    return search_user(id)

# Post


@router.post("/user/", response_model=User, status_code=201)
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
        # return {"error": "El usuario ya existe"}
    else:
        users_list.routerend(user)
        return user

# Put


@router.put("/user/")
async def update_user(user: User):

    found: bool = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user

# Delete


@router.delete("/user/{id}")
async def delete_user(id: int):
    found: bool = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}
    else:
        return {"message": "Usuario eliminado"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"message": "Usuario no encontrado"}

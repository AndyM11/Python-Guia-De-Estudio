from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

router = APIRouter(
    prefix="/userdb",
    tags=["userdb"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}}
)


@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

# Path


@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))

    # Query


@router.get("/")
async def userquery(id: str):
    return search_user("_id", ObjectId(id))

    # Post


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El usuario ya existe")
    user_dict = dict(user)  # Convertir a diccionario.
    # Eliminar el id para que MongoDB lo genere automáticamente.
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = db_client.users.find_one({"_id": id})
    if new_user is not None:
        new_user = user_schema(new_user)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")

    return User(**new_user)

# Put


@router.put("/", response_model=User)
async def update_user(updated_user: User):
    user_dict = dict(updated_user)
    del user_dict["id"]
    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(updated_user.id)}, user_dict)
    except Exception as e:
        return {"error": f"No se ha actualizado el usuario: {str(e)}"}
    return search_user("_id", ObjectId(updated_user.id))

# Delete


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):

    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(field: str, key):
    user = db_client.users.find_one({field: key})
    if user is None:
        return {"message": "Usuario no encontrado"}
    else:
        user = user_schema(user)
        return User(**user)

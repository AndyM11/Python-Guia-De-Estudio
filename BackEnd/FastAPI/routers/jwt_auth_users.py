from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "password": "$2a$12$/Zlo5cM6RYwej2OR1hvvcOdzIyv3kTDdv9jVdHOREYidT4sBFbg/."
    },
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndo@email.com",
        "disabled": True,
        "password": "$2a$12$x3GRC68LHTmm5yPvj9Gy6OgOgBM/ei5tuRBTRJm9swei.PyzZ2RAO"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Credenciales de autenticacion invalidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(  # Si no lo encuentra, lanza una excepcion
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user  # Si lo encuentra, retorna el usuario


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=400, detail="El usuario no es correcto")

    user = search_user_db(form .username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=400, detail="La contraseña no es correcta")

    access_token = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION),
    }

    access_token_encoded = jwt.encode(
        access_token, key=SECRET, algorithm=ALGORITHM)
    return {
        "access_token": access_token_encoded,
        "token_type": "bearer"
    }


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

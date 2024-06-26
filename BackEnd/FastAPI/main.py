from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# unicorn main:app --reload

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)


@app.get("/")
async def root():
    return "Hola FastAPI!"


@app.get("/url")
async def root():
    return {"url_curso": "https://mouredev.com/python"}

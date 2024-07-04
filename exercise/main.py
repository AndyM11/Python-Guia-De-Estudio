import fastapi as FastAPI
from routers import actors

app = FastAPI.FastAPI()

# unicorn main:app --reload

# Routers
app.include_router(actors.router)


@app.get("/")
async def root():
    return "Hola FastAPI!"

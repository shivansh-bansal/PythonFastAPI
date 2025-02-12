import models
from fastapi import FastAPI
from database import engine
from Routers import todos, auth

app = FastAPI()

# Only creates the database if it does not exist. Does not modifies the database when schema is changed.
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
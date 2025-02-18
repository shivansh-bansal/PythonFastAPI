from models import Todos
from starlette import status
from typing import Annotated
from Routers.TodoRequest import *
from database import SessionLocal
from sqlalchemy.orm import Session
from Routers.auth import getUser
from fastapi import APIRouter, Depends, HTTPException, Path

router = APIRouter()

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

dbDependency = Annotated[Session, Depends(getDB)]
userDependency = Annotated[dict, Depends(getUser)]

@router.get("/", status_code=status.HTTP_200_OK)
async def getAllTodos(user: userDependency, db: dbDependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    
    return db.query(Todos).filter(user.get("userID") == Todos.ownerID).all()


@router.get("/todo/{todoID}", status_code=status.HTTP_200_OK)
async def getTodoByID(user: userDependency, db: dbDependency, todoID: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    
    todo =  db.query(Todos).filter(Todos.id == todoID).filter(user.get("userID") == Todos.ownerID).first()
    if todo is not None:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found!")


@router.put("/todo/{todoID}", status_code=status.HTTP_204_NO_CONTENT)
async def updateTodo(user: userDependency, db: dbDependency, todoRequested: TodoRequest, todoID: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    
    todo = db.query(Todos).filter(Todos.id == todoID).filter(user.get("userID") == Todos.ownerID).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found!")
    todo.title = todoRequested.Title
    todo.description = todoRequested.Description
    todo.priority = todoRequested.Priority
    todo.complete = todoRequested.Complete
    db.add(todo)
    db.commit()


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def createTodo(user: userDependency, db: dbDependency, todoRequested: TodoRequest):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")
    todo = Todos(**todoRequested.model_dump(), ownerId=user.get("userID"))
    db.add(todo)
    db.commit()


@router.delete("/todo/{todoID}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteTodo(user: userDependency, db: dbDependency, todoID: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")

    todo = db.query(Todos).filter(Todos.id == todoID).filter(user.get("userID") == Todos.ownerID).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found!")
    db.delete(todo)
    db.commit()
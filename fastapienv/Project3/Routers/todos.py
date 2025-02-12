from models import Todos
from starlette import status
from typing import Annotated
from Routers.TodoRequest import *
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path

router = APIRouter()

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

dbDependency = Annotated[Session, Depends(getDB)]


@router.get("/", status_code=status.HTTP_200_OK)
async def getAllTodos(db: dbDependency):
    return db.query(Todos).all()


@router.get("/todo/{todoID}", status_code=status.HTTP_200_OK)
async def getTodoByID(db: dbDependency, todoID: int = Path(gt=0)):
    todo =  db.query(Todos).filter(Todos.id == todoID).first()
    if todo is not None:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found!")


@router.put("/todo/{todoID}", status_code=status.HTTP_204_NO_CONTENT)
async def updateTodo(db: dbDependency, todoRequested: TodoRequest, todoID: int = Path(gt=0)):
    todo = db.query(Todos).filter(Todos.id == todoID).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found!")
    todo.title = todoRequested.Title
    todo.description = todoRequested.Description
    todo.priority = todoRequested.Priority
    todo.complete = todoRequested.Complete
    db.add(todo)
    db.commit()


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def createTodo(db: dbDependency, todoRequested: TodoRequest):
    db.add(Todos(**todoRequested.model_dump()))
    db.commit()


@router.delete("/todo/{todoID}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteTodo(db: dbDependency, todoID: int = Path(gt=0)):
    todo = db.query(Todos).filter(Todos.id == todoID).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found!")
    db.delete(todo)
    db.commit()
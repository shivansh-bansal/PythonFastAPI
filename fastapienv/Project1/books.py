from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title" : "Title 1",
    "Author" : "Author 1"},
    {"title" : "Title 2",
    "Author" : "Author 2"},
]
@app.get("/books")
async def getAllBooks():
    return BOOKS
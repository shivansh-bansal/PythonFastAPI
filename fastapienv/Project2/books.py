from Book import *
from BookRequest import *
from fastapi import FastAPI, Path, Query, HTTPException
from starlette import status

app = FastAPI()


BOOKS =[
    Book(1, "CS", "Shivansh", "Nice Book", 2014, 5),
    Book(2, "Book1", "Author 1", "Book Description", 2015, 3),
    Book(3, "Book2", "Author 2", "Book Description", 2016, 4),
    Book(4, "Book3", "Author 3", "Book Description", 2014, 1),
]

@app.get("/books", status_code = status.HTTP_200_OK)
async def getAllBooks():
    return BOOKS

@app.get("/books/{bookID}", status_code = status.HTTP_200_OK)
async def getBookByID(bookID: int = Path(gt = 0)):
    for book in BOOKS:
        if book.id == bookID:
            return book
    raise HTTPException(status_code = 404, detail = "Book not found")

@app.get("/books/", status_code = status.HTTP_200_OK)
async def getBookByRating(rating: int = Query(gt = 0, lt = 6)):
    books = []
    for book in BOOKS:
        if book.rating == rating:
            books.append(book)
    return books

# ASSIGNMENT
@app.get("/books/publish/", status_code = status.HTTP_200_OK)
async def getBookByDate(date: int = Query(gt = 1999, lt = 2026)):
    books = []
    for book in BOOKS:
        if book.publishedDate == date:
            books.append(book)
    return books

@app.post("/createBook", status_code = status.HTTP_201_CREATED)
async def createBooks(requestedBook: BookRequest):
    newBook = Book(**requestedBook.model_dump())
    BOOKS.append(findBookID(newBook))

@app.put("/books/updateBook" , status_code = status.HTTP_204_NO_CONTENT)
async def updateBook(requestedBook: BookRequest):
    changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == requestedBook.id:
            changed = True
            BOOKS[i] = Book(**requestedBook.model_dump())
    if not changed:
        raise HTTPException(status_code = 404, detail = "Book not found")

@app.delete("/books/{bookID}", status_code = status.HTTP_204_NO_CONTENT)
async def deleteBookByID(bookID: int = Path(gt = 0)):
    deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == bookID:
            deleted = True
            BOOKS.pop(i)
            break
    if not deleted:
        raise HTTPException(status_code = 404, detail = "Book not found")

def findBookID(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
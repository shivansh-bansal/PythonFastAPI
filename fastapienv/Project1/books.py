from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title" : "Title 1", "author" : "Author 1", "category" : "science"},
    {"title" : "Title 2", "author" : "Author 2", "category" : "science"},
    {"title" : "Title 3", "author" : "Author 3", "category" : "history"},
    {"title" : "Title 4", "author" : "Author 4", "category" : "math"},
    {"title" : "Title 5", "author" : "Author 5", "category" : "math"},
    {"title" : "Title 6", "author" : "Author 2", "category" : "math"},
]

@app.get("/books")
async def getAllBooks():
    return BOOKS

@app.get("/books/{bookTitle}")
async def getBookByTitle(bookTitle: str):
    for book in BOOKS:
        if book.get("title").casefold() == bookTitle.casefold():
            return book

@app.get("/books/")
async def getBooksByCategory(category: str):
    books = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books.append(book)
    return books

# ASSINGMENT
@app.get("/books/byAuthor/")
async def getBookByAuthor(bookAuthor: str):
    books = []
    for book in BOOKS:
        if book.get("author").casefold() == bookAuthor.casefold():
            books.append(book)
    return books

# ASSINGMENT
@app.get("/books/byAuthor/{bookAuthor}")
async def getBookByAuthor(bookAuthor: str):
    books = []
    for book in BOOKS:
        if book.get("author").casefold() == bookAuthor.casefold():
            books.append(book)
    return books
    
@app.get("/books/{bookAuthor}/")
async def getBooksByAuthorAndCategory(bookAuthor: str, category: str):
    books = []
    for book in BOOKS:
        if book.get("author").casefold() == bookAuthor.casefold() and book.get("category").casefold() == category.casefold():
            books.append(book)
    return books

@app.post("/books/createBook")
async def postBook(newBook = Body()):
    BOOKS.append(newBook)

@app.put("/books/updateBook")
async def updateBook(updatedBook = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updatedBook.get("title").casefold():
            BOOKS[i] = updatedBook

@app.delete("/books/deleteBook/{bookTitle}")
async def deleteBook(bookTitle: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == bookTitle.casefold():
            BOOKS.pop(i)
            break
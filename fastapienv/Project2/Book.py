class Book:
    id: int
    title: str
    author: str
    description: str
    publishedDate: int
    rating: int

    def __init__(self, id, title, author, description, publishedDate, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.publishedDate = publishedDate
        self.rating = rating
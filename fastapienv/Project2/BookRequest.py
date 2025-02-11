from typing import Optional
from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id: Optional[int] = Field(description = "Not needed on create", default = None)
    title: str = Field(min_length = 3)
    author: str = Field(min_length = 1)
    description: str = Field(min_length = 1, max_length = 100)
    publishedDate: str = Field(gt = 1999, lt = 2026)
    rating: int = Field(gt = 0, ls = 6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "New book",
                "author": "Author",
                "description": "Description of New book",
                "publishedDate": 2000,
                "rating": 5
            }
        }
    }
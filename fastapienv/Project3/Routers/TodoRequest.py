from pydantic import BaseModel, Field

class TodoRequest(BaseModel):
    Title: str = Field(min_length=1)
    Description: str = Field(min_length=3, max_length=100)
    Priority: int = Field(gt=0, lt=6)
    Complete: bool = Field(default=False)
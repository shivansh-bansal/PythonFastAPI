from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    role: str
    
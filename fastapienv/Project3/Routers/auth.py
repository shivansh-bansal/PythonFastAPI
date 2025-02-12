from models import Users
from Routers.Token import *
from starlette import status
from typing import Annotated
from fastapi import APIRouter
from jose import jwt, JWTError
from database import SessionLocal
from sqlalchemy.orm import Session
from Routers.CreateUserRequest import *
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SECRET_KEY = "b7e397746b185aea1d065e239b977798ee178c753faf3cb23c3ca189bd472300"
ALGORITHM = "HS256"
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

dbDependency = Annotated[Session, Depends(getDB)]


def authenticateUser(username: str, password: str, db: dbDependency):
    user = db.query(Users).filter(username == Users.username).first()
    if user and bcrypt_context.verify(password, user.hashedPassword):
        return user
    return False


def createToken(username: str, userID: int, expireDelta: timedelta):
    encode = {"sub": username, "id": userID}
    expires = datetime.now(timezone.utc) + expireDelta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def getUser(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username:str = payload.get("sub")
        userID:int = payload.get("id")
        if username is None or userID is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user")
        return {"username": username, "userID": userID}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user")



@router.post("/", status_code=status.HTTP_201_CREATED)
async def createUser(db: dbDependency, createUserRequest: CreateUserRequest):
    createdUser = Users(
        username = createUserRequest.username,
        firstName = createUserRequest.firstName,
        lastName = createUserRequest.lastName,
        email = createUserRequest.email,
        role = createUserRequest.role,
        hashedPassword = bcrypt_context.hash(createUserRequest.password),
        isActive = True
    )
    db.add(createdUser)
    db.commit()


@router.post("/token", response_model=Token, status_code=status.HTTP_201_CREATED)
async def loginToken(formData: Annotated[OAuth2PasswordRequestForm, Depends()], db: dbDependency):
    user = authenticateUser(username=formData.username, password=formData.password, db=db)
    if user:
        token = createToken(user.username, user.id, timedelta(minutes=20))
        return {"accessToken":token, "tokenType": "bearer"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user")



@router.get("/users")
async def getAllUsers(db: dbDependency):
    return db.query(Users).all()

@router.delete("/user/{userID}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteUser(db: dbDependency, userID: int = Path(gt=0)):
    user = db.query(Users).filter(Users.id == userID).first()
    if user:
        db.delete(user)
        db.commit()
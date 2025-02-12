from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    firstName = Column(String)
    lastName = Column(String)
    hashedPassword = Column(String)
    isActive = Column(Boolean, default=True)
    role = Column(String)


class Todos(Base):
    __tablename__ = "Todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    ownerID = Column(Integer, ForeignKey("Users.id"))
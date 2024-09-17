from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    blogs: List[Blog] = []

    class Config:
        orm_mode = True

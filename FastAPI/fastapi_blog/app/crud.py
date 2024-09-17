from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException, status
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

def create_blog(db: Session, blog: schemas.BlogCreate, user_id: int):
    db_blog = models.Blog(**blog.dict(), owner_id=user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def delete_blog(db: Session, blog_id: int):
    db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(db_blog)
    db.commit()

def update_blog(db: Session, blog_id: int, blog: schemas.BlogCreate):
    db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    db_blog.title = blog.title
    db_blog.content = blog.content
    db.commit()
    db.refresh(db_blog)
    return db_blog

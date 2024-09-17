from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database, auth

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.get("/", response_model=List[schemas.Blog])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    blogs = crud.get_blogs(db, skip=skip, limit=limit)
    return blogs

@router.get("/{blog_id}", response_model=schemas.Blog)
def read_blog(blog_id: int, db: Session = Depends(database.get_db)):
    blog = crud.get_blog(db, blog_id)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.post("/", response_model=schemas.Blog)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.oauth2_scheme)):
    return crud.create_blog(db=db, blog=blog, user_id=current_user.id)

@router.delete("/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.oauth2_scheme)):
    crud.delete_blog(db=db, blog_id=blog_id)
    return {"detail": "Blog deleted"}

@router.put("/{blog_id}", response_model=schemas.Blog)
def update_blog(blog_id: int, blog: schemas.BlogCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.oauth2_scheme)):
    return crud.update_blog(db=db, blog_id=blog_id, blog=blog)

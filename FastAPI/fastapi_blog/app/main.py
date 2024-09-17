from fastapi import FastAPI
from .database import engine, Base
from .routers import blog, user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Welcome to the blog API"}

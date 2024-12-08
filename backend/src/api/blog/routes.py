from fastapi import APIRouter
from fastaapi import Depends
from sqlmodel import Session
from src.api.db.db import get_session
from src.api.blog.schemas import CreateSimpleBlogPost
from src.api.db.models import SimpleBlogPost

blog_router = APIRouter()

@blog_router.get("/blog")
def get_blogs(session: Session = Depends(get_session)):
    blogs = session.query(SimpleBlogPost).all()
    return blogs


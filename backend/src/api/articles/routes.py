from fastapi import APIRouter
from fastaapi import Depends
from sqlmodel import Session
from src.api.db.db import get_session

article_router = APIRouter()


@article_router.get("/")
def get_articles():
    return {"articles": []}

@article_router.get("/{article_id}")
def get_article(article_id: str):
    return {"article_id": article_id}

@article_router.post("/")
def create_article():
    return {"message": "Article created successfully"}

@article_router.put("/{article_id}")
def update_article(article_id: str):
    return {"message": "Article updated successfully"}

@article_router.delete("/{article_id}")
def delete_article(article_id: str):
    return {"message": "Article deleted successfully"}



from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session
from app.db.db import get_session
from app.schemas import CreateSimpleBlogPost
from app.db.models import SimpleBlogPost
from app.resources import BlogManager


from uuid import UUID

blog_router = APIRouter()


@blog_router.get("/list")
def get_blogs(
    session: Session = Depends(get_session), manager: BlogManager = Depends(BlogManager)
):
    blog_post_list = manager.get_all_blog_posts(session)
    return blog_post_list


# create blog post
@blog_router.post(f"/create/")
def create_simple_blog_post(
    blog_data: CreateSimpleBlogPost,
    session: Session = Depends(get_session),
    manager: BlogManager = Depends(BlogManager),
) -> SimpleBlogPost:
    blog_post = manager.create_simple_article(blog_data, session)
    return blog_post


# get blog post by id
@blog_router.get("/get/{post_id}")
async def get_blog_post_by_id(
    post_id: UUID,
    session: Session = Depends(get_session),
    manager: BlogManager = Depends(BlogManager),
) -> SimpleBlogPost:
    blog_post = manager.get_post_by_id(post_id, session)
    return blog_post


# get all posts
@blog_router.get("/get_all")
async def get_all_posts(
    session: Session = Depends(get_session), manager: BlogManager = Depends(BlogManager)
) -> SimpleBlogPost:
    blog_posts = manager.get_all_posts(session)
    return blog_posts

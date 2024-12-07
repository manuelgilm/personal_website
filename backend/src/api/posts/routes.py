from fastapi import APIRouter
from fastaapi import Depends

post_router = APIRouter()


@post_router.get("/posts")
async def get_posts():
    return {"message": "This is a list of posts"}


@post_router.get("/posts/{post_id}")
async def get_post(post_id: int):
    return {"message": f"This is post {post_id}"}


@post_router.post("/posts")
async def create_post():
    return {"message": "Post created successfully"}


@post_router.put("/posts/{post_id}")
async def update_post(post_id: int):
    return {"message": f"Post {post_id} updated successfully"}


@post_router.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    return {"message": f"Post {post_id} deleted successfully"}

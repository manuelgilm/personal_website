from fastapi import FastAPI
from app.db.db import init_db
from app.routers.blog import blog_router


def lifespan(app: FastAPI):
    init_db()
    print("DB initialized")
    yield


version = "v1"
description = "Blog API"
app = FastAPI(lifespan=lifespan, version=version, description=description)

app.include_router(blog_router, prefix="/api/v1/blog", tags=["blog"])

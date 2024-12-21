from fastapi import FastAPI
from app.routers.education import educ_router
from app.db.db import init_db

def lifespan(app: FastAPI):
    init_db()
    print("DB initialized")
    yield

version = "v1"
description = "CV API"
app = FastAPI(lifespan=lifespan, version=version, description=description)

app.include_router(educ_router, prefix=f"/api/{version}/education", tags=["education"])

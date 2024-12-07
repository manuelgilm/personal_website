from fastapi import FastAPI
from src.api.db.db import init_db
from contextlib import asynccontextmanager
from src.api.credentials.routes import credentials_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


version = "v1"
app = FastAPI(
    title="FastAPI with async context manager",
    version=version,
    description="This is a FastAPI app with async context manager",
    lifespan=lifespan,
)

app.include_router(credentials_router, prefix=f"/{version}", tags=["credentials"])

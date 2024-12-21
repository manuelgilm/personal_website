from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from sqlmodel import Session

from app.db.db import get_session
from app.schemas import CreateExperience
from app.schemas import ExperienceList
from app.resources import ExperienceManager

from uuid import UUID

exp_router = APIRouter()


@exp_router.get("/list", status_code=status.HTTP_200_OK)
async def list_all_experiences(
    session: Session = Depends(get_session),
    manager: ExperienceManager = Depends(ExperienceManager),
):
    experiences = manager.get_all_experiences(session)
    return experiences


@exp_router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_experience(
    experience: CreateExperience,
    session: Session = Depends(get_session),
    manager: ExperienceManager = Depends(ExperienceManager),
):
    exp = manager.get_experience_by_id(experience.id, session)
    if exp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Experience already exists"
        )
    exp = manager.create_experience(experience, session)

    return exp


@exp_router.get("/get/{exp_id}", status_code=status.HTTP_200_OK)
async def get_experience_by_id(
    exp_id: UUID,
    session: Session = Depends(get_session),
    manager: ExperienceManager = Depends(ExperienceManager),
):
    experience = manager.get_experience_by_id(exp_id, session)
    if experience is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found"
        )
    return experience


@exp_router.delete("/delete/{exp_id}", status_code=status.HTTP_200_OK)
async def delete_experience_by_id(
    exp_id: UUID,
    session: Session = Depends(get_session),
    manager: ExperienceManager = Depends(ExperienceManager),
):
    experience = manager.get_experience_by_id(exp_id, session)
    if experience is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found"
        )
    manager.delete_experience(exp_id, session)
    return experience

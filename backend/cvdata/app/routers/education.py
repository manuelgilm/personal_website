from fastapi import APIRouter
from app.db.db import get_session
from app.schemas import CreateCertificate
from app.schemas import CertificationList
from app.resources import EducationManager
from sqlmodel import Session
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from uuid import UUID

educ_router = APIRouter()


@educ_router.get("/list", status_code=status.HTTP_200_OK)
def list_all_certifications(
    session: Session = Depends(get_session),
    manager: EducationManager = Depends(EducationManager),
):
    certifications = manager.get_all_certifications(session)
    return certifications


@educ_router.post("/create/", status_code=status.HTTP_201_CREATED)
def create_certification(
    cert: CreateCertificate,
    session: Session = Depends(get_session),
    manager: EducationManager = Depends(EducationManager),
):
    cert = manager.get_certificate_by_title(cert.title, session)
    if cert:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Certificate already exists"
        )

    certification = manager.create_certificate(cert, session)
    return certification


@educ_router.get("/get/{cert_id}", status_code=status.HTTP_200_OK)
def get_certification_by_id(
    cert_id: UUID,
    session: Session = Depends(get_session),
    manager: EducationManager = Depends(EducationManager),
):
    certification = manager.get_certificate_by_id(cert_id, session)
    if certification is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Certificate not found"
        )
    return certification


@educ_router.delete("/delete/{cert_id}", status_code=status.HTTP_200_OK)
def delete_certification_by_id(
    cert_id: UUID,
    session: Session = Depends(get_session),
    manager: EducationManager = Depends(EducationManager),
):
    certification = manager.get_certificate_by_id(cert_id, session)
    if certification is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Certificate not found"
        )
    manager.delete_certificate(cert_id, session)
    return certification

from sqlmodel import Session
from app.schemas import CertificationList
from app.schemas import CreateCertificate
from app.db.models import Certificate

from sqlmodel import select


class EducationManager:

    def create_certificate(
        self, certificate: CreateCertificate, session: Session
    ) -> Certificate:
        certificate_dict = certificate.model_dump()
        cert = Certificate(**certificate_dict)

        session.add(cert)
        session.commit()
        session.refresh(cert)
        return cert

    def get_all_certifications(self, session: Session) -> CertificationList:
        statement = select(Certificate)
        certs = session.exec(statement).all()
        return certs

    def get_certificate_by_id(self, cert_id: int, session: Session) -> Certificate:
        statement = select(Certificate).where(Certificate.id == cert_id)
        cert = session.exec(statement).first()
        return cert

    def get_certificate_by_title(self, title: str, session: Session) -> Certificate:
        statement = select(Certificate).where(Certificate.title == title)
        cert = session.exec(statement).first()
        return cert

    def delete_certificate(self, cert_id: int, session: Session) -> Certificate:
        statement = select(Certificate).where(Certificate.id == cert_id)
        cert = session.exec(statement).first()
        session.delete(cert)
        session.commit()
        return cert

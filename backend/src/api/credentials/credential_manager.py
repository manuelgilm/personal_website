from src.api.credentials.schemas import CredentialCreateModel
from src.api.db.models import Credential
from sqlmodel import Session
from sqlmodel import select


class CredentialManager:

    def create_credential(
        self, credential_data: CredentialCreateModel, session: Session
    ):
        """
        Create a new credential

        :param credential_data: CredentialCreateModel
        :param session: Session
        :return: Credential
        """
        credential_data_dict = credential_data.model_dump()

        credential = Credential(**credential_data_dict)

        session.add(credential)
        session.commit()
        session.refresh(credential)
        return credential

    def get_credential_by_name(self, credential_name: str, session: Session):
        """
        Get a credential by name

        :param credential_name: Name of the credential
        :param session: Database session
        :return: Credential
        """
        statement = select(Credential).where(Credential.name == credential_name)
        result = session.exec(statement).first()
        return result

    def get_credential_by_id(self, credential_id: int, session: Session):
        """
        Get a credential by id

        :param credential_id: Id of the credential
        :param session: Database session
        :return: Credential
        """
        statement = select(Credential).where(Credential.id == credential_id)
        result = session.exec(statement).first()
        return result

    def delete_credential_by_name(self, credential_name: str, session: Session):
        """
        Delete a credential by name

        :param credential_name: Name of the credential
        :param session: Database session
        :return: None
        """
        credential = self.get_credential_by_name(credential_name, session)
        if credential:
            session.delete(credential)
            session.commit()
            return {"message": "Credential deleted successfully"}
        return {"message": "Credential not found"}

    def get_all_credentials(self, session: Session):
        """
        Get all credentials

        :param session: Database session
        :return: List of Credential
        """
        statement = select(Credential)
        result = session.exec(statement).all()
        return result

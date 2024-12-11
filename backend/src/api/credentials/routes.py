from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from src.api.credentials.schemas import CredentialCreateModel
from src.api.credentials.credential_manager import CredentialManager
from src.api.db.db import get_session
import uuid

credentials_router = APIRouter()


@credentials_router.get("/credentials")
async def get_credentials(
    credentials_manager: CredentialManager = Depends(CredentialManager),
    session=Depends(get_session),
):
    """
    Get a list of credentials

    :param credentials_manager: CredentialManager
    :param session: Database session
    :return: List of credentials

    """
    credentials = credentials_manager.get_all_credentials(session)
    return credentials


@credentials_router.get("/credentials/{credential_id}")
async def get_credential(credential_id: int):
    return {"message": f"This is credential {credential_id}"}


@credentials_router.post("/credentials", status_code=status.HTTP_201_CREATED)
async def create_credential(
    credential_data: CredentialCreateModel,
    credential_manager: CredentialManager = Depends(CredentialManager),
    session=Depends(get_session),
):
    """
    Create a new credential

    :param credentials_data: CredentialCreateModel
    :param credential_manager: CredentialManager
    :param session: Database session
    :return: Credential

    """
    credential_manager = CredentialManager()
    credential_name = credential_data.name
    credential = credential_manager.get_credential_by_name(credential_name, session)
    if credential:
        return {"message": "Credential already exists"}

    credential = credential_manager.create_credential(credential_data, session)
    return {"message": "Credential created successfully"}


@credentials_router.put("/credentials/{credential_id}")
async def update_credential(credential_id: int):
    return {"message": f"Credential {credential_id} updated successfully"}


@credentials_router.delete("/credentials/{credential_id}")
async def delete_credential(credential_id: uuid.UUID):
    return {"message": f"Credential {credential_id} deleted successfully"}

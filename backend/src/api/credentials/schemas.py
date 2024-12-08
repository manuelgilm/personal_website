from pydantic import BaseModel
from typing import Optional

class CredentialCreateModel(BaseModel):
    name: str
    description: str
    earned_date: str
    expiration_date: str
    credential_url: Optional[str] = None
    organization: str





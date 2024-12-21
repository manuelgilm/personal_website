from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from typing import List
from typing import Union
from datetime import datetime


class CreateCertificate(BaseModel):
    title: str
    description: str
    image: Optional[str] = None
    link: Optional[str] = None
    earned_date: Optional[datetime] = Field(default=datetime.now())
    expiration_date: Optional[datetime] = Field(default=None)


class CertificationList(BaseModel):
    certificates: List[CreateCertificate]

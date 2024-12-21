from sqlmodel import Field
from sqlmodel import SQLModel
import uuid
from datetime import datetime
from typing import Optional


class Certificate(SQLModel, table=True):
    certificate_id: uuid.UUID = Field(
        default=uuid.uuid4(), primary_key=True, index=True
    )
    title: str
    description: str
    image: Optional[str] = None
    link: Optional[str] = None
    earned_date: datetime
    expiration_date: Optional[datetime] = None

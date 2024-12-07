from sqlmodel import Field
from sqlmodel import SQLModel
import uuid
from datetime import datetime
from typing import Optional
from typing import List


class Credential(SQLModel, table=True):
    credential_id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True, index=True)
    name: str
    description: str
    earned_date: str
    expiration_date: str
    credential_url: Optional[str] = None
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    organization: str

def SimpleArticle(SQLModel, table=True):
    article_id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True, index=True)
    title: str
    content: str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    tags: Optional[List] = None
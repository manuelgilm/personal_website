from pydantic import BaseModel

from typing import List
from typing import Optional

class CreateSimpleArticleSchema(BaseModel):
    title: str
    content: str
    tags: Optional[List[str]] = None
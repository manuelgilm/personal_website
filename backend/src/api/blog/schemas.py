from pydantic import BaseModel

from typing import List
from typing import Optional

class CreateSimpleBlogPost(BaseModel):
    title: str
    content: str
    tags: Optional[List[str]] = None


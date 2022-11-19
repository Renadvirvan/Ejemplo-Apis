from pydantic import BaseModel
from typing import Optional
class User(BaseModel):
    userID: Optional[str]
    name: str
    email: str
    password: str

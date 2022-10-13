from typing import Optional
from pydantic import BaseModel



class Livros_POST(BaseModel):
    titulo: str
    autor: str


class Livros_PATCH(BaseModel):
    titulo: Optional[str]
    autor: Optional[str]
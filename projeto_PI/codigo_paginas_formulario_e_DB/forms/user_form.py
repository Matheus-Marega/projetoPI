# Formulário de usuário com validações de dados

from pydantic import BaseModel,EmailStr
from datetime import datetime


class User(BaseModel):
    email: EmailStr
    nome: str
    data: datetime
    gender:str
# Formulário de usuário com validações de dados

from pydantic import BaseModel,EmailStr



class User(BaseModel):
    email: EmailStr
    nome: str
    gender:str
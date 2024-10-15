from pydantic import BaseModel,EmailStr,ValidationError
from datetime import datetime


class User(BaseModel):
    email: EmailStr
    nome: str
    data: datetime
    gender:str


username = "admin"
password = "123"

lojas_shopping = [
    "Nenhuma",
    "Loja do Esporte",
    "Moda & Estilo",
    "Tecnologia Top",
    "Café Gourmet",
    "Livraria Central",
    "Brinquedos & Cia",
    "Joias de Luxo",
    "Mundo dos Games",
    "Cine Shopping",
    "Super Beleza"
]


lista_segmentos = [
    "Nenhuma",
    "Roupas e Acessórios",
    "Calçados",
    "Eletrônicos e Tecnologia",
    "Alimentação (Praça de Alimentação)",
    "Cosméticos e Perfumaria",
    "Jóias e Relógios",
    "Livrarias e Papelarias",
    "Brinquedos e Jogos",
    "Esportes e Lazer",
    "Decoração e Utilidades Domésticas"
]

nota = ["-",0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



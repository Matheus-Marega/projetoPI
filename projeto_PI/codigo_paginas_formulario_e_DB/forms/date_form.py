from pydantic import BaseModel, validator
from datetime import date

class ModeloData(BaseModel):
    data: date

    @validator('data')
    def validar_data(cls, valor):
        if valor > date.today():
            raise ValueError('A data não pode ser maior que a data atual.')
        return valor


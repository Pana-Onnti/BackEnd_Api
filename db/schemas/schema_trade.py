from pydantic import BaseModel
from typing import Optional

class TradeDict(BaseModel):
    Fecha_Entrada: int
    Fecha_Salida: Optional[int]
    Precio_Entrada: float
    Direccion: int
    Precio_Salida: Optional[float]
    Comision: float
    Id_Notas: Optional[int]
    Estado: int
    Id_Cuenta: int

    class Config:
        orm_mode = True

class TradeOut(BaseModel):
    Id: int
    Fecha_Entrada: int
    Fecha_Salida: int
    Precio_Entrada: float
    Direccion: int
    Precio_Salida: float
    Comision: float
    Id_Notas: int
    Estado: int
    Id_Cuenta: int


class Email(BaseModel):
    email:str
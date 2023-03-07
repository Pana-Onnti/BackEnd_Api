from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TradeDict(BaseModel):
    Ticker : str
    Fecha_Entrada: datetime
    Fecha_Salida: datetime
    Precio_Entrada: Optional[float]
    Direccion: int
    Precio_Salida: Optional[float]
    Comision: float
    Id_Notas: Optional[int]
    Estado: int
    Id_Cuenta: int

    class Config:
        orm_mode = True

class TradeOut(BaseModel):
    Ticker : str
    Id: int
    Fecha_Entrada: datetime
    Fecha_Salida: datetime
    Direccion: int
    Precio_Entrada: float
    Precio_Salida: float
    Comision: float
    Id_Notas: int
    Estado: int
    Id_Cuenta: int


class Email(BaseModel):
    email:str
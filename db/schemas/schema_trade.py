from pydantic import BaseModel
class TradeCreate(BaseModel):
    Fecha_Entrada: int
    Fecha_Salida: int
    Direccion: int
    Precio_Entrada: float
    Precio_Salida: float
    Comision: float
    Id_Notas: int
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
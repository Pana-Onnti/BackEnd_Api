from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    Nombre: str
    Apellido: str
    User_name: str
    Password: str
    Email: str
    class Config:
        orm_mode = True
        










class CuentaCreate(BaseModel):
    Id_Cuenta: int
    Id_Estado: int
    Id_Usuario: int
    Balance: int
    Id_Trade: str
    class Config:
        orm_mode = True

class TradeCreate(BaseModel):
    Id_Trade: int
    Fecha_Entrada: int
    Fecha_Salida: int
    Direccion: int
    Precio_Entrada: float
    Precio_Salida: float
    Comision: float
    Id_Notas: int
    Estado: int
    Id_Cuenta: str




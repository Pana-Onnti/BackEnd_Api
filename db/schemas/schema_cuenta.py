from pydantic import BaseModel

class CuentaOut:
    def __init__(self, Id: int, Id_Estado: int, Balance: int):
        self.Id = Id
        self.Id_Estado = Id_Estado
        self.Balance = Balance

    def dict(self):
        return {
            'Id': self.Id,
            'Id_Estado': self.Id_Estado,
            'Balance': self.Balance
        }
    class Config:
        orm_mode = True
        


class Cuentas(BaseModel):
    Id :int
    Id_Estado: int
    Id_Usuario: int
    Balance: int
    class Config:
        orm_mode = True


class CuentasUsuario(BaseModel):
    cuentas:list[Cuentas]
    class Config:
        orm_mode = True
        

class CuentaCreate(BaseModel):
    
    Id_Estado: int
    Balance: int
    
    class Config:
        orm_mode = True

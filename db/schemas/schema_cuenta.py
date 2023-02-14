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

class Cuentas(BaseModel):
    
    Id_Estado: int
    Id_Usuario: int
    Balance: int
    class Config:
        orm_mode = True


class CuentaCreate(BaseModel):
    
    Id_Estado: int
    Id_Usuario: int
    Balance: int
    
    class Config:
        orm_mode = True

#@app.post("/cuentas")
#def create_cuenta(cuenta: CuentaCreate, db: Session = Depends(get_db)):
#    db_cuenta = Cuenta(**cuenta.dict())
#    db.add(db_cuenta)
#    db.commit()
#    db.refresh(db_cuenta)
#    return db_cuenta
#from typing import Optional
#
#
#
#
#@app.get("/cuentas")
#def get_cuentas(db: Session = Depends(get_db)):
#    cuentas = db.query(Cuenta).all()
#    return [CuentaOut(Id=cuenta.Id, Id_Estado=cuenta.Id_Estado, Balance=cuenta.Balance).dict() for cuenta in cuentas]
# 
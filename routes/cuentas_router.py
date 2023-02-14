from fastapi import APIRouter,Depends
from db.schemas.schema_cuenta import *
from db.database import get_db
from sqlalchemy.orm import Session
from db.models.models import Cuenta

# set endpoint
router = APIRouter(
    prefix="/cuentas",
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)

# Crear #
@router.post("/crear/",response_model=CuentaCreate)
def get_cuentas(cuenta: CuentaCreate,db: Session = Depends(get_db)): 
    db_cuenta = Cuenta(**cuenta.dict())
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta

# Devolver Todas las Cuentas#
@router.get("/cuentas/")
def create_cuenta( db: Session = Depends(get_db)):
    cuentas = db.query(Cuenta).all()
    return [CuentaOut(Id=cuenta.Id,
                     Id_Estado=cuenta.Id_Estado,
                     Balance=cuenta.Balance).dict() for cuenta in cuentas]



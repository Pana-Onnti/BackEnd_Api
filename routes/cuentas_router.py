from fastapi import APIRouter,Depends
from db.schemas.schema_cuenta import *
from db.database import get_db
from sqlalchemy.orm import Session
from db.models.models import Cuenta

# set endpoint
router = APIRouter(
    prefix="/cuentas",
    tags=["Cuentas"],
    responses={404: {"description": "Not found"}},
)

# Crear #
@router.post("/crear/",response_model=CuentaCreate)
def create_cuenta(cuenta: CuentaCreate,db: Session = Depends(get_db)): 
    db_cuenta = Cuenta(**cuenta.dict())
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta

# Devolver Todas las Cuentas#
@router.get("/cuentas/")
def buscar_cuentas( db: Session = Depends(get_db)):
    cuentas = db.query(Cuenta).all()
    return [CuentaOut(Id=cuenta.Id,
                     Id_Estado=cuenta.Id_Estado,
                     Balance=cuenta.Balance).dict() for cuenta in cuentas]



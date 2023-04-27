from fastapi import APIRouter,Depends
from db.schemas.schema_cuenta import *
from db.database import get_db
from sqlalchemy.orm import Session
from db.models.models import Cuenta
from db.models.models import Usuario
from db.schemas.schema_usuario import *
from crud import *
from http_exceptions import *

# set endpoint
router = APIRouter(
    prefix="/cuentas",
    tags=["Cuentas"],
    responses={404: {"description": "Not found"}},
)
# Operaciones


@router.post('/crear/')
async def crear_cuenta_por_usuario(email: str, cuenta: CuentaCreate, db: Session = Depends(get_db)):
    usuario = validar_usuario_cuentas_creadas(db, email)
    db_cuenta = crear_cuenta(db, cuenta, usuario)
    return db_cuenta

@router.get("/cuentas/")
def obtener_cuentas( db: Session = Depends(get_db)):
    cuentas = db.query(Cuenta).all()
    return [CuentaOut(Id=cuenta.Id,
                     Id_Estado=cuenta.Id_Estado,
                     Balance=cuenta.Balance).dict() for cuenta in cuentas]
#


@router.get('/buscar/{email}',response_model=CuentasUsuario)
async def obtener_cuentas_por_email(email:str,db:Session=Depends(get_db)):
    usuario = obtener_usuario_por_email_db(db,email) 
    return CuentasUsuario(cuentas=usuario.cuentas)
        


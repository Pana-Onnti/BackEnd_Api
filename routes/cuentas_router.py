from fastapi import APIRouter,Depends
from db.schemas.schema_cuenta import *
from db.database import get_db
from sqlalchemy.orm import Session
from db.models.models import Cuenta
from db.models.models import Usuario
from db.schemas.schema_usuario import *
from crud import *


# set endpoint
router = APIRouter(
    prefix="/cuentas",
    tags=["Cuentas"],
    responses={404: {"description": "Not found"}},
)

class UsuarioNoExisteException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail='El usuario no existe')

class UsuarioMaximoCuentasException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail='El usuario ya tiene 5 cuentas')

def validar_usuario_cuentas_creadas(db: Session, email: str) -> Usuario:
    usuario = obtener_usuario_por_email_db(db, email)
    if usuario is None:
        raise UsuarioNoExisteException()
    if len(usuario.cuentas) >= 5:
        raise UsuarioMaximoCuentasException()
    return usuario

def crear_cuenta(db: Session, cuenta: CuentaCreate, usuario: Usuario) -> Cuenta:
    cuenta.Id_Usuario = usuario.Id
    cuenta.Id_Estado = 1
    db_cuenta = Cuenta(**cuenta.dict())
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta

@router.post('/crear/{email}')
async def crear_cuenta_por_usuario(email: str, cuenta: CuentaCreate, db: Session = Depends(get_db)):
    usuario = validar_usuario_cuentas_creadas(db, email)
    db_cuenta = crear_cuenta(db, cuenta, usuario)
    return db_cuenta


#

#
# Crear #
@router.post("/creard/",response_model=CuentaCreate)
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


@router.get('/cuenta/{email}',response_model=CuentasUsuario)
async def buscar_cuentas_usuario(email:str,db:Session=Depends(get_db)):
    usuario = obtener_usuario_por_email_db(db,email) 
    return CuentasUsuario(cuentas=usuario.cuentas)
        


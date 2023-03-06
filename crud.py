from db.models.models import Usuario
from db.schemas.schema_usuario import *
from sqlalchemy.orm import Session
from db.models.models import Cuenta , Trade ,Usuario
from db.schemas.schema_usuario import *
from http_exceptions import *
from db.schemas.schema_cuenta import *
from db.schemas.schema_trade import *
#Cuentas
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

#Usuarios
async def validar_usuario_nuevo(usuario: UsuarioCreate, db: Session) -> None:
    usuario_existente = db.query(Usuario).filter(Usuario.Email == usuario.Email).first()
    if usuario_existente:
        raise UsuarioEmailDuplicado()
    ocultar_password(usuario)
    return usuario


def obtener_usuario_por_nombre_usuario(nombre_usuario: str, db: Session) -> Usuario:
    usuario = db.query(Usuario).filter(Usuario.User_name == nombre_usuario).first()
    if usuario is None:
        raise UsuarioNoExisteException()
    ocultar_password(usuario)
    return usuario


def obtener_usuario_por_email_db(db: Session, email: str) -> Usuario:
    return db.query(Usuario).filter(Usuario.Email == email).first()

def ocultar_password(usuario: UsuarioOut) -> None: 
    usuario.Password = 'XXX'


#trades
def obtener_primer_cuenta(db:Session,email:str) -> CuentaOut :
    usuario = obtener_usuario_por_email_db(db,email)
    cuentas = CuentasUsuario(cuentas=usuario.cuentas)
    try:
        cuenta = cuentas.cuentas[0]
        cuenta_Id = cuenta.Id
        return cuenta_Id
    except IndexError:
        raise UsuarioSinCuentas()
    

def obtener_id_cuenta(db:Session,email:str) -> int:
    cuenta = obtener_primer_cuenta(db,email)
    cuenta_Id = cuenta.Id
    return cuenta_Id


def trade_nuevo(db:Session,trade:TradeDict,email:str) -> Trade:
    nuevo_trade = Trade(**trade.dict())
    nuevo_trade.Id_Cuenta= obtener_id_cuenta(db,email)
    db.add(nuevo_trade)
    db.commit()
    db.refresh(nuevo_trade)
    return nuevo_trade

def validar_usuario_cuenta(db: Session, email: str) -> Usuario:
    usuario = obtener_usuario_por_email_db(db, email)
    if usuario is None:
        raise UsuarioNoExisteException()
    return usuario
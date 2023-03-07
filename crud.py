from db.models.models import Usuario
from db.schemas.schema_usuario import *
from sqlalchemy.orm import Session
from db.models.models import Cuenta , Trade ,Usuario
from db.schemas.schema_usuario import *
from http_exceptions import *
from db.schemas.schema_cuenta import *
from db.schemas.schema_trade import *
from datetime import datetime
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
        raise UsuarioEmailDuplicadoException()
    #ocultar_password(usuario)
    return usuario

def hash_pw(usuario:UsuarioCreate) -> UsuarioCreate:
    password = pwd_context.hash(usuario.Password)
    usuario.Password = password
    return usuario

def crear_usuario(db:Session,usuario:UsuarioCreate) -> UsuarioCreate:
    usuario_db = Usuario(**usuario.dict())
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db


def obtener_usuario_por_nombre_usuario(nombre_usuario: str, db: Session) -> Usuario:
    usuario = db.query(Usuario).filter(Usuario.User_name == nombre_usuario).first()
    if usuario is None:
        raise UsuarioNoExisteException()
    #ocultar_password(usuario)
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
        return cuenta
    except IndexError:
        raise UsuarioSinCuentasException()
    

def obtener_id_cuenta(db:Session,email:str) -> int:
    cuenta = obtener_primer_cuenta(db,email)
    cuenta_Id = cuenta.Id
    return cuenta_Id

def trade_nuevo(db:Session,trade:TradeDict,email:str) -> Trade:
    nuevo_trade = Trade(**trade.dict())
    nuevo_trade.Id_Cuenta= obtener_id_cuenta(db,email)
    # modificacion de base de datos # 
    # timestamp
    nuevo_trade.Fecha_Entrada = datetime.now()
    nuevo_trade.Fecha_Salida = datetime.now()
    ######
    db.add(nuevo_trade)
    db.commit()
    db.refresh(nuevo_trade)
    return nuevo_trade

def validar_usuario_cuenta(db: Session, email: str) -> Usuario:
    usuario = obtener_usuario_por_email_db(db, email)
    if usuario is None:
        raise UsuarioNoExisteException()
    return usuario
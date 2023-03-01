from fastapi import APIRouter, Depends, HTTPException ,status
from db.database import get_db
from db.models.models import Usuario
from db.schemas.schema_usuario import *
from sqlalchemy.orm import Session
from passlib.context import CryptContext
#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
    responses={404: {"description": "Not found"}},
)
#    usuario_db.Password = password
#   password = pwd_context.hash(usuario.Password)



#############################################################
# Obtener usuarios por email 
#############################################################

def obtener_usuario_por_email_db(db: Session, email: str) -> Usuario:
    return db.query(Usuario).filter(Usuario.Email == email).first()

def ocultar_password(usuario: UsuarioOut) -> None: 
    usuario.Password = 'XXX'

@router.get('/{email}/',response_model=UsuarioOut)
async def obtener_usuario_por_email(email: str, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_email_db(db, email)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='El usuario no existe'
        )
    ocultar_password(usuario)
    return usuario

#############################################################
# Crear usuarios :
#############################################################
async def validar_usuario_nuevo(usuario: UsuarioCreate, db: Session) -> None:
    usuario_existente = db.query(Usuario).filter(Usuario.Email == usuario.Email).first()
    if usuario_existente:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='El correo electrónico ya está registrado')
    ocultar_password(usuario)
    return usuario

@router.post('/crear/',response_model=UsuarioCreate)
async def agregar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)) -> Usuario:
    await validar_usuario_nuevo(usuario, db)
    usuario = Usuario(**usuario.dict())
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

#############################################################
# Obtener usuarios por username:
#############################################################

#@router.get("/{username}", response_model=UsuarioOut)
#async def obtener_usuario(username: str, db: Session = Depends(get_db)):
#    usuario = db.query(Usuario).filter(Usuario.User_name == username).first()
#    if usuario is None :
#        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='El usuario no existe')
#    ocultar_password(usuario)
#    return usuario



def obtener_usuario_por_nombre_usuario(nombre_usuario: str, db: Session) -> Usuario:
    usuario = db.query(Usuario).filter(Usuario.User_name == nombre_usuario).first()
    if usuario is None:
        raise  HTTPException(status_code=status.HTTP_409_CONFLICT, detail='El usuario no existe')
    ocultar_password(usuario)
    return usuario

@router.get("/{nombre_usuario}", response_model=UsuarioOut)
async def obtener_usuario(nombre_usuario: str, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_nombre_usuario(nombre_usuario, db)
    return usuario
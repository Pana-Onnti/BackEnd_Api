from fastapi import APIRouter, Depends
from db.database import get_db
from db.models.models import Usuario
from db.schemas.schema_usuario import *
from sqlalchemy.orm import Session
from passlib.context import CryptContext
#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from crud import *
from http_exceptions import *

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
    responses={404: {"description": "Not found"}},
)
#    usuario_db.Password = password
#   password = pwd_context.hash(usuario.Password)


@router.post('/crear/',response_model=UsuarioCreate)
async def agregar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)) -> Usuario:
    await validar_usuario_nuevo(usuario, db)
    usuario = Usuario(**usuario.dict())
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


@router.get('buscar/{email}/',response_model=UsuarioOut)
async def obtener_usuario_por_email(email: str, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_email_db(db, email)
    if usuario is None:
        raise UsuarioNoExisteException()
    ocultar_password(usuario)
    return usuario

@router.get("/{nombre_usuario}", response_model=UsuarioOut)
async def obtener_usuario(nombre_usuario: str, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_nombre_usuario(nombre_usuario, db)
    return usuario
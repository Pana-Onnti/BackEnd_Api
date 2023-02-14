from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from db.models.models import Usuario
from db.schemas.schema_usuario import *
from sqlalchemy.orm import Session
from passlib.context import CryptContext
#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)

@router.post('/crear/',response_model=UsuarioCreate)
async def agregar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
#   password = pwd_context.hash(usuario.Password)
    usuario_db = Usuario(**usuario.dict())
#    usuario_db.Password = password
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db
@router.get("/usuario/{username}")
async def obtener_usuario(username: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.User_name == username).first()
    return usuario


#@router.post('/crear/', response_model=UsuarioCreate)
#async def agregar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
#    password = usuario.Password.encode("utf-8")
#    salt = bcrypt.gensalt()
#    hashed_password = bcrypt.hashpw(password, salt)
#    print (hashed_password)
#    usuario_db = Usuario(**usuario.dict())
#    usuario_db.Password = hashed_password
#    db.add(usuario_db)
#    db.commit()
#    db.refresh(usuario_db)
#    return usuario_db



from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from db.models.models import Usuario
from db.schemas.schema_usuario import *
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)

@router.post('/crear/',response_model=UsuarioCreate)
async def agregar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_db = Usuario(**usuario.dict())
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db
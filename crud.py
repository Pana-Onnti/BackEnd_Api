from fastapi import APIRouter, Depends, HTTPException ,status
from db.database import get_db
from db.models.models import Usuario
from db.schemas.schema_usuario import *
from sqlalchemy.orm import Session



def obtener_usuario_por_email_db(db: Session, email: str) -> Usuario:
    return db.query(Usuario).filter(Usuario.Email == email).first()

def ocultar_password(usuario: UsuarioOut) -> None: 
    usuario.Password = 'XXX'
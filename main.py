from fastapi import FastAPI, APIRouter,Depends,HTTPException
from typing import Union
from db.database import Base,engine, get_db
from sqlalchemy.orm import Session
from fastapi import status
from db.models.models import Usuario
from schemas.schemas import *


def create_tables():
    Base.metadata.create_all(bind=engine)
    
create_tables()

app = FastAPI()

#@app.get("/2")
#def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#    users = db.query(Usuario).offset(skip).limit(limit).all()
#    return users



@app.post("/", response_model=UsuarioCreate)
async def create_user(usuario: UsuarioCreate, db: Session = Depends(get_db)):
   user = Usuario(**usuario.dict())
   db.add(user)
   db.commit()
   db.refresh(user)
   return user
class UsuarioOut(BaseModel):
    Id: int
    Nombre: str
    Apellido: str
    User_name: str
    Email: str

@app.get("/usuarios/")
def get_usuario_by_email(email: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.Email == email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UsuarioOut(Id=usuario.Id, Nombre=usuario.Nombre, Apellido=usuario.Apellido,
                      User_name=usuario.User_name, Email=usuario.Email).dict()
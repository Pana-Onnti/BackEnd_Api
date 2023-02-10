from fastapi import FastAPI, APIRouter,Depends,HTTPException
from typing import Union
from db.models.database import Base,engine, get_db
from sqlalchemy.orm import Session
from db.models.usuario import Usuario,Cuenta,Trade
from model import UsuarioCreate
from fastapi import status

def create_tables():
    Base.metadata.create_all(bind=engine)
    
create_tables()

app = FastAPI()

@app.get("/")
def read_root(db:Session = Depends(get_db)):
    data = db.query(Usuario).all()
   
    return data,asd,asd1
@app.post('/')
async def create_user(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    existe_usuario = db.query(Usuario).filter(Usuario.Email == usuario.Email).first()


    if existe_usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='El usuario con ese correo electrónico ya existe.')

    new_usuario = Usuario(**usuario.dict())
    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    return {"message": "Usuario creado"}
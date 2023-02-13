from fastapi import FastAPI,Depends
from db.database import Base,engine
from sqlalchemy.orm import Session
from routes import usuarios_route 
from routes import cuentas_router
from routes import trades_router


def create_tables():
    Base.metadata.create_all(bind=engine)
    
create_tables()

app = FastAPI()

app.include_router(usuarios_route.router)
app.include_router(cuentas_router.router)
app.include_router(trades_router.router)



@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}









#@app.post("/usuar/", response_model=UsuarioCreate)
#def create_user(usuario: UsuarioCreate, db: Session = Depends(get_db)):
#   
#    def db_add(usuario_add,db: Session = Depends(get_db)):
#        db.add(usuario_add)
#        db.commit()
#        db.refresh(usuario_add)
#        return usuario_add
#
#@app.post("/usuario/", response_model=UsuarioCreate)
#async def create_user(usuario: UsuarioCreate, db: Session = Depends(get_db)):
#   user = Usuario(**usuario.dict())
#   db.add(user)
#   db.commit()
#   db.refresh(user)
#   return user
#
#
#
#
#@app.get("/usuario/{email}")
#def get_usuario_by_email(email: str, db: Session = Depends(get_db)):
#    usuario = db.query(Usuario).filter(Usuario.Email == email).first()
#    if not usuario:
#        raise HTTPException(status_code=404, detail="Usuario no encontrado")
#    return UsuarioOut(Id=usuario.Id, Nombre=usuario.Nombre, Apellido=usuario.Apellido,
#                      User_name=usuario.User_name, Email=usuario.Email).dict()
#
#
#@ app.get("/usuarios/{email}")
#def get_usuarios_by_email(email: str, db: Session = Depends(get_db)):
#    usuarios = db.query(Usuario).filter(Usuario.Email == email).all()
#    if not usuarios:
#        raise HTTPException(status_code=404, detail="Usuario no encontrado")
#    return [UsuarioOut(Id=usuario.Id, Nombre=usuario.Nombre, Apellido=usuario.Apellido,
#                      User_name=usuario.User_name, Email=usuario.Email).dict() for usuario in usuarios]
#
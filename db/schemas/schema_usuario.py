from pydantic import BaseModel
from typing import Union

class UsuarioCreate(BaseModel):
    Nombre: str
    Apellido: str
    User_name: str
    Password: str
    Email: str
    class Config:
        orm_mode = True
        
class UsuarioOut(BaseModel):
    Id: Union[int, None] = None
    Nombre: Union[str, None] = None
    Apellido: Union[str, None] = None
    User_name: str
    Email: Union[str, None] = None
    Password : Union[str, None] = None
    class Config:
        orm_mode = True


class UserInDB(UsuarioOut):
    Password: str



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
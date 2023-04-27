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
    class Config:
        orm_mode = True


class UserInDB(UsuarioOut):
    Password: str

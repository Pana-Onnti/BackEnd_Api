from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    Nombre: str
    Apellido: str
    User_name: str
    Password: str
    Email: str
from sqlalchemy import Column, Integer, String,Float
from db.models.database import Base


class Usuario(Base):
    __tablename__ = "Usuarios"
    Id_Usuario = Column(Integer, primary_key=True,autoincrement=True)
    Nombre = Column(String)
    Apellido = Column(String)
    User_name = Column(String)
    Password = Column(String)
    Email = Column(String)

class Cuenta(Base):
    __tablename__ = "Cuentas"
    Id_Cuenta = Column(Integer, primary_key=True)
    Id_Estado = Column(Integer)
    Id_Usuario = Column(Integer)
    Balance = Column(Integer)
    Id_Trade = Column(String)
class Trade(Base):
    __tablename__ = "Trades"
    Id_Trade = Column(Integer, primary_key=True)
    Fecha_Entrada = Column(Integer)
    Fecha_Salida = Column(Integer)
    Direccion = Column(Integer)
    Precio_Entrada = Column(Float(asdecimal=True))
    Precio_Salida = Column(Float(asdecimal=True))
    Comision = Column(Float(asdecimal=True))
    Id_Notas = Column(Integer)
    Estado = Column(Integer)
    Id_Cuenta = Column(String)
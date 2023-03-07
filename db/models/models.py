from sqlalchemy import Column, Integer, String,Float , ForeignKey,Boolean,DateTime
from db.database import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "Usuarios"
    Id = Column(Integer, primary_key=True,autoincrement=True)
    Nombre = Column(String)
    Apellido = Column(String)
    User_name = Column(String)
    Password = Column(String)
    Email = Column(String)
    #
    cuentas = relationship("Cuenta" , back_populates='usuario' )
    #
class Cuenta(Base):
    __tablename__ = "Cuentas"
    Id = Column(Integer, primary_key=True,autoincrement=True)
    Id_Estado = Column(Integer)
    Balance = Column(Integer)
    #
    Id_Usuario = Column(Integer,ForeignKey('Usuarios.Id'))
    #
    usuario = relationship("Usuario", back_populates='cuentas')
    
    trades = relationship ('Trade', back_populates=('cuenta'))

class Trade(Base):
    __tablename__ = "Trades"
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Ticker = Column(String)
    Fecha_Entrada = Column(DateTime)
    Fecha_Salida = Column(DateTime)
    Precio_Entrada = Column(Float(asdecimal=True))
    Precio_Salida = Column(Float(asdecimal=True))
    Direccion = Column(Integer)
    Comision = Column(Float(asdecimal=True))
    Id_Notas = Column(Integer)
    Estado = Column(Integer)
    Id_Cuenta = Column(Integer,ForeignKey('Cuentas.Id'))
    cuenta = relationship('Cuenta',back_populates='trades')






from sqlalchemy.orm import Session
from db.models.models import Usuario,Cuenta,Trade
from schemas.schemas import UsuarioCreate,CuentaCreate
#operacion sobre usuario
def get_user(db:Session,usuario_id:int):
    return db.query(Usuario).filter(Usuario.Id == usuario_id).first()

def get_user_by_email(db:Session,usuario_email:str):
    return db.query(Usuario).filter(Usuario.Email==usuario_email).first()

def get_users(db:Session, skip: int=0 , limit: int=100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def create_user_(db:Session, usuario:UsuarioCreate):
#    fake_hashed_password = usuario.Password 
    db_user = Usuario(**usuario.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
#operaciones sobre cuentas

def get_cuentas(db:Session, skip: int=0 , limit: int=100):
    return db.query(Cuenta).offset(skip).limit(limit).all()

def create_user_cuenta(db: Session, cuenta: CuentaCreate, user_id: int):
    db_cuenta = Cuenta(**cuenta.dict(),Id_Usuario=user_id)
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta

############


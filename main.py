from fastapi import FastAPI,Depends
from db.database import Base,engine
from sqlalchemy.orm import Session
from routes import usuarios_router 
from routes import cuentas_router
from routes import trades_router
from routes import basic_auth_users


def create_tables():
    Base.metadata.create_all(bind=engine)
    
create_tables()

app = FastAPI()

app.include_router(usuarios_router.router)
app.include_router(cuentas_router.router)
app.include_router(trades_router.router)
app.include_router(basic_auth_users.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}









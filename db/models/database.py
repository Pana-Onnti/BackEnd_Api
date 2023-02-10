from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL='postgresql://123:123@localhost:5432/1'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base= declarative_base()
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

def get_db():
    db=SessionLocal()
    try:
        yield db
        db.commit()
    finally:
        db.close()

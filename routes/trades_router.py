from fastapi import APIRouter,Depends
from db.database import get_db
from sqlalchemy.orm import Session
from db.models.models import Trade
from db.schemas.schema_trade import TradeCreate,TradeOut
from fastapi.responses import JSONResponse

#set endpoint
router = APIRouter(
    prefix="/trades",
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)
# Crear #

@router.post('/crear/',response_model=TradeCreate)
async def crear_trade(trade:TradeCreate,db:Session=Depends(get_db)):  
    nuevo_trade = Trade(**trade.dict())
    db.add(nuevo_trade)
    db.commit()
    db.refresh(nuevo_trade)
    return nuevo_trade

#Devolver todos los trades#
@router.get("/trades")
def get_trades(db: Session = Depends(get_db)):
    trades = db.query(Trade).all()
    return [TradeOut(**trade.__dict__).dict() for trade in trades]

## fecha de entrada es cualquier propiedad

@router.get("/{Fecha_Entrada}/")
def get_fechas_entrada(db: Session = Depends(get_db)):
    trades = db.query(Trade).all()
    fechas = [trade.Fecha_Entrada for trade in trades]
    return JSONResponse(content={"fechas": fechas})

@router.get("/trades/{attribute}")
def get_trade_attribute(attribute: str, db: Session = Depends(get_db)):
    trades = db.query(Trade).all()
    filtered_attribute = [getattr(trade, attribute) for trade in trades]
    return JSONResponse(content={"attribute": filtered_attribute})
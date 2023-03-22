from fastapi import APIRouter,Depends
from db.database import get_db
from sqlalchemy.orm import Session
from db.models.models import Trade
from db.schemas.schema_trade import TradeOut  ,Email ,TradeDict
from crud import *
#set endpoint
router = APIRouter(
    prefix="/trades",
    tags=["Trades"],
    responses={404: {"description": "Not found"}},
)
# Crear #



@router.post('/crear/',response_model=TradeDict) 
async def crear_trade(email:str,trade:TradeDict,db:Session=Depends(get_db)):
    usuario = validar_usuario_cuenta(db,email)
    db_trade = trade_nuevo(db,trade,email)
    return db_trade


@router.get("/obtener_trades_cuenta")
async def obtener_trades_cuenta(email: str, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_email_db(db, email)
    if usuario is None:
        return {"mensaje": "Usuario no encontrado"}
    trades = [] 
    for cuenta in usuario.cuentas:
        trades_cuenta = [TradeDict.from_orm(trade) for trade in cuenta.trades]
        trades.append(trades_cuenta)
    return trades
 



#
#
#Devolver todos los trades#
@router.get("/trades")
async def get_trades(db: Session = Depends(get_db)):
    trades = db.query(Trade).all()
    return [TradeOut(**trade.__dict__).dict() for trade in trades]


### fecha de entrada es cualquier propiedad
#
#@router.get("/{Fecha_Entrada}/")
#async def get_fechas_entrada(db: Session = Depends(get_db)):
#    trades = db.query(Trade).all()
#    fechas = [trade.Fecha_Entrada for trade in trades]
#    return JSONResponse(content={"fechas": fechas})
#
#@router.get("/trades/{attribute}")
#async def get_trade_attribute(attribute: str, db: Session = Depends(get_db)):
#    trades = db.query(Trade).all()
#    filtered_attribute = [getattr(trade, attribute) for trade in trades]
#    return JSONResponse(content={"attribute": filtered_attribute})

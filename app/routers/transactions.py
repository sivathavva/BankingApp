from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..dependencies import get_db

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/", response_model=schemas.Transaction)
def create_transaction(account_id: int, transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, account_id, transaction)

# Additional endpoints for viewing transactions can be added here. 
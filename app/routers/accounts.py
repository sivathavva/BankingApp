from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..dependencies import get_db

router = APIRouter(prefix="/accounts", tags=["accounts"])

@router.post("/", response_model=schemas.Account)
def create_account(user_id: int, db: Session = Depends(get_db)):
    return crud.create_account(db, user_id)

# Additional endpoints for editing, deleting, and viewing accounts would be added here, with appropriate permission checks. 
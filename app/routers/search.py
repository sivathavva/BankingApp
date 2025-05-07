from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/search", tags=["search"])

@router.get("/by-ssn/{ssn}", response_model=schemas.User)
def search_by_ssn(ssn: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.ssn == ssn).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Additional endpoints for account holders to search their own info/transactions can be added here. 
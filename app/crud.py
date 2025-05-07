from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        hashed_password=hashed_password,
        is_employee=user.is_employee,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        ssn=user.ssn
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_account(db: Session, user_id: int):
    db_account = models.Account(user_id=user_id)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def create_transaction(db: Session, account_id: int, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(
        account_id=account_id,
        amount=transaction.amount,
        type=transaction.type
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction 
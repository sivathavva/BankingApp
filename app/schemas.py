from pydantic import BaseModel, EmailStr, constr
from typing import Optional, List
import datetime

class TransactionBase(BaseModel):
    amount: float
    type: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    timestamp: datetime.datetime

    class Config:
        orm_mode = True

class AccountBase(BaseModel):
    balance: float = 0.0

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    transactions: List[Transaction] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: EmailStr
    is_employee: bool = False

class UserCreate(UserBase):
    password: constr(min_length=10)
    ssn: Optional[str]

class User(UserBase):
    id: int
    accounts: List[Account] = []

    class Config:
        orm_mode = True 
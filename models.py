from pydantic import BaseModel
from typing import List
from datetime import datetime

class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class TransactionCreate(BaseModel):
    type: str  # 'deposit' or 'withdrawal'
    amount: float
    account_id: int

class Transaction(BaseModel):
    id: int
    type: str
    amount: float
    date: datetime
    account_id: int

class Account(BaseModel):
    id: int
    balance: float
    transactions: List[Transaction] = []
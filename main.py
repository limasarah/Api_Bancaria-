from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta, datetime
from typing import List
from models import *
from auth import *

app = FastAPI(title="Banking API", description="API for managing bank accounts and transactions with JWT authentication")

# Simular banco de dados com dicionários e listas
accounts = {}
transactions = []
account_counter = 1
transaction_counter = 1

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/accounts", response_model=Account)
async def create_account():
    global account_counter
    account = Account(id=account_counter, balance=0.0)
    accounts[account.id] = account
    account_counter += 1
    return account

@app.post("/transactions", response_model=Transaction)
async def create_transaction(transaction: TransactionCreate, current_user: dict = Depends(get_current_user)):
    if transaction.account_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    account = accounts[transaction.account_id]
    if transaction.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    if transaction.type == "withdrawal":
        if account.balance < transaction.amount:
            raise HTTPException(status_code=400, detail="Insufficient balance")
        account.balance -= transaction.amount
    elif transaction.type == "deposit":
        account.balance += transaction.amount
    else:
        raise HTTPException(status_code=400, detail="Invalid transaction type")
    global transaction_counter
    trans = Transaction(
        id=transaction_counter,
        type=transaction.type,
        amount=transaction.amount,
        date=datetime.utcnow(),
        account_id=transaction.account_id
    )
    transactions.append(trans)
    account.transactions.append(trans)
    transaction_counter += 1
    return trans

@app.get("/accounts/{account_id}/statement", response_model=List[Transaction])
async def get_statement(account_id: int, current_user: dict = Depends(get_current_user)):
    if account_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    return accounts[account_id].transactions
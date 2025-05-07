from fastapi import FastAPI
from .routers import users, accounts, transactions, search

app = FastAPI()

app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(search.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Banking Backend API"} 
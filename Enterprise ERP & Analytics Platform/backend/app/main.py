
from fastapi import FastAPI
from app.api import auth, employees

app = FastAPI(title="Enterprise ERP Platform")

app.include_router(auth.router)
app.include_router(employees.router)

@app.get("/")
def root():
    return {"message": "ERP Platform Running"}

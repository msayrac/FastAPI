"""
HTTP Request Methods
GET : Read Resource
POST : Create Resource
Put : Update /Replace Resource
Delete : Delete Resource

CRUD Create Read Update Delete
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_api():
    return {"Welcome" : "Eric"}
















from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    name: str
    age: int
    salary: int


@app.get("/")
def home():
    return 'Zain'


@app.post("/predict")
def item(record: Data):
    return record.name

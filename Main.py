from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()


with open('', 'rb') as f:
    pickle.load(f)


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

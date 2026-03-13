from fastapi import FastAPI
import json

app = FastAPI()

from pathlib import Path

def data_loader():
    path = Path(__file__).parent / "patient_data.json"
    with open(path, "r") as f:
        return json.load(f)

@app.get('/')
def title():
    return {'message': 'Relief APP'}

@app.get('/about')
def about():
    return {'message': "A fully functional API to manager your patient's data"}

@app.get('/view')
def view():
    data = data_loader()
    return data
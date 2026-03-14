from fastapi import FastAPI, Path, HTTPException
import json

app = FastAPI()

def data_loader():
    with open('patient_data.json', 'r') as f:
        data = json.load(f)
        return data

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

@app.get('/patient/{patient_id}')
def particualr_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    data = data_loader()

    for key, value in data.items():
        if patient_id in key:
            return value
    return HTTPException(status_code=404, detail='Patient not found')
from pydantic import BaseModel, computed_field, Field, EmailStr
from typing import TypedDict, List, Dict

class patient_data(BaseModel):
    name: str
    age: int
    height: float
    weight: float
    married: bool
    email: EmailStr = Field(..., description='provide your email in valide format')
    allergies: List[str]
    contect_detail: Dict[str, str]

    @computed_field
    @property
    def bmi_calculated(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
    
def output(patient: patient_data):
    print(patient.name)
    print(patient.age)
    print(patient.height)
    print(patient.weight)
    print(patient.married)
    print(patient.email)
    print(patient.allergies)
    print(patient.contect_detail)
    print('BMI', patient.bmi_calculated)

user_input = {'name': 'adnan saeed', 'age': 70, 'email': 'saeedadnan151@gmail.com', 'weight': 88.9, 'height': 6.2, 'allergies':['dust', 'sun'], 'contect_detail': {'emergency': '03155682476', 'name': 'brother'}, 'married': True}

patient = patient_data(**user_input)

output(patient)
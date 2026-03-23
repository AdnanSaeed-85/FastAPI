from pydantic import model_validator, BaseModel, EmailStr, Field
from typing import TypedDict, List, Dict

class pydantic_elements(BaseModel):
    name: str
    age: int
    email: EmailStr = Field(..., description='just put email in valid format')
    weight: float
    height: float
    allergies: List[str]
    contect_detail: Dict[str, str]

    @model_validator(mode='after')
    def model_validator_fun(cls, model):
        if model.age > 60 and 'emergency' not in model.contect_detail:
            raise ValueError('patients older than 60 should must have emergency contact')
        return model

def output(patient: pydantic_elements):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print(patient.allergies)
    print(patient.contect_detail)

user_input = {'name': 'adnan saeed', 'age': 70, 'email': 'saeedadnan151@gmail.com', 'weight': 88, 'height': 6.2, 'allergies':['dust', 'sun'], 'contect_detail': {'emergency': '03155682476', 'name': 'brother'}}

patient = pydantic_elements(**user_input)

output(patient)
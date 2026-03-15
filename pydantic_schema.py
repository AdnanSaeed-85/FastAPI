from typing import List, Dict
from pydantic import BaseModel, EmailStr, AnyUrl

class schema(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin: AnyUrl
    smooker: bool
    weight: float
    height: float
    allergies: List[str]
    content_details: Dict[str, str]

def patient_detail(Schema: schema):
    print(Schema.name)
    print(Schema.age)
    print(Schema.email)
    print(Schema.smooker)
    print(Schema.weight)
    print(Schema.height)
    print(Schema.allergies)
    print(Schema.content_details)
    print(Schema.linkedin)

detail = {'name': 'adnan', 'age': 23, 'smooker': True, 'email': 'saeedadnan151@gmail.com', 'weight': 88.3, 'height': 6.2, 'allergies': ['dust', 'foog'], 'content_details': {'phone': '3155682476', 'cnic': '4250118129795'}, 'linkedin': 'https://linkedin.com/adnansaeed'}

pydantic_obj = schema(**detail)

patient_detail(pydantic_obj)
from typing import List, Dict, Annotated
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator

class schema(BaseModel):
    name: str
    age: int = Field(..., description="user's age", ge=20, le=40)
    email: EmailStr
    linkedin: AnyUrl
    smooker: bool
    weight: float
    height: Annotated[float, Field(..., title='Height', description='Height of the patient', strict=True, examples=[6.1, 5.6, 5.9, 6.0])]
    allergies: List[str]
    content_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def custom_email(cls, value):
        valid_email = ['gov.com', 'edu.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_email:
            raise ValueError('Not a valid domain')
        return value
        
    @field_validator('name')
    @classmethod
    def custom_name(cls, value):
        return value.upper()

    @field_validator('age', mode='before')
    @classmethod
    def custom_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('age should between 0-100')


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

detail = {'name': 'adnan', 'age': '40', 'smooker': True, 'email': 'saeedadnan151@edu.com', 'weight': 88.3, 'height': 6.2, 'allergies': ['dust', 'foog'], 'content_details': {'phone': '3155682476', 'cnic': '4250118129795'}, 'linkedin': 'https://linkedin.com/adnansaeed'}

pydantic_obj = schema(**detail)

patient_detail(pydantic_obj)
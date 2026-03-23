from pydantic import BaseModel

class Address(BaseModel):
    house_num: int
    postal_code: int
    city: str

class patient(BaseModel):
    name: str
    age: int
    marriede: bool
    address: Address

def output(user_data: patient):
    print(user_data.name)
    print(user_data.age)
    print(user_data.marriede)
    print(user_data.address.city)

patient_address = {'house_num': 12, 'postal_code': 22640, 'city': 'haripur'}
address_obj = Address(**patient_address)

patient_data = {'name': 'Adnan Saeed', 'age': 23, 'marriede': False, 'address': address_obj}
data_obj = patient(**patient_data)

output(data_obj)
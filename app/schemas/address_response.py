from pydantic import BaseModel

class AddressResponse(BaseModel):
    name:str
    street: str
    city: str
    state: str
    pincode: str


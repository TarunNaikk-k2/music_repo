from pydantic import BaseModel

class AddressCreate(BaseModel):

    name: str

    street:str

    city:str

    state:str

    pincode:str
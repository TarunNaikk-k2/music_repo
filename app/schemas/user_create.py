from pydantic import BaseModel
from typing import List

from app.schemas.address_schema import AddressCreate

class UserCreate(BaseModel):

    first_name: str

    last_name: str

    email: str

    password: str
    
    phone_number: str

    role: str

    addresses: List[AddressCreate] =[]
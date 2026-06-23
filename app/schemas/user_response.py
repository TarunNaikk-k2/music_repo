from pydantic import BaseModel
from typing import List
from app.schemas.address_schema import AddressCreate
from pydantic import ConfigDict

class UserResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    first_name: str
    last_name: str

    email: str

    phone_number: str

    role: str

    addresses: List[AddressCreate]



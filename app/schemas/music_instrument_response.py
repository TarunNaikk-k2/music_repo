from pydantic import BaseModel


class MusicInstrumentResponse(BaseModel):


    name: str

    category: str

    price: float

    quantity: int


from pydantic import BaseModel


class MusicInstrumentCreate(BaseModel):

    name: str

    category: str

    price: float

    quantity: int




from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from app.database import Base
from sqlalchemy import Float

class Music_Instrument(Base):
    __tablename__ = "music_instruments"

    id=Column(Integer,primary_key=True)

    name=Column(String)

    category=Column(String)

    price=Column(Float)

    quantity = Column(Integer)

    
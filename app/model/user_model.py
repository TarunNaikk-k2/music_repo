from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database import Base

class User(Base):

    __tablename__="users"

    id = Column(Integer,primary_key=True)

    first_name = Column(String)
    last_name = Column(String)

    email=Column(String,unique=True)

    phone_number=Column(String)
    role=Column(String)

    addresses = relationship(
        "Address",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    password=Column(String)

    

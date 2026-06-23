from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Address(Base):
    __tablename__ = "addresses"

    id=Column(Integer,primary_key=True)

    name=Column(String)

    street = Column(String)

    city = Column(String)

    state = Column(String)

    pincode = Column(String)

    user_id = Column(
        Integer,
        ForeignKey("users.id")

    )

    user = relationship(
        "User",
        back_populates="addresses"
    )
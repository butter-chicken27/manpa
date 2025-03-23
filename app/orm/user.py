from sqlalchemy import Column, Integer, String
from orm.base import Base

class DBUser(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String, nullable=True)
    lastName = Column(String, nullable=True)
from models.engine.db_connection import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Party(Base):
    __tablename__ = 'party'

    id = Column(Integer, primary_key=True, autoincrement=True)
    partyid = Column(String(255), unique=True, nullable=False)
    partyname = Column(String(255), nullable=False)
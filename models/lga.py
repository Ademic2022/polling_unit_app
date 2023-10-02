from models.engine.db_connection import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Lga(Base):
    __tablename__ = 'lga'

    uniqueid = Column(Integer, primary_key=True)
    lga_id = Column(Integer)
    lga_name = Column(String(50))
    state_id = Column(Integer)
    lga_description = Column(Text)
    entered_by_user = Column(String(50))
    date_entered = Column(DateTime)
    user_ip_address = Column(String(50))
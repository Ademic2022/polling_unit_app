from models.engine.db_connection import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class PollingUnit(Base):
    __tablename__ = 'polling_unit'

    uniqueid = Column(Integer, primary_key=True)
    polling_unit_id = Column(Integer)
    ward_id = Column(Integer)
    lga_id = Column(Integer)
    uniquewardid = Column(Integer)
    polling_unit_number = Column(String(50))
    polling_unit_name = Column(String(50))
    polling_unit_description = Column(Text)
    lat = Column(String(255))
    long = Column(String(255))
    entered_by_user = Column(String(50))
    date_entered = Column(DateTime)
    user_ip_address = Column(String(50))
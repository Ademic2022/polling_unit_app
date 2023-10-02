from models.engine.db_connection import Base
from sqlalchemy import Column, Integer, String


class AnnouncedPuResult(Base):
    __tablename__ = 'announced_pu_results'

    result_id = Column(Integer, primary_key=True)
    polling_unit_uniqueid = Column(Integer)
    party_abbreviation = Column(String(4))
    party_score = Column(Integer)
    entered_by_user = Column(String(50))
    date_entered = Column(String(50))
    user_ip_address = Column(String(50))
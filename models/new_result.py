from sqlalchemy import Column, Integer, String, JSON
from models.engine.db_connection import Base


class Result(Base):
    __tablename__ = 'result'

    id = Column(Integer, primary_key=True, autoincrement=True)
    polling_unit_name = Column(String(128), nullable=False)
    pdp = Column(Integer, nullable=False, default=0)
    dpp = Column(Integer, nullable=False, default=0)
    acn = Column(Integer, nullable=False, default=0)
    ppa = Column(Integer, nullable=False, default=0)
    cdc = Column(Integer, nullable=False, default=0)
    jp = Column(Integer, nullable=False, default=0)
    anpp = Column(Integer, nullable=False, default=0)
    labour = Column(Integer, nullable=False, default=0)
    cpp = Column(Integer, nullable=False, default=0)

    def __init__(self, polling_unit_name, pdp, dpp, acn, ppa, cdc, jp, anpp, labour, cpp):
        self.polling_unit_name = polling_unit_name
        self.pdp = pdp
        self.dpp = dpp
        self.acn = acn
        self.ppa = ppa
        self.cdc = cdc
        self.jp = jp
        self.anpp = anpp
        self.labour = labour
        self.cpp = cpp

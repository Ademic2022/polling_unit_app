""" new class for sqlAlchemy """
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""This module defines the DBStorage class for handling database operations."""
class DBStorage():
    """Initialize the DBStorage class."""
    def __init__(self):
        """initializing session and engine"""
        self.__engine = None
        self.__session = None
        self.__setup_engine()
        self.__create_session() #initialize the session


    def __setup_engine(self):
        """Set up the SQLAlchemy engine based on environment variables."""
        user = 'root'
        database_pwd = 'root'
        database = 'bincomphptest'
        host = 'localhost'
        env = 'db'

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{database_pwd}@{host}/{database}',
            pool_pre_ping=True
        )

    def __create_session(self):
        """Create a session with the SQLAlchemy engine."""
        if self.__session is None:
            sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = scoped_session(sec)
        return self.__session()

    def new(self, obj):
        """add new object"""
        session = self.__create_session()
        session.add(obj)

    def save(self):
        """save objects in the database"""
        session = self.__create_session()
        session.commit()

    def delete(self, obj=None):
        """delete method--delete from database"""
        session = self.__create_session()
        if obj:
            session.delete(obj)
    def update(self, obj):
        """update database"""
        session = self.__create_session()
        session.merge(obj)  # Use the merge method to update the object
        session.commit()

    def count(self, class_name, id):
        """count objects in the database"""
        
        pass

    def get_polling_unit(self):
        """get polling unit"""
        from models.polling_unit import PollingUnit
        session = self.__create_session()
        query = session.query(PollingUnit).all()
        return query
    
    def get_polling_unit_by_id(self, polling_unit_id):
        """get polling unit by id"""
        from models.polling_unit import PollingUnit
        session = self.__create_session()
        query = session.query(PollingUnit).filter_by(polling_unit_id=polling_unit_id).first()
        return query

    def get_polling_units_by_ids(self, polling_unit_ids):
        """Get polling units by their IDs."""
        from models.polling_unit import PollingUnit
        session = self.__create_session()
        polling_units = session.query(PollingUnit).filter(PollingUnit.polling_unit_id.in_(polling_unit_ids)).all()
        return polling_units


    def get_polling_unit_results(self, polling_unit):
        """get polling unit"""
        from models.announced_pu_result import AnnouncedPuResult
        session = self.__create_session()
        query = session.query(AnnouncedPuResult).filter_by(polling_unit_uniqueid=polling_unit).all()
        return query
    
    def get_lga(self):
        """get polling unit"""
        from models.lga import Lga
        session = self.__create_session()
        query = session.query(Lga).all()
        return query

    def reload(self):
        """reload database session"""
        Base.metadata.create_all(self.__engine)
        self.__create_session()

    def close(self):
        """close database session"""
        if self.__session:
            self.__session.remove()
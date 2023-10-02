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
        import importlib
        # Import the module containing the class dynamically
        module = importlib.import_module('models.' + class_name.lower())
        # Get the class from the module
        cls = getattr(module, class_name)

        session = self.__create_session()
        query = session.query(cls).filter_by(family_id=id, status=0).all()
        
        count = len(query)  # count the objects in the list
        return count

    def get_polling_unit(self):
        """get polling unit"""
        session = self.__create_session()
        query = session.query().all()
        return query

    def reload(self):
        """reload database session"""
        Base.metadata.create_all(self.__engine)
        self.__create_session()

    def close(self):
        """close database session"""
        if self.__session:
            self.__session.remove()
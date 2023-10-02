"""get the storage type configuration """
storage_env = 'db'

if storage_env == 'db':
    """ import and create an instance of DBStorage class """
    from models.engine.db_connection import DBStorage
    storage = DBStorage()
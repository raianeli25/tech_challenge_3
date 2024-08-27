import logging
from typing import Any
from sqlalchemy import create_engine

class DBInterface():
    def __init__(self, user:str, password:str, db_name:str, hostname:str) -> None:
        logging.info('Instatiate DBInterface class')
        self.user:str = user
        self.password:str = password
        self.db_name:str = db_name
        self.hostname:str = hostname
    
    def create_connection_string(self)->str:
        conn_string = 'postgresql+psycopg2://'+\
                            self.user+':'+self.password+'@'+\
                            self.hostname+'/'+self.db_name
        print("Connection String:"+conn_string)
        logging.info("Connection String:"+conn_string)
        return conn_string

    def get_connection_engine(self)->Any:
        conn_string = self.create_connection_string()
        print("Creating SQLAlchemy Engine...")
        logging.info("Creating SQLAlchemy Engine...")
        return create_engine(conn_string)


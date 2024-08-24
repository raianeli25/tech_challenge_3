import pytest

from .db_interfaces import DBInterface
from .db_definitions import DatabaseDefs

from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

db_defs = DatabaseDefs()
db_interface = DBInterface(
    user=db_defs.POSTGRES_USER,
    password=db_defs.POSTGRES_PASSWORD,
    db_name=db_defs.POSTGRES_DB,
    hostname=db_defs.POSTGRES_HOST
)

COL_NAME = 'Name'
COL_AGE = 'Age'
COL_CITY = 'City'

TEST_NAME = 'Alice'
TEST_AGE = 25
# Sample data for the DataFrame
data = {
    COL_NAME: [TEST_NAME, 'Bob', 'Charlie'],
    COL_AGE: [TEST_AGE, 30, 35],
    COL_CITY: ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
TABLE_NAME = 'test_table'

def test_conn_engine_creation():
    print("Starting Engine Connection Test")
    conn_status_ok_flag:bool = False
    try:
        conn_engine = db_interface.get_connection_engine()
        conn_engine.connect()
        conn_status_ok_flag = True
        print("Connection Passed")
    except SQLAlchemyError as err:
        print("Connection Failed. Error:", err.__cause__)
    assert conn_status_ok_flag == True

def test_insert_data_into_psql():
    insert_status_ok_flag:bool = False
    try:
        conn_engine = db_interface.get_connection_engine()
        print(f"Inserting df data into {db_defs.POSTGRES_DB}.{TABLE_NAME}")
        df.to_sql(TABLE_NAME, con=conn_engine, if_exists='replace', index=False)
        print("Data has been inserted to the Database.Table")
        insert_status_ok_flag = True
    except SQLAlchemyError as err:
        print("Connection Failed. Error:", err.__cause__)
    assert insert_status_ok_flag == True

def test_select_data_from_psql():
    select_status_ok_flag:bool = False
    try:
        conn_engine = db_interface.get_connection_engine()
        print(f"Inserting df data into {db_defs.POSTGRES_DB}.{TABLE_NAME}")
        df.to_sql(TABLE_NAME, con=conn_engine, if_exists='replace', index=False)
        print("Data has been inserted to the Database.Table")
        query = "SELECT * FROM "+TABLE_NAME
        print(f"Running query: {query}")
        df_sql = pd.read_sql(query,con=conn_engine)
        select_status_ok_flag = df_sql[COL_AGE][df_sql[COL_NAME]==TEST_NAME][0] == TEST_AGE
        print(df_sql[COL_AGE][df_sql[COL_NAME]==TEST_NAME][0])
        print(select_status_ok_flag)
    except SQLAlchemyError as err:
        print("Connection Failed. Error:", err.__cause__)
    assert select_status_ok_flag == True
    
    
    



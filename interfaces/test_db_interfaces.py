# import pytest
# from .db_interfaces import DBInterface
from db_interfaces import DBInterface
from db_definitions import DatabaseDefs
import pandas as pd

db_defs = DatabaseDefs()
db_interface = DBInterface(
    user=db_defs.POSTGRES_USER,
    password=db_defs.POSTGRES_PASSWORD,
    db_name=db_defs.POSTGRES_DB,
    hostname=db_defs.POSTGRES_HOST
)

# print(db_interface.user)

conn_str = db_interface.create_connection_string()
conn_engine = db_interface.get_connection_engine()
print("Connection Engine created successfully")

# Sample data for the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DF:")
print(df)

TABLE_NAME = 'test_table'

print(f"INSERTING df data into {db_defs.POSTGRES_DB}.{TABLE_NAME}")
df.to_sql(TABLE_NAME, con=conn_engine, if_exists='replace', index=False)
print("Data has been inserted to the Database.Table")

query = "SELECT * FROM "+TABLE_NAME

print(f"Running query: {query}")
print(pd.read_sql(query,con=conn_engine))
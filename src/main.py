import logging

import pandas as pd

from fastapi import FastAPI

from interfaces.db_definitions import DatabaseDefs
from interfaces.db_interfaces import DBInterface

db_defs = DatabaseDefs()
db_interface = DBInterface(
    user=db_defs.POSTGRES_USER,
    password=db_defs.POSTGRES_PASSWORD,
    db_name=db_defs.POSTGRES_DB,
    hostname=db_defs.POSTGRES_HOST
)

CSV_FILE = "./data/spotify_raw_dataset.csv"
TABLE_NAME = "Spotify_Songs"

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='w',
    filename="mainlog.log", 
    encoding='utf-8', 
    level=logging.DEBUG
    )

logging.info('############## STARTING MAIN ##################')

app = FastAPI()

logging.info('Created instances of FatAPI')

@app.get("/")
async def home():
    return "Hello World!!"

@app.get("/connect_db")
async def connect_db():
    try:
        conn_engine = db_interface.get_connection_engine()
        conn_engine.connect()
        return "Connection Passed"
    except:
        return "Connection Failed"
    
@app.get("/load_data_to_db")
async def load_data_to_db():
    try:
        spotify_df = pd.read_csv(CSV_FILE)
        conn_engine = db_interface.get_connection_engine()
        n_rows = spotify_df.to_sql(TABLE_NAME, con=conn_engine, if_exists='replace', index=False)
        return f"The file {CSV_FILE} has been loaded to psql database. !{n_rows}!"
    except:
        return "Ops! Something went wrong!"

@app.get("/count_total_rows_db")
async def count_total_rows_db():
    try:
        conn_engine = db_interface.get_connection_engine()
        sql_str = f'SELECT count(*) AS count_1 FROM "{TABLE_NAME}"'
        df = pd.read_sql(sql_str,con=conn_engine)
        return f"Total number of rows = {df['count_1'][0]}"
    except:
        return "Ops! Something went wrong!"




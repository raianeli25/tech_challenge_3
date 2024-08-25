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

CSV_FILE = "/data/spotify_raw_dataset.csv"

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
        # conn_engine = db_interface.get_connection_engine()
        spotify_df = pd.read_csv(CSV_FILE)
        # return {spotify_df.to_dict()}
        return "OK3!"
    except:
        return "Ops! Something went wrong!"





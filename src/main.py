import logging

from fastapi import FastAPI
import psycopg2

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

        conn = psycopg2.connect("host=db dbname=postgres user=postgres password=postgres")

        return "Conexão OK"
    
    except:

        return "Conexão FAIL"




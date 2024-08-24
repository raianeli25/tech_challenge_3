from pydantic import BaseModel

class DatabaseDefs(BaseModel):
    POSTGRES_USER:str = 'pguser'
    POSTGRES_PASSWORD:str = 'pgpass'
    POSTGRES_DB:str = 'pgdb'
    POSTGRES_HOST:str = 'localhost'
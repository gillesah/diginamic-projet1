from sqlalchemy import create_engine, ForeignKey, String, select
from sqlalchemy.orm import DeclarativeBase
from decouple import config

class Base(DeclarativeBase):
    pass


engine = None


# CONNEXION

connector = "mysql+pymysql"
user = config("DB_USER")
password = config("DB_PSWD")
host = config("DB_HOST")
database = "BDD_projet_client"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")
conn = engine.connect()

# créer les tables
class Base(DeclarativeBase):
    pass

Base.metadata.create_all(engine)
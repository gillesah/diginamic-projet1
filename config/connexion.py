from sqlalchemy import create_engine, ForeignKey, String, select
from sqlalchemy.orm import DeclarativeBase
from decouple import config
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass


engine = None


# CONNEXION

connector = "mysql+pymysql"
user = config("DB_USER")
password = config("DB_PSWD")
host = config("DB_HOST")
database = "Librairie"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")
conn = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# créer les tables


class Base(DeclarativeBase):
    pass


Base.metadata.create_all(engine)

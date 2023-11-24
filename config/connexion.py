from sqlalchemy import create_engine, ForeignKey, String, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from decouple import config


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

# Gilles
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Session = sessionmaker(bind=engine)

# Fonction pour donner la connexion à la BDD aux routes.
def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()

# créer les tables
class Base(DeclarativeBase):
    pass


Base.metadata.create_all(engine)

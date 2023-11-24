from sqlalchemy import create_engine
from typing import Optional
from sqlalchemy import String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, sessionmaker
from config.connexion import Base, engine
from fastapi import FastAPI
from src.models.client import Client
from src.models.ouvrage import Ouvrage
# from models.theme import Theme
# from models.commentaire import Commentaire
# from models.theme_ouvrage import ThemeOuvrage
# ??? import src.router ???
from src.router.ouvrage_router import ouvrage_router
from src.router.client_router import client_router

Base.metadata.create_all(engine)


# appel FastApi
app = FastAPI()

# with Session(engine) as session:
#     trucmuch = Client(nom_client="BUDULE", prenom_client="christophe", email_client="email@email.com", telephone_client="000000",
#                       preferences_client="je suis la preference", adresse_livraison_client="adresse livraison", adresse_facturation_client="adresse facturation")
#     session.add_all([trucmuch])
#     print(trucmuch)
#     session.commit()

# router d'Ouvrage
app.include_router(ouvrage_router)
app.include_router(client_router)

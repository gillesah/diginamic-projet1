from sqlalchemy import create_engine
from typing import Optional
from sqlalchemy import String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from config.connexion import Base, engine
from models.client import Client
# from models.ouvrage import Ouvrage
# from models.theme import Theme
# from models.commentaire import Commentaire
#from models.theme_ouvrage import ThemeOuvrage

Base.metadata.create_all(engine)

with Session(engine) as session:
    trucmuch = Client("BUDULE", "christophe", "email@email.com", "000000", "je suis la preference", "adresse livraison", "adresse facturation")
    print(trucmuch)
    session.commit()

    
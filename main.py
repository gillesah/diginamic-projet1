from sqlalchemy import create_engine
from typing import Optional
from sqlalchemy import String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from config.connexion import Base, engine
from models.client import Client
# from models.ouvrage import Ouvrage
# from models.theme import Theme
# from models.commentaire import Commentaire
# from models.theme_ouvrage import ThemeOuvrage

Base.metadata.create_all(engine)

with Session(engine) as session:
    trucmuch = Client(nom_client="BUDULE", prenom_client="christophe", email_client="email@email.com", telephone_client="000000",
                      preferences_client="je suis la preference", adresse_livraison_client="adresse livraison", adresse_facturation_client="adresse facturation")
    print(trucmuch)
    session.commit()

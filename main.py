from sqlalchemy import create_engine
from typing import Optional
from sqlalchemy import String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, sessionmaker
from config.connexion import Base, engine
from fastapi import FastAPI
from src.models.client import Client
from src.models.ouvrage import Ouvrage
from src.models.commentaire import Commentaire
# from models.theme import Theme
# from models.commentaire import Commentaire
# from models.theme_ouvrage import ThemeOuvrage
# ??? import src.router ???
from src.router.ouvrage_router import ouvrage_router
from src.router.client_router import client_router
from src.router.commentaire_router import commentaire_router
import uvicorn

Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(ouvrage_router)
app.include_router(client_router)
app.include_router(commentaire_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

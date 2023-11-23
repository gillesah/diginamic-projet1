from config.connexion import Base
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Commentaire(Base):
    __tablename__ = "Commentaire"

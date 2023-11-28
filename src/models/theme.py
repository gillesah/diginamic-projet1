from config.connexion import Base
from sqlalchemy import String, ForeignKey, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
# from .theme_ouvrage import Theme_Ouvrage
from typing import List


class Theme(Base):
    __tablename__ = "Theme"
    id_theme: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)
    nom_theme: Mapped[str] = mapped_column(String(255))
    ouvrages: Mapped[list["Ouvrage"]] = relationship(secondary="theme_ouvrage", back_populates="themes")
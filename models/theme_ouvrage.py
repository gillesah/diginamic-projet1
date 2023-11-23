from config.connexion import Base
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ThemeOuvrage(Base):
    __tablename__ = "Theme_Ouvrage"
    id_ouvrage : Mapped[int] = mapped_column(ForeignKey("Ouvrage.id_ouvrage"),PRIMARY_KEY = True)
    id_theme  : Mapped[int] = mapped_column(ForeignKey("Theme.id_theme"), PRIMARY_KEY = True)

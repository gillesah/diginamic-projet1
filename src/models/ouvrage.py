from config.connexion import Base
from sqlalchemy import String, Date, Numeric, Integer, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from pydantic import BaseModel
from .theme_ouvrage import theme_ouvrage_association
from .theme import Theme
from typing import Optional, List


class Ouvrage(Base):
    __tablename__ = "Ouvrage"
    id_ouvrage: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)

    titre_ouvrage: Mapped[str] = mapped_column(String(255))
    auteur_ouvrage: Mapped[str] = mapped_column(String(255))
    isbn_ouvrage: Mapped[str] = mapped_column(String(20))
    langue_ouvrage: Mapped[str] = mapped_column(String(20))
    prix_ouvrage: Mapped[float] = mapped_column(Numeric(10, 2))
    date_parution_ouvrage: Mapped[Date] = mapped_column(Date)
    categorie_ouvrage: Mapped[str] = mapped_column(String(255))
    date_disponibilite_libraire_ouvrage: Mapped[Date] = mapped_column(Date)
    date_disponibilite_particulier_ouvrage: Mapped[Date] = mapped_column(Date)
    image_ouvrage: Mapped[str] = mapped_column(String(255))
    table_des_matieres_ouvrage: Mapped[str] = mapped_column(String(255))
    mot_cle_ouvrage: Mapped[str] = mapped_column(String(255))
    description_ouvrage: Mapped[str] = mapped_column(String(255))

    children: Mapped[List[Theme]] = relationship(secondary=theme_ouvrage_association)

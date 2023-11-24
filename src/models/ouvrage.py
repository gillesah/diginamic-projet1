from config.connexion import Base
from sqlalchemy import String, Date, Numeric, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from pydantic import BaseModel


class Ouvrage(Base):
    __tablename__ = "Ouvrage"
    id_ouvrage: Mapped[int] = Column(
        Integer, primary_key=True, autoincrement=True)
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


class OuvrageCreate(BaseModel):
    titre_ouvrage: str
    auteur_ouvrage: str
    isbn_ouvrage: str
    langue_ouvrage: str
    prix_ouvrage: float
    date_parution_ouvrage: date
    categorie_ouvrage: str
    date_disponibilite_libraire_ouvrage: date
    date_disponibilite_particulier_ouvrage: date
    image_ouvrage: str
    table_des_matieres_ouvrage: str
    mot_cle_ouvrage: str
    description_ouvrage: str
    
    
    
class OuvrageUpdate(BaseModel):
    titre_ouvrage: str
    auteur_ouvrage: str
    isbn_ouvrage: str
    langue_ouvrage: str
    prix_ouvrage: float
    date_parution_ouvrage: date
    categorie_ouvrage: str
    date_disponibilite_libraire_ouvrage: date
    date_disponibilite_particulier_ouvrage: date
    image_ouvrage: str
    table_des_matieres_ouvrage: str
    mot_cle_ouvrage: str
    description_ouvrage: str

from config.connexion import Base
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Client(Base):
    """
    Table Client
    """
    __tablename__ = "Client"
    id_client: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom_client: Mapped[str] = mapped_column(String(255))
    prenom_client: Mapped[str] = mapped_column(String(255))
    email_client: Mapped[str] = mapped_column(String(255))
    telephone_client: Mapped[str] = mapped_column(String(20))
    preferences_client: Mapped[str] = mapped_column(String(255))
    adresse_livraison_client: Mapped[str] = mapped_column(String(255))
    adresse_facturation_client: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"id : {self.id_client} | Prénom : {self.prenom_client} | Nom : {self.nom_client} \nTéléphone : {self.telephone_client}"


"""
    id_client INT PRIMARY KEY AUTO_INCREMENT,
    nom_client VARCHAR(255),
    prenom_client VARCHAR(255),
    email_client VARCHAR(255),
    telephone_client VARCHAR(20),
    preferences_client TEXT,
    adresse_livraison_client TEXT,
    adresse_facturation_client TEXT

"""

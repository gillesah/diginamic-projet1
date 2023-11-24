from pydantic import BaseModel
from datetime import date


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

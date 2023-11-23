from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status
from sqlalchemy import Numeric, Date, String


# Schémas Pydantic pour la validation des données
class OuvrageCreate(BaseModel):
    titre_ouvrage : str
    auteur_ouvrage : str
    isbn_ouvrage : str
    langue_ouvrage : str
    prix_ouvrage : Numeric = Numeric(10,2)
    date_parution_ouvrage : Date = Date
    categorie_ouvrage : str
    date_disponibilite_libraire_ouvrage : Date
    date_disponibilite_particulier_ouvrage : Date
    image_ouvrage : str
    table_des_matieres_ouvrage : str 
    mot_cle_ouvrage : str
    description_ouvrage : str
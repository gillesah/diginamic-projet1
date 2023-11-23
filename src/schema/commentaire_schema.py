from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Date

class Commentaire(BaseModel):
    date_publication_commentaire : Date 
    auteur_commentaire : str 
    titre_commentaire : str 
    
class Commentaire_create(Commentaire):
    date_publication_commentaire : Date 
    auteur_commentaire : str 
    titre_commentaire : str 
    id_client : int constraint foreign key
    id_ouvrage :int constraint foreign key
    
class CommentaireUpdate(Commentaire):
    auteur_commentaire : str 
    titre_commentaire : str
    
class CommentaireResponse(BaseModel):
    id_commentaire : int
    date_publication_commentaire : Date 
    auteur_commentaire : str 
    titre_commentaire : str 
    id_client : int constraint foreign key
    id_ouvrage :int constraint foreign key
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Date

class Commentaire(BaseModel):
    date_publication_commentaire : Date 
    auteur_commentaire : str 
    titre_commentaire : str 
    id_client : int
    id_ouvrage :int
    
    class Config:
        orm_mode = True
        from_attributes = True
    
class Commentaire_create(Commentaire):
    date_publication_commentaire : Date 
    auteur_commentaire : str 
    titre_commentaire : str
    
class CommentaireUpdate(Commentaire):
    auteur_commentaire : str 
    titre_commentaire : str
    
class CommentaireResponse(BaseModel):
    id_commentaire : int
    date_publication_commentaire : Date 
    auteur_commentaire : str 
    titre_commentaire : str 
    id_client : int
    id_ouvrage :int
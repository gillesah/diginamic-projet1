from pydantic import BaseModel
from datetime import date

class Commentaire(BaseModel):
    date_publication_commentaire : date 
    auteur_commentaire : str 
    titre_commentaire : str 
    id_client : int
    id_ouvrage :int
    
class Commentaire_create(Commentaire):
    date_publication_commentaire : date 
    auteur_commentaire : str 
    titre_commentaire : str
    
class CommentaireUpdate(Commentaire):
    auteur_commentaire : str 
    titre_commentaire : str
    
class CommentaireResponse(BaseModel):
    id_commentaire : int
    date_publication_commentaire : date 
    auteur_commentaire : str 
    titre_commentaire : str 
    id_client : int
    id_ouvrage :int
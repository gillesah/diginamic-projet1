from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from config.connexion import get_db
from src.models.client import Client
from src.models.ouvrage import Ouvrage
from src.models.commentaire import Commentaire
from src.schema.commentaire_schema import CommentaireCreate, CommentaireResponse, CommentaireUpdate

app = FastAPI()
commentaire_router = APIRouter()

#POST : création d'un commentaire, demande l'id_client et l'id_ouvrage en parametre car on ne peut pas créer un commnetaire si les deux autres objets n'existent pas 
@commentaire_router.post("/commentaires/", response_model= CommentaireResponse, tags = ["Commentaires"], status_code=status.HTTP_201_CREATED, summary="création d'une occurence.")
async def create_Commentaire(commentaire : CommentaireCreate, client_id : int, ouvrage_id : int, db: Session = Depends(get_db)):
    """
        Creer un nouveau commentaire dans la bdd

    Args:
        commentaire (CommentaireCreate): schema de la création de commentaire
        client_id (int): l'id du client qui écrit le commentaire /!\ doit exister dans la bdd
        ouvrage_id (int): l'id de l'ouvrage concerné par le commentaire /!\ doit exister dans la bdd
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Returns:
        CommentaireResponse: le commentaire apres la création avec toute les infos
    """
    db_comment = Commentaire(**commentaire.dict(), id_client = client_id, id_ouvrage = ouvrage_id)
    db.add(db_comment)
    db.commit()
    return db_comment

#GET : retourne la liste de la totalité des commentaires enregistrés dans la table commentaire
@commentaire_router.get("/commentaires/", response_model=list[CommentaireResponse], tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation de toute les occurences de commentaires.")
async def read_commentaires(db: Session = Depends(get_db)):
    """
        Renvoie la liste de tous les commentaires

    Args:
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Returns:
        La liste des commentaire, avec l'id du client et de l'ouvrage
    """
    db_commentaires = db.query(Commentaire).all()
    return db_commentaires
        
#GET : retourne un commentaire spécifique en fonction de son id
@commentaire_router.get("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation d'une occurence d'apres un id.")
async def read_commentaire(commentaire_id : int, db: Session = Depends(get_db)):
    """
        Renvoie les informations d'un commentaire spécifique

    Args:
        commentaire_id (int): l'identifiant unique du commentaire recherché
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Raises:
        HTTPException: renvoie un message si le commentaire n'est pas dans la bdd

    Returns:
        toutes les informations du commentaire spécifié 
    """
    db_commentaire = db.get(Commentaire, commentaire_id)
    if db_commentaire:
            return db_commentaire
    else : 
        raise HTTPException(status_code=404, detail="Comment not found.")

#GET : retourne la liste de tous les commentaires d'un client a pu faire
@commentaire_router.get("/commentairesduclient/{id_client}", response_model=list[CommentaireResponse], tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation d'une liste de commentaire écrit par un client.")
async def read_commentaire_client(client_id : int, db: Session = Depends(get_db)):
    """
        Retourne la liste de tous les commentaires d'un client

    Args:
        client_id (int): l'id du client recherché
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Returns:
        La liste des commentaires concernants un client spécifique, avec les infos habituelles, vide si le client n'a pas écrit de commentaire
    """
    db_commentaire = db.query(Commentaire).filter(Commentaire.id_client == client_id)
    if db_commentaire:
        return db_commentaire
    
#GET : retourne tous les commentaires qu'un ouvrage a pu recevoir
@commentaire_router.get("/commentairesdelouvrage/{id_ouvrage}", response_model=list[CommentaireResponse], tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation d'une liste de commentaires concernant un ouvrage.")
async def read_commentaire_ouvrage(ouvrage_id : int, db: Session = Depends(get_db)):
    """
        Retourne la liste de tous les commentaires d'un ouvrage 

    Args:
        ouvrage_id (int): l'id de l'ouvrage 
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Returns:
        La liste des commentaires concernants un ouvrage spécifique, avec les infos habituelles , vide si il n'y en a pas
    """
    db_commentaire = db.query(Commentaire).filter(Commentaire.id_ouvrage == ouvrage_id)
    if db_commentaire:
        return db_commentaire

#GET : retourne tous les commentaires qu'un client a écrit pour un ouvrage 
@commentaire_router.get("/commentairesduclient/{id_client}/commentairesdelouvrage/{id_ouvrage}", response_model=list[CommentaireResponse], tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation d'une liste de commentaires ecrit par un client pour un ouvrage.")
async def read_commentaire_ouvrage(client_id : int, ouvrage_id : int, db: Session = Depends(get_db)):
    """
        Retourne la liste des commentaires d'un client a écrit pour un ouvrage

    Args:
        client_id (int): l'id du client recherché /!\ doit exister dans la table Client
        ouvrage_id (int): l'id de l'ouvrage recherché /!\ doit exister dans la table Ouvrage 
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Raises:
        HTTPException: renvoie un message si le client ou l'ouvrage n'existe pas dans la bdd

    Returns:
        La liste des commentaires lié au client et a l'ouvrage, vide si il n'y en a pas
    """
    db_client = db.get(Client, client_id)
    db_ouvrage = db.get(Ouvrage, ouvrage_id)
    if db_client and db_ouvrage :     
        db_commentaire = db.query(Commentaire).filter(Commentaire.id_client == client_id).filter(Commentaire.id_ouvrage == ouvrage_id)
        if db_commentaire:
            return db_commentaire
    else : 
        raise HTTPException(status_code=404, detail = "client or ouvrage not found" )
    
#PUT : la modification complete d'un commentaire concernant un client et un ouvrage /!\ on ne peut pas modifier le client et l'ouvrage
@commentaire_router.put("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="modification complete d'une occurence.")
async def update_commentaire(commentaire_id : int, commentUpdate : CommentaireCreate, db: Session = Depends(get_db)):
    """
        Permet la modification complete d'un commentaire, sans en changer le client et l'ouvrage

    Args:
        commentaire_id (int): l'id du commentaire recherché
        commentUpdate (CommentaireCreate): le schema de modication du commentaire, permet de modifier le titre, le contenu, et la date d'un commentaire
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Raises:
        HTTPException: renvoie un message si le commentaire recherché n'existe pas

    Returns:
        Le commentaire modifié
    """
    db_commentaire = db.get(Commentaire, commentaire_id)
    if db_commentaire:
        for key, value in commentUpdate.dict().items():
            # attribuer les nouvelles valeurs avec setattr
            setattr(db_commentaire, key, value)
        db.commit()
        return db_commentaire
    else: 
        raise HTTPException(status_code=404, detail="Comment not found.")
    
#PATCH : la modification partielle d'un commentaire concernant un client et un ouvrage /!\ on ne peut pas modifier le client et l'ouvrage
@commentaire_router.patch("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="modification partielle.")
async def patch_commentaire(commentaire_id : int, commentUpdate : CommentaireUpdate, db: Session = Depends(get_db)):
    """
        Permet la modification partielle d'un commentaire, sans en changer le client et l'ouvrage

    Args:
        commentaire_id (int): l'id du commentaire recherché
        commentUpdate (CommentaireUpdate): le schema de modification du commentaire, qui permet de ne renseigner d'une partie des infos a modifier
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Raises:
        HTTPException: renvoie un message si le commentaire recherché n'existe pas 

    Returns:
        Le commentaire modifié
    """
    db_commentaire = db.get(Commentaire, commentaire_id)
    updated_comment = commentUpdate.dict(exclude_unset=True)
    if db_commentaire:
        for key, value in updated_comment.items():
            if hasattr(db_commentaire, key):
                setattr(db_commentaire, key, value)
        db.commit()
        return db_commentaire
    else : 
        raise HTTPException(status_code=404, detail="Comment not found")

#DELETE : supression d'un commentaire, hasta la vista baby
@commentaire_router.delete("/commentaires/{id_commentaire}", response_model = dict, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary = "suppression d'une occurence précise.")
async def delete_commentaire(commentaire_id : int, db: Session = Depends(get_db)):
    """
        Permet la suppression d'un commentaire en fonction de son id

    Args:
        commentaire_id (int): l'id du commentaire recherché
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Raises:
        HTTPException: renvoie un message si le commentaire recherché n'existe pas 

    Returns:
        Un message confirmant la supression du commentaire
    """
    db_commentaire = db.get(Commentaire, commentaire_id)
    if db_commentaire:
            db.delete(db_commentaire)
            db.commit()
            return {"Message " : "Commentaire supprimé."}
    else : 
        raise HTTPException(status_code=404, detail="Comment not found.")
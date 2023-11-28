from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from config.connexion import get_db
from src.models.commentaire import Commentaire
from src.schema.commentaire_schema import CommentaireCreate, CommentaireResponse, CommentaireUpdate

app = FastAPI()
commentaire_router = APIRouter()

@commentaire_router.post("/commentaires/", response_model= CommentaireResponse, tags = ["Commentaires"], status_code=status.HTTP_201_CREATED, summary="création d'une occurence.")
async def create_Commentaire(commentaire : CommentaireCreate, client_id : int, ouvrage_id : int, db: Session = Depends(get_db)):
    db_comment = Commentaire(**commentaire.dict(), id_client = client_id, id_ouvrage = ouvrage_id)
    db.add(db_comment)
    db.commit()
    return db_comment

@commentaire_router.get("/commentaires/", response_model=list[CommentaireResponse], tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation de toute les occurences de commentaires.")
async def read_commentaires(db: Session = Depends(get_db)):
    db_commentaires = db.query(Commentaire).all()
    return db_commentaires
        

@commentaire_router.get("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation d'une occurence d'apres un id.")
async def read_commentaire(commentaire_id : int, db: Session = Depends(get_db)):
    db_commentaire = db.get(Commentaire, commentaire_id)
    if db_commentaire:
            return db_commentaire
    else : 
        raise HTTPException(status_code=404, detail="Comment not found.")

@commentaire_router.get("/commentairesduclient/{id_client}", response_model=list[CommentaireResponse], tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation d'une liste de commentaire écrit par un client.")
async def read_commentaire_client(client_id : int, db: Session = Depends(get_db)):
    db_commentaire = db.query(Commentaire).filter(Commentaire.id_client == client_id)
    if db_commentaire:
        return db_commentaire
    else : 
        raise HTTPException(status_code=404, detail="Comment not found.")
    
@commentaire_router.get("/commentairesdelouvrage/{id_ouvrage}", response_model=list[CommentaireResponse], tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation d'une liste de commentaires concernant un ouvrage.")
async def read_commentaire_ouvrage(ouvrage_id : int, db: Session = Depends(get_db)):
    db_commentaire = db.query(Commentaire).filter(Commentaire.id_ouvrage == ouvrage_id)
    if db_commentaire:
        return db_commentaire
    else : 
        raise HTTPException(status_code=404, detail="Comment not found.")
    
@commentaire_router.put("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="modification complete d'une occurence.")
async def update_commentaire(commentaire_id : int, commentUpdate : CommentaireCreate, db: Session = Depends(get_db)):
    db_commentaire = db.get(Commentaire, commentaire_id)
    if db_commentaire:
        for key, value in commentUpdate.dict().items():
            # attribuer les nouvelles valeurs avec setattr
            setattr(db_commentaire, key, value)
        db.commit()
        return db_commentaire
    else: 
        raise HTTPException(status_code=404, detail="Comment not found.")

@commentaire_router.patch("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="modification partielle.")
async def patch_commentaire(commentaire_id : int, commentUpdate : CommentaireUpdate, db: Session = Depends(get_db)):
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

@commentaire_router.delete("/commentaires/{id_commentaire}", response_model = dict, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary = "suppression d'une occurence précise.")
async def delete_commentaire(commentaire_id : int, db: Session = Depends(get_db)):
    db_commentaire = db.get(Commentaire, commentaire_id)
    if db_commentaire:
            db.delete(db_commentaire)
            db.commit()
            return {"Message " : "Commentaire supprimé."}
    else : 
        raise HTTPException(status_code=404, detail="Comment not found.")
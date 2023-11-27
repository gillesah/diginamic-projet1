from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from config.connexion import get_db
from src.models.commentaire import Commentaire
from src.schema.commentaire_schema import Commentaire_create, CommentaireResponse, CommentaireUpdate

app = FastAPI()
commentaire_router = APIRouter()

@app.post("/commentaires/", response_model= CommentaireResponse, tags = ["commentaires"], status_code=status.HTTP_201_CREATED, summary="création d'une occurence.")
async def create_Commentaire(commentaire : Commentaire_create, client_id : int, ouvrage_id : int, db: Session = Depends(get_db)):
    db_comment = Commentaire(**commentaire.dict(), id_client = client_id, id_ouvrage = ouvrage_id)
    db.add(db_comment)
    db.commit()
    return CommentaireResponse.from_orm(db_comment)

@app.get("/commentaires/", response_model=list[CommentaireResponse], tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation de toute les occurences de commentaires.")
async def read_commentaire(db: Session = Depends(get_db)):
    db_commentaire = select(Commentaire)
    if db_commentaire:
        result = db.scalars(db_commentaire).all()
        return result
    else: 
            raise HTTPException(status_code=404, detail="Comment not found.")
        
    # db_commentaire = db.get(Commentaire)
    # if db_commentaire:
    #         return {f"Titre : {db_commentaire.titre_commentaire}, commentaire : {db_commentaire.auteur_commentaire}, publié le {db_commentaire.date_publication_commentaire}."}
    # else : 
    #     raise HTTPException(status_code=404, detail="Comment not found.")

@app.get("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation d'une occurence d'apres un id.")
async def read_commentaire(commentaire_id : int, db: Session = Depends(get_db)):
    db_commentaire = select(Commentaire).where(id_commentaire = commentaire_id)
    if db_commentaire:
        result = db.scalars(db_commentaire).all()
        return result
    else: 
        raise HTTPException(status_code=404, detail="Comment not found.")
    # db_commentaire = db.get(Commentaire, commentaire_id)
    # if db_commentaire:
    #         return {f"Titre : {db_commentaire.titre_commentaire}, commentaire : {db_commentaire.auteur_commentaire}, publié le {db_commentaire.date_publication_commentaire}."}
    # else : 
    #     raise HTTPException(status_code=404, detail="Comment not found.")

@app.get("/commentaires/{id_client}", response_model=list[CommentaireResponse], tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation d'une liste de commentaire écrit par un client.")
async def read_commentaire_client(client_id : int, db: Session = Depends(get_db)):
    db_commentaire = select(Commentaire).where(id_client = client_id)
    if db_commentaire:
        result = db.scalars(db_commentaire).all()
        return result
    else: 
        raise HTTPException(status_code=404, detail="Comment not found.")
    
@app.get("/commentaires/{id_ouvrage}", response_model=list[CommentaireResponse], tags=["Commentaires"], status_code=status.HTTP_200_OK, summary="visualisation d'une liste de commentaires concernant un ouvrage.")
async def read_commentaire_ouvrage(ouvrage_id : int, db: Session = Depends(get_db)):
    db_commentaire = select(Commentaire).where(id_ouvrage = ouvrage_id)
    if db_commentaire:
        result = db.scalars(db_commentaire).all()
        return result
    else: 
        raise HTTPException(status_code=404, detail="Comment not found.")
    
@app.put("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaire"], status_code=status.HTTP_200_OK, summary="modification complete d'une occurence.")
async def update_item(commentaire_id : int, commentUpdate : CommentaireUpdate, db: Session = Depends(get_db)):
    db_commentaire = db.get(Commentaire, commentaire_id)
    if db_commentaire:
        updated_comment = CommentaireResponse(**commentUpdate.dict())
        db_commentaire[db_commentaire.index(commentaire_id)] = updated_comment
        return updated_comment
    else: 
        raise HTTPException(status_code=404, detail="Comment not found.")

@app.patch("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaire"], status_code=status.HTTP_200_OK, summary="modification partielle.")
async def patch_item(commentaire_id : int, commentUpdate : CommentaireUpdate, db: Session = Depends(get_db)):
    db_commentaire = db.get(Commentaire, commentaire_id)
    client_comment = CommentaireResponse(id = commentaire_id,**commentUpdate.dict())
    if db_commentaire:
        db_commentaire.copy(update=client_comment)
        return db_commentaire
    else : 
        raise HTTPException(status_code=404, detail="Comment not found")

@app.delete("/commentaires/{id_commentaire}", response_model = dict, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary = "suppression d'une occurence précise.")
async def delete_item(commentaire_id : int, db: Session = Depends(get_db)):
    db_commentaire = db.get(Commentaire, commentaire_id)
    if db_commentaire:
            db.delete(db_commentaire)
            db.commit()
            return {"Message " : "Commentaire supprimé."}
    else : 
        raise HTTPException(status_code=404, detail="Comment not found.")
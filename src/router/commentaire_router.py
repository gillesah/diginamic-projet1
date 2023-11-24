from fastapi import FastAPI, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from config.connexion import SessionLocal
from src.models.commentaire import Commentaire
from src.schema.commentaire_schema import Commentaire_create, CommentaireResponse, CommentaireUpdate

app = FastAPI()
commentaire_router = APIRouter()

@app.post("/commentaire/", response_model= CommentaireResponse, tags = ["commentaires"])
async def create_Commentaire(commentaire : Commentaire):
    return commentaire

@app.get("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaires"])
async def read_commentaire(commentaire_id : int):
    for comment in TableCommentaire:
        if comment.id_commentaire == commentaire_id:
            return {f"Auteur : {comment.auteur_commentaire}, publié le {comment.date_publication_commentaire}, titre : {comment.titre_commentaire}"}
    raise HTTPException(status_code=404, detail="Comment not found")

@app.put("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaire"])
async def update_item(commentaire_id : int, commentUpdate : CommentaireUpdate):
    for comment in TableCommentaire:
        if comment.id_commentaire == commentaire_id:
            update_item = CommentaireResponse(id=commentaire_id, auteur_commentaire=commentUpdate.auteur_commentaire, titre_commentaire=commentUpdate.titre_commentaire)
            TableCommentaire[TableCommentaire.index(comment)] = update_item
            return update_item
    raise HTTPException(status_code=404, detail="Comment not found")

@app.patch("/commentaires/{id_commentaire}", response_model=CommentaireResponse, tags=["Commentaire"], status_code=status.HTTP_200_OK, summary="modification partielle")
async def patch_item(commentaire_id : int, commentUpdate : CommentaireUpdate):
    client_comment = CommentaireResponse(id = commentaire_id,**commentUpdate.dict())
    
    for comment in TableCommentaire:
        if comment.id_commentaire == commentaire_id:
            comment.copy(update=client_comment)
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@app.delete("/commentaires/{id_commentaire}", response_model = dict, tags=["Commentaires"], status_code=status.HTTP_200_OK, summary = "suppression d'une occurence précise")
async def delete_item(commentaire_id : int):
    for comment in TableCommentaire:
        if comment.id_commentaire == commentaire_id:
            TableCommentaire.remove(comment)
            return {"Message" : "Commentaire supprimé"}
    raise HTTPException(status_code=404, detail="Comment not found")
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from config.connexion import get_db
from models.client import Client
from src.schema.client_schema import ClientSchema, ClientSchemaIn, ClientSchemaOut
from typing import List

client_router = APIRouter(tags=["client"], prefix="/client")

@client_router.post("/add_client", response_model=ClientSchemaOut, summary="Ajoute les informations pour un client", status_code=status.HTTP_201_CREATED)
def add_client(client: ClientSchema, db: Session = Depends(get_db)):
    client_db = Client(**client.dict())
    db.add(client_db)
    db.commit()
    return ClientSchemaOut.from_orm(client_db)

@client_router.get("/list", response_model=List[ClientSchemaOut], summary="Affiche les informations client", status_code=status.HTTP_200_OK)
async def get_client(client: ClientSchema, db: Session = Depends(get_db)):
    """Permet d'afficher les informations des clients"""
    l = []
    req = select(client)
    for client in db.scalars(req).all():
        l.append(client)
    # return ClientSchemaOut.from_orm()
    return l




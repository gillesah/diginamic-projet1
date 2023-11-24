from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from config.connexion import get_db
from src.models.client import Client
from src.schema.client_schema import ClientSchema, ClientSchemaIn, ClientSchemaOut
from typing import List

client_router = APIRouter(tags=["client"], prefix="/client")

@client_router.post("/add_client", response_model=ClientSchemaOut, summary="Ajoute les informations pour un client", status_code=status.HTTP_201_CREATED)
def add_client(client: ClientSchema, db: Session = Depends(get_db)):
    """Permet d'ajouter les informations pour un nouveau client"""
    client_db = Client(**client.dict())
    db.add(client_db)
    db.commit()
    return ClientSchemaOut.from_orm(client_db)

@client_router.get("/list", response_model=List[ClientSchemaOut], summary="Affiche les informations client", status_code=status.HTTP_200_OK)
async def get_client():
    """Permet d'afficher les informations des clients"""
    try:
        l = []
        db = Depends(get_db)
        req = select(Client)
        result = db.scalars(req).all()
        for item in result:
            l.append(ClientSchemaOut(**item.dict()))
        return l
    except Exception as e:
        print(e)
        return []



from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from config.connexion import get_db
from src.models.client import Client
from src.schema.client_schema import ClientSchema, ClientSchemaIn, ClientSchemaOut
from typing import List

client_router = APIRouter(tags=["client"], prefix="/client")

@client_router.post("/add_client", response_model=ClientSchemaOut, summary="Ajoute les informations pour un nouveau client", status_code=status.HTTP_201_CREATED)
def add_client(client: ClientSchema, db: Session = Depends(get_db)):
    """
    Permet d'ajouter les informations pour un nouveau client.

    Args:
        client: à partir du schema ClientSchema.
        db: la session de connection à la base de donnée.

    Returns:
        le nouveau client à partir du schema ClienSchemeOut.
    """
    client_db = Client(**client.dict())
    db.add(client_db)
    db.commit()
    return ClientSchemaOut.from_orm(client_db)

@client_router.get("/", response_model=List[ClientSchemaOut], summary="Affiche les informations de tous les client", status_code=status.HTTP_200_OK)
async def get_client(db: Session = Depends(get_db)):
    """
    Permet d'afficher les informations de tous les clients.

    Args:
        db: la session de connection à la base de donnée.

    Returns:
        la liste de tous les clients à partir du schema ClientSchemaOut.
    """
    l = []
    stmt = select(Client)
    result = db.scalars(stmt).all()
    for item in result:
        l.append(ClientSchemaOut.from_orm(item))
    return l

@client_router.get("/{id_client}", response_model=ClientSchemaOut, summary="Affiche les informations d'un client à partir de son id_client", status_code=status.HTTP_200_OK)
async def get_client(id_client: int, db: Session = Depends(get_db)):
    """
    Permet d'afficher les informations d'un client à partir de son id_client.

    Args:
        id_client (int): id du client.
        db: la session de connection à la base de donnée.

    Returns:
        le client correspondant à partir du schema ClienSchemeOut.
    """
    try:
        stmt = select(Client).where(Client.id_client == id_client)
        result = db.scalars(stmt).one()
        return ClientSchemaOut.from_orm(result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="client not found")



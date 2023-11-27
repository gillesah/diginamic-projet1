from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from config.connexion import get_db
from src.models.client import Client
from src.schema.client_schema import ClientSchema, ClientSchemaIn, ClientSchemaOut
from typing import List

client_router = APIRouter(tags=["client"], prefix="/client")

# Create
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

# Read
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

# Read
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

# Patch
@client_router.patch("/{id_client}", response_model=ClientSchemaOut, summary="Mise à jour partielle des informations d'un client à partir de son id_client", status_code=status.HTTP_200_OK)
async def get_client(id_client: int, client_update: ClientSchemaIn, db: Session = Depends(get_db)):
    """
    Permet de mettre à jour de façon partielle les informations d'un client à partir de son id_client.

    Args:
        id_client (int): id du client.
        client_update (ClientSchemaIn): informations client à modifier à partir du schema ClientSchemaIn.
        db (Session): la session de connection à la base de donnée.

    Returns:
        Les informations du client après modification.
    """
    try:
        client = db.get(Client, id_client)
        update_data = client_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            if hasattr(client, key):
                setattr(client, key, value)
        db.commit()
        return client
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="client not found")
    
    
# Put
@client_router.put("/{id_client}", response_model=ClientSchemaOut, summary="Mise à jour des informations d'un client à partir de son id_client", status_code=status.HTTP_200_OK)
async def get_client(id_client: int, client_update: ClientSchemaIn, db: Session = Depends(get_db)):
    """
    Permet de mettre à jour les informations d'un client à partir de son id_client.

    Args:
        id_client (int): id du client.
        client_update (ClientSchemaIn): informations client à modifier à partir du schema ClientSchemaIn.
        db (Session): la session de connection à la base de donnée.

    Returns:
        Les informations du client après modification.
    """
    try:
        client = db.get(Client, id_client)
        for key, value in client_update.dict().items():
            setattr(client, key, value)
        db.commit()
        return client
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="client not found")
    
    
# Delete
@client_router.delete("/{id_client}", response_model=dict, summary="Supression des informations d'un client à partir de son id_client", status_code=status.HTTP_200_OK)
async def delete_client(id_client: int, db: Session = Depends(get_db)):
    """
    Permet de supprimer les informations d'un client à paritr de son id_client.

    Args:
        id_client (int): id du client.
        db (Session): la session de connection à la base de donnée.

    Returns:
        un message indiquant que les informations du client ont bien été supprimé.
    """
    try:
        client = db.get(Client, id_client)
        db.delete(client)
        db.commit()
        return {"message": "informations client supprimé"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="client not found")
from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from config.connexion import Session, get_db
from src.models.ouvrage import Ouvrage
from src.schema.ouvrage_schema import OuvrageStrict, OuvrageUpdate
from fastapi.encoders import jsonable_encoder
from typing import List, Optional
from sqlalchemy import or_

app = FastAPI()
ouvrage_router = APIRouter()


# GET : lecture d'un ouvrages
@ouvrage_router.get("/ouvrages/{id_ouvrage}", response_model=OuvrageUpdate, status_code=status.HTTP_200_OK, summary="Lecture d'un ouvrage par id")
def read_ouvrage(id_ouvrage: int, db: Session = Depends(get_db)):
    """
    lecture des informations d'un ouvrage de la base de données.

    Args:
        id_ouvrage: L'identifiant de l'ouvrage à obtenir(lire).
        db: La session de base de données.

    Returns:
        les informations de l'ouvrage désiré.
    """
    db_ouvrage = db.get(Ouvrage, id_ouvrage)
    if db_ouvrage:
        return db_ouvrage
    else:
        db.close()
        raise HTTPException(status_code=404, detail="ouvrage pas trouvé")


# GET : lecture des ouvrages
@ouvrage_router.get("/ouvrages", status_code=status.HTTP_200_OK, summary="Lecture des ouvrages")
def read_ouvrages(db: Session = Depends(get_db)):
    """
    lecture de tous les ouvrages de la base de données.

    Args:
        db: La session de base de données.

    Returns:
        une liste des ouvrages.
    """
    ouvrages = db.query(Ouvrage).all()
    return ouvrages


# POST : création d'un ouvrage
@ouvrage_router.post("/ouvrages/", status_code=status.HTTP_201_CREATED, summary="Création d'un ouvrage")
def create_ouvrage(ouvrage: OuvrageStrict, db: Session = Depends(get_db)):
    """
    Création d'un ouvrage dans la base de données.

    Args:
        ouvrage: à partir du shéma OuvrageStrict
        db: La session de base de données.

    Returns:
        l'ouvrage après création
    """
    db_ouvrage = Ouvrage(**ouvrage.dict())
    db.add(db_ouvrage)
    db.commit()
    db.refresh(db_ouvrage)
    db.close()
    return db_ouvrage


# DELETE : suppression d'un ouvrage
@ouvrage_router.delete("/ouvrages/{id_ouvrage}", status_code=status.HTTP_200_OK, summary="Suppression d'un ouvrage")
def delete_ouvrage(id_ouvrage: int, db: Session = Depends(get_db)):
    """
    Supprime un ouvrage de la base de données.

    Args:
        id_ouvrage: L'identifiant de l'ouvrage à supprimer.
        db: La session de base de données.

    Returns:
        Un message indiquant que l'ouvrage a été supprimé.
    """

    db_ouvrage = db.get(Ouvrage, id_ouvrage)
    # vérification si l'ouvrage existe
    if db_ouvrage:
        # supprime l'ouvrage
        db.delete(db_ouvrage)
        db.commit()
        # retourne un message indiquant que l'ouvrage a bien été supprimé
        return {"message": "ouvrage supprimé"}
    # si l'ouvrage n'est pas trouvé
    else:
        db.close()
        raise HTTPException(status_code=404, detail="ouvrage pas trouvé")


# PUT : mise à jour d'un Ouvrage
@ouvrage_router.put("/ouvrages/{id_ouvrage}", response_model=OuvrageUpdate, status_code=status.HTTP_200_OK, summary="Mise à jour d'un ouvrage")
async def update_ouvrage(id_ouvrage: int, ouvrage_update: OuvrageUpdate, db: Session = Depends(get_db)):
    """
    mise à jour d'un ouvrage de la base de données.

    Args:
        id_ouvrage: L'identifiant de l'ouvrage à supprimer.
        ouvrage_update : les éléments à modifier à partir du shéma OuvrageUpdate
        db: La session de base de données.

    Returns:
        L'ouvrage modifié
    """
    db_ouvrage = db.get(Ouvrage, id_ouvrage) or None
    if db_ouvrage is not None:
        for key, value in ouvrage_update.dict().items():
            # attribuer les nouvelles valeurs avec setattr
            setattr(db_ouvrage, key, value)
        db.commit()
        return db_ouvrage
    raise HTTPException(
        status_code=404, detail="L'ouvrage n'est pas trouvé")


# PATH
@ouvrage_router.patch("/ouvrages/{id_ouvrage}", response_model=OuvrageUpdate, status_code=status.HTTP_200_OK, summary="Mise à jour partielle d'un ouvrage")
async def patch_ouvrage(id_ouvrage: int, ouvrage_update: OuvrageUpdate, db: Session = Depends(get_db)):
    """
    Mise à jour partielle d'un ouvrage dans la base de données.

    Args:
        id_ouvrage: L'identifiant de l'ouvrage à mettre à jour.
        ouvrage_update: Les éléments à modifier à partir du schéma OuvrageUpdate.
        db: La session de base de données.

    Returns:
        L'ouvrage après modification.
    """
    db_ouvrage = db.get(Ouvrage, id_ouvrage)
    if db_ouvrage is None:
        raise HTTPException(status_code=404, detail="Ouvrage not found")

    update_data = ouvrage_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        if hasattr(db_ouvrage, key):
            setattr(db_ouvrage, key, value)

    db.commit()
    return db_ouvrage


# RECHERCHE ok
@ouvrage_router.get("/search", response_model=List[OuvrageStrict], status_code=status.HTTP_200_OK, summary="Recherche des ouvrages")
def ouvrage_search(titre: Optional[str] = None, auteur: Optional[str] = None, langue: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Ouvrage)

    # Construire dynamiquement la liste des filtres
    filters = []
    if titre:
        filters.append(Ouvrage.titre_ouvrage.contains(titre))
    if auteur:
        filters.append(Ouvrage.auteur_ouvrage.contains(auteur))
    if langue:
        filters.append(Ouvrage.langue_ouvrage.contains(langue))

    # Appliquer les filtres
    if filters:
        query = query.filter(or_(*filters))

    ouvrages = query.all()

    if ouvrages:
        return ouvrages
    else:
        raise HTTPException(status_code=404, detail="Aucun ouvrage trouvé")


# RECHERCHE par une requete unique
@ouvrage_router.get("/search2", response_model=List[OuvrageUpdate],  status_code=status.HTTP_200_OK, summary="Recherche avec une requête unique des ouvrages")
def ouvrage_search(requete_user: str, db: Session = Depends(get_db)):
    ouvrages = db.query(Ouvrage).all()
    # mise en minuscule de la requete utilisateur
    requete_user = requete_user.lower()
    # on met tous les résultats dans une liste
    resultats = []
    for ouvrage in ouvrages:
        if requete_user in ouvrage.titre_ouvrage.lower() or requete_user in ouvrage.auteur_ouvrage.lower() or requete_user in ouvrage.langue_ouvrage.lower() or requete_user in ouvrage.categorie_ouvrage.lower() or requete_user in ouvrage.description_ouvrage.lower() or requete_user in ouvrage.mot_cle_ouvrage.lower():
            resultats.append(ouvrage)
    if resultats:
        return resultats
    else:
        raise HTTPException(status_code=404, detail="Aucun ouvrage trouvé")

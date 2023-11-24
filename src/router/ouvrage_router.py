from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from config.connexion import get_db
from src.models.ouvrage import Ouvrage, OuvrageCreate, OuvrageUpdate

app = FastAPI()
ouvrage_router = APIRouter()


@ouvrage_router.post("/ouvrages/", status_code=status.HTTP_201_CREATED)
def create_ouvrage(ouvrage: OuvrageCreate, db: Session = Depends(get_db)):
    db_ouvrage = Ouvrage(**ouvrage.dict())
    db.add(db_ouvrage)
    db.commit()
    db.refresh(db_ouvrage)
    db.close()
    return db_ouvrage


@ouvrage_router.delete("/ouvrages/{id_ouvrage}", status_code=status.HTTP_201_CREATED)
def delete_ouvrage(id_ouvrage: int, db: Session = Depends(get_db)):
    db_ouvrage = db.get(Ouvrage, id_ouvrage)

    if db_ouvrage:
        db.delete(db_ouvrage)
        db.commit()
        return {"message": "ouvrage supprimé"}
    else:
        db.close()
        raise HTTPException(status_code=404, detail="ouvrage pas trouvé")

# PUT : mise à jour d'un ITEM


@ouvrage_router.put("/ouvrages/{id_ouvrage}", response_model=OuvrageUpdate, status_code=status.HTTP_200_OK)
async def update_ouvrage(id_ouvrage: int, ouvrage_update: OuvrageUpdate, db: Session = Depends(get_db)):
    db_ouvrage = db.get(Ouvrage, id_ouvrage)
    for ouvrage in db_ouvrage:
        if ouvrage.id == id_ouvrage:
            updated_ouvrage = OuvrageUpdate(
                id=id_ouvrage, **ouvrage.dict())
            db_ouvrage[db_ouvrage.index(ouvrage)] = updated_ouvrage
            return updated_ouvrage
        raise HTTPException(
            status_code=404, detail="L'ouvrage n'est pas trouvé")

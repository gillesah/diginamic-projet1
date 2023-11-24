from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from config.connexion import SessionLocal, get_db
from src.models.ouvrage import Ouvrage, OuvrageCreate

app = FastAPI()
ouvrage_router = APIRouter()


@ouvrage_router.post("/ouvrages/", status_code=status.HTTP_201_CREATED)
def create_ouvrage(ouvrage: OuvrageCreate, db : Session = Depends(get_db)):
    db = SessionLocal()
    db_ouvrage = Ouvrage(**ouvrage.dict())
    db.add(db_ouvrage)
    db.commit()
    db.refresh(db_ouvrage)
    db.close()
    return db_ouvrage


@ouvrage_router.delete("/ouvrages/{id_ouvrage}", status_code=status.HTTP_201_CREATED)
def delete_ouvrage(id_ouvrage: int):
    db = SessionLocal()
    db_ouvrage = db.get(Ouvrage, id_ouvrage)

    if db_ouvrage:
        db.delete(db_ouvrage)
        db.commit()
        return {"message": "ouvrage supprimé"}
    else:
        db.close()
        raise HTTPException(status_code=404, detail="ouvrage pas trouvé")


@ouvrage_router.put("/ouvrages/{id_ouvrage}", response_model=OuvrageCreate, status_code=status.HTTP_201_CREATED)
async def update_ouvrage(id_ouvrage: int, ouvrage: OuvrageCreate):
    db = SessionLocal()
    db_ouvrage = db.get(Ouvrage, id_ouvrage)
    for ouvrage in db_ouvrage:
        if ouvrage.id == id_ouvrage:
            updated_ouvrage = OuvrageCreate(
                id=id_ouvrage, **ouvrage.dict())
            db_ouvrage[db_ouvrage.index(ouvrage)] = updated_ouvrage
            return updated_ouvrage
        raise HTTPException(
            status_code=404, detail="L'ouvrage n'est pas trouvé")

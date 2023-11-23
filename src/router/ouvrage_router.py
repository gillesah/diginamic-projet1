from fastapi import FastAPI, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from config.connexion import SessionLocal
from src.models.ouvrage import Ouvrage, OuvrageCreate

app = FastAPI()
ouvrage_router = APIRouter()


@ouvrage_router.post("/ouvrages/", status_code=status.HTTP_201_CREATED)
def create_ouvrage(ouvrage: OuvrageCreate):
    db = SessionLocal()
    db_ouvrage = Ouvrage(**ouvrage.dict())
    db.add(db_ouvrage)
    db.commit()
    db.refresh(db_ouvrage)
    db.close()
    return db_ouvrage

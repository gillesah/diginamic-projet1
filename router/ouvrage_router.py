from fastapi import FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from config.connexion import SessionLocal
from models.ouvrage import Ouvrage, OuvrageCreate

app = FastAPI()


@app.post("/ouvrages/", status_code=status.HTTP_201_CREATED)
def create_ouvrage(ouvrage: OuvrageCreate):
    db = SessionLocal()
    db_ouvrage = Ouvrage(**ouvrage.dict())
    db.add(db_ouvrage)
    db.commit()
    db.refresh(db_ouvrage)
    db.close()
    return db_ouvrage

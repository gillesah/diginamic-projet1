from fastapi import FastAPI, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from config.connexion import SessionLocal
from src.models.ouvrage import Ouvrage, OuvrageCreate

app = FastAPI()
commentaire_router = APIRouter()


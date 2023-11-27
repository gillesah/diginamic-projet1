from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from config.connexion import get_db
from src.models.theme import Theme
from src.schema.theme_schema import ThemeCreate, ThemeUpdate, ThemeResponse

app = FastAPI()
theme_router = APIRouter()

@theme_router.post("/themes/", response_model= ThemeResponse, tags = ["Theme"], status_code=status.HTTP_201_CREATED, summary="création d'une occurence de theme.")
async def create_theme(theme: ThemeCreate, db: Session = Depends(get_db)):
    db_theme = Theme(**theme.dict())
    db.add(db_theme)
    db.commit()
    return db_theme

@theme_router.get("/themes/", response_model=list[ThemeResponse], tags=["Theme"], status_code=status.HTTP_200_OK, summary="visualisation de toute les occurences de Theme.")
async def read_themes(db: Session = Depends(get_db)):
    themes = db.query(Theme).all()
    return themes

@theme_router.get("/themes/{id_theme}", response_model=ThemeResponse, tags=["Theme"], status_code=status.HTTP_200_OK, summary="visualisation d'une occurence d'apres un id.")
async def read_theme(theme_id : int, db: Session = Depends(get_db)):
    db_theme = db.get(Theme, theme_id)
    if db_theme:
            return db_theme
    else : 
        raise HTTPException(status_code=404, detail="Theme not found.")
    
@theme_router.put("/themes/{id_theme}", response_model=ThemeResponse, tags=["Theme"], status_code=status.HTTP_200_OK, summary="modification d'un theme")
async def update_theme(theme_id : int, themeUpdate : ThemeUpdate, db: Session = Depends(get_db)):
    db_theme = db.get(Theme, theme_id)
    if db_theme:
        for key, value in themeUpdate.dict().items():
            # attribuer les nouvelles valeurs avec setattr
            setattr(db_theme, key, value)
        db.commit()
        return db_theme
    else: 
        raise HTTPException(status_code=404, detail="Theme not found.")
    
@theme_router.delete("/themes/{id_theme}", response_model = dict, tags=["Theme"], status_code=status.HTTP_200_OK, summary = "suppression d'une occurence précise.")
async def delete_theme(theme_id : int, db: Session = Depends(get_db)):
    db_theme = db.get(Theme, theme_id)
    if db_theme:
            db.delete(db_theme)
            db.commit()
            return {"Message " : "Theme supprimé."}
    else : 
        raise HTTPException(status_code=404, detail="Theme not found.")
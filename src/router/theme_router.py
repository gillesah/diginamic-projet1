from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from config.connexion import get_db
from src.models.theme import Theme
from src.schema.theme_schema import ThemeCreate, ThemeUpdate, ThemeResponse

app = FastAPI()
theme_router = APIRouter()

#POST : création d'un nouveau theme
@theme_router.post("/themes/", response_model= ThemeResponse, tags = ["Theme"], status_code=status.HTTP_201_CREATED, summary="création d'une occurence de theme.")
async def create_theme(theme: ThemeCreate, db: Session = Depends(get_db)):
    """
        Créer un nouveau theme

    Args:
        theme (ThemeCreate): le schema de theme, avec les information a donner pour le créer
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Returns:
        Renvoie le theme créer avec son id et ses attributs 
    """
    db_theme = Theme(**theme.dict())
    db.add(db_theme)
    db.commit()
    return db_theme

#GET : la liste de tous les themes 
@theme_router.get("/themes/", response_model=list[ThemeResponse], tags=["Theme"], status_code=status.HTTP_200_OK, summary="visualisation de toute les occurences de Theme.")
async def read_themes(db: Session = Depends(get_db)):
    """
        Renvoie la liste de tous les themes 

    Args:
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Returns:
        La liste de tout les themes 
    """
    themes = db.query(Theme).all()
    return themes

#GET : un theme spécifique
@theme_router.get("/themes/{id_theme}", response_model=ThemeResponse, tags=["Theme"], status_code=status.HTTP_200_OK, summary="visualisation d'une occurence d'apres un id.")
async def read_theme(theme_id : int, db: Session = Depends(get_db)):
    """
        Retourne les infos d'un theme spécifique

    Args:
        theme_id (int): l'id du theme recherché
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Raises:
        HTTPException: renvoie un message si le theme n'est pas dans la bdd

    Returns:
        Renvoies les information du theme recherché
    """
    db_theme = db.get(Theme, theme_id)
    if db_theme:
            return db_theme
    else : 
        raise HTTPException(status_code=404, detail="Theme not found.")

#PUT : modification complete d'un theme     
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
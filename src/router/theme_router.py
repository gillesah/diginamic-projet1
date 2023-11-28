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
        La liste de tous les themes 
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
async def update_theme(theme_id : int, themeUpdate : ThemeCreate, db: Session = Depends(get_db)):
    """
        Modification complete d'un theme 

    Args:
        theme_id (int): l'idée du theme recherché
        themeUpdate (ThemeCreate): les infos modifiés du theme
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Raises:
        HTTPException: renvoie un message si le theme à modifier n'existe pas dans la bdd

    Returns:
        Renvoie le theme modifié
    """
    db_theme = db.get(Theme, theme_id)
    if db_theme:
        for key, value in themeUpdate.dict().items():
            # attribuer les nouvelles valeurs avec setattr
            setattr(db_theme, key, value)
        db.commit()
        return db_theme
    else: 
        raise HTTPException(status_code=404, detail="Theme not found.")

#PATCH : la modification partielle d'un theme /!\ pour l'instant Theme ne contient qu'un attribut, mais pour l'avenir si une modification de la dbb ajouter plus de champ au theme
@theme_router.patch("/theme/{id_theme}", response_model=ThemeResponse, tags=["Theme"], status_code=status.HTTP_200_OK, summary="modification partielle d'un theme")
async def patch_theme(theme_id : int, themeUpdate : ThemeUpdate, db: Session = Depends(get_db)):
    """
        Modification partielle du theme

    Args:
        theme_id (int): l'id du theme recherché
        themeUpdate (ThemeUpdate): les infos modifiés du theme, permet de ne rien rensiegner
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).


    Raises:
        HTTPException: renvoie un message si le theme à modifier n'existe pas dans la bdd

    Returns:
        Renvoie le theme avec les modifications effectués
    """
    db_theme = db.get(Theme, theme_id)
    updated_theme = themeUpdate.dict(exclude_unset=True)
    if db_theme:
        for key, value in updated_theme.items():
            if hasattr(db_theme, key):
                setattr(db_theme, key, value)
        db.commit()
        return db_theme
    else : 
        raise HTTPException(status_code=404, detail="Comment not found")

    

#DELETE : la suppression d'un theme    
@theme_router.delete("/themes/{id_theme}", response_model = dict, tags=["Theme"], status_code=status.HTTP_200_OK, summary = "suppression d'une occurence précise.")
async def delete_theme(theme_id : int, db: Session = Depends(get_db)):
    """
        La suppression d'un theme

    Args:
        theme_id (int): l'id du theme a supprimer
        db (Session, optional): a ne pas renseigner par l'utilisateur, est la connexion a la bdd | Defaults to Depends(get_db).

    Raises:
        HTTPException: renvoie un message si le theme a supprimer n'existe pas dans la bdd

    Returns:
        Retourne un message confirmant la suppressin d'un theme 
    """
    db_theme = db.get(Theme, theme_id)
    if db_theme:
            db.delete(db_theme)
            db.commit()
            return {"Message " : "Theme supprimé."}
    else : 
        raise HTTPException(status_code=404, detail="Theme not found.")
from pydantic import BaseModel


class Theme(BaseModel):
    nom_theme: str


class ThemeCreate(Theme):
    nom_theme: str


class ThemeUpdate(Theme):
    nom_theme: str | None = None


class ThemeResponse(Theme):
    id_theme: int
    nom_theme: str


class ThemeId(Theme):
    id_theme: int

from config.connexion import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Theme(Base):
    __tablename__ = "Theme"
    id_theme : Mapped[int] = mapped_column(PRIMARY_KEY = True, autoincrement=True)
    nom_theme : Mapped[str] =  mapped_column(String(255))
    ouvrage_id: Mapped[int] = mapped_column(ForeignKey("Ouvrage.id"))
    ouvrage: Mapped["Ouvrage"] = relationship(back_populates="child")


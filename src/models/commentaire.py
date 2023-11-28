from config.connexion import Base
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import Mapped, mapped_column

class Commentaire(Base):
    __tablename__ = "Commentaire"
    id_commentaire : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_client : Mapped[int] = mapped_column(ForeignKey("Client.id_client"))
    id_ouvrage : Mapped[int] = mapped_column(ForeignKey("Ouvrage.id_ouvrage"))
    date_publication_commentaire : Mapped[Date] = mapped_column(Date)
    auteur_commentaire : Mapped[str] = mapped_column(String(255))
    titre_commentaire : Mapped[str] = mapped_column(String(255))

from config.connexion import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, MetaData
from sqlalchemy.orm import Mapped, mapped_column
# from .ouvrage import Ouvrage
# from .theme import Theme
# from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# class ThemeOuvrage(Base):
#     __tablename__ = 'Theme_Ouvrage'
#     id_ouvrage = Column(Integer, ForeignKey(
#         'Ouvrage.id_ouvrage'), primary_key=True)
#     id_theme = Column(Integer, ForeignKey('Theme.id_theme'), primary_key=True)
#     themes: Mapped["themes"] = relationship(
#         back_populates="parent_associations")

#     ouvrages: Mapped["ouvrages"] = relationship(
#         back_populates="child_associations")

theme_ouvrage_association = Table(
    'theme_ouvrage',
    Base.metadata,
    Column('id_ouvrage', Integer, ForeignKey('Ouvrage.id_ouvrage',
           name='fk_theme_ouvrage_id_ouvrage'), primary_key=True),
    Column('id_theme', Integer, ForeignKey('Theme.id_theme',
           name='fk_theme_ouvrage_id_theme'), primary_key=True)
)

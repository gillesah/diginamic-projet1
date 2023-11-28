from config.connexion import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, MetaData
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


theme_ouvrage_association = Table(
    'theme_ouvrage',
    Base.metadata,
    Column('id_ouvrage', Integer, ForeignKey('Ouvrage.id_ouvrage',
           name='fk_theme_ouvrage_id_ouvrage'), primary_key=True),
    Column('id_theme', Integer, ForeignKey('Theme.id_theme',
           name='fk_theme_ouvrage_id_theme'), primary_key=True)
)

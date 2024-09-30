from sqlalchemy import Column, Integer, String, Float, Date
from agriculture.database import Base

# Modelos de la base de datos
class Cultivo(Base):
    __tablename__ = 'cultivos'
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50))
    areaCultivada = Column(Float)
    fechaSiembra = Column(String(20))
    fechaCosecha = Column(String(20))

class Silo(Base):
    __tablename__ = 'silos'
    id = Column(Integer, primary_key=True, index=True)
    ubicacion = Column(String(100))
    capacidad = Column(Float)
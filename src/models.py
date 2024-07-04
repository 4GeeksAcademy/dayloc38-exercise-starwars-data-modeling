import os
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    apellido = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    fecha_subscripcion = Column(DateTime, nullable=False, default=datetime.utcnow)
    favoritos = relationship('Favorito', backref='usuario', lazy=True)

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    genero = Column(String(120), nullable=False)
    nacimiento = Column(String(120), nullable=False)
    favoritos = relationship('Favorito', backref='personaje', lazy=True)

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    clima = Column(String(120), nullable=False)
    terreno = Column(String(120), nullable=False)
    favoritos = relationship('Favorito', backref='planeta', lazy=True)

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)

    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')

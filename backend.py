from sqlalchemy import create_engine, Column, Table
from sqlalchemy import Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_engine = create_engine('sqlite:///fisher_friend_database.db')
Base = declarative_base()


table_zuvis_vietove = Table(
    'zuvis_vietove',
    Base.metadata,
    Column('zuvis_id', Integer, ForeignKey('zuvis.id')),
    Column('vietove_id', Integer, ForeignKey('vietove.id'))
)

class Zuvis(Base):
    __tablename__= 'zuvis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    svoris = Column("Svoris", Float)
    ilgis = Column("Ilgis", Float)
    kada_pagauta = Column("Pagavimo data", Date)
    rusis_id = Column(Integer, ForeignKey('rusis.id'))
    rusis = relationship('Rusis')
    vietove_id = Column(Integer, ForeignKey('vietove.id'))
    vietove = relationship('Vietove')

    def __repr__(self):
        return f"{self.id}, {self.svoris}, {self.ilgis}, {self.kada_pagauta}"
    

class Rusis(Base):
    __tablename__='rusis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pavadinimas = Column("Pavadinimas", String(50))

    def __repr__(self):
        return f"{self.id}, {self.pavadinimas}"
    

class Vietove(Base):
    __tablename__= 'vietove'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pavadinimas = Column("Pavadinimas", String(50))
    tipas = Column("Tipas", String(50))

    def __repr__(self):
        return f"{self.id}, {self.pavadinimas}, {self.tipas}"
    

Base.metadata.create_all(db_engine)
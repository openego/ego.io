# coding: utf-8
from sqlalchemy import Column, Integer, Numeric, String, Table, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Gn250B(Base):
    __tablename__ = 'gn250_b'
    __table_args__ = {'schema': 'orig_geo_gn250'}

    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_gn250.gn250_b_gid_seq'::regclass)"))
    nnid = Column(String(16))
    datum = Column(String(10))
    oba = Column(String(40))
    oba_wert = Column(String(40))
    name = Column(String(90))
    sprache = Column(String(25))
    genus = Column(String(10))
    name2 = Column(String(90))
    sprache2 = Column(String(25))
    genus2 = Column(String(10))
    zusatz = Column(String(40))
    ags = Column(String(8))
    rs = Column(String(12))
    hoehe = Column(String(8))
    hoehe_ger = Column(String(5))
    ewz = Column(String(8))
    ewz_ger = Column(String(8))
    gewk = Column(String(18))
    gemteil = Column(String(4))
    virtuell = Column(String(4))
    gemeinde = Column(String(40))
    verwgem = Column(String(40))
    kreis = Column(String(40))
    regbezirk = Column(String(40))
    bundesland = Column(String(40))
    staat = Column(String(40))
    geola = Column(String(6))
    geobr = Column(String(6))
    gkre = Column(Numeric)
    gkho = Column(Numeric)
    utmre = Column(Numeric)
    utmho = Column(Numeric)
    box_geo = Column(String(250))
    box_gk = Column(String(250))
    box_utm = Column(String(250))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


t_gn250_b_oba_view = Table(
    'gn250_b_oba_view', metadata,
    Column('gid', Integer),
    Column('oba', String(40)),
    Column('name', String(90)),
    Column('ewz', String(8)),
    Column('ewz_ger', String(8)),
    Column('gemeinde', String(40)),
    Column('geom', Geometry('MULTIPOLYGON', 31467)),
    schema='orig_geo_gn250'
)


class Gn250P(Base):
    __tablename__ = 'gn250_p'
    __table_args__ = {'schema': 'orig_geo_gn250'}

    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_gn250.gn250_p_gid_seq'::regclass)"))
    nnid = Column(String(16))
    datum = Column(String(10))
    oba = Column(String(40))
    oba_wert = Column(String(40))
    name = Column(String(90))
    sprache = Column(String(25))
    genus = Column(String(10))
    name2 = Column(String(90))
    sprache2 = Column(String(25))
    genus2 = Column(String(10))
    zusatz = Column(String(40))
    ags = Column(String(8))
    rs = Column(String(12))
    hoehe = Column(String(8))
    hoehe_ger = Column(String(5))
    ewz = Column(String(8))
    ewz_ger = Column(String(8))
    gewk = Column(String(18))
    gemteil = Column(String(4))
    virtuell = Column(String(4))
    gemeinde = Column(String(40))
    verwgem = Column(String(40))
    kreis = Column(String(40))
    regbezirk = Column(String(40))
    bundesland = Column(String(40))
    staat = Column(String(40))
    geola = Column(String(6))
    geobr = Column(String(6))
    gkre = Column(Numeric)
    gkho = Column(Numeric)
    utmre = Column(Numeric)
    utmho = Column(Numeric)
    box_geo = Column(String(250))
    box_gk = Column(String(250))
    box_utm = Column(String(250))
    geom = Column(Geometry('POINT', 31467), index=True)

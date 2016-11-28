# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, Integer, SmallInteger, String, \
    Table, Text, text, Numeric
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class EgoDeuDea(Base):
    __tablename__ = 'ego_deu_dea'
    __table_args__ = {'schema': 'calc_ego_re'}

    id = Column(Integer, primary_key=True)
    sort = Column(Integer)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    voltage_type = Column(String(2))
    subst_id = Column(Integer)
    la_id = Column(Integer)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    geom = Column(Geometry('POINT', 3035), index=True)
    geom_new = Column(Geometry('POINT', 3035), index=True)
    flag = Column(String)


class EgoDeaAllocation(Base):
    __tablename__ = 'ego_dea_allocation'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    sort = Column(Integer)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    postcode = Column(String)
    subst_id = Column(Integer)
    la_id = Column(Integer)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    geom = Column(Geometry('POINT', 3035), index=True)
    geom_new = Column(Geometry('POINT', 3035), index=True)
    flag = Column(String)

# coding: utf-8
from sqlalchemy import Column, Integer, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Cosmoclmgrid(Base):
    __tablename__ = 'cosmoclmgrid'
    __table_args__ = {'schema': 'weather'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('weather.cosmoclmgrid_gid_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 4326), index=True)

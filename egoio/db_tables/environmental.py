# coding: utf-8
from sqlalchemy import Column, Integer, text
from geoalchemy2.types import Raster
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class EcjrcGlc2000(Base):
    __tablename__ = 'ecjrc_glc2000'
    __table_args__ = {'schema': 'environmental'}

    rid = Column(Integer, primary_key=True, server_default=text("nextval('environmental.ecjrc_glc2000_rid_seq'::regclass)"))
    rast = Column(Raster)


class NoaaGlobe(Base):
    __tablename__ = 'noaa_globe'
    __table_args__ = {'schema': 'environmental'}

    rid = Column(Integer, primary_key=True, server_default=text("nextval('environmental.noaa_globe_rid_seq'::regclass)"))
    rast = Column(Raster)

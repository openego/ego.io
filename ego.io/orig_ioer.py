# coding: utf-8
from sqlalchemy import Column, Integer, Numeric, text
from geoalchemy2.types import Geometry, Raster
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IoerUrbanShareIndustrial(Base):
    __tablename__ = 'ioer_urban_share_industrial'
    __table_args__ = {'schema': 'orig_ioer'}

    rid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ioer.ioer_urban_share_industrial_rid_seq'::regclass)"))
    rast = Column(Raster)


class IoerUrbanShareIndustrialCentroid(Base):
    __tablename__ = 'ioer_urban_share_industrial_centroid'
    __table_args__ = {'schema': 'orig_ioer'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ioer.ioer_urban_share_industrial_centroid_id_seq'::regclass)"))
    rid = Column(Integer)
    ioer_share = Column(Numeric)
    geom = Column(Geometry('POINT', 3035), index=True)

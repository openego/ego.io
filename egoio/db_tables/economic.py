# coding: utf-8
from sqlalchemy import Column, Float, Integer, Numeric, String, text
from geoalchemy2.types import Geometry, Raster
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class DestatisGvaPerDistrict(Base):
    __tablename__ = 'destatis_gva_per_district'
    __table_args__ = {'schema': 'economic'}

    eu_code = Column(String(7), primary_key=True)
    district = Column(String, nullable=False)
    total_gva = Column(Float(53), nullable=False)
    gva_industry = Column(Float(53), nullable=False)
    gva_tertiary_sector = Column(Float(53), nullable=False)


class IoerUrbanShareIndustrial(Base):
    __tablename__ = 'ioer_urban_share_industrial'
    __table_args__ = {'schema': 'economic'}

    rid = Column(Integer, primary_key=True, server_default=text("nextval('economic.ioer_urban_share_industrial_rid_seq'::regclass)"))
    rast = Column(Raster)


class IoerUrbanShareIndustrialCentroid(Base):
    __tablename__ = 'ioer_urban_share_industrial_centroid'
    __table_args__ = {'schema': 'economic'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('economic.ioer_urban_share_industrial_centroid_id_seq'::regclass)"))
    rid = Column(Integer)
    ioer_share = Column(Numeric)
    geom = Column(Geometry('POINT', 3035), index=True)

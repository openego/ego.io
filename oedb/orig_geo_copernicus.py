# coding: utf-8
from sqlalchemy import Column, Float, Integer, Numeric, String, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CopernicusClc2012V184(Base):
    __tablename__ = 'copernicus_clc_2012_v_18_4'
    __table_args__ = {'schema': 'orig_geo_copernicus'}

    ogc_fid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_copernicus.clc_corine_land_cover_2012_v_18_4_ogc_fid_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    code_12 = Column(String)
    id = Column(String)
    remark = Column(String)
    area_ha = Column(Float(53))
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))


class CopernicusClc2012V184Filter(Base):
    __tablename__ = 'copernicus_clc_2012_v_18_4_filter'
    __table_args__ = {'schema': 'orig_geo_copernicus'}

    ogc_fid = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035))
    code_12 = Column(String)
    id = Column(String)
    remark = Column(String)
    area_ha = Column(Float(53))
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))


class CopernicusClc2012V184Germany(Base):
    __tablename__ = 'copernicus_clc_2012_v_18_4_germany'
    __table_args__ = {'schema': 'orig_geo_copernicus'}

    ogc_fid = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    code_12 = Column(String)
    id = Column(String)
    remark = Column(String)
    area_ha = Column(Float(53))
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))


class LanduseCalc(Base):
    __tablename__ = 'landuse_calc'
    __table_args__ = {'schema': 'orig_geo_copernicus'}

    id = Column(Integer, primary_key=True)
    source = Column(Text)
    attribute = Column(Text)
    count_int = Column(Integer)
    area_ha = Column(Numeric(15, 1))

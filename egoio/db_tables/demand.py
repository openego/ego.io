# coding: utf-8
from sqlalchemy import Column, Float, Integer, Numeric, String, Text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class EgoDemandFederalstate(Base):
    __tablename__ = 'ego_demand_federalstate'
    __table_args__ = {'schema': 'demand'}

    eu_code = Column(String(7), primary_key=True)
    federal_states = Column(String)
    elec_consumption_households = Column(Float(53))
    elec_consumption_industry = Column(Float(53))
    elec_consumption_tertiary_sector = Column(Float(53))
    population = Column(Integer)
    elec_consumption_households_per_person = Column(Float(53))


class EgoDpLoadarea(Base):
    __tablename__ = 'ego_dp_loadarea'
    __table_args__ = {'schema': 'demand'}

    version = Column(Text, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    otg_id = Column(Integer)
    un_id = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    ioer_sum = Column(Numeric)
    ioer_count = Column(Integer)
    ioer_density = Column(Numeric)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_area_sum = Column(Numeric)
    sector_share_residential = Column(Numeric)
    sector_share_retail = Column(Numeric)
    sector_share_industrial = Column(Numeric)
    sector_share_agricultural = Column(Numeric)
    sector_share_sum = Column(Numeric)
    sector_count_residential = Column(Integer)
    sector_count_retail = Column(Integer)
    sector_count_industrial = Column(Integer)
    sector_count_agricultural = Column(Integer)
    sector_count_sum = Column(Integer)
    sector_consumption_residential = Column(Float(53))
    sector_consumption_retail = Column(Float(53))
    sector_consumption_industrial = Column(Float(53))
    sector_consumption_agricultural = Column(Float(53))
    sector_consumption_sum = Column(Float(53))
    sector_peakload_retail = Column(Float(53))
    sector_peakload_residential = Column(Float(53))
    sector_peakload_industrial = Column(Float(53))
    sector_peakload_agricultural = Column(Float(53))
    geom_centroid = Column(Geometry('POINT', 3035))
    geom_surfacepoint = Column(Geometry('POINT', 3035))
    geom_centre = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035), index=True)

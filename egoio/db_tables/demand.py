# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, Numeric, String, Table, Text
from geoalchemy2.types import Geometry
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


t_ego_demand_federalstate = Table(
    'ego_demand_federalstate', metadata,
    Column('eu_code', String(7)),
    Column('federal_states', String),
    Column('elec_consumption_households', Float(53)),
    Column('elec_consumption_industry', Float(53)),
    Column('elec_consumption_tertiary_sector', Float(53)),
    Column('population', Integer),
    Column('elec_consumption_households_per_person', Float(53)),
    schema='demand'
)


class EgoLoadarea(Base):
    __tablename__ = 'ego_loadarea'
    __table_args__ = {'schema': 'demand'}

    version = Column(ForeignKey('model_draft.ego_scenario.version'), primary_key=True, nullable=False)
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
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)
    sector_consumption_sum = Column(Numeric)
    geom_centroid = Column(Geometry('POINT', 3035))
    geom_surfacepoint = Column(Geometry('POINT', 3035))
    geom_centre = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035))

    ego_scenario = relationship('EgoScenario')


class EgoScenario(Base):
    __tablename__ = 'ego_scenario'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True)
    version_name = Column(Text)
    release = Column(Boolean)
    comment = Column(Text)
    timestamp = Column(DateTime)

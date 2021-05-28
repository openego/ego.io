# coding: utf-8
from sqlalchemy import Column, Float, Integer, Numeric, String, Table, Text
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
    area_ha = Column(Float(53))
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    otg_id = Column(Integer)
    un_id = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Float(53))
    ioer_sum = Column(Float(53))
    ioer_count = Column(Integer)
    ioer_density = Column(Float(53))
    sector_area_residential = Column(Float(53))
    sector_area_retail = Column(Float(53))
    sector_area_industrial = Column(Float(53))
    sector_area_agricultural = Column(Float(53))
    sector_area_sum = Column(Float(53))
    sector_share_residential = Column(Float(53))
    sector_share_retail = Column(Float(53))
    sector_share_industrial = Column(Float(53))
    sector_share_agricultural = Column(Float(53))
    sector_share_sum = Column(Float(53))
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


t_ego_dp_loadarea_v0_4_3_mview = Table(
    'ego_dp_loadarea_v0_4_3_mview', metadata,
    Column('version', Text),
    Column('id', Integer, unique=True),
    Column('subst_id', Integer),
    Column('area_ha', Numeric),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('otg_id', Integer),
    Column('un_id', Integer),
    Column('zensus_sum', Integer),
    Column('zensus_count', Integer),
    Column('zensus_density', Numeric),
    Column('ioer_sum', Numeric),
    Column('ioer_count', Integer),
    Column('ioer_density', Numeric),
    Column('sector_area_residential', Numeric),
    Column('sector_area_retail', Numeric),
    Column('sector_area_industrial', Numeric),
    Column('sector_area_agricultural', Numeric),
    Column('sector_area_sum', Numeric),
    Column('sector_share_residential', Numeric),
    Column('sector_share_retail', Numeric),
    Column('sector_share_industrial', Numeric),
    Column('sector_share_agricultural', Numeric),
    Column('sector_share_sum', Numeric),
    Column('sector_count_residential', Integer),
    Column('sector_count_retail', Integer),
    Column('sector_count_industrial', Integer),
    Column('sector_count_agricultural', Integer),
    Column('sector_count_sum', Integer),
    Column('sector_consumption_residential', Float(53)),
    Column('sector_consumption_retail', Float(53)),
    Column('sector_consumption_industrial', Float(53)),
    Column('sector_consumption_agricultural', Float(53)),
    Column('sector_consumption_sum', Float(53)),
    Column('sector_peakload_retail', Float(53)),
    Column('sector_peakload_residential', Float(53)),
    Column('sector_peakload_industrial', Float(53)),
    Column('sector_peakload_agricultural', Float(53)),
    Column('geom_centroid', Geometry('POINT', 3035)),
    Column('geom_surfacepoint', Geometry('POINT', 3035)),
    Column('geom_centre', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='demand'
)


t_ego_dp_loadarea_v0_4_5_mview = Table(
    'ego_dp_loadarea_v0_4_5_mview', metadata,
    Column('version', Text),
    Column('id', Integer, unique=True),
    Column('subst_id', Integer),
    Column('area_ha', Numeric),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('otg_id', Integer),
    Column('un_id', Integer),
    Column('zensus_sum', Integer),
    Column('zensus_count', Integer),
    Column('zensus_density', Numeric),
    Column('ioer_sum', Numeric),
    Column('ioer_count', Integer),
    Column('ioer_density', Numeric),
    Column('sector_area_residential', Numeric),
    Column('sector_area_retail', Numeric),
    Column('sector_area_industrial', Numeric),
    Column('sector_area_agricultural', Numeric),
    Column('sector_area_sum', Numeric),
    Column('sector_share_residential', Numeric),
    Column('sector_share_retail', Numeric),
    Column('sector_share_industrial', Numeric),
    Column('sector_share_agricultural', Numeric),
    Column('sector_share_sum', Numeric),
    Column('sector_count_residential', Integer),
    Column('sector_count_retail', Integer),
    Column('sector_count_industrial', Integer),
    Column('sector_count_agricultural', Integer),
    Column('sector_count_sum', Integer),
    Column('sector_consumption_residential', Float(53)),
    Column('sector_consumption_retail', Float(53)),
    Column('sector_consumption_industrial', Float(53)),
    Column('sector_consumption_agricultural', Float(53)),
    Column('sector_consumption_sum', Float(53)),
    Column('sector_peakload_retail', Float(53)),
    Column('sector_peakload_residential', Float(53)),
    Column('sector_peakload_industrial', Float(53)),
    Column('sector_peakload_agricultural', Float(53)),
    Column('geom_centroid', Geometry('POINT', 3035)),
    Column('geom_surfacepoint', Geometry('POINT', 3035)),
    Column('geom_centre', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='demand'
)

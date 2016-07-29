# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, Integer, Numeric, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.dialects.postgresql.hstore import HSTORE
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class CalcEgoPeakLoad(Base):
    __tablename__ = 'calc_ego_peak_load'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(BigInteger, primary_key=True, index=True)
    retail = Column(Float(53))
    residential = Column(Float(53))
    industrial = Column(Float(53))
    agricultural = Column(Float(53))


t_calc_ego_peak_load_ta = Table(
    'calc_ego_peak_load_ta', metadata,
    Column('id', BigInteger, index=True),
    Column('retail', Float(53)),
    Column('residential', Float(53)),
    Column('industrial', Float(53)),
    Column('agricultural', Float(53)),
    schema='calc_ego_loads'
)


class EgoDeuConsumption(Base):
    __tablename__ = 'ego_deu_consumption'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)


class EgoDeuConsumptionArea(Base):
    __tablename__ = 'ego_deu_consumption_area'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)
    consumption_sum = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDeuConsumptionAreaTa(Base):
    __tablename__ = 'ego_deu_consumption_area_ta'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)
    consumption_sum = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_deu_consumption_sum = Table(
    'ego_deu_consumption_sum', metadata,
    Column('id', BigInteger),
    Column('sector_consumption_residential', Numeric),
    Column('sector_consumption_retail', Numeric),
    Column('sector_consumption_industrial', Numeric),
    Column('sector_consumption_agricultural', Numeric),
    schema='calc_ego_loads'
)


class EgoDeuConsumptionTa(Base):
    __tablename__ = 'ego_deu_consumption_ta'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)


t_ego_deu_consumption_ta_sum = Table(
    'ego_deu_consumption_ta_sum', metadata,
    Column('id', BigInteger),
    Column('sector_consumption_residential', Numeric),
    Column('sector_consumption_retail', Numeric),
    Column('sector_consumption_industrial', Numeric),
    Column('sector_consumption_agricultural', Numeric),
    schema='calc_ego_loads'
)


class EgoDeuLoadArea(Base):
    __tablename__ = 'ego_deu_load_area'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_loads.ego_deu_loads_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    ioer_sum = Column(Numeric)
    ioer_count = Column(Integer)
    ioer_density = Column(Numeric)
    area_ha = Column(Numeric)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_share_residential = Column(Numeric)
    sector_share_retail = Column(Numeric)
    sector_share_industrial = Column(Numeric)
    sector_share_agricultural = Column(Numeric)
    sector_count_residential = Column(Integer)
    sector_count_retail = Column(Integer)
    sector_count_industrial = Column(Integer)
    sector_count_agricultural = Column(Integer)
    subst_id = Column(Integer)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)
    sector_area_sum = Column(Numeric)
    sector_share_sum = Column(Numeric)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)
    sector_consumption_sum = Column(Numeric)


class EgoDeuLoadAreaLittleTa(Base):
    __tablename__ = 'ego_deu_load_area_little_ta'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    ioer_sum = Column(Numeric)
    ioer_count = Column(Integer)
    ioer_density = Column(Numeric)
    area_ha = Column(Numeric)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_share_residential = Column(Numeric)
    sector_share_retail = Column(Numeric)
    sector_share_industrial = Column(Numeric)
    sector_share_agricultural = Column(Numeric)
    sector_count_residential = Column(Integer)
    sector_count_retail = Column(Integer)
    sector_count_industrial = Column(Integer)
    sector_count_agricultural = Column(Integer)
    subst_id = Column(Integer)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    geom_centroid = Column(Geometry('POINT', 3035))
    geom_surfacepoint = Column(Geometry('POINT', 3035))
    geom_centre = Column(Geometry('POINT', 3035))
    sector_area_sum = Column(Numeric)
    sector_share_sum = Column(Numeric)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)
    sector_consumption_sum = Column(Numeric)


class EgoDeuLoadAreaTa(Base):
    __tablename__ = 'ego_deu_load_area_ta'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    ioer_sum = Column(Numeric)
    ioer_count = Column(Integer)
    ioer_density = Column(Numeric)
    area_ha = Column(Numeric)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_share_residential = Column(Numeric)
    sector_share_retail = Column(Numeric)
    sector_share_industrial = Column(Numeric)
    sector_share_agricultural = Column(Numeric)
    sector_count_residential = Column(Integer)
    sector_count_retail = Column(Integer)
    sector_count_industrial = Column(Integer)
    sector_count_agricultural = Column(Integer)
    subst_id = Column(Integer)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    geom_centroid = Column(Geometry('POINT', 3035))
    geom_surfacepoint = Column(Geometry('POINT', 3035))
    geom_centre = Column(Geometry('POINT', 3035))
    sector_area_sum = Column(Numeric)
    sector_share_sum = Column(Numeric)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)
    sector_consumption_sum = Column(Numeric)


t_ego_deu_load_area_ta_with_peak_loads_mview = Table(
    'ego_deu_load_area_ta_with_peak_loads_mview', metadata,
    Column('id', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    Column('zensus_sum', Integer),
    Column('zensus_count', Integer),
    Column('zensus_density', Numeric),
    Column('ioer_sum', Numeric),
    Column('ioer_count', Integer),
    Column('ioer_density', Numeric),
    Column('area_ha', Numeric),
    Column('sector_area_residential', Numeric),
    Column('sector_area_retail', Numeric),
    Column('sector_area_industrial', Numeric),
    Column('sector_area_agricultural', Numeric),
    Column('sector_share_residential', Numeric),
    Column('sector_share_retail', Numeric),
    Column('sector_share_industrial', Numeric),
    Column('sector_share_agricultural', Numeric),
    Column('sector_count_residential', Integer),
    Column('sector_count_retail', Integer),
    Column('sector_count_industrial', Integer),
    Column('sector_count_agricultural', Integer),
    Column('subst_id', Integer),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('geom_centroid', Geometry('POINT', 3035)),
    Column('geom_surfacepoint', Geometry('POINT', 3035)),
    Column('geom_centre', Geometry('POINT', 3035)),
    Column('sector_area_sum', Numeric),
    Column('sector_share_sum', Numeric),
    Column('sector_consumption_residential', Numeric),
    Column('sector_consumption_retail', Numeric),
    Column('sector_consumption_industrial', Numeric),
    Column('sector_consumption_agricultural', Numeric),
    Column('sector_consumption_sum', Numeric),
    Column('retail', Float(53)),
    Column('residential', Float(53)),
    Column('industrial', Float(53)),
    Column('agricultural', Float(53)),
    schema='calc_ego_loads'
)


t_ego_deu_loads_centre_mview = Table(
    'ego_deu_loads_centre_mview', metadata,
    Column('id', Integer),
    Column('geom_centroid', Geometry('POINT', 3035)),
    schema='calc_ego_loads'
)


t_ego_deu_loads_error_area_ha_mview = Table(
    'ego_deu_loads_error_area_ha_mview', metadata,
    Column('id', Integer),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='calc_ego_loads'
)


class LanduseIndustry(Base):
    __tablename__ = 'landuse_industry'
    __table_args__ = {'schema': 'calc_ego_loads'}

    gid = Column(Integer, primary_key=True)
    osm_id = Column(Integer)
    landuse = Column(Text)
    man_made = Column(Text)
    aeroway = Column(Text)
    name = Column(Text)
    way_area = Column(Float(53))
    area_ha = Column(Float(53))
    tags = Column(HSTORE)
    geom = Column(Geometry('MULTIPOLYGON', 3035))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)
    nuts = Column(String(5))
    consumption = Column(Numeric)
    peak_load = Column(Numeric)


class LargeScaleConsumer(Base):
    __tablename__ = 'large_scale_consumer'
    __table_args__ = {'schema': 'calc_ego_loads'}

    polygon_id = Column(Integer)
    area_ha = Column(Float(53))
    powerplant_id = Column(Integer)
    voltage_level = Column(Float(53))
    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_loads.large_scale_consumer_id_seq'::regclass)"))
    consumption = Column(Numeric)
    peak_load = Column(Numeric)
    geom_centre = Column(Geometry('POINT', 3035))


class LoadsTotal(Base):
    __tablename__ = 'loads_total'
    __table_args__ = {'schema': 'calc_ego_loads'}

    un_id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_loads.loads_total_un_id_seq'::regclass)"))
    la_id = Column(Integer)
    lsc_id = Column(Integer)
    aggr_id_pf = Column(Integer)
    aggr_id_ms = Column(Integer)
    geom_centre = Column(Geometry('POINT', 3035))


class UrbanSectorPerGridDistrict1Residential(Base):
    __tablename__ = 'urban_sector_per_grid_district_1_residential'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_loads.urban_sector_per_grid_district_1_residential_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class UrbanSectorPerGridDistrict2Retail(Base):
    __tablename__ = 'urban_sector_per_grid_district_2_retail'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_loads.urban_sector_per_grid_district_2_retail_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class UrbanSectorPerGridDistrict3Industrial(Base):
    __tablename__ = 'urban_sector_per_grid_district_3_industrial'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_loads.urban_sector_per_grid_district_3_industrial_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class UrbanSectorPerGridDistrict4Agricultural(Base):
    __tablename__ = 'urban_sector_per_grid_district_4_agricultural'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_loads.urban_sector_per_grid_district_4_agricultural_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    subst_id = Column(Integer)

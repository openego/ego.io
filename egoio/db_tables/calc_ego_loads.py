# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, Integer, Numeric, String, \
    Table, text, ForeignKey
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ARRAY

Base = declarative_base()
metadata = Base.metadata


class CalcEgoPeakLoadTa(Base):
    __tablename__ = 'calc_ego_peak_load_ta'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(BigInteger, primary_key=True, index=True)
    retail = Column(Float(53))
    residential = Column(Float(53))
    industrial = Column(Float(53))
    agricultural = Column(Float(53))


class CalcEgoPeakLoad(Base):
    __tablename__ = 'calc_ego_peak_load'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(BigInteger, primary_key=True, index=True)
    retail = Column(Float(53))
    residential = Column(Float(53))
    industrial = Column(Float(53))
    agricultural = Column(Float(53))


class EgoDeuConsumption(Base):
    __tablename__ = 'ego_deu_consumption'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    otg_id = Column(Integer)
    un_id = Column(Integer)
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


class EgoDeuConsumptionTa(Base):
    __tablename__ = 'ego_deu_consumption_ta'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)


class EgoDeuLoadArea(Base):
    __tablename__ = 'ego_deu_load_area'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_ego_loads.ego_deu_loads_id_seq'::regclass)"))
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


class UrbanSectorPerGridDistrict1Residential(Base):
    __tablename__ = 'urban_sector_per_grid_district_1_residential'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_ego_loads.urban_sector_per_grid_district_1_residential_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class UrbanSectorPerGridDistrict2Retail(Base):
    __tablename__ = 'urban_sector_per_grid_district_2_retail'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_ego_loads.urban_sector_per_grid_district_2_retail_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class UrbanSectorPerGridDistrict3Industrial(Base):
    __tablename__ = 'urban_sector_per_grid_district_3_industrial'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_ego_loads.urban_sector_per_grid_district_3_industrial_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class UrbanSectorPerGridDistrict4Agricultural(Base):
    __tablename__ = 'urban_sector_per_grid_district_4_agricultural'
    __table_args__ = {'schema': 'calc_ego_loads'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_ego_loads.urban_sector_per_grid_district_4_agricultural_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDemandPerTransitionPoint(Base):
    __tablename__ = 'ego_demand_per_transition_point'
    __table_args__ = {'schema': 'calc_ego_loads'}
    id = Column(Integer,
                primary_key=True,
                nullable=False)
    p_set = Column(ARRAY(Float(53)))
    q_set = Column(ARRAY(Float(53)))

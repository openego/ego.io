# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Float, ForeignKey, ForeignKeyConstraint, Integer, Numeric, SmallInteger, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY, DOUBLE_PRECISION, INTEGER, NUMERIC, TEXT
from sqlalchemy.dialects.postgresql.hstore import HSTORE
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class DeaGermanyPerLoadArea(Base):
    __tablename__ = 'dea_germany_per_load_area'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)


class EgoDataProcessingResult(Base):
    __tablename__ = 'ego_data_processing_results'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_data_processing_results_id_seq'::regclass)"))
    schema_name = Column(Text)
    table_name = Column(Text)
    description = Column(Text)
    result = Column(Integer)
    unit = Column(Text)
    timestamp = Column(DateTime)


class EgoDataProcessingResultsMvgd(Base):
    __tablename__ = 'ego_data_processing_results_mvgd'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    type1 = Column(Integer)
    type1_cnt = Column(Integer)
    type2 = Column(Integer)
    type2_cnt = Column(Integer)
    type3 = Column(Integer)
    type3_cnt = Column(Integer)
    gem = Column(Integer)
    gem_clean = Column(Integer)
    la_count = Column(Integer)
    area_ha = Column(Numeric(10, 1))
    la_area = Column(Numeric(10, 1))
    free_area = Column(Numeric(10, 1))
    area_share = Column(Numeric(4, 1))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    timestamp = Column(DateTime)
    compound = Column(Text)
    group = Column(String(1))
    consumption = Column(Numeric)
    consumption_per_area = Column(Numeric)


class EgoDeaAgriculturalSectorPerGridDistrict(Base):
    __tablename__ = 'ego_dea_agricultural_sector_per_grid_district'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_dea_agricultural_sector_per_grid_district_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDeaAllocation(Base):
    __tablename__ = 'ego_dea_allocation'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    sort = Column(Integer)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    postcode = Column(String)
    subst_id = Column(Integer)
    source = Column(String)
    la_id = Column(Integer)
    flag = Column(String)
    geom = Column(Geometry('POINT', 3035), index=True)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    geom_new = Column(Geometry('POINT', 3035), index=True)


t_ego_dea_allocation_m1_1_a_mview = Table(
    'ego_dea_allocation_m1_1_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m1_1_mview = Table(
    'ego_dea_allocation_m1_1_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m1_1_rest_mview = Table(
    'ego_dea_allocation_m1_1_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m1_2_a_mview = Table(
    'ego_dea_allocation_m1_2_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m1_2_mview = Table(
    'ego_dea_allocation_m1_2_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m1_2_rest_mview = Table(
    'ego_dea_allocation_m1_2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m2_a_mview = Table(
    'ego_dea_allocation_m2_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m2_mview = Table(
    'ego_dea_allocation_m2_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m2_rest_mview = Table(
    'ego_dea_allocation_m2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m3_a_mview = Table(
    'ego_dea_allocation_m3_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m3_mview = Table(
    'ego_dea_allocation_m3_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m3_rest_mview = Table(
    'ego_dea_allocation_m3_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m4_a_mview = Table(
    'ego_dea_allocation_m4_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m4_mview = Table(
    'ego_dea_allocation_m4_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m4_rest_mview = Table(
    'ego_dea_allocation_m4_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m5_a_mview = Table(
    'ego_dea_allocation_m5_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m5_mview = Table(
    'ego_dea_allocation_m5_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m5_rest_mview = Table(
    'ego_dea_allocation_m5_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_out_mview = Table(
    'ego_dea_allocation_out_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


class EgoDeaPerGenerationTypeAndVoltageLevel(Base):
    __tablename__ = 'ego_dea_per_generation_type_and_voltage_level'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    capacity = Column(Numeric)
    count = Column(BigInteger)


class EgoDeaPerGridDistrict(Base):
    __tablename__ = 'ego_dea_per_grid_district'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)
    mv_dea_cnt = Column(Integer)
    mv_dea_capacity = Column(Numeric)


class EgoDeaPerLoadArea(Base):
    __tablename__ = 'ego_dea_per_load_area'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)


class EgoDeaPerMethod(Base):
    __tablename__ = 'ego_dea_per_method'
    __table_args__ = {'schema': 'model_draft'}

    name = Column(Text, primary_key=True)
    capacity = Column(Numeric)
    count = Column(BigInteger)


class EgoDemandHvLargescaleconsumer(Base):
    __tablename__ = 'ego_demand_hv_largescaleconsumer'
    __table_args__ = {'schema': 'model_draft'}

    polygon_id = Column(Integer)
    area_ha = Column(Float(53))
    powerplant_id = Column(Integer)
    voltage_level = Column(Float(53))
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_hv_largescaleconsumer_id_seq'::regclass)"))
    subst_id = Column(Integer)
    otg_id = Column(Integer)
    un_id = Column(Integer)
    consumption = Column(Float(53))
    peak_load = Column(Float(53))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)


class EgoDemandLoadCollect(Base):
    __tablename__ = 'ego_demand_load_collect'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_load_collect_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDemandLoadCollectBuffer100(Base):
    __tablename__ = 'ego_demand_load_collect_buffer100'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_load_collect_buffer100_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDemandLoadMelt(Base):
    __tablename__ = 'ego_demand_load_melt'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_load_melt_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_demand_load_melt_error_2_geom_mview = Table(
    'ego_demand_load_melt_error_2_geom_mview', metadata,
    Column('id', Integer, unique=True),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_demand_load_melt_error_geom_fix_mview = Table(
    'ego_demand_load_melt_error_geom_fix_mview', metadata,
    Column('id', Integer, unique=True),
    Column('error', Boolean),
    Column('geom_type', Text),
    Column('area', Float(53)),
    Column('geom_buffer', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_demand_load_melt_error_geom_mview = Table(
    'ego_demand_load_melt_error_geom_mview', metadata,
    Column('id', Integer, unique=True),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoDemandLoadarea(Base):
    __tablename__ = 'ego_demand_loadarea'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_loadarea_id_seq'::regclass)"))
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
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_demand_loadarea_error_noags_mview = Table(
    'ego_demand_loadarea_error_noags_mview', metadata,
    Column('id', Integer, unique=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoDemandLoadareaPeakLoad(Base):
    __tablename__ = 'ego_demand_loadarea_peak_load'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, index=True, server_default=text("nextval('model_draft.ego_demand_loadarea_peak_load_id_seq'::regclass)"))
    retail = Column(Float(53))
    residential = Column(Float(53))
    industrial = Column(Float(53))
    agricultural = Column(Float(53))


t_ego_demand_loadarea_smaller100m2_mview = Table(
    'ego_demand_loadarea_smaller100m2_mview', metadata,
    Column('id', Integer, unique=True),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoDemandLoadareaVoi(Base):
    __tablename__ = 'ego_demand_loadarea_voi'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_loadarea_voi_id_seq'::regclass)"))
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
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_demand_loadarea_voi_error_noags_mview = Table(
    'ego_demand_loadarea_voi_error_noags_mview', metadata,
    Column('id', Integer, unique=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_demand_loadarea_voi_smaller100m2_mview = Table(
    'ego_demand_loadarea_voi_smaller100m2_mview', metadata,
    Column('id', Integer, unique=True),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_demand_loadarea_with_peak_loads_mview = Table(
    'ego_demand_loadarea_with_peak_loads_mview', metadata,
    Column('id', Integer),
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
    Column('sector_consumption_residential', Numeric),
    Column('sector_consumption_retail', Numeric),
    Column('sector_consumption_industrial', Numeric),
    Column('sector_consumption_agricultural', Numeric),
    Column('sector_consumption_sum', Numeric),
    Column('geom_centroid', Geometry('POINT', 3035)),
    Column('geom_surfacepoint', Geometry('POINT', 3035)),
    Column('geom_centre', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035)),
    Column('retail', Float(53)),
    Column('residential', Float(53)),
    Column('industrial', Float(53)),
    Column('agricultural', Float(53)),
    schema='model_draft'
)


class EgoDemandLoad(Base):
    __tablename__ = 'ego_demand_loads'
    __table_args__ = {'schema': 'model_draft'}

    un_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_loads_un_id_seq'::regclass)"))
    ssc_id = Column(Integer)
    lsc_id = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoDemandPerDistrict(Base):
    __tablename__ = 'ego_demand_per_district'
    __table_args__ = {'schema': 'model_draft'}

    eu_code = Column(String(7), primary_key=True)
    district = Column(String)
    elec_consumption_industry = Column(Float(53))
    elec_consumption_tertiary_sector = Column(Float(53))
    area_industry = Column(Float(53))
    consumption_per_area_industry = Column(Float(53))
    area_retail = Column(Float(53))
    area_agriculture = Column(Float(53))
    area_tertiary_sector = Column(Float(53))


class EgoDemandPerGva(Base):
    __tablename__ = 'ego_demand_per_gva'
    __table_args__ = {'schema': 'model_draft'}

    eu_code = Column(String(7), primary_key=True)
    federal_states = Column(String)
    elec_consumption_industry = Column(Float(53))
    elec_consumption_tertiary_sector = Column(Float(53))


t_ego_demand_per_load_area = Table(
    'ego_demand_per_load_area', metadata,
    Column('id', Integer),
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
    Column('sector_consumption_residential', Numeric),
    Column('sector_consumption_retail', Numeric),
    Column('sector_consumption_industrial', Numeric),
    Column('sector_consumption_agricultural', Numeric),
    Column('sector_consumption_sum', Numeric),
    Column('geom_centroid', Geometry('POINT', 3035)),
    Column('geom_surfacepoint', Geometry('POINT', 3035)),
    Column('geom_centre', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='model_draft'
)


class EgoDemandPfLoadSingle(Base):
    __tablename__ = 'ego_demand_pf_load_single'
    __table_args__ = (
        ForeignKeyConstraint(['bus', 'scn_name'], ['model_draft.ego_grid_pf_hv_bus.bus_id', 'model_draft.ego_grid_pf_hv_bus.scn_name']),
        {'schema': 'model_draft'}
    )

    scn_name = Column(String, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True)
    bus = Column(BigInteger)
    sign = Column(Float(53), server_default=text("(-1)"))
    e_annual = Column(Float(53))

    ego_grid_pf_hv_bu = relationship('EgoGridPfHvBu')


class EgoDeuLoadsOsm(Base):
    __tablename__ = 'ego_deu_loads_osm'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_deu_loads_osm_id_seq'::regclass)"))
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridEhvSubstation(Base):
    __tablename__ = 'ego_grid_ehv_substation'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, nullable=False, unique=True, server_default=text("nextval('model_draft.ego_grid_ehv_substation_subst_id_seq'::regclass)"))
    lon = Column(Float(53), nullable=False)
    lat = Column(Float(53), nullable=False)
    point = Column(Geometry('POINT', 4326), nullable=False)
    polygon = Column(Geometry, nullable=False)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text, primary_key=True)
    osm_www = Column(Text, nullable=False)
    frequency = Column(Text)
    subst_name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger, nullable=False)
    otg_id = Column(BigInteger)


class EgoGridEhvSubstationVoronoi(EgoGridEhvSubstation):
    __tablename__ = 'ego_grid_ehv_substation_voronoi'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry('POLYGON', 4326), index=True)
    subst_id = Column(ForeignKey('model_draft.ego_grid_ehv_substation.subst_id'), primary_key=True)


class EgoGridHvmvSubstation(Base):
    __tablename__ = 'ego_grid_hvmv_substation'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, nullable=False, server_default=text("nextval('model_draft.ego_grid_hvmv_substation_subst_id_seq'::regclass)"))
    lon = Column(Float(53), nullable=False)
    lat = Column(Float(53), nullable=False)
    point = Column(Geometry('POINT', 4326), nullable=False)
    polygon = Column(Geometry, nullable=False)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text, primary_key=True)
    osm_www = Column(Text, nullable=False)
    frequency = Column(Text)
    subst_name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger, nullable=False)
    otg_id = Column(BigInteger)
    ags_0 = Column(Text)
    geom = Column(Geometry('POINT', 3035), index=True)


class EgoGridHvmvSubstationDummy(Base):
    __tablename__ = 'ego_grid_hvmv_substation_dummy'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    geom = Column(Geometry('POINT', 3035), index=True)


t_ego_grid_hvmv_substation_mun_2_mview = Table(
    'ego_grid_hvmv_substation_mun_2_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('subst_name', Text),
    Column('subst_type', Integer),
    Column('geom', Geometry('POINT', 3035)),
    schema='model_draft'
)


class EgoGridHvmvSubstationVoronoi(Base):
    __tablename__ = 'ego_grid_hvmv_substation_voronoi'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry('POLYGON', 3035), index=True)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_hvmv_substation_voronoi_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_sum = Column(Integer)


class EgoGridHvmvSubstationVoronoiCut(Base):
    __tablename__ = 'ego_grid_hvmv_substation_voronoi_cut'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    subst_id = Column(Integer)
    mun_id = Column(Integer)
    voi_id = Column(Integer)
    ags_0 = Column(String(12))
    subst_type = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    subst_sum = Column(Integer)
    geom_sub = Column(Geometry('POINT', 3035), index=True)


t_ego_grid_hvmv_substation_voronoi_cut_0subst_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_0subst_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('subst_id', Integer),
    Column('mun_id', Integer),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_cut_0subst_nn_line_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_0subst_nn_line_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('voi_id', BigInteger),
    Column('subst_id', Integer),
    Column('geom_centre', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_cut_0subst_nn_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_0subst_nn_mview', metadata,
    Column('voi_id', BigInteger, unique=True),
    Column('voi_ags_0', String(12)),
    Column('geom_voi', Geometry('POLYGON', 3035), index=True),
    Column('subst_id', Integer),
    Column('ags_0', String(12)),
    Column('geom_sub', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_cut_0subst_nn_union_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_0subst_nn_union_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_cut_1subst_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_1subst_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('subst_id', Integer),
    Column('mun_id', Integer),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    Column('subst_sum', Integer),
    Column('geom_sub', Geometry('POINT', 3035)),
    schema='model_draft'
)


class EgoGridHvmvSubstationVoronoiCutNnCollect(Base):
    __tablename__ = 'ego_grid_hvmv_substation_voronoi_cut_nn_collect'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_hvmv_substation_voronoi_cut_nn_collect_id_seq'::regclass)"))
    subst_id = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_ego_grid_hvmv_substation_voronoi_cut_nn_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_nn_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_mview = Table(
    'ego_grid_hvmv_substation_voronoi_mview', metadata,
    Column('id', Integer, unique=True),
    Column('subst_id', Integer),
    Column('subst_sum', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoGridLvGridDistrictsVoronoi(Base):
    __tablename__ = 'ego_grid_lv_grid_districts_voronoi'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_grid_districts_voronoi_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035))
    la_id = Column(Integer)


class EgoGridLvGriddistrict(Base):
    __tablename__ = 'ego_grid_lv_griddistrict'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry('POLYGON', 3035), index=True)
    load_area_id = Column(Integer)
    merge_id = Column(Integer)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_cut_id_seq'::regclass)"))
    ons_id = Column(Integer)


class EgoGridLvGriddistrictpt(Base):
    __tablename__ = 'ego_grid_lv_griddistrictpts'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_griddistrictpts_id_seq'::regclass)"))
    geom = Column(Geometry('POINT', 3035))
    textgeom = Column(Text)
    ont = Column(Integer)
    ont_distance = Column(Integer)


class EgoGridLvHouseconnection(Base):
    __tablename__ = 'ego_grid_lv_houseconnection'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_houseconnection_id_seq'::regclass)"))
    geom = Column(Geometry('POINT', 3035))


t_ego_grid_lv_loadarea_ta_mview = Table(
    'ego_grid_lv_loadarea_ta_mview', metadata,
    Column('id', Integer, unique=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
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
    Column('sector_consumption_residential', Numeric),
    Column('sector_consumption_retail', Numeric),
    Column('sector_consumption_industrial', Numeric),
    Column('sector_consumption_agricultural', Numeric),
    Column('sector_consumption_sum', Numeric),
    Column('subst_id', Integer),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('geom_centroid', Geometry('POINT', 3035)),
    Column('geom_surfacepoint', Geometry('POINT', 3035)),
    Column('geom_centre', Geometry('POINT', 3035)),
    Column('realnr', BigInteger),
    schema='model_draft'
)


t_ego_grid_lv_ontnumber = Table(
    'ego_grid_lv_ontnumber', metadata,
    Column('id', Integer),
    Column('modnr', BigInteger),
    schema='model_draft'
)


class EgoGridLvStreet(Base):
    __tablename__ = 'ego_grid_lv_streets'
    __table_args__ = {'schema': 'model_draft'}

    line_gid = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    load_area_id = Column(Integer)
    ontnumber = Column(BigInteger)
    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('model_draft.ego_grid_lv_streets_id_seq'::regclass)"))


class EgoGridLvStreetsegment(Base):
    __tablename__ = 'ego_grid_lv_streetsegments'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_streetsegments_id_seq'::regclass)"))
    geom = Column(Geometry('LINESTRING', 3035))


class EgoGridLvTestont(Base):
    __tablename__ = 'ego_grid_lv_testonts'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry('POINT', 3035), index=True)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_testonts_id_seq'::regclass)"))
    subst_id = Column(Integer)
    load_area_id = Column(Integer)
    is_dummy = Column(Boolean)


t_ego_grid_lv_validationstreets_mview = Table(
    'ego_grid_lv_validationstreets_mview', metadata,
    Column('id', Integer, unique=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='model_draft'
)


class EgoGridMvGriddistrict(Base):
    __tablename__ = 'ego_grid_mv_griddistrict'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    subst_sum = Column(Integer)
    area_ha = Column(Numeric)
    geom_type = Column(Text)
    type1 = Column(Integer)
    type1_cnt = Column(Integer)
    type2 = Column(Integer)
    type2_cnt = Column(Integer)
    type3 = Column(Integer)
    type3_cnt = Column(Integer)
    group = Column(String(1))
    gem = Column(Integer)
    gem_clean = Column(Integer)
    la_count = Column(Integer)
    la_area = Column(Numeric(10, 1))
    free_area = Column(Numeric(10, 1))
    area_share = Column(Numeric(4, 1))
    consumption = Column(Numeric)
    consumption_per_area = Column(Numeric)
    dea_cnt = Column(Integer)
    dea_capacity = Column(Numeric)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)
    mv_dea_cnt = Column(Integer)
    mv_dea_capacity = Column(Numeric)


class EgoGridMvGriddistrictCollect(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_collect'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_collect_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictDump(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    subst_id = Column(Integer)
    geom = Column(Geometry, index=True)
    subst_cnt = Column(Integer)


class EgoGridMvGriddistrictSimple(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_simple'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True, nullable=False)
    factor = Column(Text, primary_key=True, nullable=False)
    geom = Column(Geometry('MULTIPOLYGON', 3035))


class EgoGridMvGriddistrictType1(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_type1'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictType2(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_type2'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictType3(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_type3'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvlvOntcontrolgroup(Base):
    __tablename__ = 'ego_grid_mvlv_ontcontrolgroup'
    __table_args__ = {'schema': 'model_draft'}

    area_id = Column(Integer)
    geom = Column(Geometry('POINT', 3035), index=True)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mvlv_ontcontrolgroup_id_seq'::regclass)"))
    pop50 = Column(Integer)
    pop100 = Column(Integer)
    pop250 = Column(Integer)
    pop500 = Column(Integer)
    pop1000 = Column(Integer)
    diststreet = Column(Integer)
    distcrossroad = Column(Integer)
    buildingsnr50 = Column(Integer)
    buildingsnr100 = Column(Integer)
    buildingsnr250 = Column(Integer)
    buildingsnr500 = Column(Integer)
    buildingsnr1000 = Column(Integer)
    buildingsarea50 = Column(Integer)
    buildingsarea100 = Column(Integer)
    buildingsarea250 = Column(Integer)
    buildingsarea500 = Column(Integer)
    buildingsarea1000 = Column(Integer)


class EgoGridMvlvOnt(Base):
    __tablename__ = 'ego_grid_mvlv_onts'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_onts_id_seq'::regclass)"))
    geom = Column(Geometry('POINT', 3035), index=True)
    subst_id = Column(Integer)
    la_id = Column(Integer)
    is_dummy = Column(Boolean)


class EgoGridMvlvReferenceontpoint(Base):
    __tablename__ = 'ego_grid_mvlv_referenceontpoints'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POINT', 3035), index=True)
    pop50 = Column(Integer)
    pop100 = Column(Integer)
    pop250 = Column(Integer)
    pop500 = Column(Integer)
    pop1000 = Column(Integer)
    diststreet = Column(Integer)
    distcrossroad = Column(Integer)
    buildingsnr50 = Column(Integer)
    buildingsnr100 = Column(Integer)
    buildingsnr250 = Column(Integer)
    buildingsnr500 = Column(Integer)
    buildingsnr1000 = Column(Integer)
    buildingsarea50 = Column(Integer)
    buildingsarea100 = Column(Integer)
    buildingsarea250 = Column(Integer)
    buildingsarea500 = Column(Integer)
    buildingsarea1000 = Column(Integer)


class EgoGridMvlvReferenceont(Base):
    __tablename__ = 'ego_grid_mvlv_referenceonts'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(Numeric(10, 0))
    extrude = Column(Numeric(10, 0))
    visibility = Column(Numeric(10, 0))
    draworder = Column(Numeric(10, 0))
    icon = Column(String(254))
    geom = Column(Geometry('LINESTRINGZM', 3035), index=True)
    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('model_draft.ego_grid_mvlv_referenceonts_id_seq'::regclass)"))


class EgoGridPfHvBu(Base):
    __tablename__ = 'ego_grid_pf_hv_bus'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    current_type = Column(Text, server_default=text("'AC'::text"))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))


class EgoGridPfHvBusVMagSet(Base):
    __tablename__ = 'ego_grid_pf_hv_bus_v_mag_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('model_draft.ego_grid_pf_hv_temp_resolution.temp_id'), primary_key=True, nullable=False)
    v_mag_pu_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))

    temp = relationship('EgoGridPfHvTempResolution')


class EgoGridPfHvGenerator(Base):
    __tablename__ = 'ego_grid_pf_hv_generator'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    dispatch = Column(Text, server_default=text("'flexible'::text"))
    control = Column(Text, server_default=text("'PQ'::text"))
    p_nom = Column(Float(53), server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    p_min_pu_fixed = Column(Float(53), server_default=text("0"))
    p_max_pu_fixed = Column(Float(53), server_default=text("1"))
    sign = Column(Float(53), server_default=text("1"))
    source = Column(ForeignKey('model_draft.ego_grid_pf_hv_source.source_id'), index=True)
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))

    ego_grid_pf_hv_source = relationship('EgoGridPfHvSource')


class EgoGridPfHvGeneratorPqSet(Base):
    __tablename__ = 'ego_grid_pf_hv_generator_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('model_draft.ego_grid_pf_hv_temp_resolution.temp_id'), primary_key=True, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_min_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_max_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))

    temp = relationship('EgoGridPfHvTempResolution')


class EgoGridPfHvLine(Base):
    __tablename__ = 'ego_grid_pf_hv_line'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    line_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Numeric, server_default=text("0"))
    s_nom_extendable = Column(Boolean, server_default=text("false"))
    s_nom_min = Column(Float(53), server_default=text("0"))
    s_nom_max = Column(Float(53))
    capital_cost = Column(Float(53))
    length = Column(Float(53))
    cables = Column(Integer)
    frequency = Column(Numeric)
    terrain_factor = Column(Float(53), server_default=text("1"))
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))


class EgoGridPfHvLoad(Base):
    __tablename__ = 'ego_grid_pf_hv_load'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    sign = Column(Float(53), server_default=text("(-1)"))
    e_annual = Column(Float(53))


class EgoGridPfHvLoadPqSet(Base):
    __tablename__ = 'ego_grid_pf_hv_load_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('model_draft.ego_grid_pf_hv_temp_resolution.temp_id'), primary_key=True, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))

    temp = relationship('EgoGridPfHvTempResolution')


class EgoGridPfHvScenarioSetting(Base):
    __tablename__ = 'ego_grid_pf_hv_scenario_settings'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, server_default=text("'Status Quo'::character varying"))
    bus = Column(String)
    bus_v_mag_set = Column(String)
    generator = Column(String)
    generator_pq_set = Column(String)
    line = Column(String)
    load = Column(String)
    load_pq_set = Column(String)
    storage = Column(String)
    storage_pq_set = Column(String)
    temp_resolution = Column(String)
    transformer = Column(String)


class EgoGridPfHvSource(Base):
    __tablename__ = 'ego_grid_pf_hv_source'
    __table_args__ = {'schema': 'model_draft'}

    source_id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    co2_emissions = Column(Float(53))
    commentary = Column(Text)


class EgoGridPfHvStorage(Base):
    __tablename__ = 'ego_grid_pf_hv_storage'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    dispatch = Column(Text, server_default=text("'flexible'::text"))
    control = Column(Text, server_default=text("'PQ'::text"))
    p_nom = Column(Float(53), server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    p_min_pu_fixed = Column(Float(53), server_default=text("0"))
    p_max_pu_fixed = Column(Float(53), server_default=text("1"))
    sign = Column(Float(53), server_default=text("1"))
    source = Column(ForeignKey('model_draft.ego_grid_pf_hv_source.source_id'), index=True)
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))
    soc_initial = Column(Float(53))
    soc_cyclic = Column(Boolean, server_default=text("false"))
    max_hours = Column(Float(53))
    efficiency_store = Column(Float(53))
    efficiency_dispatch = Column(Float(53))
    standing_loss = Column(Float(53))

    ego_grid_pf_hv_source = relationship('EgoGridPfHvSource')


class EgoGridPfHvStoragePqSet(Base):
    __tablename__ = 'ego_grid_pf_hv_storage_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('model_draft.ego_grid_pf_hv_temp_resolution.temp_id'), primary_key=True, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_min_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_max_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    soc_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    inflow = Column(ARRAY(DOUBLE_PRECISION(precision=53)))

    temp = relationship('EgoGridPfHvTempResolution')


class EgoGridPfHvTempResolution(Base):
    __tablename__ = 'ego_grid_pf_hv_temp_resolution'
    __table_args__ = {'schema': 'model_draft'}

    temp_id = Column(BigInteger, primary_key=True)
    timesteps = Column(BigInteger, nullable=False)
    resolution = Column(Text)
    start_time = Column(DateTime)


class EgoGridPfHvTransformer(Base):
    __tablename__ = 'ego_grid_pf_hv_transformer'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    trafo_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger, index=True)
    bus1 = Column(BigInteger, index=True)
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Float(53), server_default=text("0"))
    s_nom_extendable = Column(Boolean, server_default=text("false"))
    s_nom_min = Column(Float(53), server_default=text("0"))
    s_nom_max = Column(Float(53))
    tap_ratio = Column(Float(53))
    phase_shift = Column(Float(53))
    capital_cost = Column(Float(53), server_default=text("0"))
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))


class EgoLanduseIndustry(Base):
    __tablename__ = 'ego_landuse_industry'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True)
    osm_id = Column(Integer)
    name = Column(Text)
    sector = Column(Integer)
    area_ha = Column(Float(53))
    tags = Column(HSTORE)
    vg250 = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)
    nuts = Column(String(5))
    consumption = Column(Numeric)
    peak_load = Column(Numeric)


class EgoLattice500m(Base):
    __tablename__ = 'ego_lattice_500m'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_lattice_500m_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_type = Column(Text)
    geom_box = Column(Geometry('POLYGON', 3035), index=True)
    geom = Column(Geometry('POINT', 3035), index=True)


t_ego_lattice_500m_la_mview = Table(
    'ego_lattice_500m_la_mview', metadata,
    Column('id', Integer),
    Column('subst_id', Integer),
    Column('area_type', Text),
    Column('geom_box', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_lattice_500m_out_mview = Table(
    'ego_lattice_500m_out_mview', metadata,
    Column('id', Integer),
    Column('subst_id', Integer),
    Column('area_type', Text),
    Column('geom_box', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_lattice_500m_wpa_mview = Table(
    'ego_lattice_500m_wpa_mview', metadata,
    Column('id', Integer),
    Column('subst_id', Integer),
    Column('area_type', Text),
    Column('geom_box', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_lattice_500m_x_mview = Table(
    'ego_lattice_500m_x_mview', metadata,
    Column('id', Integer),
    Column('subst_id', Integer),
    Column('area_type', Text),
    Column('geom_box', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


class EgoLattice50m(Base):
    __tablename__ = 'ego_lattice_50m'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_lattice_50m_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_type = Column(Text)
    geom_box = Column(Geometry('POLYGON', 3035), index=True)
    geom = Column(Geometry('POINT', 3035), index=True)


t_ego_lattice_50m_la_mview = Table(
    'ego_lattice_50m_la_mview', metadata,
    Column('id', Integer),
    Column('subst_id', Integer),
    Column('area_type', Text),
    Column('geom_box', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


class EgoLatticeDeu500m(Base):
    __tablename__ = 'ego_lattice_deu_500m'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_lattice_deu_500m_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_type = Column(Text)
    geom_box = Column(Geometry('POLYGON', 3035), index=True)
    geom = Column(Geometry('POINT', 3035), index=True)


t_ego_lv_validationarea = Table(
    'ego_lv_validationarea', metadata,
    Column('gid', Integer),
    Column('__gid', Numeric(10, 0)),
    Column('ade', Numeric),
    Column('gf', Numeric),
    Column('bsg', Numeric),
    Column('rs', String(12)),
    Column('ags', String(12)),
    Column('sdv_rs', String(12)),
    Column('gen', String(50)),
    Column('bez', String(50)),
    Column('ibz', Numeric),
    Column('bem', String(75)),
    Column('nbd', String(4)),
    Column('sn_l', String(2)),
    Column('sn_r', String(1)),
    Column('sn_k', String(2)),
    Column('sn_v1', String(2)),
    Column('sn_v2', String(2)),
    Column('sn_g', String(3)),
    Column('fk_s3', String(2)),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('wsk', Date),
    Column('debkg_id', String(16)),
    Column('geom', Geometry('MULTIPOLYGON'), index=True),
    Column('vnb_name', Text),
    schema='model_draft'
)


class EgoOsmAgriculturePerMvgd(Base):
    __tablename__ = 'ego_osm_agriculture_per_mvgd'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_agriculture_per_mvgd_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmDeuStreetStreetcrossing(Base):
    __tablename__ = 'ego_osm_deu_street_streetcrossing'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry, index=True)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_deu_street_streetcrossing_id_seq'::regclass)"))


class EgoOsmSectorPerGriddistrict1Residential(Base):
    __tablename__ = 'ego_osm_sector_per_griddistrict_1_residential'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_griddistrict_1_residential_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerGriddistrict2Retail(Base):
    __tablename__ = 'ego_osm_sector_per_griddistrict_2_retail'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_griddistrict_2_retail_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerGriddistrict3Industrial(Base):
    __tablename__ = 'ego_osm_sector_per_griddistrict_3_industrial'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_griddistrict_3_industrial_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerGriddistrict4Agricultural(Base):
    __tablename__ = 'ego_osm_sector_per_griddistrict_4_agricultural'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_griddistrict_4_agricultural_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoPoliticalBoundaryBkgVg2506GemClean(Base):
    __tablename__ = 'ego_political_boundary_bkg_vg250_6_gem_clean'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_political_boundary_bkg_vg250_6_gem_clean_id_seq'::regclass)"))
    old_id = Column(Integer)
    gen = Column(Text)
    bez = Column(Text)
    bem = Column(Text)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    area_km2 = Column(Numeric)
    count_hole = Column(Integer)
    path = Column(ARRAY(INTEGER()))
    is_hole = Column(Boolean)
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_political_boundary_bkg_vg250_6_gem_hole_mview = Table(
    'ego_political_boundary_bkg_vg250_6_gem_hole_mview', metadata,
    Column('id', Integer, unique=True),
    Column('old_id', Integer),
    Column('gen', Text),
    Column('bez', Text),
    Column('bem', Text),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('area_km2', Numeric),
    Column('count_hole', Integer),
    Column('path', ARRAY(INTEGER())),
    Column('is_hole', Boolean),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoPoliticalBoundaryHvmvSubstPerGem(Base):
    __tablename__ = 'ego_political_boundary_hvmv_subst_per_gem'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    old_id = Column(Integer)
    gen = Column(Text)
    bez = Column(Text)
    bem = Column(Text)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    area_km2 = Column(Numeric)
    count_hole = Column(Integer)
    path = Column(ARRAY(INTEGER()))
    is_hole = Column(Boolean)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)


t_ego_political_boundary_hvmv_subst_per_gem_1_mview = Table(
    'ego_political_boundary_hvmv_subst_per_gem_1_mview', metadata,
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='model_draft'
)


t_ego_political_boundary_hvmv_subst_per_gem_2_mview = Table(
    'ego_political_boundary_hvmv_subst_per_gem_2_mview', metadata,
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='model_draft'
)


t_ego_political_boundary_hvmv_subst_per_gem_3_mview = Table(
    'ego_political_boundary_hvmv_subst_per_gem_3_mview', metadata,
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='model_draft'
)


class EgoPoliticalBoundaryHvmvSubstPerGem3Nn(Base):
    __tablename__ = 'ego_political_boundary_hvmv_subst_per_gem_3_nn'
    __table_args__ = {'schema': 'model_draft'}

    mun_id = Column(Integer, primary_key=True)
    mun_ags_0 = Column(String(12))
    subst_ags_0 = Column(Text)
    subst_id = Column(Integer)
    subst_type = Column(Integer)
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    distance = Column(Float(53))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_ego_political_boundary_hvmv_subst_per_gem_3_nn_line = Table(
    'ego_political_boundary_hvmv_subst_per_gem_3_nn_line', metadata,
    Column('id', BigInteger, unique=True),
    Column('nn_id', Integer),
    Column('subst_id', Integer),
    Column('geom_centre', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='model_draft'
)


t_ego_political_boundary_hvmv_subst_per_gem_3_nn_union = Table(
    'ego_political_boundary_hvmv_subst_per_gem_3_nn_union', metadata,
    Column('subst_id', Integer, unique=True),
    Column('subst_type', Integer),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoScenario(Base):
    __tablename__ = 'ego_scenario'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True)
    version_name = Column(Text)
    release = Column(Boolean)
    comment = Column(Text)
    timestamp = Column(DateTime)


class EgoScenarioLog(Base):
    __tablename__ = 'ego_scenario_log'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_scenario_log_id_seq'::regclass)"))
    version = Column(ForeignKey('model_draft.ego_scenario.version'))
    io = Column(Text)
    schema_name = Column(Text)
    table_name = Column(Text)
    script_name = Column(Text)
    entries = Column(Integer)
    status = Column(Text)
    user_name = Column(Text)
    timestamp = Column(DateTime)
    meta_data = Column('metadata', Text)

    ego_scenario = relationship('EgoScenario')


class EgoSmallChpPlantGermany(Base):
    __tablename__ = 'ego_small_chp_plant_germany'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    start_up_date = Column(DateTime)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    thermal_capacity = Column(Numeric)
    city = Column(String)
    postcode = Column(String)
    address = Column(String)
    lon = Column(Numeric)
    lat = Column(Numeric)
    gps_accuracy = Column(String)
    validation = Column(String)
    notification_reason = Column(String)
    eeg_id = Column(String)
    tso = Column(Float(53))
    tso_eic = Column(String)
    dso_id = Column(String)
    dso = Column(String)
    voltage_level = Column(String)
    network_node = Column(String)
    power_plant_id = Column(String)
    source = Column(String)
    comment = Column(String)
    geom = Column(Geometry('POINT', 4326))


class EgoSocialZensusLoad(Base):
    __tablename__ = 'ego_social_zensus_load'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_social_zensus_load_id_seq'::regclass)"))
    gid = Column(Integer)
    population = Column(Integer)
    inside_la = Column(Boolean)
    geom_point = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoSocialZensusLoadCluster(Base):
    __tablename__ = 'ego_social_zensus_load_cluster'
    __table_args__ = {'schema': 'model_draft'}

    cid = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_social_zensus_load_cluster_cid_seq'::regclass)"))
    zensus_sum = Column(Integer)
    area_ha = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_buffer = Column(Geometry('POLYGON', 3035))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)


t_ego_social_zensus_per_la_mview = Table(
    'ego_social_zensus_per_la_mview', metadata,
    Column('name', Text),
    Column('population', Numeric),
    schema='model_draft'
)


class EgoSupplyGenerator(Base):
    __tablename__ = 'ego_supply_generator'
    __table_args__ = {'schema': 'model_draft'}

    un_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_generator_un_id_seq'::regclass)"))
    re_id = Column(Integer)
    conv_id = Column(Integer)
    aggr_id_pf = Column(Integer)
    aggr_id_ms = Column(Integer)
    geom = Column(Geometry('POINT', 4326), index=True)


class EgoSupplyPfGeneratorSingle(Base):
    __tablename__ = 'ego_supply_pf_generator_single'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    dispatch = Column(Text, server_default=text("'flexible'::text"))
    control = Column(Text, server_default=text("'PQ'::text"))
    p_nom = Column(Float(53), server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    p_min_pu_fixed = Column(Float(53), server_default=text("0"))
    p_max_pu_fixed = Column(Float(53), server_default=text("1"))
    sign = Column(Float(53), server_default=text("1"))
    source = Column(ForeignKey('model_draft.ego_grid_pf_hv_source.source_id'))
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))
    w_id = Column(Integer)
    aggr_id = Column(Integer)

    ego_grid_pf_hv_source = relationship('EgoGridPfHvSource')


class EgoSupplyPvDev2035GermanyMun(Base):
    __tablename__ = 'ego_supply_pv_dev_2035_germany_mun'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.ego_supply_pv_dev_2035_germany_mun_id_seq'::regclass)"))
    pv_units = Column(Integer)
    pv_cap_2014 = Column(Integer)
    pv_add_cap_2035 = Column(Integer)
    voltage_level = Column(SmallInteger)
    rs_0 = Column(String(12))
    pv_avg_cap = Column(Integer)
    pv_new_units = Column(Numeric(9, 2))


class EgoSupplyRea(Base):
    __tablename__ = 'ego_supply_rea'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    postcode = Column(String)
    source = Column(String)
    subst_id = Column(BigInteger)
    la_id = Column(Integer)
    sort = Column(Integer)
    flag = Column(String)
    geom = Column(Geometry('POINT', 3035), index=True)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    geom_new = Column(Geometry('POINT', 3035), index=True)


t_ego_supply_rea_m1_1_a_mview = Table(
    'ego_supply_rea_m1_1_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m1_1_mview = Table(
    'ego_supply_rea_m1_1_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('source', String),
    Column('subst_id', BigInteger),
    Column('la_id', Integer),
    Column('sort', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m1_1_rest_mview = Table(
    'ego_supply_rea_m1_1_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m1_2_a_mview = Table(
    'ego_supply_rea_m1_2_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m1_2_mview = Table(
    'ego_supply_rea_m1_2_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('source', String),
    Column('subst_id', BigInteger),
    Column('la_id', Integer),
    Column('sort', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m1_2_rest_mview = Table(
    'ego_supply_rea_m1_2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m2_a_mview = Table(
    'ego_supply_rea_m2_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m2_mview = Table(
    'ego_supply_rea_m2_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('source', String),
    Column('subst_id', BigInteger),
    Column('la_id', Integer),
    Column('sort', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m2_rest_mview = Table(
    'ego_supply_rea_m2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


class EgoSupplyReaM2Windfarm(Base):
    __tablename__ = 'ego_supply_rea_m2_windfarm'
    __table_args__ = {'schema': 'model_draft'}

    farm_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_rea_m2_windfarm_farm_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    dea_cnt = Column(Integer)
    electrical_capacity_sum = Column(Numeric)
    geom_new = Column(Geometry('POLYGON', 3035))
    geom_line = Column(Geometry('LINESTRING', 3035))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_supply_rea_m3_a_mview = Table(
    'ego_supply_rea_m3_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m3_mview = Table(
    'ego_supply_rea_m3_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('source', String),
    Column('subst_id', BigInteger),
    Column('la_id', Integer),
    Column('sort', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m3_rest_mview = Table(
    'ego_supply_rea_m3_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m4_a_mview = Table(
    'ego_supply_rea_m4_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m4_mview = Table(
    'ego_supply_rea_m4_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('source', String),
    Column('subst_id', BigInteger),
    Column('la_id', Integer),
    Column('sort', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m4_rest_mview = Table(
    'ego_supply_rea_m4_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m5_a_mview = Table(
    'ego_supply_rea_m5_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m5_mview = Table(
    'ego_supply_rea_m5_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('source', String),
    Column('subst_id', BigInteger),
    Column('la_id', Integer),
    Column('sort', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m5_rest_mview = Table(
    'ego_supply_rea_m5_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_supply_rea_out_mview = Table(
    'ego_supply_rea_out_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('source', String),
    Column('subst_id', BigInteger),
    Column('la_id', Integer),
    Column('sort', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


class EgoSupplyReaPerGentypeAndVoltlevel(Base):
    __tablename__ = 'ego_supply_rea_per_gentype_and_voltlevel'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(SmallInteger)
    capacity = Column(Numeric)
    count = Column(BigInteger)


class EgoSupplyReaPerLoadarea(Base):
    __tablename__ = 'ego_supply_rea_per_loadarea'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)


class EgoSupplyReaPerMethod(Base):
    __tablename__ = 'ego_supply_rea_per_method'
    __table_args__ = {'schema': 'model_draft'}

    name = Column(Text, primary_key=True)
    capacity = Column(Numeric)
    count = Column(BigInteger)


class EgoSupplyReaPerMvgd(Base):
    __tablename__ = 'ego_supply_rea_per_mvgd'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    dea_cnt = Column(Integer)
    dea_capacity = Column(Numeric)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)
    mv_dea_cnt = Column(Integer)
    mv_dea_capacity = Column(Numeric)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoSupplyResPowerplant2035(Base):
    __tablename__ = 'ego_supply_res_powerplant_2035'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    scenario_year = Column(Integer)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text, index=True)
    generation_subtype = Column(String)
    thermal_capacity = Column(Numeric)
    nuts = Column(String)
    lon = Column(Numeric)
    lat = Column(Numeric)
    voltage_level = Column(SmallInteger)
    network_node = Column(String)
    source = Column(String)
    comment = Column(String)
    geom = Column(Geometry('POINT', 4326), index=True)
    voltage = Column(String)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)


class EgoSupplyResPowerplant2050(Base):
    __tablename__ = 'ego_supply_res_powerplant_2050'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    scenario_year = Column(Integer)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text, index=True)
    generation_subtype = Column(String)
    thermal_capacity = Column(Numeric)
    nuts = Column(String)
    lon = Column(Numeric)
    lat = Column(Numeric)
    voltage_level = Column(SmallInteger)
    network_node = Column(String)
    source = Column(String)
    comment = Column(String)
    geom = Column(Geometry('POINT', 4326), index=True)
    voltage = Column(String)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)


class EgoSupplyResPowerplantGermanyToRegion(Base):
    __tablename__ = 'ego_supply_res_powerplant_germany_to_region'
    __table_args__ = {'schema': 'model_draft'}

    re_id = Column(BigInteger, primary_key=True)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    id_vg250 = Column(BigInteger)


class EgoSupplyResPowerplantGermanyToRegion2050(Base):
    __tablename__ = 'ego_supply_res_powerplant_germany_to_region_2050'
    __table_args__ = {'schema': 'model_draft'}

    re_id = Column(BigInteger, primary_key=True)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    id_vg250 = Column(BigInteger)


class EgoSupplyWoDev2035GermanyMun(Base):
    __tablename__ = 'ego_supply_wo_dev_2035_germany_mun'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.ego_supply_wo_dev_2035_germany_mun_id_seq'::regclass)"))
    wo_units = Column(Integer)
    wo_cap_2014 = Column(Integer)
    wo_add_cap_2035 = Column(Integer)
    voltage_level = Column(SmallInteger)
    rs_0 = Column(String(12))
    wo_avg_cap = Column(Integer)
    wo_new_units = Column(Numeric(9, 2))


class EgoSupplyWpa(Base):
    __tablename__ = 'ego_supply_wpa'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_wpa_id_seq'::regclass)"))
    region_key = Column(String(12))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoSupplyWpaPerMvgd(Base):
    __tablename__ = 'ego_supply_wpa_per_mvgd'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_wpa_per_mvgd_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoWpa(Base):
    __tablename__ = 'ego_wpa'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_wpa_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoWpaPerGridDistrict(Base):
    __tablename__ = 'ego_wpa_per_grid_district'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_wpa_per_grid_district_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035))


t_osm_deu_polygon_urban_buffer100_mview = Table(
    'osm_deu_polygon_urban_buffer100_mview', metadata,
    Column('id', Integer, unique=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class RenpassGisEconomicLinearTransformer(Base):
    __tablename__ = 'renpass_gis_economic_linear_transformer'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_economic_linear_transformer_id_seq'::regclass)"))
    scenario_id = Column(ForeignKey('model_draft.renpass_gis_economic_scenario.id'))
    label = Column(String(250))
    source = Column(String(250))
    target = Column(String(250))
    conversion_factors = Column(ARRAY(NUMERIC()))
    summed_min = Column(ARRAY(NUMERIC()))
    nominal_value = Column(ARRAY(NUMERIC()))
    actual_value = Column(ARRAY(NUMERIC()))
    fixed = Column(Boolean)
    variable_costs = Column(ARRAY(NUMERIC()))
    fixed_costs = Column(ARRAY(NUMERIC()))

    scenario = relationship('RenpassGisEconomicScenario')


class RenpassGisEconomicScenario(Base):
    __tablename__ = 'renpass_gis_economic_scenario'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_economic_scenario_id_seq'::regclass)"))
    name = Column(String(250), nullable=False, unique=True)


class RenpassGisEconomicSink(Base):
    __tablename__ = 'renpass_gis_economic_sink'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_economic_sink_id_seq'::regclass)"))
    scenario_id = Column(ForeignKey('model_draft.renpass_gis_economic_scenario.id'))
    label = Column(String(250))
    source = Column(String(250))
    target = Column(String(250))
    nominal_value = Column(ARRAY(NUMERIC()))
    actual_value = Column(ARRAY(NUMERIC()))
    fixed = Column(Boolean)

    scenario = relationship('RenpassGisEconomicScenario')


class RenpassGisEconomicSource(Base):
    __tablename__ = 'renpass_gis_economic_source'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_economic_source_id_seq'::regclass)"))
    scenario_id = Column(ForeignKey('model_draft.renpass_gis_economic_scenario.id'))
    label = Column(String(250))
    source = Column(String(250))
    target = Column(String(250))
    nominal_value = Column(ARRAY(NUMERIC()))
    actual_value = Column(ARRAY(NUMERIC()))
    variable_costs = Column(ARRAY(NUMERIC()))
    fixed = Column(Boolean)

    scenario = relationship('RenpassGisEconomicScenario')


class RenpassGisEconomicStorage(Base):
    __tablename__ = 'renpass_gis_economic_storage'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_economic_storage_id_seq'::regclass)"))
    scenario_id = Column(ForeignKey('model_draft.renpass_gis_economic_scenario.id'))
    label = Column(String(250))
    source = Column(String(250))
    target = Column(String(250))
    conversion_factors = Column(ARRAY(NUMERIC()))
    summed_min = Column(ARRAY(NUMERIC()))
    nominal_value = Column(ARRAY(NUMERIC()))
    min = Column(ARRAY(NUMERIC()))
    max = Column(ARRAY(NUMERIC()))
    actual_value = Column(ARRAY(NUMERIC()))
    fixed = Column(Boolean)
    variable_costs = Column(ARRAY(NUMERIC()))
    fixed_costs = Column(ARRAY(NUMERIC()))
    nominal_capacity = Column(ARRAY(NUMERIC()))
    capacity_loss = Column(ARRAY(NUMERIC()))
    inflow_conversion_factor = Column(ARRAY(NUMERIC()))
    outflow_conversion_factor = Column(ARRAY(NUMERIC()))
    initial_capacity = Column(ARRAY(NUMERIC()))
    capacity_min = Column(ARRAY(NUMERIC()))
    capacity_max = Column(ARRAY(NUMERIC()))

    scenario = relationship('RenpassGisEconomicScenario')


class RenpassGisScenarioResult(Base):
    __tablename__ = 'renpass_gis_scenario_results'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_scenario_results_id_seq'::regclass)"))
    scenario_id = Column(ForeignKey('model_draft.renpass_gis_economic_scenario.id'))
    bus_label = Column(String(250))
    type = Column(String(250))
    obj_label = Column(String(250))
    datetime = Column(DateTime)
    val = Column(Numeric)

    scenario = relationship('RenpassGisEconomicScenario')


class RenpassgisEconomicWeatherpointVoronoi(Base):
    __tablename__ = 'renpassgis_economic_weatherpoint_voronoi'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry('POLYGON', 4326), index=True)
    id = Column(Integer, primary_key=True)


class TemplateTable(Base):
    __tablename__ = 'template_table'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.template_table_id_seq'::regclass)"))
    base_id = Column(Integer)
    area_type = Column(Text)
    geom_poly = Column(Geometry('POLYGON', 3035), index=True)
    geom = Column(Geometry('POINT', 3035), index=True)


t_template_table_mview = Table(
    'template_table_mview', metadata,
    Column('id', Integer),
    Column('base_id', Integer),
    Column('area_type', Text),
    Column('geom', Geometry, index=True),
    schema='model_draft'
)


t_way_substations_test = Table(
    'way_substations_test', metadata,
    Column('id', BigInteger),
    Column('tags', ARRAY(TEXT())),
    Column('geom', Geometry),
    schema='model_draft'
)

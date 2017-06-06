# coding: utf-8
from sqlalchemy import ARRAY, BigInteger, Boolean, CheckConstraint, Column, Date, DateTime, Float, ForeignKey, ForeignKeyConstraint, Integer, Numeric, SmallInteger, String, Table, Text, text
from geoalchemy2.types import Geometry, Raster
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.hstore import HSTORE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ARRAY, DOUBLE_PRECISION, INTEGER, NUMERIC, TEXT


Base = declarative_base()
metadata = Base.metadata


class BkgVg250201501011Sta(Base):
    __tablename__ = 'bkg_vg250_20150101_1_sta'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.bkg_vg250_20150101_1_sta_id_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 31467))
    ade = Column(BigInteger)
    gf = Column(BigInteger)
    bsg = Column(BigInteger)
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(BigInteger)
    bem = Column(String(75))
    nbd = Column(String(4))
    sn_l = Column(String(2))
    sn_r = Column(String(1))
    sn_k = Column(String(2))
    sn_v1 = Column(String(2))
    sn_v2 = Column(String(2))
    sn_g = Column(String(3))
    fk_s3 = Column(String(2))
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    wsk = Column(Date)
    debkg_id = Column(String(16))


class BkgVg250201601011Sta(Base):
    __tablename__ = 'bkg_vg250_20160101_1_sta'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.bkg_vg250_20160101_1_sta_id_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 31467))
    ade = Column(BigInteger)
    gf = Column(BigInteger)
    bsg = Column(BigInteger)
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(BigInteger)
    bem = Column(String(75))
    nbd = Column(String(4))
    sn_l = Column(String(2))
    sn_r = Column(String(1))
    sn_k = Column(String(2))
    sn_v1 = Column(String(2))
    sn_v2 = Column(String(2))
    sn_g = Column(String(3))
    fk_s3 = Column(String(2))
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    wsk = Column(Date)
    debkg_id = Column(String(16))


class DeaGermanyPerLoadArea(Base):
    __tablename__ = 'dea_germany_per_load_area'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)


class DestatisZensusPopulationPerHaInside(Base):
    __tablename__ = 'destatis_zensus_population_per_ha_inside'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True)
    inside_borders = Column(Boolean)


t_destatis_zensus_population_per_ha_invg_mview = Table(
    'destatis_zensus_population_per_ha_invg_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('population', Numeric(10, 0)),
    Column('inside_borders', Boolean),
    Column('geom_point', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_destatis_zensus_population_per_ha_outvg_mview = Table(
    'destatis_zensus_population_per_ha_outvg_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('population', Numeric(10, 0)),
    Column('inside_borders', Boolean),
    Column('geom_point', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoDataProcessingCleanRun(Base):
    __tablename__ = 'ego_data_processing_clean_run'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_data_processing_clean_run_id_seq'::regclass)"))
    version = Column(Text)
    schema_name = Column(Text)
    table_name = Column(Text)
    script_name = Column(Text)
    entries = Column(Integer)
    status = Column(Text)
    timestamp = Column(DateTime)
    user_name = Column(Text)


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

    polygon_id = Column(Integer, primary_key=True)
    area_ha = Column(Float(53))
    powerplant_id = Column(Integer)
    voltage_level = Column(SmallInteger)
    subst_id = Column(Integer)
    otg_id = Column(Integer)
    un_id = Column(Integer)
    consumption = Column(Numeric)
    peak_load = Column(Numeric)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)


class EgoDemandHvmvDemand(Base):
    __tablename__ = 'ego_demand_hvmv_demand'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_hvmv_demand_id_seq'::regclass)"))
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))


class EgoDemandLaOsm(Base):
    __tablename__ = 'ego_demand_la_osm'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_la_osm_id_seq'::regclass)"))
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDemandLaZensu(Base):
    __tablename__ = 'ego_demand_la_zensus'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_la_zensus_id_seq'::regclass)"))
    gid = Column(Integer)
    population = Column(Integer)
    inside_la = Column(Boolean)
    geom_point = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDemandLaZensusCluster(Base):
    __tablename__ = 'ego_demand_la_zensus_cluster'
    __table_args__ = {'schema': 'model_draft'}

    cid = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_la_zensus_cluster_cid_seq'::regclass)"))
    zensus_sum = Column(Integer)
    area_ha = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_buffer = Column(Geometry('POLYGON', 3035))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)


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
    sector_consumption_residential = Column(Float(53))
    sector_consumption_retail = Column(Float(53))
    sector_consumption_industrial = Column(Float(53))
    sector_consumption_agricultural = Column(Float(53))
    sector_consumption_sum = Column(Float(53))
    sector_peakload_retail = Column(Float(53))
    sector_peakload_residential = Column(Float(53))
    sector_peakload_industrial = Column(Float(53))
    sector_peakload_agricultural = Column(Float(53))
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


class EgoDemandLoadareaTemp(Base):
    __tablename__ = 'ego_demand_loadarea_temp'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
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
    geom_centroid = Column(Geometry('POINT', 3035))
    geom_surfacepoint = Column(Geometry('POINT', 3035))
    geom_centre = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035))


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


t_ego_demand_per_gva_test = Table(
    'ego_demand_per_gva_test', metadata,
    Column('eu_code', String(7)),
    Column('federal_states', String),
    Column('elec_consumption_industry', Float(53)),
    Column('elec_consumption_tertiary_sector', Float(53)),
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

    ego_grid_pf_hv_bu = relationship('EgoGridPfHvBus')


class EgoDeuLoadsOsm(Base):
    __tablename__ = 'ego_deu_loads_osm'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_deu_loads_osm_id_seq'::regclass)"))
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_dp_res_powerplant_vg_enavan_mview = Table(
    'ego_dp_res_powerplant_vg_enavan_mview', metadata,
    Column('version', Text),
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    schema='model_draft'
)


class EgoEhvSubstation(Base):
    __tablename__ = 'ego_ehv_substation'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True, nullable=False)
    subst_id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('model_draft.ego_ehv_substation_subst_id_seq'::regclass)"))
    lon = Column(Float(53), nullable=False)
    lat = Column(Float(53), nullable=False)
    point = Column(Geometry('POINT', 4326), nullable=False)
    polygon = Column(Geometry, nullable=False)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text, nullable=False)
    osm_www = Column(Text, nullable=False)
    frequency = Column(Text)
    subst_name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger, nullable=False)
    otg_id = Column(BigInteger)


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


class EgoGridHvElectricalNeighboursBus(Base):
    __tablename__ = 'ego_grid_hv_electrical_neighbours_bus'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    id = Column(BigInteger, nullable=False)
    cntr_id = Column(Text)
    current_type = Column(Text, server_default=text("'AC'::text"))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))


class EgoGridHvElectricalNeighboursLine(Base):
    __tablename__ = 'ego_grid_hv_electrical_neighbours_line'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    line_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    cntr_id = Column(Text)
    v_nom = Column(BigInteger)
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


class EgoGridHvElectricalNeighboursTransformer(Base):
    __tablename__ = 'ego_grid_hv_electrical_neighbours_transformer'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    trafo_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    cntr_id = Column(Text)
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
    s1 = Column(Float(53), server_default=text("0"))
    s2 = Column(Float(53), server_default=text("0"))
    s_min = Column(Float(53), server_default=text("0"))


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

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_hvmv_substation_voronoi_cut_id_seq'::regclass)"))
    subst_id = Column(Integer)
    mun_id = Column(Integer)
    voi_id = Column(Integer)
    ags_0 = Column(String(12))
    subst_type = Column(Integer)
    subst_sum = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_sub = Column(Geometry('POINT', 3035), index=True)


t_ego_grid_hvmv_substation_voronoi_cut_0subst_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_0subst_mview', metadata,
    Column('id', Integer, unique=True),
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
    Column('voi_id', Integer),
    Column('subst_id', Integer),
    Column('geom_centre', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_cut_0subst_nn_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_0subst_nn_mview', metadata,
    Column('voi_id', Integer, unique=True),
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
    Column('id', Integer, unique=True),
    Column('subst_id', Integer),
    Column('mun_id', Integer),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('subst_sum', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
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


class EgoGridLvGriddistrict(Base):
    __tablename__ = 'ego_grid_lv_griddistrict'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    mvlv_subst_id = Column(Integer)
    subst_id = Column(Integer)
    la_id = Column(Integer)
    nn = Column(Boolean)
    subst_cnt = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Float(53))
    population_density = Column(Float(53))
    area_ha = Column(Float(53))
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
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridLvGriddistrictCut(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_griddistrict_cut_id_seq'::regclass)"))
    la_id = Column(Integer)
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridLvGriddistrictCut0subst(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut_0subst'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    la_id = Column(Integer)
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridLvGriddistrictCut1subst(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut_1subst'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    la_id = Column(Integer)
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridLvGriddistrictCutNn(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut_nn'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_griddistrict_cut_nn_id_seq'::regclass)"))
    a_id = Column(Integer)
    b_id = Column(Integer)
    subst_id = Column(Integer)
    la_id = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    distance = Column(Float(53))


class EgoGridLvGriddistrictCutNnCollect(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut_nn_collect'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    mvlv_subst_id = Column(Integer)
    subst_id = Column(Integer)
    la_id = Column(Integer)
    nn = Column(Boolean)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridLvGriddistrictCutXsubst(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut_xsubst'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    la_id = Column(Integer)
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridLvGriddistrictPaper(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_paper'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POINT', 3035), index=True)
    la_id = Column(Integer)
    ont_count = Column(Integer)
    ont_id = Column(Integer)
    merge_id = Column(Integer)
    mvlv_subst_id = Column(Integer)


class EgoGridLvGriddistrictsvoronoi(Base):
    __tablename__ = 'ego_grid_lv_griddistrictsvoronoi'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_griddistrictsvoronoi_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    subst_id = Column(Integer)


class EgoGridLvGriddistrictwithoutpop(Base):
    __tablename__ = 'ego_grid_lv_griddistrictwithoutpop'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_griddistrictwithoutpop_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    load_area_id = Column(Integer)


class EgoGridLvLoadareaRest(Base):
    __tablename__ = 'ego_grid_lv_loadarea_rest'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_loadarea_rest_id_seq'::regclass)"))
    la_id = Column(Integer)
    geom_point = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridMvGriddistrict(Base):
    __tablename__ = 'ego_grid_mv_griddistrict'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    subst_sum = Column(Integer)
    type1 = Column(Integer)
    type1_cnt = Column(Integer)
    type2 = Column(Integer)
    type2_cnt = Column(Integer)
    type3 = Column(Integer)
    type3_cnt = Column(Integer)
    group = Column(String(1))
    gem = Column(Integer)
    gem_clean = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    population_density = Column(Numeric)
    la_count = Column(Integer)
    area_ha = Column(Numeric)
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
    geom_type = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


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

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_dump_id_seq1'::regclass)"))
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom_point = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridMvGriddistrictDump0sub(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_0sub'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_dump_0sub_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom_point = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridMvGriddistrictDump1sub(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_1sub'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_dump_1sub_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridMvGriddistrictDumpNn(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_nn'
    __table_args__ = {'schema': 'model_draft'}

    a_id = Column(Integer, primary_key=True)
    a_geom_point = Column(Geometry('POINT', 3035))
    a_geom = Column(Geometry('POLYGON', 3035))
    b_id = Column(Integer)
    subst_id = Column(Integer)
    b_subst_cnt = Column(Integer)
    b_geom = Column(Geometry('POLYGON', 3035))
    distance = Column(Float(53))


class EgoGridMvGriddistrictDumpNnCollect(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_nn_collect'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_dump_nn_collect_id_seq'::regclass)"))
    subst_id = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridMvGriddistrictDumpNnCollectUnion(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_nn_collect_union'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictDumpNnLine(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_nn_line'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_dump_nn_line_id_seq'::regclass)"))
    a_id = Column(Integer)
    subst_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)


class EgoGridMvGriddistrictDumpNnUnion(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_nn_union'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictNew(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_new'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictNewDump(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_new_dump'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_new_dump_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom_point = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035), index=True)


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


class EgoGridMvGriddistrictUnion(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_union'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvVisualizationBranch(Base):
    __tablename__ = 'ego_grid_mv_visualization_branches'
    __table_args__ = {'schema': 'model_draft'}

    branch_id = Column(String(25), primary_key=True)
    grid_id = Column(Integer)
    type_name = Column(String(25))
    type_kind = Column(String(5))
    type_v_nom = Column(Integer)
    type_s_nom = Column(Float(53))
    length = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 4326), index=True)
    s_res0 = Column(Float(53))
    s_res1 = Column(Float(53))


class EgoGridMvVisualizationBunch(Base):
    __tablename__ = 'ego_grid_mv_visualization_bunch'
    __table_args__ = {'schema': 'model_draft'}

    grid_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_visualization_bunch_grid_id_seq'::regclass)"))
    geom_mv_station = Column(Geometry('POINT', 4326), index=True)
    geom_mv_cable_dists = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_circuit_breakers = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_lv_load_area_centres = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_lv_stations = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_generators = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_lines = Column(Geometry('MULTILINESTRING', 4326), index=True)


class EgoGridMvVisualizationBunchPaper1(Base):
    __tablename__ = 'ego_grid_mv_visualization_bunch_paper1'
    __table_args__ = {'schema': 'model_draft'}

    grid_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_visualization_bunch_paper1_grid_id_seq'::regclass)"))
    geom_mv_station = Column(Geometry('POINT', 4326), index=True)
    geom_mv_cable_dists = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_circuit_breakers = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_lv_load_area_centres = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_lv_stations = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_generators = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_lines = Column(Geometry('MULTILINESTRING', 4326), index=True)


class EgoGridMvVisualizationNode(Base):
    __tablename__ = 'ego_grid_mv_visualization_nodes'
    __table_args__ = {'schema': 'model_draft'}

    node_id = Column(String(100), primary_key=True)
    grid_id = Column(Integer)
    v_nom = Column(Integer)
    geom = Column(Geometry('POINT', 4326), index=True)
    v_res0 = Column(Float(53))
    v_res1 = Column(Float(53))


class EgoGridMvlvSubstation(Base):
    __tablename__ = 'ego_grid_mvlv_substation'
    __table_args__ = {'schema': 'model_draft'}

    mvlv_subst_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mvlv_substation_mvlv_subst_id_seq'::regclass)"))
    la_id = Column(Integer)
    subst_id = Column(Integer)
    geom = Column(Geometry('POINT', 3035), index=True)
    is_dummy = Column(Boolean)


class EgoGridMvlvSubstationPaper(Base):
    __tablename__ = 'ego_grid_mvlv_substation_paper'
    __table_args__ = {'schema': 'model_draft'}

    mvlv_subst_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mvlv_substation_paper_mvlv_subst_id_seq'::regclass)"))
    la_id = Column(Integer)
    subst_id = Column(Integer)
    geom = Column(Geometry('POINT', 3035), index=True)
    is_dummy = Column(Boolean)


class EgoGridMvlvSubstationVoronoi(Base):
    __tablename__ = 'ego_grid_mvlv_substation_voronoi'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mvlv_substation_voronoi_id_seq'::regclass)"))
    subst_id = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridPfHvBus(Base):
    __tablename__ = 'ego_grid_pf_hv_bus'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    current_type = Column(Text, server_default=text("'AC'::text"))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))

class EgoGridPfHvBusmap(Base):
    __tablename__ = 'ego_grid_pf_hv_busmap'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(Text, primary_key=True, nullable=False)
    bus0 = Column(Text, primary_key=True, nullable=False)
    bus1 = Column(Text, primary_key=True, nullable=False)
    path_length = Column(Numeric)

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


class EgoGridPfMvBus(Base):
    __tablename__ = 'ego_grid_pf_mv_bus'
    __table_args__ = {'schema': 'model_draft'}

    bus_id = Column(String(25), primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    grid_id = Column(Integer)


class EgoGridPfMvBusVMagSet(Base):
    __tablename__ = 'ego_grid_pf_mv_bus_v_mag_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(String(25), primary_key=True, nullable=False)
    temp_id = Column(Integer, primary_key=True, nullable=False)
    v_mag_pu_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    grid_id = Column(Integer)


class EgoGridPfMvGenerator(Base):
    __tablename__ = 'ego_grid_pf_mv_generator'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(String(25), primary_key=True, nullable=False)
    bus = Column(String(25))
    control = Column(Text, server_default=text("'PQ'::text"))
    p_nom = Column(Float(53), server_default=text("0"))
    p_min_pu_fixed = Column(Float(53), server_default=text("0"))
    p_max_pu_fixed = Column(Float(53), server_default=text("1"))
    sign = Column(Float(53), server_default=text("1"))
    grid_id = Column(Integer)


class EgoGridPfMvGeneratorPqSet(Base):
    __tablename__ = 'ego_grid_pf_mv_generator_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(String(25), primary_key=True, nullable=False)
    temp_id = Column(Integer, primary_key=True, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_min_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_max_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    grid_id = Column(Integer)


class EgoGridPfMvLine(Base):
    __tablename__ = 'ego_grid_pf_mv_line'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    line_id = Column(String(25), primary_key=True, nullable=False)
    bus0 = Column(String(25))
    bus1 = Column(String(25))
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Numeric, server_default=text("0"))
    length = Column(Float(53))
    cables = Column(Integer)
    geom = Column(Geometry('LINESTRING', 4326))
    grid_id = Column(Integer)


class EgoGridPfMvLoad(Base):
    __tablename__ = 'ego_grid_pf_mv_load'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(String(25), primary_key=True, nullable=False)
    bus = Column(String(25))
    sign = Column(Float(53), server_default=text("(-1)"))
    grid_id = Column(Integer)


class EgoGridPfMvLoadPqSet(Base):
    __tablename__ = 'ego_grid_pf_mv_load_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(String(25), primary_key=True, nullable=False)
    temp_id = Column(Integer, primary_key=True, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    grid_id = Column(Integer)


class EgoGridPfMvResBus(Base):
    __tablename__ = 'ego_grid_pf_mv_res_bus'
    __table_args__ = {'schema': 'model_draft'}

    bus_id = Column(String(25), primary_key=True)
    v_mag_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))


class EgoGridPfMvResLine(Base):
    __tablename__ = 'ego_grid_pf_mv_res_line'
    __table_args__ = {'schema': 'model_draft'}

    line_id = Column(String(25), primary_key=True)
    p0 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p1 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q0 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q1 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))


class EgoGridPfMvResTransformer(Base):
    __tablename__ = 'ego_grid_pf_mv_res_transformer'
    __table_args__ = {'schema': 'model_draft'}

    trafo_id = Column(String(25), primary_key=True)
    p0 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p1 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q0 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q1 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))


class EgoGridPfMvScenarioSetting(Base):
    __tablename__ = 'ego_grid_pf_mv_scenario_settings'
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


class EgoGridPfMvSource(Base):
    __tablename__ = 'ego_grid_pf_mv_source'
    __table_args__ = {'schema': 'model_draft'}

    source_id = Column(String(25), primary_key=True)
    name = Column(Text)
    co2_emissions = Column(Float(53))
    commentary = Column(Text)


class EgoGridPfMvTempResolution(Base):
    __tablename__ = 'ego_grid_pf_mv_temp_resolution'
    __table_args__ = {'schema': 'model_draft'}

    temp_id = Column(BigInteger, primary_key=True)
    timesteps = Column(BigInteger, nullable=False)
    resolution = Column(Text)
    start_time = Column(DateTime)
    grid_id = Column(Integer)


class EgoGridPfMvTransformer(Base):
    __tablename__ = 'ego_grid_pf_mv_transformer'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    trafo_id = Column(String(25), primary_key=True, nullable=False)
    bus0 = Column(String(25))
    bus1 = Column(String(25))
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Float(53), server_default=text("0"))
    tap_ratio = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))
    grid_id = Column(Integer)


class EgoHvmvSubstation(Base):
    __tablename__ = 'ego_hvmv_substation'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True, nullable=False)
    subst_id = Column(SmallInteger, primary_key=True, nullable=False)
    subst_name = Column(Text)
    ags_0 = Column(Text)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text)
    osm_www = Column(Text)
    frequency = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger)
    otg_id = Column(BigInteger)
    lat = Column(Float(53))
    lon = Column(Float(53))
    point = Column(Geometry('POINT', 4326))
    polygon = Column(Geometry)
    geom = Column(Geometry('POINT', 3035))


class EgoLanduseIndustry(Base):
    __tablename__ = 'ego_landuse_industry'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True)
    osm_id = Column(Integer)
    name = Column(Text)
    sector = Column(Integer)
    area_ha = Column(Float(53))
    tags = Column(HSTORE(Text()))
    vg250 = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)
    nuts = Column(String(5))
    consumption = Column(Numeric)
    peak_load = Column(Numeric)


class EgoLattice360mLv(Base):
    __tablename__ = 'ego_lattice_360m_lv'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_lattice_360m_lv_id_seq'::regclass)"))
    la_id = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


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


class EgoLoadarea(Base):
    __tablename__ = 'ego_loadarea'
    __table_args__ = {'schema': 'model_draft'}

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
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)
    sector_consumption_sum = Column(Numeric)
    geom_centroid = Column(Geometry('POINT', 3035))
    geom_surfacepoint = Column(Geometry('POINT', 3035))
    geom_centre = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035))


class EgoMvGriddistrict(Base):
    __tablename__ = 'ego_mv_griddistrict'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True, nullable=False)
    subst_id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('model_draft.ego_mv_griddistrict_subst_id_seq'::regclass)"))
    subst_sum = Column(Text)
    area_ha = Column(Numeric)
    geom_type = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035))


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
    subst_id = Column(Integer)
    area_ha = Column(Float(53))


class EgoOsmSectorPerLvgd1Residential(Base):
    __tablename__ = 'ego_osm_sector_per_lvgd_1_residential'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_lvgd_1_residential_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerLvgd2Retail(Base):
    __tablename__ = 'ego_osm_sector_per_lvgd_2_retail'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_lvgd_2_retail_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerLvgd3Industrial(Base):
    __tablename__ = 'ego_osm_sector_per_lvgd_3_industrial'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_lvgd_3_industrial_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerLvgd4Agricultural(Base):
    __tablename__ = 'ego_osm_sector_per_lvgd_4_agricultural'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_lvgd_4_agricultural_id_seq'::regclass)"))
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
    area_ha = Column(Numeric)
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
    Column('area_ha', Numeric),
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
    area_ha = Column(Numeric)
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


t_ego_renewable_powerplant_eaa_mview = Table(
    'ego_renewable_powerplant_eaa_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
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
    version = Column(Text)
    io = Column(Text)
    schema_name = Column(Text)
    table_name = Column(Text)
    script_name = Column(Text)
    entries = Column(Integer)
    status = Column(Text)
    user_name = Column(Text)
    timestamp = Column(DateTime)
    meta_data = Column('metadata', Text)


class EgoScenarioOverview(Base):
    __tablename__ = 'ego_scenario_overview'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_scenario_overview_id_seq'::regclass)"))
    name = Column(Text)
    version = Column(Text)
    cnt = Column(Integer)


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
    Column('sum', Numeric),
    Column('census_count', BigInteger),
    schema='model_draft'
)


class EgoSupplyConvPowerplant(Base):
    __tablename__ = 'ego_supply_conv_powerplant'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True)
    bnetza_id = Column(Text)
    company = Column(Text)
    name = Column(Text)
    postcode = Column(Text)
    city = Column(Text)
    street = Column(Text)
    state = Column(Text)
    block = Column(Text)
    commissioned_original = Column(Text)
    commissioned = Column(Float(53))
    retrofit = Column(Float(53))
    shutdown = Column(Float(53))
    status = Column(Text)
    fuel = Column(Text)
    technology = Column(Text)
    type = Column(Text)
    eeg = Column(Text)
    chp = Column(Text)
    capacity = Column(Float(53))
    capacity_uba = Column(Float(53))
    chp_capacity_uba = Column(Float(53))
    efficiency_data = Column(Float(53))
    efficiency_estimate = Column(Float(53))
    network_node = Column(Text)
    voltage = Column(Text)
    network_operator = Column(Text)
    name_uba = Column(Text)
    lat = Column(Float(53))
    lon = Column(Float(53))
    comment = Column(Text)
    geom = Column(Geometry('POINT', 4326), index=True)
    voltage_level = Column(SmallInteger)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)


t_ego_supply_conv_powerplant_2035 = Table(
    'ego_supply_conv_powerplant_2035', metadata,
    Column('bnetza_id', String),
    Column('tso', String),
    Column('power_plant_name', String),
    Column('unit_name', String),
    Column('postcode', String),
    Column('state', String),
    Column('commissioning', Integer),
    Column('chp', String),
    Column('fuel', String),
    Column('rated_power', Numeric),
    Column('rated_power_a2025', Numeric),
    Column('rated_power_b2025', Numeric),
    Column('rated_power_b2035', Numeric),
    Column('rated_power_c2025', Numeric),
    Column('lat', Float(53)),
    Column('lon', Float(53)),
    Column('location_checked', Text),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('gid', Integer),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('la_id', Integer),
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


class EgoSupplyGeneratorNep2035(Base):
    __tablename__ = 'ego_supply_generator_nep2035'
    __table_args__ = {'schema': 'model_draft'}

    un_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_generator_nep2035_un_id_seq'::regclass)"))
    re_id = Column(BigInteger)
    conv_id = Column(BigInteger)
    aggr_id_pf = Column(BigInteger)
    aggr_id_ms = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326), index=True)


class EgoSupplyGeneratorTest(Base):
    __tablename__ = 'ego_supply_generator_test'
    __table_args__ = {'schema': 'model_draft'}

    un_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_generator_test_un_id_seq'::regclass)"))
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
    w_id = Column(BigInteger)
    aggr_id = Column(BigInteger)

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


class EgoSupplyPvDev2050GermanyMun(Base):
    __tablename__ = 'ego_supply_pv_dev_2050_germany_mun'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.ego_supply_dev_2050_germany_mun_id_seq'::regclass)"))
    pv_units = Column(Integer)
    pv_cap_2035 = Column(Integer)
    pv_add_cap_2050 = Column(Integer)
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
    voltage_level = Column(SmallInteger)
    postcode = Column(String)
    source = Column(String)
    subst_id = Column(BigInteger)
    la_id = Column(Integer)
    sort = Column(Integer)
    flag = Column(String)
    geom = Column(Geometry('POINT', 3035), index=True)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    geom_new = Column(Geometry('POINT', 3035), index=True)


class EgoSupplyRea2035(Base):
    __tablename__ = 'ego_supply_rea_2035'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(SmallInteger)
    postcode = Column(String)
    source = Column(String)
    subst_id = Column(BigInteger)
    la_id = Column(Integer)
    sort = Column(Integer)
    flag = Column(String)
    geom = Column(Geometry('POINT', 3035))
    geom_line = Column(Geometry('LINESTRING', 3035))
    geom_new = Column(Geometry('POINT', 3035))
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)


t_ego_supply_rea_2035_m1_1_mview = Table(
    'ego_supply_rea_2035_m1_1_mview', metadata,
    Column('id', BigInteger),
    Column('scenario_year', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('nuts', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('voltage_level', SmallInteger),
    Column('network_node', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('voltage', String),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_2035_m1_1_rest_mview = Table(
    'ego_supply_rea_2035_m1_1_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_2035_m1_2_mview = Table(
    'ego_supply_rea_2035_m1_2_mview', metadata,
    Column('id', BigInteger),
    Column('scenario_year', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('nuts', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('voltage_level', SmallInteger),
    Column('network_node', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('voltage', String),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_2035_m1_2_rest_mview = Table(
    'ego_supply_rea_2035_m1_2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


class EgoSupplyRea2050(Base):
    __tablename__ = 'ego_supply_rea_2050'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(SmallInteger)
    postcode = Column(String)
    source = Column(String)
    subst_id = Column(BigInteger)
    la_id = Column(Integer)
    sort = Column(Integer)
    flag = Column(String)
    geom = Column(Geometry('POINT', 3035), index=True)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    geom_new = Column(Geometry('POINT', 3035), index=True)


t_ego_supply_rea_2050_out_mview = Table(
    'ego_supply_rea_2050_out_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
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


class EgoSupplyRea2050OutNn(Base):
    __tablename__ = 'ego_supply_rea_2050_out_nn'
    __table_args__ = {'schema': 'model_draft'}

    dea_id = Column(BigInteger, primary_key=True)
    generation_type = Column(Text)
    subst_id = Column(Integer)
    geom_sub = Column(Geometry('POINT', 3035))
    distance = Column(Float(53))
    geom = Column(Geometry('POINT', 3035))


class EgoSupplyReaM11DeaTemp(Base):
    __tablename__ = 'ego_supply_rea_m1_1_dea_temp'
    __table_args__ = {'schema': 'model_draft'}

    rea_sorted = Column(BigInteger, primary_key=True)
    id = Column(BigInteger, nullable=False)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    subst_id = Column(Integer)
    geom = Column(Geometry('POINT', 3035))
    rea_flag = Column(String)


t_ego_supply_rea_m1_1_mview = Table(
    'ego_supply_rea_m1_1_mview', metadata,
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


class EgoSupplyReaM11OsmTemp(Base):
    __tablename__ = 'ego_supply_rea_m1_1_osm_temp'
    __table_args__ = {'schema': 'model_draft'}

    rea_sorted = Column(BigInteger, primary_key=True)
    id = Column(Integer)
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_supply_rea_m1_1_rest_mview = Table(
    'ego_supply_rea_m1_1_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m1_2_mview = Table(
    'ego_supply_rea_m1_2_mview', metadata,
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m1_2_rest_mview = Table(
    'ego_supply_rea_m1_2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m2_mview = Table(
    'ego_supply_rea_m2_mview', metadata,
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m2_rest_mview = Table(
    'ego_supply_rea_m2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
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
    rea_geom_new = Column(Geometry('POLYGON', 3035))
    rea_geom_line = Column(Geometry('LINESTRING', 3035))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_supply_rea_m3_mview = Table(
    'ego_supply_rea_m3_mview', metadata,
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m3_rest_mview = Table(
    'ego_supply_rea_m3_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m4_mview = Table(
    'ego_supply_rea_m4_mview', metadata,
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m4_rest_mview = Table(
    'ego_supply_rea_m4_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m5_mview = Table(
    'ego_supply_rea_m5_mview', metadata,
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m5_rest_mview = Table(
    'ego_supply_rea_m5_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_out_mview = Table(
    'ego_supply_rea_out_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
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


class EgoSupplyResPowerplant(Base):
    __tablename__ = 'ego_supply_res_powerplant'
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
    voltage_level_var = Column(String)
    network_node = Column(String)
    power_plant_id = Column(String)
    source = Column(String)
    comment = Column(String)
    geom = Column(Geometry('POINT', 4326), index=True)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)
    voltage_level = Column(SmallInteger)
    la_id = Column(Integer)
    mvlv_subst_id = Column(Integer)
    rea_sort = Column(Integer)
    rea_flag = Column(String)
    rea_geom_line = Column(Geometry('LINESTRING', 3035))
    rea_geom_new = Column(Geometry('POINT', 3035))


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
    la_id = Column(Integer)
    mvlv_subst_id = Column(Integer)
    rea_sort = Column(Integer)
    rea_flag = Column(String)
    rea_geom_line = Column(Geometry('LINESTRING', 3035))
    rea_geom_new = Column(Geometry('POINT', 3035))


t_ego_supply_res_powerplant_2035_out_mview = Table(
    'ego_supply_res_powerplant_2035_out_mview', metadata,
    Column('id', BigInteger),
    Column('scenario_year', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('nuts', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('voltage_level', SmallInteger),
    Column('network_node', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('voltage', String),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


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


t_ego_supply_res_powerplant_out_mview = Table(
    'ego_supply_res_powerplant_out_mview', metadata,
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


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


class EgoSupplyWoDev2050GermanyMun(Base):
    __tablename__ = 'ego_supply_wo_dev_2050_germany_mun'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.ego_supply_wo_dev_2050_germany_mun_id_seq'::regclass)"))
    wo_units = Column(Integer)
    wo_cap_2035 = Column(Integer)
    wo_add_cap_2050 = Column(Integer)
    voltage_level = Column(SmallInteger)
    rs_0 = Column(String(12))
    wo_avg_cap = Column(Integer)
    wo_new_units = Column(Numeric(9, 2))


class EgoSupplyWpaPerMvgd(Base):
    __tablename__ = 'ego_supply_wpa_per_mvgd'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_wpa_per_mvgd_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class IoerUrbanShareIndustrial(Base):
    __tablename__ = 'ioer_urban_share_industrial'
    __table_args__ = (
        CheckConstraint('(st_scalex(rast))::numeric(16,10) = (100)::numeric(16,10)'),
        CheckConstraint('(st_scaley(rast))::numeric(16,10) = ((-100))::numeric(16,10)'),
        CheckConstraint("_raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("_raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('st_height(rast) = 500'),
        CheckConstraint('st_numbands(rast) = 1'),
        CheckConstraint('st_srid(rast) = 3035'),
        CheckConstraint('st_width(rast) = 500'),
        CheckConstraint("t_coveredby(st_convexhull(rast), '0103000020DB0B000001000000430000000000000028E64E4100000000C83744410000000080844E4100000000C83744410000000080844E4100000000709944410000000080844E410000000018FB44410000000080844E4100000000C05C45410000000080844E410000000068BE45410000000080844E4100000000102046410000000080844E4100000000B88146410000000080844E410000000060E346410000000080844E4100000000084547410000000080844E4100000000B0A647410000000080844E4100000000580848410000000080844E4100000000006A48410000000080844E4100000000A8CB48410000000080844E4100000000502D49410000000080844E4100000000F88E49410000000080844E4100000000A0F049410000000080844E410000000048524A410000000080844E4100000000F0B34A410000000080844E410000000098154B410000000080844E410000000040774B410000000028E64E410000000040774B4100000000D0474F410000000040774B410000000078A94F410000000040774B4100000000900550410000000040774B4100000000643650410000000040774B4100000000386750410000000040774B41000000000C9850410000000040774B4100000000E0C850410000000040774B4100000000B4F950410000000040774B4100000000882A51410000000040774B41000000005C5B51410000000040774B4100000000308C51410000000040774B410000000004BD51410000000040774B4100000000D8ED51410000000040774B4100000000D8ED51410000000098154B4100000000D8ED514100000000F0B34A4100000000D8ED51410000000048524A4100000000D8ED514100000000A0F0494100000000D8ED514100000000F88E494100000000D8ED514100000000502D494100000000D8ED514100000000A8CB484100000000D8ED514100000000006A484100000000D8ED5141000000005808484100000000D8ED514100000000B0A6474100000000D8ED5141000000000845474100000000D8ED51410000000060E3464100000000D8ED514100000000B881464100000000D8ED5141000000001020464100000000D8ED51410000000068BE454100000000D8ED514100000000C05C454100000000D8ED51410000000018FB444100000000D8ED5141000000007099444100000000D8ED514100000000C83744410000000004BD514100000000C837444100000000308C514100000000C8374441000000005C5B514100000000C837444100000000882A514100000000C837444100000000B4F9504100000000C837444100000000E0C8504100000000C8374441000000000C98504100000000C8374441000000003867504100000000C8374441000000006436504100000000C8374441000000009005504100000000C83744410000000078A94F4100000000C837444100000000D0474F4100000000C83744410000000028E64E4100000000C8374441'::geometry"),
        CheckConstraint("t_iscoveragetile(rast, '0100000000000000000000594000000000000059C00000000080844E410000000040774B4100000000000000000000000000000000DB0B0000581B1C25'::raster, 500, 500"),
        CheckConstraint("t_samealignment(rast, '0100000000000000000000594000000000000059C00000000080844E410000000040774B4100000000000000000000000000000000DB0B000001000100'::raster"),
        {'schema': 'model_draft'}
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ioer_urban_share_industrial_rid_seq'::regclass)"))
    rast = Column(Raster)


class IoerUrbanShareIndustrialCentroid(Base):
    __tablename__ = 'ioer_urban_share_industrial_centroid'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ioer_urban_share_industrial_centroid_id_seq'::regclass)"))
    rid = Column(Integer)
    ioer_share = Column(Numeric)
    geom = Column(Geometry('POINT', 3035), index=True)


class LanduseCalc(Base):
    __tablename__ = 'landuse_calc'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    source = Column(Text)
    attribute = Column(Text)
    count_int = Column(Integer)
    area_ha = Column(Numeric(15, 1))


class NepSupplyConvPowerplantNep2015(Base):
    __tablename__ = 'nep_supply_conv_powerplant_nep2015'
    __table_args__ = {'schema': 'model_draft'}

    bnetza_id = Column(String)
    tso = Column(String)
    power_plant_name = Column(String)
    unit_name = Column(String)
    postcode = Column(String)
    state = Column(String)
    commissioning = Column(Integer)
    chp = Column(String)
    fuel = Column(String)
    rated_power = Column(Numeric)
    rated_power_a2025 = Column(Numeric)
    rated_power_b2025 = Column(Numeric)
    rated_power_b2035 = Column(Numeric)
    rated_power_c2025 = Column(Numeric)
    lat = Column(Float(53))
    lon = Column(Float(53))
    location_checked = Column(Text)
    geom = Column(Geometry('POINT', 4326))
    gid = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.nep_supply_conv_powerplant_nep2015_seq'::regclass)"))


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


class RenpassGisParameterRegion(Base):
    __tablename__ = 'renpass_gis_parameter_region'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True)
    u_region_id = Column(String(14), nullable=False)
    stat_level = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 4326))
    geom_point = Column(Geometry('POINT', 4326))


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


class SupplyWriWorldpowerwatch(Base):
    __tablename__ = 'supply_wri_worldpowerwatch'
    __table_args__ = {'schema': 'model_draft'}

    pw_idnr = Column(String, primary_key=True)
    geom = Column(Geometry('POINT', 4326))
    name = Column(String)
    capacity_mw = Column(Float(53))
    year_of_capacity_data = Column(String)
    annual_generation_gwh = Column(String)
    year_of_generation_data = Column(String)
    country = Column(String)
    owner = Column(String)
    source = Column(String)
    url = Column(String)
    latitude = Column(Float(53))
    longitude = Column(Float(53))
    fuel1 = Column(String)
    fuel2 = Column(String)
    fuel3 = Column(String)
    fuel4 = Column(String)
    field_17 = Column(String)
    field_18 = Column(String)


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

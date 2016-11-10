# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Float, Integer, Numeric, \
    SmallInteger, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class EgoDeuLoad(Base):
    __tablename__ = 'ego_deu_loads'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_deu_loads_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035))


class EgoDeuLoadsCollect(Base):
    __tablename__ = 'ego_deu_loads_collect'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_deu_loads_collect_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_deu_loads_collect_buffer100_mview = Table(
    'ego_deu_loads_collect_buffer100_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_ego'
)


class EgoDeuLoadsConsumptionSpf(Base):
    __tablename__ = 'ego_deu_loads_consumption_spf'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(Integer, primary_key=True)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)


class EgoDeuLoadsMelted(Base):
    __tablename__ = 'ego_deu_loads_melted'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDeuLoadsMeltedCutGem(Base):
    __tablename__ = 'ego_deu_loads_melted_cut_gem'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_deu_loads_melted_cut_gem_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_deu_loads_melted_error_geom_fix_mview = Table(
    'ego_deu_loads_melted_error_geom_fix_mview', metadata,
    Column('id', BigInteger),
    Column('error', Boolean),
    Column('geom_type', Text),
    Column('area', Float(53)),
    Column('geom_buffer', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_ego'
)

t_ego_deu_loads_melted_error_geom_mview = Table(
    'ego_deu_loads_melted_error_geom_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_ego'
)

t_ego_deu_loads_melted_error_geom_view = Table(
    'ego_deu_loads_melted_error_geom_view', metadata,
    Column('id', BigInteger),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_ego'
)


class EgoDeuLoadsMeltedSpf(Base):
    __tablename__ = 'ego_deu_loads_melted_spf'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)


class EgoDeuLoadsOsm(Base):
    __tablename__ = 'ego_deu_loads_osm'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True)
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDeuLoadsSpf(Base):
    __tablename__ = 'ego_deu_loads_spf'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_deu_loads_spf_id_seq'::regclass)"))
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
    rs = Column(String(12))
    ags_0 = Column(String(8))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)


t_ego_deu_loads_spf_centre_mview = Table(
    'ego_deu_loads_spf_centre_mview', metadata,
    Column('id', Integer),
    Column('geom_centroid', Geometry('POINT', 3035)),
    schema='orig_ego'
)

t_ego_deu_loads_spf_error_area_ha_mview = Table(
    'ego_deu_loads_spf_error_area_ha_mview', metadata,
    Column('id', Integer),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_ego'
)


class EgoDeuLoadsZensu(Base):
    __tablename__ = 'ego_deu_loads_zensus'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True)
    gid = Column(Integer)
    population = Column(Integer)
    inside_la = Column(Boolean)
    geom = Column(Geometry('POINT', 3035), index=True)
    geom_grid = Column(Geometry('POLYGON', 3035), index=True)


class EgoDeuLoadsZensusCluster(Base):
    __tablename__ = 'ego_deu_loads_zensus_cluster'
    __table_args__ = {'schema': 'orig_ego'}

    cid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_deu_loads_zensus_cluster_cid_seq'::regclass)"))
    zensus_sum = Column(Integer)
    area_ha = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_buffer = Column(Geometry('POLYGON', 3035))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)


class EgoDeuMunicipalitiesSub(Base):
    __tablename__ = 'ego_deu_municipalities_sub'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True)
    gid = Column(Integer)
    gen = Column(Text)
    bez = Column(Text)
    bem = Column(Text)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    area_ha = Column(Float(53))
    count_ring = Column(Integer)
    path = Column(ARRAY(INTEGER()))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    is_ring = Column(Boolean)
    sub_sum = Column(Integer)
    sub_type = Column(Integer)


t_ego_deu_municipalities_sub_1_mview = Table(
    'ego_deu_municipalities_sub_1_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('sub_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_ego'
)

t_ego_deu_municipalities_sub_2_mview = Table(
    'ego_deu_municipalities_sub_2_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('sub_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_ego'
)

t_ego_deu_municipalities_sub_3_mview = Table(
    'ego_deu_municipalities_sub_3_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('sub_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_ego'
)


class EgoDeuMunicipalitiesSub3Nn(Base):
    __tablename__ = 'ego_deu_municipalities_sub_3_nn'
    __table_args__ = {'schema': 'orig_ego'}

    mun_id = Column(BigInteger, primary_key=True)
    mun_ags_0 = Column(String(12))
    sub_ags_0 = Column(String(12))
    sub_id = Column(Integer)
    sub_type = Column(Integer)
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    distance = Column(Float(53))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_ego_deu_municipalities_sub_3_nn_line = Table(
    'ego_deu_municipalities_sub_3_nn_line', metadata,
    Column('id', BigInteger, unique=True),
    Column('nn_id', BigInteger),
    Column('sub_id', Integer),
    Column('geom_centre', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='orig_ego'
)

t_ego_deu_municipalities_sub_3_nn_union = Table(
    'ego_deu_municipalities_sub_3_nn_union', metadata,
    Column('sub_id', Integer, unique=True),
    Column('sub_type', Integer),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_ego'
)


class EgoDeuPeakLoadSpf(Base):
    __tablename__ = 'ego_deu_peak_load_spf'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True, index=True)
    retail = Column(Float(53))
    residential = Column(Float(53))
    industrial = Column(Float(53))
    agricultural = Column(Float(53))


class EgoDeuSubstations110(Base):
    __tablename__ = 'ego_deu_substations_110'
    __table_args__ = {'schema': 'orig_ego'}

    sub_id = Column(Integer, primary_key=True)
    sub_name = Column(Text)
    geom = Column(Geometry('POINT', 3035), index=True)
    ags_0 = Column(String(12))


class EgoDeuSubstations110Voronoi(Base):
    __tablename__ = 'ego_deu_substations_110_voronoi'
    __table_args__ = {'schema': 'orig_ego'}

    geom = Column(Geometry('POLYGON', 3035), index=True)
    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_deu_substations_110_voronoi_id_seq'::regclass)"))
    sub_id = Column(Integer)
    sub_sum = Column(Integer)


class EgoDeuSubstations110VoronoiCut(Base):
    __tablename__ = 'ego_deu_substations_110_voronoi_cut'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True)
    sub_id = Column(Integer)
    mun_id = Column(BigInteger)
    voi_id = Column(Integer)
    ags_0 = Column(String(12))
    sub_type = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    sub_sum = Column(Integer)
    geom_sub = Column(Geometry('POINT', 3035), index=True)


t_ego_deu_substations_110_voronoi_cut_0sub_mview = Table(
    'ego_deu_substations_110_voronoi_cut_0sub_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('sub_id', Integer),
    Column('mun_id', BigInteger),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('sub_type', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_ego'
)

t_ego_deu_substations_110_voronoi_cut_0sub_nn_line_mview = Table(
    'ego_deu_substations_110_voronoi_cut_0sub_nn_line_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('voi_id', BigInteger),
    Column('sub_id', Integer),
    Column('geom_centre', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='orig_ego'
)

t_ego_deu_substations_110_voronoi_cut_0sub_nn_mview = Table(
    'ego_deu_substations_110_voronoi_cut_0sub_nn_mview', metadata,
    Column('voi_id', BigInteger, unique=True),
    Column('voi_ags_0', String(12)),
    Column('geom_voi', Geometry('POLYGON', 3035), index=True),
    Column('sub_id', Integer),
    Column('ags_0', String(12)),
    Column('geom_sub', Geometry('POLYGON', 3035), index=True),
    schema='orig_ego'
)

t_ego_deu_substations_110_voronoi_cut_0sub_nn_union_mview = Table(
    'ego_deu_substations_110_voronoi_cut_0sub_nn_union_mview', metadata,
    Column('sub_id', Integer, unique=True),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_ego'
)

t_ego_deu_substations_110_voronoi_cut_1sub_mview = Table(
    'ego_deu_substations_110_voronoi_cut_1sub_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('sub_id', Integer),
    Column('mun_id', BigInteger),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('sub_type', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    Column('sub_sum', Integer),
    Column('geom_sub', Geometry('POINT', 3035)),
    schema='orig_ego'
)


class EgoDeuSubstations110VoronoiCutNnCollect(Base):
    __tablename__ = 'ego_deu_substations_110_voronoi_cut_nn_collect'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_deu_substations_110_voronoi_cut_nn_collect_id_seq'::regclass)"))
    sub_id = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_ego_deu_substations_110_voronoi_cut_nn_mview = Table(
    'ego_deu_substations_110_voronoi_cut_nn_mview', metadata,
    Column('sub_id', Integer, unique=True),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_ego'
)

t_ego_deu_substations_110_voronoi_mview = Table(
    'ego_deu_substations_110_voronoi_mview', metadata,
    Column('id', Integer, unique=True),
    Column('sub_id', Integer),
    Column('sub_sum', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_ego'
)


class EgoDeuSubstationsAdd(Base):
    __tablename__ = 'ego_deu_substations_add'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(Integer, primary_key=True)
    lon = Column(Float(53))
    lat = Column(Float(53))
    point = Column(Text)
    polygon = Column(Text)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text)
    osm_www = Column(Text)
    frequency = Column(Text)
    name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger)
    visible = Column(SmallInteger)
    geom = Column(Geometry('POINT', 4326), index=True)
    ags_0 = Column(String(12))


class EgoDeuSubstationsPlu(Base):
    __tablename__ = 'ego_deu_substations_plus'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True)
    geom = Column(Geometry('POINT', 4326), index=True)


class EgoDeuSubstationsVoronoi(Base):
    __tablename__ = 'ego_deu_substations_voronoi'
    __table_args__ = {'schema': 'orig_ego'}

    geom = Column(Geometry('POLYGON', 4326), index=True)
    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_deu_substations_voronoi_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_sum = Column(Integer)


class EgoDeuSubstationsVoronoiCut(Base):
    __tablename__ = 'ego_deu_substations_voronoi_cut'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True)
    subst_id = Column(Integer)
    mun_id = Column(BigInteger)
    voi_id = Column(Integer)
    ags_0 = Column(String(12))
    subst_typ = Column(Integer)
    geom = Column(Geometry('POLYGON', 4326), index=True)
    subst_sum = Column(Integer)
    geom_sub = Column(Geometry('POINT', 4326), index=True)


t_ego_deu_substations_voronoi_cut_0sub_mview = Table(
    'ego_deu_substations_voronoi_cut_0sub_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('subst_id', Integer),
    Column('mun_id', BigInteger),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('subst_typ', Integer),
    Column('geom', Geometry('POLYGON', 4326), index=True),
    schema='orig_ego'
)

t_ego_deu_substations_voronoi_cut_0sub_nn_line_mview = Table(
    'ego_deu_substations_voronoi_cut_0sub_nn_line_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('voi_id', BigInteger),
    Column('subst_id', Integer),
    Column('geom_centre', Geometry('POINT', 4326), index=True),
    Column('geom', Geometry('LINESTRING', 4326), index=True),
    schema='orig_ego'
)

t_ego_deu_substations_voronoi_cut_0sub_nn_mview = Table(
    'ego_deu_substations_voronoi_cut_0sub_nn_mview', metadata,
    Column('voi_id', BigInteger, unique=True),
    Column('voi_ags_0', String(12)),
    Column('geom_voi', Geometry('POLYGON', 4326), index=True),
    Column('subst_id', Integer),
    Column('ags_0', String(12)),
    Column('geom_sub', Geometry('POLYGON', 4326), index=True),
    schema='orig_ego'
)

t_ego_deu_substations_voronoi_cut_0sub_nn_union_mview = Table(
    'ego_deu_substations_voronoi_cut_0sub_nn_union_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('geom', Geometry('MULTIPOLYGON', 4326), index=True),
    schema='orig_ego'
)

t_ego_deu_substations_voronoi_cut_1sub_mview = Table(
    'ego_deu_substations_voronoi_cut_1sub_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('subst_id', Integer),
    Column('mun_id', BigInteger),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('subst_typ', Integer),
    Column('geom', Geometry('POLYGON', 4326), index=True),
    Column('subst_sum', Integer),
    Column('geom_sub', Geometry('POINT', 4326)),
    schema='orig_ego'
)

t_ego_deu_substations_voronoi_cut_nn = Table(
    'ego_deu_substations_voronoi_cut_nn', metadata,
    Column('subst_id', Integer),
    Column('geom', Geometry('MULTIPOLYGON', 3035)),
    schema='orig_ego'
)


class EgoDeuSubstationsVoronoiCutNnCollect(Base):
    __tablename__ = 'ego_deu_substations_voronoi_cut_nn_collect'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_deu_substations_voronoi_cut_nn_collect_id_seq'::regclass)"))
    subst_id = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 4326), index=True)


t_ego_deu_substations_voronoi_cut_nn_mview = Table(
    'ego_deu_substations_voronoi_cut_nn_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('geom', Geometry('MULTIPOLYGON', 4326), index=True),
    schema='orig_ego'
)


class EgoDeuVoronoiEhv(Base):
    __tablename__ = 'ego_deu_voronoi_ehv'
    __table_args__ = {'schema': 'orig_ego'}

    geom = Column(Geometry('POLYGON', 4326), index=True)
    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_deu_voronoi_ehv_id_seq'::regclass)"))


class EgoGridDistrict(Base):
    __tablename__ = 'ego_grid_districts'
    __table_args__ = {'schema': 'orig_ego'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry, index=True)
    subst_sum = Column(Integer)
    area_ha = Column(Numeric)
    geom_type = Column(Text)


class EgoGridDistrictsCollect(Base):
    __tablename__ = 'ego_grid_districts_collect'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.ego_grid_districts_collect_id_seq'::regclass)"))
    sub_id = Column(Integer)
    sub_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035))
    sub_sum = Column(Integer)
    sub_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035))


class EgoGridDistrictsDump(Base):
    __tablename__ = 'ego_grid_districts_dump'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True)
    subst_id = Column(Integer)
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    subst_sum = Column(Integer)


class EgoGridDistrictsHull(Base):
    __tablename__ = 'ego_grid_districts_hull'
    __table_args__ = {'schema': 'orig_ego'}

    subst_id = Column(Integer, primary_key=True)
    area_ha = Column(Float(53))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    subst_sum = Column(Integer)


class EgoGridDistrictsType1(Base):
    __tablename__ = 'ego_grid_districts_type_1'
    __table_args__ = {'schema': 'orig_ego'}

    sub_id = Column(Integer, primary_key=True)
    sub_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    sub_sum = Column(Integer)
    sub_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridDistrictsType2(Base):
    __tablename__ = 'ego_grid_districts_type_2'
    __table_args__ = {'schema': 'orig_ego'}

    sub_id = Column(Integer, primary_key=True)
    sub_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    sub_sum = Column(Integer)
    sub_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridDistrictsType3(Base):
    __tablename__ = 'ego_grid_districts_type_3'
    __table_args__ = {'schema': 'orig_ego'}

    sub_id = Column(Integer, primary_key=True)
    sub_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    sub_sum = Column(Integer)
    sub_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class Netzinseln110(Base):
    __tablename__ = 'netzinseln_110'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_ego.netzinseln_110_id_seq'::regclass)"))
    lon = Column(Float(53), nullable=False)
    lat = Column(Float(53), nullable=False)
    point = Column(Text, nullable=False)
    polygon = Column(Text, nullable=False)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text, nullable=False)
    osm_www = Column(Text, nullable=False)
    frequency = Column(Text)
    name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger, nullable=False)
    visible = Column(SmallInteger, nullable=False)


class Vg2506GemClean(Base):
    __tablename__ = 'vg250_6_gem_clean'
    __table_args__ = {'schema': 'orig_ego'}

    id = Column(BigInteger, primary_key=True)
    gid = Column(Integer)
    gen = Column(Text)
    bez = Column(Text)
    bem = Column(Text)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    area_ha = Column(Float(53))
    count_ring = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)

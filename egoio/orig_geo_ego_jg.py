# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Float, Index, Integer, \
    Numeric, SmallInteger, String, Table, Text, text
from geoalchemy2.types import Geometry, Raster
from sqlalchemy.dialects.postgresql.hstore import HSTORE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class EgoDeuLoad(Base):
    __tablename__ = 'ego_deu_loads'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.ego_deu_loads_id_seq'::regclass)"))
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
    mv_poly_id = Column(Integer)
    nuts = Column(String(5))
    rs = Column(String(12))
    ags_0 = Column(String(8))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)


t_ego_deu_loads_centre_mview = Table(
    'ego_deu_loads_centre_mview', metadata,
    Column('id', Integer),
    Column('geom_centroid', Geometry('POINT', 3035)),
    schema='orig_geo_ego_jg'
)

t_ego_deu_loads_city_area_1_mview = Table(
    'ego_deu_loads_city_area_1_mview', metadata,
    Column('id', Integer),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_geo_ego_jg'
)

t_ego_deu_loads_city_area_2_mview = Table(
    'ego_deu_loads_city_area_2_mview', metadata,
    Column('id', Integer),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_geo_ego_jg'
)

t_ego_deu_loads_city_area_3_mview = Table(
    'ego_deu_loads_city_area_3_mview', metadata,
    Column('id', Integer),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_geo_ego_jg'
)

t_ego_deu_loads_city_area_4_mview = Table(
    'ego_deu_loads_city_area_4_mview', metadata,
    Column('id', Integer),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_geo_ego_jg'
)

t_ego_deu_loads_city_area_5_mview = Table(
    'ego_deu_loads_city_area_5_mview', metadata,
    Column('id', Integer),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_geo_ego_jg'
)


class EgoDeuLoadsCollect(Base):
    __tablename__ = 'ego_deu_loads_collect'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.ego_deu_loads_collect_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDeuLoadsCollectBuffer100(Base):
    __tablename__ = 'ego_deu_loads_collect_buffer100'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.ego_deu_loads_collect_buffer100_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDeuLoadsCollectBuffer100Unbuffer(Base):
    __tablename__ = 'ego_deu_loads_collect_buffer100_unbuffer'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.ego_deu_loads_collect_buffer100_unbuffer_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_centroid = Column(Geometry('POINT', 3035), index=True)


class EgoDeuLoadsCollectBuffer100UnbufferCut(Base):
    __tablename__ = 'ego_deu_loads_collect_buffer100_unbuffer_cut'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.ego_deu_loads_collect_buffer100_unbuffer_cut_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035))
    geom_buffer = Column(Geometry('POLYGON', 3035))


class EgoDeuLoadsCollectBuffer100UnbufferCutGem(Base):
    __tablename__ = 'ego_deu_loads_collect_buffer100_unbuffer_cut_gem'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.ego_deu_loads_collect_buffer100_unbuffer_cut_gem_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDeuLoadsCollectBuffer100UnbufferCutSpf(Base):
    __tablename__ = 'ego_deu_loads_collect_buffer100_unbuffer_cut_spf'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.ego_deu_loads_collect_buffer100_unbuffer_cut_spf_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_deu_loads_collect_buffer100_unbuffer_error_geom_fix_mview = Table(
    'ego_deu_loads_collect_buffer100_unbuffer_error_geom_fix_mview', metadata,
    Column('id', Integer),
    Column('error', Boolean),
    Column('geom_type', Text),
    Column('area', Float(53)),
    Column('geom_buffer', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_geo_ego_jg'
)

t_ego_deu_loads_collect_buffer100_unbuffer_error_geom_view = Table(
    'ego_deu_loads_collect_buffer100_unbuffer_error_geom_view', metadata,
    Column('id', Integer),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_geo_ego_jg'
)


class EgoDeuLoadsCollectBuffer100UnbufferSpf(Base):
    __tablename__ = 'ego_deu_loads_collect_buffer100_unbuffer_spf'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_centroid = Column(Geometry('POINT', 3035), index=True)


class EgoDeuLoadsConsumptionSpf(Base):
    __tablename__ = 'ego_deu_loads_consumption_spf'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)


t_ego_deu_loads_error_area_ha_mview = Table(
    'ego_deu_loads_error_area_ha_mview', metadata,
    Column('id', Integer),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_geo_ego_jg'
)

t_ego_deu_loads_error_noags_view = Table(
    'ego_deu_loads_error_noags_view', metadata,
    Column('id', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_geo_ego_jg'
)


class EgoDeuLoadsSpf(Base):
    __tablename__ = 'ego_deu_loads_spf'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

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
    mv_poly_id = Column(Integer)
    nuts = Column(String(5))
    rs = Column(String(12))
    ags_0 = Column(String(8))
    geom_centroid = Column(Geometry('POINT', 3035))
    geom_surfacepoint = Column(Geometry('POINT', 3035))
    geom_centre = Column(Geometry('POINT', 3035), index=True)


class EgoDeuLoadsZensu(Base):
    __tablename__ = 'ego_deu_loads_zensus'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(BigInteger, primary_key=True)
    gid = Column(Integer)
    population = Column(Integer)
    inside_la = Column(Boolean)
    geom = Column(Geometry('POINT', 3035), index=True)


class EgoDeuMvGridcellFull(Base):
    __tablename__ = 'ego_deu_mv_gridcell_full'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(BigInteger, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.ego_deu_mv_gridcell_full_id_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 3035))


t_ego_deu_mv_gridcell_full_mview = Table(
    'ego_deu_mv_gridcell_full_mview', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_geo_ego_jg'
)

t_ego_deu_mv_gridcell_full_mview_error_geom_mview = Table(
    'ego_deu_mv_gridcell_full_mview_error_geom_mview', metadata,
    Column('id', BigInteger),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_geo_ego_jg'
)

t_ego_deu_mv_gridcell_mview = Table(
    'ego_deu_mv_gridcell_mview', metadata,
    Column('id', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_geo_ego_jg'
)

t_ego_deu_mv_substations_mview = Table(
    'ego_deu_mv_substations_mview', metadata,
    Column('subst_id', Integer),
    Column('subst_voltage', Text),
    Column('subst_name', Text),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='orig_geo_ego_jg'
)


class EgoDeuOsmLoadarea(Base):
    __tablename__ = 'ego_deu_osm_loadarea'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    uid = Column(Integer)
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
    mv_poly_id = Column(Integer)
    nuts = Column(String(5))
    rs = Column(String(12))
    ags_0 = Column(String(8))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_buffer = Column(Geometry('POLYGON', 3035), index=True)
    la_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.ego_deu_osm_loadarea_la_id_seq'::regclass)"))


class EgoDeuOsmLoadareaSpf(Base):
    __tablename__ = 'ego_deu_osm_loadarea_spf'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    uid = Column(Integer)
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
    mv_poly_id = Column(Integer)
    nuts = Column(String(5))
    rs = Column(String(12))
    ags_0 = Column(String(8))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_buffer = Column(Geometry('POLYGON', 3035), index=True)
    la_id = Column(Integer, primary_key=True)


class EgoDeuZensusLoadpointsCluster(Base):
    __tablename__ = 'ego_deu_zensus_loadpoints_cluster'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    cid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.ego_deu_zensus_loadpoints_cluster_cid_seq'::regclass)"))
    zensus_sum = Column(Integer)
    area_ha = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_buffer = Column(Geometry('POLYGON', 3035))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)


class EgoDeuZensusLoadpointsClusterSpf(Base):
    __tablename__ = 'ego_deu_zensus_loadpoints_cluster_spf'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    cid = Column(Integer, primary_key=True)
    zensus_sum = Column(Integer)
    area_ha = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_buffer = Column(Geometry('POLYGON', 3035), index=True)
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)


class EgoMsNetzbezirke(Base):
    __tablename__ = 'ego_ms_netzbezirke'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry)
    geom_gem = Column(Geometry('MULTIPOLYGON', 3035))


class JgMSBy(Base):
    __tablename__ = 'jg_MS_Bies'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        """nextval('orig_geo_ego_jg."jg_MS_Bies_id_seq"'::regclass)"""))
    geom = Column(Geometry('MULTILINESTRING', 4326), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))
    name_2 = Column(String(254))
    descript_2 = Column(String(254))
    timestam_2 = Column(String(24))
    begin_2 = Column(String(24))
    end_2 = Column(String(24))
    altitude_2 = Column(String(254))
    tessella_2 = Column(BigInteger)
    extrude_2 = Column(BigInteger)
    visibili_2 = Column(BigInteger)
    draworde_2 = Column(BigInteger)
    icon_2 = Column(String(254))


class JgMSBreit(Base):
    __tablename__ = 'jg_MS_Breit'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        """nextval('orig_geo_ego_jg."jg_MS_Breit_id_seq"'::regclass)"""))
    geom = Column(Geometry('MULTILINESTRING', 4326), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))
    name_2 = Column(String(254))
    descript_2 = Column(String(254))
    timestam_2 = Column(String(24))
    begin_2 = Column(String(24))
    end_2 = Column(String(24))
    altitude_2 = Column(String(254))
    tessella_2 = Column(BigInteger)
    extrude_2 = Column(BigInteger)
    visibili_2 = Column(BigInteger)
    draworde_2 = Column(BigInteger)
    icon_2 = Column(String(254))


class JgMSBuch(Base):
    __tablename__ = 'jg_MS_Buch'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        """nextval('orig_geo_ego_jg."jg_MS_Buch_id_seq"'::regclass)"""))
    geom = Column(Geometry('MULTILINESTRING', 4326), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))
    name_2 = Column(String(254))
    descript_2 = Column(String(254))
    timestam_2 = Column(String(24))
    begin_2 = Column(String(24))
    end_2 = Column(String(24))
    altitude_2 = Column(String(254))
    tessella_2 = Column(BigInteger)
    extrude_2 = Column(BigInteger)
    visibili_2 = Column(BigInteger)
    draworde_2 = Column(BigInteger)
    icon_2 = Column(String(254))


class JgMSHorg(Base):
    __tablename__ = 'jg_MS_Horg'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        """nextval('orig_geo_ego_jg."jg_MS_Horg_id_seq"'::regclass)"""))
    geom = Column(Geometry('MULTILINESTRING', 4326), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))
    name_2 = Column(String(254))
    descript_2 = Column(String(254))
    timestam_2 = Column(String(24))
    begin_2 = Column(String(24))
    end_2 = Column(String(24))
    altitude_2 = Column(String(254))
    tessella_2 = Column(BigInteger)
    extrude_2 = Column(BigInteger)
    visibili_2 = Column(BigInteger)
    draworde_2 = Column(BigInteger)
    icon_2 = Column(String(254))


class JgMSLage(Base):
    __tablename__ = 'jg_MS_Lage'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        """nextval('orig_geo_ego_jg."jg_MS_Lage_id_seq"'::regclass)"""))
    geom = Column(Geometry('MULTILINESTRING', 4326), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))
    name_2 = Column(String(254))
    descript_2 = Column(String(254))
    timestam_2 = Column(String(24))
    begin_2 = Column(String(24))
    end_2 = Column(String(24))
    altitude_2 = Column(String(254))
    tessella_2 = Column(BigInteger)
    extrude_2 = Column(BigInteger)
    visibili_2 = Column(BigInteger)
    draworde_2 = Column(BigInteger)
    icon_2 = Column(String(254))


class JgMSLeng(Base):
    __tablename__ = 'jg_MS_Leng'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        """"nextval('orig_geo_ego_jg."jg_MS_Leng_id_seq"'::regclass)"""))
    geom = Column(Geometry('MULTILINESTRING', 4326), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))
    name_2 = Column(String(254))
    descript_2 = Column(String(254))
    timestam_2 = Column(String(24))
    begin_2 = Column(String(24))
    end_2 = Column(String(24))
    altitude_2 = Column(String(254))
    tessella_2 = Column(BigInteger)
    extrude_2 = Column(BigInteger)
    visibili_2 = Column(BigInteger)
    draworde_2 = Column(BigInteger)
    icon_2 = Column(String(254))


class JgMSMemm(Base):
    __tablename__ = 'jg_MS_Memm'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        """nextval('orig_geo_ego_jg."jg_MS_Memm_id_seq"'::regclass)"""))
    geom = Column(Geometry('MULTILINESTRING', 4326), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))
    name_2 = Column(String(254))
    descript_2 = Column(String(254))
    timestam_2 = Column(String(24))
    begin_2 = Column(String(24))
    end_2 = Column(String(24))
    altitude_2 = Column(String(254))
    tessella_2 = Column(BigInteger)
    extrude_2 = Column(BigInteger)
    visibili_2 = Column(BigInteger)
    draworde_2 = Column(BigInteger)
    icon_2 = Column(String(254))


class JgMSObau(Base):
    __tablename__ = 'jg_MS_Obau'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        """nextval('orig_geo_ego_jg."jg_MS_Obau_id_seq"'::regclass)"""))
    geom = Column(Geometry('MULTILINESTRING', 4326), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))
    name_2 = Column(String(254))
    descript_2 = Column(String(254))
    timestam_2 = Column(String(24))
    begin_2 = Column(String(24))
    end_2 = Column(String(24))
    altitude_2 = Column(String(254))
    tessella_2 = Column(BigInteger)
    extrude_2 = Column(BigInteger)
    visibili_2 = Column(BigInteger)
    draworde_2 = Column(BigInteger)
    icon_2 = Column(String(254))


class JgMSOtto(Base):
    __tablename__ = 'jg_MS_Otto'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        """"nextval('orig_geo_ego_jg."jg_MS_Otto_id_seq"'::regclass)"""))
    geom = Column(Geometry('MULTILINESTRING', 4326), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))
    name_2 = Column(String(254))
    descript_2 = Column(String(254))
    timestam_2 = Column(String(24))
    begin_2 = Column(String(24))
    end_2 = Column(String(24))
    altitude_2 = Column(String(254))
    tessella_2 = Column(BigInteger)
    extrude_2 = Column(BigInteger)
    visibili_2 = Column(BigInteger)
    draworde_2 = Column(BigInteger)
    icon_2 = Column(String(254))


class JgMSUntei(Base):
    __tablename__ = 'jg_MS_Untei'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True, server_default=text(
        """nextval('orig_geo_ego_jg."jg_MS_Untei_id_seq"'::regclass)"""))
    geom = Column(Geometry('MULTILINESTRING', 4326), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))
    name_2 = Column(String(254))
    descript_2 = Column(String(254))
    timestam_2 = Column(String(24))
    begin_2 = Column(String(24))
    end_2 = Column(String(24))
    altitude_2 = Column(String(254))
    tessella_2 = Column(BigInteger)
    extrude_2 = Column(BigInteger)
    visibili_2 = Column(BigInteger)
    draworde_2 = Column(BigInteger)
    icon_2 = Column(String(254))


class JgMSSpf(Base):
    __tablename__ = 'jg_MS_spf'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    name = Column(String(254))
    pid = Column(Integer, primary_key=True, server_default=text(
        """"nextval('orig_geo_ego_jg."jg_MS_spf_pid_seq"'::regclass)"""))


class JgMSSpfBb(Base):
    __tablename__ = 'jg_MS_spf_bb'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    geom = Column(Geometry, index=True)
    id = Column(BigInteger, primary_key=True)


class JgNSTu(Base):
    __tablename__ = 'jg_NS_Tus'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    Name = Column(Integer, primary_key=True, server_default=text(
        """"nextval('orig_geo_ego_jg."jg_NS_Tus_Name_seq"'::regclass)"""))
    geom = Column(Geometry('LINESTRINGZ', 3035), index=True)
    name = Column(String(254))
    descriptio = Column(String(254))
    timestamp = Column(String(24))
    begin = Column(String(24))
    end = Column(String(24))
    altitudemo = Column(String(254))
    tessellate = Column(BigInteger)
    extrude = Column(BigInteger)
    visibility = Column(BigInteger)
    draworder = Column(BigInteger)
    icon = Column(String(254))


class JgNSTusHausanschluesse(Base):
    __tablename__ = 'jg_NS_Tus_Hausanschluesse'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    Name = Column(Integer, primary_key=True)
    geom = Column(Geometry('LINESTRINGZ', 3035), index=True)


class JgNSTusAngle(Base):
    __tablename__ = 'jg_NS_Tus_angles'
    __table_args__ = (
        Index('orig_geo_ego_jg_tus_angles_geom_idx', 'p1', 'p2', 'p3'),
        {'schema': 'orig_geo_ego_jg'}
    )

    p2 = Column(Geometry, primary_key=True, nullable=False)
    p1 = Column(Geometry, primary_key=True, nullable=False)
    p3 = Column(Geometry, primary_key=True, nullable=False)


class JgNSTusAnglesGi(Base):
    __tablename__ = 'jg_NS_Tus_angles_gis'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    geom = Column(Geometry('POINTZ'), primary_key=True)


class JgNSTusCont3_75(Base):
    __tablename__ = 'jg_NS_Tus_cont_3.75'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    geom = Column(Geometry('MULTILINESTRING', 3035), index=True)
    id = Column(BigInteger, primary_key=True)


class JgNSTusCont9_75(Base):
    __tablename__ = 'jg_NS_Tus_cont_9.75'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    geom = Column(Geometry('MULTILINESTRING', 3035), index=True)
    id = Column(BigInteger, primary_key=True)


class JgNSTusFinal(Base):
    __tablename__ = 'jg_NS_Tus_final'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    Name = Column(Integer, primary_key=True)
    geom = Column(Geometry('LINESTRINGZ', 3035), index=True)


class JgONTsSpf(Base):
    __tablename__ = 'jg_ONTs_spf'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    geom = Column(Geometry('POINT'), index=True)
    id = Column(Integer, primary_key=True, server_default=text(
        """nextval('orig_geo_ego_jg."jg_ONTs_spf_id_seq"'::regclass)"""))


class JgBboxesSpf(Base):
    __tablename__ = 'jg_bboxes_spf'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    geom = Column(Geometry('POLYGON', 3035), index=True)
    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.jg_bboxes_spf_id_seq'::regclass)"))
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    onts = Column(Numeric)


class JgOsmTusStreet(Base):
    __tablename__ = 'jg_osm_tus_streets'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    osm_id = Column(String, primary_key=True)
    geom = Column(Geometry('MULTILINESTRING', 4326))
    name = Column(String(254))
    highway = Column(String(254))
    waterway = Column(String(254))
    aerialway = Column(String(254))
    barrier = Column(String(254))
    man_made = Column(String(254))
    z_order = Column(BigInteger)
    other_tags = Column(String(254))


class JgOsmTusStreetsFinal(Base):
    __tablename__ = 'jg_osm_tus_streets_final'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    osm_id = Column(String, primary_key=True)
    geom = Column(Geometry('MULTILINESTRING', 3035), index=True)


t_jg_pop_spf = Table(
    'jg_pop_spf', metadata,
    Column('rast', Raster),
    schema='orig_geo_ego_jg'
)


class JgPopulatedAreasL(Base):
    __tablename__ = 'jg_populated_areas_ls'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    geom = Column(Geometry, index=True)
    box_id = Column(Integer)
    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.jg_populated_areas_ls_id_seq'::regclass)"))
    zensus_sum = Column(Integer)
    onts = Column(Numeric)


class JgStreetsBuffered9_75(Base):
    __tablename__ = 'jg_streets_buffered_9.75'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    osm_id = Column(String, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_nn_gem3_usw_mview = Table(
    'nn_gem3_usw_mview', metadata,
    Column('gref_gid', Integer),
    Column('gref_ags_0', String(12)),
    Column('gref_geom', Geometry('MULTIPOLYGON', 3035)),
    Column('gnn_gid', Integer),
    Column('gnn_subst_name', Text),
    Column('gnn_geom', Geometry('POINT', 3035)),
    schema='orig_geo_ego_jg'
)


class OsmDeuPolygonUrban(Base):
    __tablename__ = 'osm_deu_polygon_urban'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    gid = Column(Integer, primary_key=True)
    osm_id = Column(Integer)
    landuse = Column(Text)
    man_made = Column(Text)
    aeroway = Column(Text)
    name = Column(Text)
    way_area = Column(Float(53))
    area_ha = Column(Float(53))
    tags = Column(HSTORE)
    vg250 = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class OsmDeuPolygonUrbanBuffer100Unbuffer(Base):
    __tablename__ = 'osm_deu_polygon_urban_buffer100_unbuffer'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    uid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.osm_deu_polygon_urban_buffer100_unbuffer_uid_seq'::regclass)"))
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
    mv_poly_id = Column(Integer)
    nuts = Column(String(5))
    rs = Column(String(12))
    ags_0 = Column(String(8))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_buffer = Column(Geometry('POLYGON', 3035), index=True)


t_osm_deu_polygon_urban_buffer100_unbuffer_check_res_combination_ = Table(
    'osm_deu_polygon_urban_buffer100_unbuffer_check_res_combination_', metadata,
    Column('uid', Integer),
    Column('zensus_sum', Integer),
    Column('zensus_count', Integer),
    Column('zensus_density', Numeric),
    Column('area_ha', Numeric),
    Column('ioer_sum', Numeric),
    Column('geom_buffer', Geometry('POLYGON', 3035), index=True),
    schema='orig_geo_ego_jg'
)

t_osm_deu_polygon_urban_buffer100_unbuffer_error_area_ha_mview = Table(
    'osm_deu_polygon_urban_buffer100_unbuffer_error_area_ha_mview', metadata,
    Column('uid', Integer),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='orig_geo_ego_jg'
)

t_osm_deu_polygon_urban_error_geom_vg250_mview = Table(
    'osm_deu_polygon_urban_error_geom_vg250_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('landuse', Text),
    Column('man_made', Text),
    Column('aeroway', Text),
    Column('name', Text),
    Column('way_area', Float(53)),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_geo_ego_jg'
)

t_osm_deu_polygon_urban_error_geom_view = Table(
    'osm_deu_polygon_urban_error_geom_view', metadata,
    Column('id', Integer),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    schema='orig_geo_ego_jg'
)

t_test_2_voronoi = Table(
    'test_2_voronoi', metadata,
    Column('geom', Geometry),
    schema='orig_geo_ego_jg'
)

t_test_2_voronoi_pts = Table(
    'test_2_voronoi_pts', metadata,
    Column('id', Integer),
    Column('geom', Geometry),
    schema='orig_geo_ego_jg'
)

t_test_voronoi = Table(
    'test_voronoi', metadata,
    Column('geom', Geometry),
    Column('name', SmallInteger),
    schema='orig_geo_ego_jg'
)


class TestVoronoiGeom(Base):
    __tablename__ = 'test_voronoi_geom'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    geom = Column(Geometry('POLYGON', 4326), index=True)
    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_ego_jg.test_voronoi_geom_id_seq'::regclass)"))


t_test_voronoi_pts = Table(
    'test_voronoi_pts', metadata,
    Column('id', Integer),
    Column('geom', Geometry),
    schema='orig_geo_ego_jg'
)


class TestVoronoiPtsGeom(Base):
    __tablename__ = 'test_voronoi_pts_geom'
    __table_args__ = {'schema': 'orig_geo_ego_jg'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOINT', 4326), index=True)


t_usw_2_pts_mview = Table(
    'usw_2_pts_mview', metadata,
    Column('id', Integer),
    Column('geom', Geometry('POINT', 3035)),
    schema='orig_geo_ego_jg'
)

t_usw_voronoi = Table(
    'usw_voronoi', metadata,
    Column('geom', Geometry),
    schema='orig_geo_ego_jg'
)

t_vg250_6_gem_usw_1_mview = Table(
    'vg250_6_gem_usw_1_mview', metadata,
    Column('gid', Integer),
    Column('gen', String(50)),
    Column('nuts', String(5)),
    Column('rs', String(12)),
    Column('ags_0', String(12)),
    Column('geom', Geometry('MULTIPOLYGON', 3035)),
    Column('usw_sum', Integer),
    schema='orig_geo_ego_jg'
)

t_vg250_6_gem_usw_2_mview = Table(
    'vg250_6_gem_usw_2_mview', metadata,
    Column('gid', Integer),
    Column('gen', String(50)),
    Column('nuts', String(5)),
    Column('rs', String(12)),
    Column('ags_0', String(12)),
    Column('geom', Geometry('MULTIPOLYGON', 3035)),
    Column('usw_sum', Integer),
    schema='orig_geo_ego_jg'
)

t_vg250_6_gem_usw_2_pts_mview = Table(
    'vg250_6_gem_usw_2_pts_mview', metadata,
    Column('id', Integer),
    Column('geom', Geometry),
    schema='orig_geo_ego_jg'
)

t_vg250_6_gem_usw_3_mview = Table(
    'vg250_6_gem_usw_3_mview', metadata,
    Column('gid', Integer),
    Column('gen', String(50)),
    Column('nuts', String(5)),
    Column('rs', String(12)),
    Column('ags_0', String(12)),
    Column('geom', Geometry('MULTIPOLYGON', 3035)),
    Column('usw_sum', Integer),
    schema='orig_geo_ego_jg'
)

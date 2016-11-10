# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, Integer, SmallInteger, String, \
    Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class EgoDeuSubstation(Base):
    __tablename__ = 'ego_deu_substations'
    __table_args__ = {'schema': 'calc_ego_substation'}

    subst_id = Column(Integer, primary_key=True)
    lon = Column(Float(53))
    lat = Column(Float(53))
    point = Column(Geometry('POINT', 4326), index=True)
    polygon = Column(Geometry('POLYGON', 4326), index=True)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text)
    osm_www = Column(Text)
    frequency = Column(Text)
    subst_name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger)
    visible = Column(SmallInteger)
    otg_id = Column(BigInteger)


class Substation110(Base):
    __tablename__ = 'substation_110'
    __table_args__ = {'schema': 'calc_ego_substation'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    geom = Column(Geometry('POINT', 3035), index=True)
    ags_0 = Column(String(12))


t_substation_110_mun_2_mview = Table(
    'substation_110_mun_2_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('subst_name', Text),
    Column('subst_type', Integer),
    Column('geom', Geometry('POINT', 3035)),
    schema='calc_ego_substation'
)


class Substation110Voronoi(Base):
    __tablename__ = 'substation_110_voronoi'
    __table_args__ = {'schema': 'calc_ego_substation'}

    geom = Column(Geometry('POLYGON', 3035), index=True)
    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_ego_substation.substation_110_voronoi_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_sum = Column(Integer)


class Substation110VoronoiCut(Base):
    __tablename__ = 'substation_110_voronoi_cut'
    __table_args__ = {'schema': 'calc_ego_substation'}

    id = Column(BigInteger, primary_key=True)
    subst_id = Column(Integer)
    mun_id = Column(BigInteger)
    voi_id = Column(Integer)
    ags_0 = Column(String(12))
    subst_type = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    subst_sum = Column(Integer)
    geom_sub = Column(Geometry('POINT', 3035), index=True)


t_substation_110_voronoi_cut_0subst_mview = Table(
    'substation_110_voronoi_cut_0subst_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('subst_id', Integer),
    Column('mun_id', BigInteger),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='calc_ego_substation'
)

t_substation_110_voronoi_cut_0subst_nn_line_mview = Table(
    'substation_110_voronoi_cut_0subst_nn_line_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('voi_id', BigInteger),
    Column('subst_id', Integer),
    Column('geom_centre', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='calc_ego_substation'
)

t_substation_110_voronoi_cut_0subst_nn_mview = Table(
    'substation_110_voronoi_cut_0subst_nn_mview', metadata,
    Column('voi_id', BigInteger, unique=True),
    Column('voi_ags_0', String(12)),
    Column('geom_voi', Geometry('POLYGON', 3035), index=True),
    Column('subst_id', Integer),
    Column('ags_0', String(12)),
    Column('geom_sub', Geometry('POLYGON', 3035), index=True),
    schema='calc_ego_substation'
)

t_substation_110_voronoi_cut_0subst_nn_union_mview = Table(
    'substation_110_voronoi_cut_0subst_nn_union_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='calc_ego_substation'
)

t_substation_110_voronoi_cut_1subst_mview = Table(
    'substation_110_voronoi_cut_1subst_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('subst_id', Integer),
    Column('mun_id', BigInteger),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    Column('subst_sum', Integer),
    Column('geom_sub', Geometry('POINT', 3035)),
    schema='calc_ego_substation'
)


class Substation110VoronoiCutNnCollect(Base):
    __tablename__ = 'substation_110_voronoi_cut_nn_collect'
    __table_args__ = {'schema': 'calc_ego_substation'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_ego_substation.substation_110_voronoi_cut_nn_collect_id_seq'::regclass)"))
    subst_id = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_substation_110_voronoi_cut_nn_mview = Table(
    'substation_110_voronoi_cut_nn_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='calc_ego_substation'
)


class SubstationDummy(Base):
    __tablename__ = 'substation_dummy'
    __table_args__ = {'schema': 'calc_ego_substation'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    geom = Column(Geometry('POINT', 3035), index=True)

class EgoDeuOnts(Base):
    __tablename__ = 'ego_deu_onts'
    __table_args__ = {"schema": 'calc_ego_substation'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    geom = Column(Geometry(geometry_type="POINT", srid=3035))
    load_area_id = Column(Integer)

class EgoDeuOntsTa(Base):
    __tablename__ = 'ego_deu_onts_ta'
    __table_args__ = {"schema": 'calc_ego_substation'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry(geometry_type="POINT", srid=3035))
    load_area_id = Column(Integer)

class EgoDeuOntsLittleTa(Base):
    __tablename__ = 'ego_deu_onts_little_ta'
    __table_args__ = {"schema": 'calc_ego_substation'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry(geometry_type="POINT", srid=3035))
    load_area_id = Column(Integer)


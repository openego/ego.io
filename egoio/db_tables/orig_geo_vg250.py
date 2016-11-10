# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Date, Float, Integer, \
    String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Vg2501Sta(Base):
    __tablename__ = 'vg250_1_sta'
    __table_args__ = {'schema': 'orig_geo_vg250'}

    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_vg250.vg250_1_sta_gid_seq'::regclass)"))
    ade = Column(Float(53))
    gf = Column(Float(53))
    bsg = Column(Float(53))
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(Float(53))
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
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)
    water = Column(Boolean)


t_vg250_1_sta_error_geom_mview = Table(
    'vg250_1_sta_error_geom_mview', metadata,
    Column('id', Integer, unique=True),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='orig_geo_vg250'
)

t_vg250_1_sta_mview = Table(
    'vg250_1_sta_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('bez', Text),
    Column('area_km2', Float(53)),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_geo_vg250'
)

t_vg250_1_sta_union_mview = Table(
    'vg250_1_sta_union_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('bez', Text),
    Column('area_km2', Float(53)),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_geo_vg250'
)


class Vg2502Lan(Base):
    __tablename__ = 'vg250_2_lan'
    __table_args__ = {'schema': 'orig_geo_vg250'}

    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_vg250.vg250_2_lan_gid_seq'::regclass)"))
    ade = Column(Float(53))
    gf = Column(Float(53))
    bsg = Column(Float(53))
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(Float(53))
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
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


t_vg250_2_lan_mview = Table(
    'vg250_2_lan_mview', metadata,
    Column('ags_0', String(12), unique=True),
    Column('gen', Text),
    Column('geom', Geometry, index=True),
    schema='orig_geo_vg250'
)


class Vg2503Rbz(Base):
    __tablename__ = 'vg250_3_rbz'
    __table_args__ = {'schema': 'orig_geo_vg250'}

    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_vg250.vg250_3_rbz_gid_seq'::regclass)"))
    ade = Column(Float(53))
    gf = Column(Float(53))
    bsg = Column(Float(53))
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(Float(53))
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
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Vg2504Kr(Base):
    __tablename__ = 'vg250_4_krs'
    __table_args__ = {'schema': 'orig_geo_vg250'}

    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_vg250.vg250_4_krs_gid_seq'::regclass)"))
    ade = Column(Float(53))
    gf = Column(Float(53))
    bsg = Column(Float(53))
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(Float(53))
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
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


t_vg250_4_krs_mview = Table(
    'vg250_4_krs_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('area_km2', Float(53)),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_geo_vg250'
)

t_vg250_4_krs_spf_mview = Table(
    'vg250_4_krs_spf_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('name', String(50)),
    Column('area_km2', Float(53)),
    Column('geom', Geometry('MULTIPOLYGON', 31467), index=True),
    schema='orig_geo_vg250'
)


class Vg2505Vwg(Base):
    __tablename__ = 'vg250_5_vwg'
    __table_args__ = {'schema': 'orig_geo_vg250'}

    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_vg250.vg250_5_vwg_gid_seq'::regclass)"))
    ade = Column(Float(53))
    gf = Column(Float(53))
    bsg = Column(Float(53))
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(Float(53))
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
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Vg2506Gem(Base):
    __tablename__ = 'vg250_6_gem'
    __table_args__ = {'schema': 'orig_geo_vg250'}

    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_vg250.vg250_6_gem_gid_seq'::regclass)"))
    ade = Column(Float(53))
    gf = Column(Float(53))
    bsg = Column(Float(53))
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(Float(53))
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
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Vg2506GemClean(Base):
    __tablename__ = 'vg250_6_gem_clean'
    __table_args__ = {'schema': 'orig_geo_vg250'}

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


t_vg250_6_gem_dump_mview = Table(
    'vg250_6_gem_dump_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('gid', Integer),
    Column('gen', Text),
    Column('bez', Text),
    Column('bem', Text),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('area_km2', Float(53)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_geo_vg250'
)

t_vg250_6_gem_mview = Table(
    'vg250_6_gem_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('bem', Text),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('area_ha', Float(53)),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_geo_vg250'
)

t_vg250_6_gem_rings_mview = Table(
    'vg250_6_gem_rings_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('gid', Integer),
    Column('gen', Text),
    Column('bez', Text),
    Column('bem', Text),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('area_ha', Float(53)),
    Column('count_ring', Integer),
    Column('path', ARRAY(INTEGER())),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    Column('is_ring', Boolean),
    schema='orig_geo_vg250'
)


class Vg2506GemUsw(Base):
    __tablename__ = 'vg250_6_gem_usw'
    __table_args__ = {'schema': 'orig_geo_vg250'}

    gid = Column(Integer, primary_key=True)
    gen = Column(String(50))
    nuts = Column(String(5))
    rs = Column(String(12))
    ags_0 = Column(String(12))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    usw_sum = Column(Integer)

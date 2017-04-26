# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Date, Float, Integer, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class BkgVg2501Sta(Base):
    __tablename__ = 'bkg_vg250_1_sta'
    __table_args__ = {'schema': 'political_boundary'}

    reference_date = Column(Date, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('political_boundary.bkg_vg250_1_sta_id_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)
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


t_bkg_vg250_1_sta_bbox_mview = Table(
    'bkg_vg250_1_sta_bbox_mview', metadata,
    Column('reference_date', Text),
    Column('id', Integer, unique=True),
    Column('bez', Text),
    Column('area_km2', Float(53)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='political_boundary'
)


t_bkg_vg250_1_sta_error_geom_mview = Table(
    'bkg_vg250_1_sta_error_geom_mview', metadata,
    Column('id', Integer, unique=True),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='political_boundary'
)


t_bkg_vg250_1_sta_mview = Table(
    'bkg_vg250_1_sta_mview', metadata,
    Column('reference_date', Text),
    Column('id', Integer, unique=True),
    Column('bez', Text),
    Column('gf', Float(53)),
    Column('area_km2', Float(53)),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='political_boundary'
)


t_bkg_vg250_1_sta_union_mview = Table(
    'bkg_vg250_1_sta_union_mview', metadata,
    Column('reference_date', Text),
    Column('id', Integer, unique=True),
    Column('bez', Text),
    Column('area_km2', Float(53)),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='political_boundary'
)


class BkgVg250201501011Sta(Base):
    __tablename__ = 'bkg_vg250_20150101_1_sta'
    __table_args__ = {'schema': 'political_boundary'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('political_boundary.bkg_vg250_20150101_1_sta_id_seq'::regclass)"))
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
    __table_args__ = {'schema': 'political_boundary'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('political_boundary.bkg_vg250_20160101_1_sta_id_seq'::regclass)"))
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


class BkgVg2502Lan(Base):
    __tablename__ = 'bkg_vg250_2_lan'
    __table_args__ = {'schema': 'political_boundary'}

    reference_date = Column(Date, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('political_boundary.bkg_vg250_2_lan_id_seq'::regclass)"))
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


t_bkg_vg250_2_lan_mview = Table(
    'bkg_vg250_2_lan_mview', metadata,
    Column('reference_date', Text),
    Column('ags_0', String(12), unique=True),
    Column('gen', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='political_boundary'
)


class BkgVg2503Rbz(Base):
    __tablename__ = 'bkg_vg250_3_rbz'
    __table_args__ = {'schema': 'political_boundary'}

    reference_date = Column(Date, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('political_boundary.bkg_vg250_3_rbz_id_seq'::regclass)"))
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


class BkgVg2504Kr(Base):
    __tablename__ = 'bkg_vg250_4_krs'
    __table_args__ = {'schema': 'political_boundary'}

    reference_date = Column(Date, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('political_boundary.bkg_vg250_4_krs_id_seq'::regclass)"))
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


t_bkg_vg250_4_krs_mview = Table(
    'bkg_vg250_4_krs_mview', metadata,
    Column('reference_date', Text),
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('area_km2', Float(53)),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='political_boundary'
)


class BkgVg2505Vwg(Base):
    __tablename__ = 'bkg_vg250_5_vwg'
    __table_args__ = {'schema': 'political_boundary'}

    reference_date = Column(Date, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('political_boundary.bkg_vg250_5_vwg_id_seq'::regclass)"))
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


class BkgVg2506Gem(Base):
    __tablename__ = 'bkg_vg250_6_gem'
    __table_args__ = {'schema': 'political_boundary'}

    reference_date = Column(Date, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('political_boundary.bkg_vg250_6_gem_id_seq'::regclass)"))
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


t_bkg_vg250_6_gem_dump_mview = Table(
    'bkg_vg250_6_gem_dump_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('old_id', Integer),
    Column('gen', Text),
    Column('bez', Text),
    Column('bem', Text),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('area_km2', Float(53)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='political_boundary'
)


t_bkg_vg250_6_gem_mview = Table(
    'bkg_vg250_6_gem_mview', metadata,
    Column('reference_date', Text),
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('bem', Text),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('area_ha', Float(53)),
    Column('area_km2', Float(53)),
    Column('census_sum', Integer),
    Column('census_count', Integer),
    Column('census_density', Integer),
    Column('pd', Float(53)),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='political_boundary'
)


t_bkg_vg250_6_gem_pts = Table(
    'bkg_vg250_6_gem_pts', metadata,
    Column('id', Integer),
    Column('ags_0', String(12)),
    Column('geom', Geometry),
    schema='political_boundary'
)


t_bkg_vg250_statistics_mview = Table(
    'bkg_vg250_statistics_mview', metadata,
    Column('id', Integer),
    Column('table', Text),
    Column('descript_nameion', Text),
    Column('area_sum_km2', Integer),
    schema='political_boundary'
)


t_bkg_vg250_statistics_view = Table(
    'bkg_vg250_statistics_view', metadata,
    Column('id', Text),
    Column('area_sum_km2', Integer),
    schema='political_boundary'
)


t_vg250_6_gem_berlin_mview = Table(
    'vg250_6_gem_berlin_mview', metadata,
    Column('gid', Integer),
    Column('gen', String(50)),
    Column('ags_0', String(12)),
    Column('geom', Geometry),
    schema='political_boundary'
)

# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, Integer, SmallInteger, String, Table, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CopernicusClc2012V184(Base):
    __tablename__ = 'copernicus_clc_2012_v_18_4'
    __table_args__ = {'schema': 'environment'}

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('environment.clc_corine_land_cover_2012_v_18_4_ogc_fid_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    code_12 = Column(String)
    id = Column(String)
    remark = Column(String)
    area_ha = Column(Float(53))
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))


class CopernicusClc2012V184Filter(Base):
    __tablename__ = 'copernicus_clc_2012_v_18_4_filter'
    __table_args__ = {'schema': 'environment'}

    ogc_fid = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035))
    code_12 = Column(String)
    id = Column(String)
    remark = Column(String)
    area_ha = Column(Float(53))
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))


class CopernicusClc2012V184Germany(Base):
    __tablename__ = 'copernicus_clc_2012_v_18_4_germany'
    __table_args__ = {'schema': 'environment'}

    ogc_fid = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    code_12 = Column(String)
    id = Column(String)
    remark = Column(String)
    area_ha = Column(Float(53))
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))


class Dlm250Geb01F(Base):
    __tablename__ = 'dlm250_geb01_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_geb01_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    adm = Column(String(20))
    bez_nat = Column(String(60))
    bez_lan = Column(String(60))
    bez_rbz = Column(String(60))
    bez_krs = Column(String(60))
    bez_vwg = Column(String(60))
    bez_gem = Column(String(60))
    rgs = Column(String(100))
    sch = Column(String(20))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Geb01L(Base):
    __tablename__ = 'dlm250_geb01_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_geb01_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    agz = Column(String(30))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Geb02F(Base):
    __tablename__ = 'dlm250_geb02_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_geb02_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    ltp = Column(String(4))
    nam = Column(String(100))
    rgs = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Geb03F(Base):
    __tablename__ = 'dlm250_geb03_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_geb03_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    objart_z = Column(String(5))
    objid_z = Column(String(16))
    adf = Column(String(4))
    bez = Column(String(60))
    nam = Column(String(120))
    nrs = Column(String(20))
    sgn = Column(String(20))
    zon = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


t_dlm250_gew0103_l = Table(
    'dlm250_gew0103_l', metadata,
    Column('gid', Integer),
    Column('land', String(3)),
    Column('modellart', String(20)),
    Column('objart', String(5)),
    Column('objart_txt', String(50)),
    Column('objid', String(16)),
    Column('hdu_x', SmallInteger),
    Column('beginn', String(20)),
    Column('ende', String(20)),
    Column('objart_z', String(5)),
    Column('objid_z', String(16)),
    Column('brg', SmallInteger),
    Column('fkt', String(4)),
    Column('flr', SmallInteger),
    Column('gwk', String(20)),
    Column('hyd', String(4)),
    Column('nam', String(100)),
    Column('sfk', String(4)),
    Column('wdm', String(4)),
    Column('znm', String(100)),
    Column('zus', String(4)),
    Column('bemerkung', String(200)),
    Column('geom', Geometry('MULTILINESTRING', 31467), index=True),
    schema='environment'
)


class Dlm250Gew01F(Base):
    __tablename__ = 'dlm250_gew01_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_gew01_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    objart_z = Column(String(5))
    objid_z = Column(String(16))
    fkt = Column(String(4))
    gwk = Column(String(20))
    hyd = Column(String(4))
    nam = Column(String(100))
    sfk = Column(String(4))
    skz = Column(String(20))
    wdm = Column(String(4))
    znm = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Gew01L(Base):
    __tablename__ = 'dlm250_gew01_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_gew01_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    objart_z = Column(String(5))
    objid_z = Column(String(16))
    brg = Column(SmallInteger)
    fkt = Column(String(4))
    flr = Column(SmallInteger)
    gwk = Column(String(20))
    hyd = Column(String(4))
    nam = Column(String(100))
    sfk = Column(String(4))
    wdm = Column(String(4))
    znm = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Gew02F(Base):
    __tablename__ = 'dlm250_gew02_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_gew02_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    art = Column(String(4))
    nam = Column(String(100))
    znm = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Gew02L(Base):
    __tablename__ = 'dlm250_gew02_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_gew02_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    flr = Column(SmallInteger)
    gwk = Column(String(20))
    nam = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Gew02P(Base):
    __tablename__ = 'dlm250_gew02_p'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_gew02_p_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    art = Column(String(4))
    hws = Column(Float(53))
    nam = Column(String(100))
    znm = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('POINT', 31467), index=True)


class Dlm250Gew03L(Base):
    __tablename__ = 'dlm250_gew03_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_gew03_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    aga = Column(String(4))
    flr = Column(SmallInteger)
    gwk = Column(String(30))
    nam = Column(String(100))
    sfk = Column(String(4))
    znm = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Hdu01B(Base):
    __tablename__ = 'dlm250_hdu01_b'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_hdu01_b_gid_seq'::regclass)"))
    land = Column(String(3))
    objart_1 = Column(String(5))
    objid_1 = Column(String(16))
    ebene_1 = Column(String(7))
    objart_2 = Column(String(5))
    objid_2 = Column(String(16))
    ebene_2 = Column(String(7))
    geom = Column(Geometry('POINT', 31467), index=True)


class Dlm250Rel01L(Base):
    __tablename__ = 'dlm250_rel01_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_rel01_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    objart_z = Column(String(5))
    objid_z = Column(String(16))
    art = Column(String(4))
    fkt = Column(String(4))
    hhl = Column(SmallInteger)
    hho = Column(SmallInteger)
    nam = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Rel01P(Base):
    __tablename__ = 'dlm250_rel01_p'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_rel01_p_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    nam = Column(String(100))
    znm = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('POINT', 31467), index=True)


class Dlm250Rel02P(Base):
    __tablename__ = 'dlm250_rel02_p'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_rel02_p_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    ang = Column(String(4))
    hoehe = Column(Float(53))
    bemerkung = Column(String(200))
    geom = Column(Geometry('POINT', 31467), index=True)


class Dlm250Sie01F(Base):
    __tablename__ = 'dlm250_sie01_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_sie01_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    nam = Column(String(100))
    rgs = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Sie01P(Base):
    __tablename__ = 'dlm250_sie01_p'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_sie01_p_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    nam = Column(String(100))
    rgs = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('POINT', 31467), index=True)


class Dlm250Sie02F(Base):
    __tablename__ = 'dlm250_sie02_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_sie02_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    agt = Column(String(4))
    fkt = Column(String(4))
    nam = Column(String(100))
    rgs = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Sie03F(Base):
    __tablename__ = 'dlm250_sie03_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_sie03_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    bwf = Column(String(4))
    hho = Column(Float(53))
    nam = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Sie03L(Base):
    __tablename__ = 'dlm250_sie03_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_sie03_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    bwf = Column(String(4))
    pro = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Sie03P(Base):
    __tablename__ = 'dlm250_sie03_p'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_sie03_p_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    bwf = Column(String(4))
    hho = Column(Float(53))
    nam = Column(String(100))
    spo = Column(String(4))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('POINT', 31467), index=True)


class Dlm250Sie04F(Base):
    __tablename__ = 'dlm250_sie04_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_sie04_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    nam = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Sie04L(Base):
    __tablename__ = 'dlm250_sie04_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_sie04_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    kon = Column(String(4))
    nam = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Sie04P(Base):
    __tablename__ = 'dlm250_sie04_p'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_sie04_p_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    kon = Column(String(4))
    nam = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('POINT', 31467), index=True)


class Dlm250Sie05P(Base):
    __tablename__ = 'dlm250_sie05_p'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_sie05_p_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    bwf = Column(String(20))
    gfk = Column(String(4))
    hho = Column(Float(53))
    nam = Column(String(200))
    znm = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('POINT', 31467), index=True)


class Dlm250Veg01F(Base):
    __tablename__ = 'dlm250_veg01_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_veg01_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    nam = Column(String(100))
    veg = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Veg02F(Base):
    __tablename__ = 'dlm250_veg02_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_veg02_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    nam = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Veg03F(Base):
    __tablename__ = 'dlm250_veg03_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_veg03_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    fkt = Column(String(4))
    nam = Column(String(100))
    ofm = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Veg04F(Base):
    __tablename__ = 'dlm250_veg04_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_veg04_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    bws = Column(String(4))
    nam = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Ver01L(Base):
    __tablename__ = 'dlm250_ver01_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_ver01_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    objart_z = Column(String(5))
    objid_z = Column(String(16))
    bez = Column(String(30))
    brf = Column(Float(53))
    bvb = Column(String(4))
    fsz = Column(SmallInteger)
    ftr = Column(String(4))
    ibd = Column(String(4))
    wdm = Column(String(4))
    znm = Column(String(200))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Ver02L(Base):
    __tablename__ = 'dlm250_ver02_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_ver02_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    fkt = Column(String(4))
    nam = Column(String(100))
    znm = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Ver03F(Base):
    __tablename__ = 'dlm250_ver03_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_ver03_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Ver03L(Base):
    __tablename__ = 'dlm250_ver03_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_ver03_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    bkt = Column(String(20))
    elk = Column(String(4))
    gls = Column(String(4))
    nam = Column(String(100))
    nrb = Column(String(60))
    spw = Column(String(4))
    znm = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Ver04F(Base):
    __tablename__ = 'dlm250_ver04_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_ver04_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    art = Column(String(4))
    bez = Column(String(60))
    nam = Column(String(100))
    ntz = Column(String(4))
    znm = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Ver05L(Base):
    __tablename__ = 'dlm250_ver05_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_ver05_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    art = Column(String(20))
    nam = Column(String(100))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Ver06F(Base):
    __tablename__ = 'dlm250_ver06_f'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_ver06_f_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    bwf = Column(String(4))
    nam = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class Dlm250Ver06L(Base):
    __tablename__ = 'dlm250_ver06_l'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_ver06_l_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    art = Column(String(4))
    bez = Column(String(60))
    bro = Column(Float(53))
    bwf = Column(String(4))
    nam = Column(String(100))
    ofm = Column(String(4))
    znm = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('MULTILINESTRING', 31467), index=True)


class Dlm250Ver06P(Base):
    __tablename__ = 'dlm250_ver06_p'
    __table_args__ = {'schema': 'environment'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('environment.dlm250_ver06_p_gid_seq'::regclass)"))
    land = Column(String(3))
    modellart = Column(String(20))
    objart = Column(String(5))
    objart_txt = Column(String(50))
    objid = Column(String(16))
    hdu_x = Column(SmallInteger)
    beginn = Column(String(20))
    ende = Column(String(20))
    art = Column(String(4))
    bez = Column(String(60))
    bfk = Column(String(4))
    bro = Column(Float(53))
    bwf = Column(String(4))
    nam = Column(String(100))
    ofm = Column(String(4))
    znm = Column(String(100))
    zus = Column(String(4))
    bemerkung = Column(String(200))
    geom = Column(Geometry('POINT', 31467), index=True)


t_fred_dp_river_mosel_mview = Table(
    'fred_dp_river_mosel_mview', metadata,
    Column('land', String(3)),
    Column('modellart', String(20)),
    Column('objart', String(5)),
    Column('objart_txt', String(50)),
    Column('aga', String(4)),
    Column('flr', SmallInteger),
    Column('gwk', String(30), unique=True),
    Column('nam', String(100)),
    Column('geom', Geometry('MULTILINESTRING', 3035), index=True),
    schema='environment'
)


t_fred_dp_rivers2_mview = Table(
    'fred_dp_rivers2_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('land', String(3)),
    Column('modellart', String(20)),
    Column('gwk', String(20)),
    Column('nam', String(100)),
    Column('geom', Geometry('MULTILINESTRING', 3035), index=True),
    schema='environment'
)


t_fred_dp_rivers_mview = Table(
    'fred_dp_rivers_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('land', String(3)),
    Column('modellart', String(20)),
    Column('objart', String(5)),
    Column('objart_txt', String(50)),
    Column('objid', String(16)),
    Column('hdu_x', SmallInteger),
    Column('beginn', String(20)),
    Column('ende', String(20)),
    Column('flr', SmallInteger),
    Column('gwk', String(20)),
    Column('nam', String(100)),
    Column('sfk', String(4)),
    Column('znm', String(100)),
    Column('bemerkung', String(200)),
    Column('geom', Geometry('MULTILINESTRING', 3035), index=True),
    schema='environment'
)

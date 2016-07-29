# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Float, Integer, Numeric, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.dialects.postgresql.base import ARRAY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class EgoDeuLoadAreaRest(Base):
    __tablename__ = 'ego_deu_load_area_rest'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_grid_district.ego_deu_load_area_rest_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDeuLoadAreaRestLittleTa(Base):
    __tablename__ = 'ego_deu_load_area_rest_little_ta'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_grid_district.ego_deu_load_area_rest_little_ta_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    load_area_id = Column(Integer)


class EgoDeuLoadAreaRestTa(Base):
    __tablename__ = 'ego_deu_load_area_rest_ta'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_grid_district.ego_deu_load_area_rest_ta_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    load_area_id = Column(Integer)


class EgoDeuLvCutTa(Base):
    __tablename__ = 'ego_deu_lv_cut_ta'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    geom = Column(Geometry('POLYGON', 3035))
    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_grid_district.ego_deu_lv_cut_ta_id_seq'::regclass)"))
    ont_count = Column(Integer)
    ont_id = Column(Integer)
    merge_id = Column(Integer)


class EgoDeuLvGridDistrictTa(Base):
    __tablename__ = 'ego_deu_lv_grid_district_ta'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    geom = Column(Geometry('POLYGON', 3035))
    id = Column(Integer, primary_key=True)
    load_area_id = Column(Integer)
    population = Column(Numeric)


class EgoDeuLvGridDistrictTaWithoutpop(Base):
    __tablename__ = 'ego_deu_lv_grid_district_ta_withoutpop'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    geom = Column(Geometry('POLYGON', 3035))
    id = Column(Integer, primary_key=True)
    load_area_id = Column(Integer)


class EgoDeuLvGridDistrictsTaVoronoi(Base):
    __tablename__ = 'ego_deu_lv_grid_districts_ta_voronoi'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    geom = Column(Geometry('POLYGON', 3035), index=True)
    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_grid_district.ego_deu_lv_grid_districts_ta_voronoi_id_seq'::regclass)"))


class EgoDeuOntgrid(Base):
    __tablename__ = 'ego_deu_ontgrids'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_grid_district.ego_deu_ontgrids_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    load_area_id = Column(Integer)


class EgoDeuOntgridsLittleTa(Base):
    __tablename__ = 'ego_deu_ontgrids_little_ta'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_grid_district.ego_deu_ontgrids_little_ta_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    load_area_id = Column(Integer)


class EgoDeuOntgridsTa(Base):
    __tablename__ = 'ego_deu_ontgrids_ta'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_grid_district.ego_deu_ontgrids_ta_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    load_area_id = Column(Integer)


class GridDistrict(Base):
    __tablename__ = 'grid_district'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    subst_sum = Column(Integer)
    area_ha = Column(Numeric)
    geom_type = Column(Text)


class GridDistrictCollect(Base):
    __tablename__ = 'grid_district_collect'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_grid_district.grid_district_collect_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class GridDistrictTa(Base):
    __tablename__ = 'grid_district_ta'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    subst_sum = Column(Integer)
    area_ha = Column(Numeric)
    geom_type = Column(Text)


class GridDistrictType1(Base):
    __tablename__ = 'grid_district_type_1'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class GridDistrictType2(Base):
    __tablename__ = 'grid_district_type_2'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class GridDistrictType3(Base):
    __tablename__ = 'grid_district_type_3'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class LvGridDistrictTa(Base):
    __tablename__ = 'lv_grid_district_ta'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('calc_ego_grid_district.lv_grid_district_ta_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    population = Column(Integer)
    peak_load = Column(Numeric)


class MunicipalitiesSubst(Base):
    __tablename__ = 'municipalities_subst'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

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
    subst_sum = Column(Integer)
    subst_type = Column(Integer)


t_municipalities_subst_1_mview = Table(
    'municipalities_subst_1_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='calc_ego_grid_district'
)


t_municipalities_subst_2_mview = Table(
    'municipalities_subst_2_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='calc_ego_grid_district'
)


t_municipalities_subst_3_mview = Table(
    'municipalities_subst_3_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='calc_ego_grid_district'
)


class MunicipalitiesSubst3Nn(Base):
    __tablename__ = 'municipalities_subst_3_nn'
    __table_args__ = {'schema': 'calc_ego_grid_district'}

    mun_id = Column(BigInteger, primary_key=True)
    mun_ags_0 = Column(String(12))
    subst_ags_0 = Column(String(12))
    subst_id = Column(Integer)
    subst_type = Column(Integer)
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    distance = Column(Float(53))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_municipalities_subst_3_nn_line = Table(
    'municipalities_subst_3_nn_line', metadata,
    Column('id', BigInteger, unique=True),
    Column('nn_id', BigInteger),
    Column('subst_id', Integer),
    Column('geom_centre', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='calc_ego_grid_district'
)


t_municipalities_subst_3_nn_union = Table(
    'municipalities_subst_3_nn_union', metadata,
    Column('subst_id', Integer, unique=True),
    Column('subst_type', Integer),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='calc_ego_grid_district'
)

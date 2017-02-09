# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, Numeric, SmallInteger, String, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class EgoHvmvSubstation(Base):
    __tablename__ = 'ego_hvmv_substation'
    __table_args__ = {'schema': 'grid'}

    version = Column(ForeignKey('model_draft.ego_scenario.version'), primary_key=True, nullable=False)
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

    ego_scenario = relationship('EgoScenario')


class EgoMvGriddistrict(Base):
    __tablename__ = 'ego_mv_griddistrict'
    __table_args__ = {'schema': 'grid'}

    version = Column(ForeignKey('model_draft.ego_scenario.version'), primary_key=True, nullable=False)
    subst_id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('grid.ego_mv_griddistrict_subst_id_seq'::regclass)"))
    subst_sum = Column(Text)
    area_ha = Column(Numeric)
    geom_type = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035))

    ego_scenario = relationship('EgoScenario')


class OtgEhvhvBranchDatum(Base):
    __tablename__ = 'otg_ehvhv_branch_data'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(ForeignKey('grid.otg_ehvhv_results_metadata.id', ondelete='CASCADE'))
    view_id = Column(Integer, primary_key=True, server_default=text("nextval('grid.otg_ehvhv_branch_data_view_id_seq'::regclass)"))
    branch_id = Column(BigInteger)
    f_bus = Column(BigInteger)
    t_bus = Column(BigInteger)
    br_r = Column(Numeric)
    br_x = Column(Numeric)
    br_b = Column(Numeric)
    rate_a = Column(Numeric)
    rate_b = Column(Numeric)
    rate_c = Column(Numeric)
    tap = Column(Numeric)
    shift = Column(Numeric)
    br_status = Column(Integer)
    link_type = Column(Text)
    branch_voltage = Column(Integer)
    cables = Column(Integer)
    frequency = Column(Numeric)
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))

    result = relationship('OtgEhvhvResultsMetadatum')


class OtgEhvhvBusDatum(Base):
    __tablename__ = 'otg_ehvhv_bus_data'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(ForeignKey('grid.otg_ehvhv_results_metadata.id', ondelete='CASCADE'))
    view_id = Column(Integer, primary_key=True, server_default=text("nextval('grid.otg_ehvhv_bus_data_view_id_seq'::regclass)"))
    bus_i = Column(BigInteger)
    bus_type = Column(Integer)
    pd = Column(Numeric)
    qd = Column(Numeric)
    gs = Column(Numeric)
    bs = Column(Numeric)
    bus_area = Column(Integer)
    vm = Column(Numeric)
    va = Column(Numeric)
    base_kv = Column(Numeric)
    zone = Column(Integer)
    vmax = Column(Numeric)
    vmin = Column(Numeric)
    osm_substation_id = Column(BigInteger)
    cntr_id = Column(String(2))
    frequency = Column(Numeric)
    geom = Column(Geometry('POINT', 4326))
    osm_name = Column(Text)

    result = relationship('OtgEhvhvResultsMetadatum')


class OtgEhvhvDclineDatum(Base):
    __tablename__ = 'otg_ehvhv_dcline_data'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(ForeignKey('grid.otg_ehvhv_results_metadata.id', ondelete='CASCADE'))
    view_id = Column(Integer, primary_key=True, server_default=text("nextval('grid.otg_ehvhv_dcline_data_view_id_seq'::regclass)"))
    dcline_id = Column(BigInteger)
    f_bus = Column(BigInteger)
    t_bus = Column(BigInteger)
    br_status = Column(Integer)
    pf = Column(Numeric)
    pt = Column(Numeric)
    qf = Column(Numeric)
    qt = Column(Numeric)
    vf = Column(Numeric)
    vt = Column(Numeric)
    pmin = Column(Numeric)
    pmax = Column(Numeric)
    qminf = Column(Numeric)
    qmaxf = Column(Numeric)
    qmint = Column(Numeric)
    qmaxt = Column(Numeric)
    loss0 = Column(Numeric)
    loss1 = Column(Numeric)
    link_type = Column(Text)
    branch_voltage = Column(Integer)
    cables = Column(Integer)
    frequency = Column(Numeric)
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))

    result = relationship('OtgEhvhvResultsMetadatum')


class OtgEhvhvResultsMetadatum(Base):
    __tablename__ = 'otg_ehvhv_results_metadata'
    __table_args__ = {'schema': 'grid'}

    id = Column(Integer, primary_key=True)
    osm_date = Column(Date)
    abstraction_date = Column(Date)
    applied_plans = Column(Text)
    applied_year = Column(Integer)
    user_comment = Column(Text)


class EgoScenario(Base):
    __tablename__ = 'ego_scenario'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True)
    version_name = Column(Text)
    release = Column(Boolean)
    comment = Column(Text)
    timestamp = Column(DateTime)

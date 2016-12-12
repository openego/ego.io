# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, ForeignKey, Integer, Numeric, String, Text, text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

Base = declarative_base()
metadata = Base.metadata


class Bus(Base):
    __tablename__ = 'bus'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    current_type = Column(Text, server_default=text("'AC'::text"))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT'))


class BusVMagSet(Base):
    __tablename__ = 'bus_v_mag_set'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('calc_ego_hv_powerflow.temp_resolution.temp_id'), primary_key=True, nullable=False)
    v_mag_pu_set = Column(ARRAY(Float(53)))

    temp = relationship('TempResolution')


class Generator(Base):
    __tablename__ = 'generator'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

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
    source = Column(ForeignKey('calc_ego_hv_powerflow.source.source_id'), index=True)
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))

    source1 = relationship('Source')


class GeneratorPqSet(Base):
    __tablename__ = 'generator_pq_set'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('calc_ego_hv_powerflow.temp_resolution.temp_id'), primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(53)))
    q_set = Column(ARRAY(Float(53)))
    p_min_pu = Column(ARRAY(Float(53)))
    p_max_pu = Column(ARRAY(Float(53)))

    temp = relationship('TempResolution')


class Line(Base):
    __tablename__ = 'line'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

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
    geom = Column(Geometry('MULTILINESTRING'))
    topo = Column(Geometry('LINESTRING'))


class Load(Base):
    __tablename__ = 'load'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    sign = Column(Float(53), server_default=text("'-1'::integer"))
    e_annual = Column(Float(53))


class LoadPqSet(Base):
    __tablename__ = 'load_pq_set'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('calc_ego_hv_powerflow.temp_resolution.temp_id'), primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(53)))
    q_set = Column(ARRAY(Float(53)))

    temp = relationship('TempResolution')


class ScenarioSetting(Base):
    __tablename__ = 'scenario_settings'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

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


class Source(Base):
    __tablename__ = 'source'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

    source_id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    co2_emissions = Column(Float(53))
    commentary = Column(Text)


class StorageUnit(Base):
    __tablename__ = 'storage'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

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
    source = Column(ForeignKey('calc_ego_hv_powerflow.source.source_id'), index=True)
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))
    soc_initial = Column(Float(53))
    soc_cyclic = Column(Boolean, server_default=text("false"))
    max_hours = Column(Float(53))
    efficiency_store = Column(Float(53))
    efficiency_dispatch = Column(Float(53))
    standing_loss = Column(Float(53))
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))

    source1 = relationship('Source')


class StoragePqSet(Base):
    __tablename__ = 'storage_pq_set'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('calc_ego_hv_powerflow.temp_resolution.temp_id'), primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(53)))
    q_set = Column(ARRAY(Float(53)))
    p_min_pu = Column(ARRAY(Float(53)))
    p_max_pu = Column(ARRAY(Float(53)))
    soc_set = Column(ARRAY(Float(53)))
    inflow = Column(ARRAY(Float(53)))

    temp = relationship('TempResolution')


class TempResolution(Base):
    __tablename__ = 'temp_resolution'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

    temp_id = Column(BigInteger, primary_key=True)
    timesteps = Column(BigInteger, nullable=False)
    resolution = Column(Text)
    start_time = Column(DateTime)


class Transformer(Base):
    __tablename__ = 'transformer'
    __table_args__ = {'schema': 'calc_ego_hv_powerflow'}

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
    geom = Column(Geometry('MULTILINESTRING'))
    topo = Column(Geometry('LINESTRING'))

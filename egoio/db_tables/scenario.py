# coding: utf-8
from sqlalchemy import Column, Float, Integer, Numeric, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AbbbConstraint(Base):
    __tablename__ = 'abbb_constraints'
    __table_args__ = {'schema': 'scenario'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('scenario.abbb_constraints_id_seq'::regclass)"))
    scenario = Column(Text)
    constr = Column(Text)
    val = Column(Numeric)


class AbbbDemand(Base):
    __tablename__ = 'abbb_demand'
    __table_args__ = {'schema': 'scenario'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('scenario.abbb_demand_id_seq'::regclass)"))
    scenario = Column(Text)
    region = Column(Text)
    sector = Column(Text)
    type = Column(Text)
    demand = Column(Numeric)


class AbbbEmob(Base):
    __tablename__ = 'abbb_emob'
    __table_args__ = {'schema': 'scenario'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('scenario.abbb_emob_id_seq'::regclass)"))
    scenario = Column(Text)
    region = Column(Text)
    energy = Column(Numeric)


class AbbbRegion(Base):
    __tablename__ = 'abbb_regions'
    __table_args__ = {'schema': 'scenario'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('scenario.abbb_regions_id_seq'::regclass)"))
    region = Column(Text)
    reg = Column(Text)
    nutsid = Column(Text)
    geom = Column(Geometry('POLYGON', 25832))


class AbbbSimulationParameter(Base):
    __tablename__ = 'abbb_simulation_parameter'
    __table_args__ = {'schema': 'scenario'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('scenario.abbb_simulation_parameter_id_seq'::regclass)"))
    technology = Column(Text)
    co2_var = Column(Numeric)
    co2_fix = Column(Numeric)
    eta_elec = Column(Numeric)
    eta_th = Column(Numeric)
    eta_el_chp = Column(Numeric)
    eta_th_chp = Column(Numeric)
    eta_chp_flex_el = Column(Numeric)
    sigma_chp = Column(Numeric)
    beta_chp = Column(Numeric)
    opex_var = Column(Numeric)
    opex_fix = Column(Numeric)
    capex = Column(Numeric)
    c_rate_in = Column(Numeric)
    c_rate_out = Column(Numeric)
    eta_in = Column(Numeric)
    eta_out = Column(Numeric)
    cap_loss = Column(Numeric)
    lifetime = Column(Integer)
    wacc = Column(Numeric)


class AbbbTransformer(Base):
    __tablename__ = 'abbb_transformer'
    __table_args__ = {'schema': 'scenario'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('scenario.abbb_transformer_id_seq'::regclass)"))
    scenario = Column(Text)
    region = Column(Text)
    ressource = Column(Text)
    transformer = Column(Text)
    power = Column(Numeric)


class AbbbTransmissionCapacity(Base):
    __tablename__ = 'abbb_transmission_capacity'
    __table_args__ = {'schema': 'scenario'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('scenario.abbb_transmission_capacity_id_seq'::regclass)"))
    scenario = Column(Text)
    from_region = Column(Text)
    to_region = Column(Text)
    capacity = Column(Numeric)


class EgoSlpParameter(Base):
    __tablename__ = 'ego_slp_parameters'
    __table_args__ = {'schema': 'scenario'}

    parameter = Column(Text, primary_key=True)
    value = Column(Float(53))
    unit = Column(Text)

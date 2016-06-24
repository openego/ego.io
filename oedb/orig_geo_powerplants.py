# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, Numeric, \
    String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

t_industry_hoes_substations = Table(
    'industry_hoes_substations', metadata,
    Column('polygon_gid', Integer),
    Column('power_plant_gid', Integer),
    Column('voltage_level', Text),
    schema='orig_geo_powerplants'
)

t_industry_hs_substations = Table(
    'industry_hs_substations', metadata,
    Column('polygon_gid', Integer),
    Column('power_plant_gid', Integer),
    Column('voltage_level', Text),
    schema='orig_geo_powerplants'
)

t_industry_powerplant = Table(
    'industry_powerplant', metadata,
    Column('polygon_id', Integer),
    Column('powerplant_id', Integer),
    Column('voltage_level', Text),
    schema='orig_geo_powerplants'
)


class Nep2015Powerplant(Base):
    __tablename__ = 'nep_2015_powerplants'
    __table_args__ = {'schema': 'orig_geo_powerplants'}

    bnetza_id = Column(String)
    tso = Column(String)
    power_plant_name = Column(String)
    unit_name = Column(String)
    postcode = Column(String)
    state = Column(String)
    commissioning = Column(Integer)
    chp = Column(String)
    fuel = Column(String)
    rated_power = Column(Numeric)
    rated_power_a2025 = Column(Numeric)
    rated_power_b2025 = Column(Numeric)
    rated_power_b2035 = Column(Numeric)
    rated_power_c2025 = Column(Numeric)
    lat = Column(Float(53))
    lon = Column(Float(53))
    location_checked = Column(Text)
    geom = Column(Geometry('POINT', 4326))
    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_geo_powerplants.nep_2015_powerplants_gid_seq'::regclass)"))


class ProcPowerPlantGermany(Base):
    __tablename__ = 'proc_power_plant_germany'
    __table_args__ = {'schema': 'orig_geo_powerplants'}

    gid = Column(Integer, primary_key=True)
    bnetza_id = Column(Text)
    company = Column(Text)
    name = Column(Text)
    postcode = Column(Text)
    city = Column(Text)
    street = Column(Text)
    state = Column(Text)
    block = Column(Text)
    commissioned_original = Column(Text)
    commissioned = Column(Float(53))
    retrofit = Column(Float(53))
    shutdown = Column(Float(53))
    status = Column(Text)
    fuel = Column(Text)
    technology = Column(Text)
    type = Column(Text)
    eeg = Column(Text)
    chp = Column(Text)
    capacity = Column(Float(53))
    capacity_uba = Column(Float(53))
    chp_capacity_uba = Column(Float(53))
    efficiency_data = Column(Float(53))
    efficiency_estimate = Column(Float(53))
    network_node = Column(Text)
    voltage = Column(Text)
    network_operator = Column(Text)
    name_uba = Column(Text)
    lat = Column(Float(53))
    lon = Column(Float(53))
    comment = Column(Text)
    geom = Column(Geometry('POINT', 4326))
    voltage_level = Column(Text)
    temp = Column(Integer)


class RenewablePowerPlantsGermany(Base):
    __tablename__ = 'renewable_power_plants_germany'
    __table_args__ = {'schema': 'orig_geo_powerplants'}

    id = Column(BigInteger, primary_key=True)
    start_up_date = Column(DateTime)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    thermal_capacity = Column(Numeric)
    city = Column(String)
    postcode = Column(String)
    address = Column(String)
    lon = Column(Numeric)
    lat = Column(Numeric)
    gps_accuracy = Column(String)
    validation = Column(String)
    notification_reason = Column(String)
    eeg_id = Column(String)
    tso = Column(Float(53))
    tso_eic = Column(String)
    dso_id = Column(String)
    dso = Column(String)
    voltage_level = Column(String)
    network_node = Column(String)
    power_plant_id = Column(String)
    source = Column(String)
    comment = Column(String)
    geom = Column(Geometry('POINT', 4326), index=True)


class VoltageLevel(Base):
    __tablename__ = 'voltage_levels'
    __table_args__ = {'schema': 'orig_geo_powerplants'}

    voltage_level = Column(Text, primary_key=True)
    voltage = Column(Text)
    voltage_disc = Column(Text)

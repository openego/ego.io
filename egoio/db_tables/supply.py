# coding: utf-8
from sqlalchemy import ARRAY, BigInteger, Column, DateTime, Float, Integer, Numeric, SmallInteger, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import REAL


Base = declarative_base()
metadata = Base.metadata


class EgoConventionalPowerplant(Base):
    __tablename__ = 'ego_conventional_powerplant'
    __table_args__ = {'schema': 'supply'}

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


class EgoDpConvPowerplant(Base):
    __tablename__ = 'ego_dp_conv_powerplant'
    __table_args__ = {'schema': 'supply'}

    version = Column(Text, primary_key=True, nullable=False)
    gid = Column(Integer, primary_key=True, nullable=False)
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
    geom = Column(Geometry('POINT', 4326), index=True)
    voltage_level = Column(SmallInteger)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)


class EgoDpResPowerplant(Base):
    __tablename__ = 'ego_dp_res_powerplant'
    __table_args__ = {'schema': 'supply'}

    version = Column(Text, primary_key=True, nullable=False)
    id = Column(BigInteger, primary_key=True, nullable=False)
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
    voltage_level_var = Column(String)
    network_node = Column(String)
    power_plant_id = Column(String)
    source = Column(String)
    comment = Column(String)
    geom = Column(Geometry('POINT', 4326), index=True)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)
    voltage_level = Column(SmallInteger)
    la_id = Column(Integer)
    mvlv_subst_id = Column(Integer)
    rea_sort = Column(Integer)
    rea_flag = Column(String)
    rea_geom_line = Column(Geometry('LINESTRING', 3035))
    rea_geom_new = Column(Geometry('POINT', 3035), index=True)


t_ego_renewable_power_plants_germany_hydro_mview = Table(
    'ego_renewable_power_plants_germany_hydro_mview', metadata,
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    schema='supply'
)


t_ego_renewable_power_plants_germany_hydro_per_voltage_level_view = Table(
    'ego_renewable_power_plants_germany_hydro_per_voltage_level_view', metadata,
    Column('generation_type', Text),
    Column('voltage_level', String),
    Column('capacity', Numeric),
    Column('count', BigInteger),
    schema='supply'
)


class EgoRenewablePowerplant(Base):
    __tablename__ = 'ego_renewable_powerplant'
    __table_args__ = {'schema': 'supply'}

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


class ForwindOekoRenewableCapacityPerFederalstate(Base):
    __tablename__ = 'forwind_oeko_renewable_capacity_per_federalstate'
    __table_args__ = {'schema': 'supply'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('supply.forwind_oeko_renewable_capacity_per_federalstate_id_seq'::regclass)"))
    technology = Column(Text)
    year = Column(SmallInteger, nullable=False)
    federal_state = Column(Text)
    comment = Column(Text)
    capacity = Column(Integer)


class ForwindOekoRenewableFeedinPerFederalstate(Base):
    __tablename__ = 'forwind_oeko_renewable_feedin_per_federalstate'
    __table_args__ = {'schema': 'supply'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('supply.forwind_oeko_renewable_feedin_per_federalstate_id_seq'::regclass)"))
    technology = Column(Text)
    factor = Column(Text)
    year = Column(SmallInteger, nullable=False)
    federal_state = Column(Text)
    comment = Column(Text)
    time_series = Column(ARRAY(REAL()))


t_opsd_power_plants_germany_hydro_mview = Table(
    'opsd_power_plants_germany_hydro_mview', metadata,
    Column('gid', Integer),
    Column('bnetza_id', Text),
    Column('company', Text),
    Column('name', Text),
    Column('postcode', Text),
    Column('city', Text),
    Column('street', Text),
    Column('state', Text),
    Column('block', Text),
    Column('commissioned_original', Text),
    Column('commissioned', Float(53)),
    Column('retrofit', Float(53)),
    Column('shutdown', Float(53)),
    Column('status', Text),
    Column('fuel', Text),
    Column('technology', Text),
    Column('type', Text),
    Column('eeg', Text),
    Column('chp', Text),
    Column('capacity', Float(53)),
    Column('capacity_uba', Float(53)),
    Column('chp_capacity_uba', Float(53)),
    Column('efficiency_data', Float(53)),
    Column('efficiency_estimate', Float(53)),
    Column('network_node', Text),
    Column('voltage', Text),
    Column('network_operator', Text),
    Column('name_uba', Text),
    Column('lat', Float(53)),
    Column('lon', Float(53)),
    Column('comment', Text),
    Column('geom', Geometry('POINT', 4326), index=True),
    schema='supply'
)


class VernetzenWindPotentialArea(Base):
    __tablename__ = 'vernetzen_wind_potential_area'
    __table_args__ = {'schema': 'supply'}

    region_key = Column(String, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 25832), index=True)

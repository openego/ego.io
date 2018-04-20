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
    preversion = Column(Text)
    la_id = Column(Integer)
    scenario = Column(Text, primary_key=True, nullable=False, server_default=text("'none'::text"))
    flag = Column(Text)
    nuts = Column(String)


t_ego_dp_conv_powerplant_ego100_mview = Table(
    'ego_dp_conv_powerplant_ego100_mview', metadata,
    Column('version', Text),
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 4326)),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('la_id', Integer),
    Column('scenario', Text),
    Column('flag', Text),
    Column('nuts', String),
    schema='supply'
)


t_ego_dp_conv_powerplant_nep2035_mview = Table(
    'ego_dp_conv_powerplant_nep2035_mview', metadata,
    Column('version', Text),
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
    Column('geom', Geometry('POINT', 4326)),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('preversion', Text),
    Column('la_id', Integer),
    Column('scenario', Text),
    Column('flag', Text),
    Column('nuts', String),
    schema='supply'
)


t_ego_dp_conv_powerplant_sq_mview = Table(
    'ego_dp_conv_powerplant_sq_mview', metadata,
    Column('version', Text),
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
    Column('geom', Geometry('POINT', 4326)),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('preversion', Text),
    Column('la_id', Integer),
    Column('scenario', Text),
    Column('flag', Text),
    Column('nuts', String),
    schema='supply'
)


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
    preversion = Column(Text)
    flag = Column(String)
    scenario = Column(String, primary_key=True, nullable=False, server_default=text("'none'::character varying"))
    nuts = Column(String)


t_ego_dp_res_powerplant_ego100_mview = Table(
    'ego_dp_res_powerplant_ego100_mview', metadata,
    Column('version', Text),
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
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326)),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    Column('preversion', Text),
    Column('flag', String),
    Column('scenario', String),
    Column('nuts', String),
    schema='supply'
)


t_ego_dp_res_powerplant_nep2035_mview = Table(
    'ego_dp_res_powerplant_nep2035_mview', metadata,
    Column('version', Text),
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
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326)),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    Column('preversion', Text),
    Column('flag', String),
    Column('scenario', String),
    Column('nuts', String),
    schema='supply'
)


t_ego_dp_res_powerplant_sq_mview = Table(
    'ego_dp_res_powerplant_sq_mview', metadata,
    Column('version', Text),
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
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326)),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    Column('preversion', Text),
    Column('flag', String),
    Column('scenario', String),
    Column('nuts', String),
    schema='supply'
)


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


t_ego_res_powerplant_altmark_vg_mview = Table(
    'ego_res_powerplant_altmark_vg_mview', metadata,
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
    Column('voltage_level', SmallInteger),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326)),
    schema='supply'
)


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


t_fred_dp_conv_powerplant_hydro_mview = Table(
    'fred_dp_conv_powerplant_hydro_mview', metadata,
    Column('version', Text),
    Column('gid', Integer, unique=True),
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
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    schema='supply'
)


t_fred_dp_conv_powerplant_hydro_on_gaugeheight_mview = Table(
    'fred_dp_conv_powerplant_hydro_on_gaugeheight_mview', metadata,
    Column('gid', Integer),
    Column('id', Integer),
    Column('station_id', BigInteger),
    Column('station', String),
    Column('water', String),
    Column('geom', Geometry('POINT', 4326)),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_fred_dp_conv_powerplant_hydro_on_river_mview = Table(
    'fred_dp_conv_powerplant_hydro_on_river_mview', metadata,
    Column('gid', Integer),
    Column('gwk', String(30)),
    Column('nam', String(100)),
    Column('geom', Geometry('POINT', 4326)),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_fred_dp_res_powerplant_hydro_on_gauge_mview = Table(
    'fred_dp_res_powerplant_hydro_on_gauge_mview', metadata,
    Column('plant_id', BigInteger, unique=True),
    Column('gauge_id', Integer),
    Column('station_id', BigInteger),
    Column('station', String),
    Column('water', String),
    Column('source', Text),
    Column('dp_geom', Geometry, index=True),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_fred_dp_res_powerplant_hydro_on_river_mview = Table(
    'fred_dp_res_powerplant_hydro_on_river_mview', metadata,
    Column('id', BigInteger),
    Column('gwk', String(20)),
    Column('nam', String(100)),
    Column('orig_geom', Geometry('POINT', 4326)),
    Column('dp_geom', Geometry),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_fred_dp_res_powerplant_hydro_on_wg_mview = Table(
    'fred_dp_res_powerplant_hydro_on_wg_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('dp_geom', Geometry, index=True),
    Column('wg_id', Integer),
    schema='supply'
)


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


t_temp_table_cl = Table(
    'temp_table_cl', metadata,
    Column('name', Text),
    Column('geom', Geometry),
    Column('num_turb', Integer),
    Column('dvn', Float(53)),
    Column('hn', Float(53)),
    Column('pn', Float(53)),
    Column('turb_type', Text),
    schema='supply'
)


t_temp_table_cl_gauge_mview = Table(
    'temp_table_cl_gauge_mview', metadata,
    Column('plant_id', Text),
    Column('gauge_id', Integer),
    Column('station_id', BigInteger),
    Column('station', String),
    Column('water', String),
    Column('source', Text),
    Column('dp_geom', Geometry),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_temp_table_cl_river_mview = Table(
    'temp_table_cl_river_mview', metadata,
    Column('name', Text),
    Column('gwk', String(20)),
    Column('nam', String(100)),
    Column('orig_geom', Geometry),
    Column('dp_geom', Geometry),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_temp_table_cl_wg_mview = Table(
    'temp_table_cl_wg_mview', metadata,
    Column('name', Text),
    Column('dp_geom', Geometry),
    Column('wg_id', Integer),
    schema='supply'
)


class VernetzenWindPotentialArea(Base):
    __tablename__ = 'vernetzen_wind_potential_area'
    __table_args__ = {'schema': 'supply'}

    region_key = Column(String, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 25832), index=True)

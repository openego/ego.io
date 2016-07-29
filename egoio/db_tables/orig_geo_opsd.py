# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, Numeric, String, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class OpsdHourlyTimesery(Base):
    __tablename__ = 'opsd_hourly_timeseries'
    __table_args__ = {'schema': 'orig_geo_opsd'}

    timestamp = Column(DateTime, primary_key=True)
    load_at = Column(Numeric(12, 2))
    load_ba = Column(Numeric(12, 2))
    load_be = Column(Numeric(12, 2))
    load_bg = Column(Numeric(12, 2))
    load_ch = Column(Numeric(12, 2))
    load_cs = Column(Numeric(12, 2))
    load_cy = Column(Numeric(12, 2))
    load_cz = Column(Numeric(12, 2))
    load_de = Column(Numeric(12, 2))
    load_dk = Column(Numeric(12, 2))
    load_dkw = Column(Numeric(12, 2))
    load_ee = Column(Numeric(12, 2))
    load_es = Column(Numeric(12, 2))
    load_fi = Column(Numeric(12, 2))
    load_fr = Column(Numeric(12, 2))
    load_gb = Column(Numeric(12, 2))
    load_gr = Column(Numeric(12, 2))
    load_hr = Column(Numeric(12, 2))
    load_hu = Column(Numeric(12, 2))
    load_ie = Column(Numeric(12, 2))
    load_is = Column(Numeric(12, 2))
    load_it = Column(Numeric(12, 2))
    load_lt = Column(Numeric(12, 2))
    load_lu = Column(Numeric(12, 2))
    load_lv = Column(Numeric(12, 2))
    load_me = Column(Numeric(12, 2))
    load_mk = Column(Numeric(12, 2))
    load_ni = Column(Numeric(12, 2))
    load_nl = Column(Numeric(12, 2))
    load_no = Column(Numeric(12, 2))
    load_pl = Column(Numeric(12, 2))
    load_pt = Column(Numeric(12, 2))
    load_ro = Column(Numeric(12, 2))
    load_rs = Column(Numeric(12, 2))
    load_se = Column(Numeric(12, 2))
    load_si = Column(Numeric(12, 2))
    load_sk = Column(Numeric(12, 2))
    load_uaw = Column(Numeric(12, 2))
    solar_de_capacity = Column(Numeric(12, 2))
    solar_de_forecast = Column(Numeric(12, 2))
    solar_de_generation = Column(Numeric(12, 2))
    solar_de_profile = Column(Numeric(12, 2))
    solar_de50hertz_forecast = Column(Numeric(12, 2))
    solar_de50hertz_generation = Column(Numeric(12, 2))
    solar_deamprion_forecast = Column(Numeric(12, 2))
    solar_deamprion_generation = Column(Numeric(12, 2))
    solar_detennet_forecast = Column(Numeric(12, 2))
    solar_detennet_generation = Column(Numeric(12, 2))
    solar_detransnetbw_forecast = Column(Numeric(12, 2))
    solar_detransnetbw_generation = Column(Numeric(12, 2))
    wind_de_capacity = Column(Numeric(12, 2))
    wind_de_forecast = Column(Numeric(12, 2))
    wind_de_generation = Column(Numeric(12, 2))
    wind_de_profile = Column(Numeric(12, 2))
    wind_de50hertz_forecast = Column(Numeric(12, 2))
    wind_de50hertz_generation = Column(Numeric(12, 2))
    wind_deamprion_forecast = Column(Numeric(12, 2))
    wind_deamprion_generation = Column(Numeric(12, 2))
    wind_detennet_forecast = Column(Numeric(12, 2))
    wind_detennet_generation = Column(Numeric(12, 2))
    wind_detransnetbw_forecast = Column(Numeric(12, 2))
    wind_detransnetbw_generation = Column(Numeric(12, 2))


class OpsdPowerPlantsGermany(Base):
    __tablename__ = 'opsd_power_plants_germany'
    __table_args__ = {'schema': 'orig_geo_opsd'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('orig_geo_opsd.opsd_power_plants_germany_seq'::regclass)"))
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


class RenewablePowerPlantsGermany(Base):
    __tablename__ = 'renewable_power_plants_germany'
    __table_args__ = {'schema': 'orig_geo_opsd'}

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


class RenewablePowerPlantsGermanyHvSolarRoof(Base):
    __tablename__ = 'renewable_power_plants_germany_hv_solar_roof'
    __table_args__ = {'schema': 'orig_geo_opsd'}

    id = Column(BigInteger, primary_key=True)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    subst_id = Column(Integer)
    geom = Column(Geometry('POINT', 3035), index=True)


class TestDea(Base):
    __tablename__ = 'test_dea'
    __table_args__ = {'schema': 'orig_geo_opsd'}

    sorted = Column(BigInteger, primary_key=True)
    id = Column(BigInteger)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    subst_id = Column(Integer)
    geom = Column(Geometry('POINT', 3035))


class TestNew(Base):
    __tablename__ = 'test_new'
    __table_args__ = {'schema': 'orig_geo_opsd'}

    sorted = Column(BigInteger, primary_key=True)
    id = Column(BigInteger)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    subst_id = Column(Integer)
    old_geom = Column(Geometry('POINT', 3035))
    geom_line = Column(Geometry('LINESTRING', 3035))
    geom = Column(Geometry('POINT', 3035))


class TestOsm(Base):
    __tablename__ = 'test_osm'
    __table_args__ = {'schema': 'orig_geo_opsd'}

    sorted = Column(BigInteger, primary_key=True)
    id = Column(Integer)
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035))


class UrbanSectorPerGridDistrict4Agricultural(Base):
    __tablename__ = 'urban_sector_per_grid_district_4_agricultural'
    __table_args__ = {'schema': 'orig_geo_opsd'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('orig_geo_opsd.urban_sector_per_grid_district_4_agricultural_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035), index=True)

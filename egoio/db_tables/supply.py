# coding: utf-8

from sqlalchemy import BigInteger, Column, Float, Integer, SmallInteger, String, \
    Table, Text, text, Numeric, DateTime
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class EgoConvPowerplant(Base):
    __tablename__ = 'ego_conv_powerplant'
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
    geom = Column(Geometry('POINT', 4326), index=True)
    voltage_level = Column(Float(53))
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)


class EgoResPowerplant(Base):
    __tablename__ = 'ego_res_powerplant'
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
    voltage_level = Column(SmallInteger)
    network_node = Column(String)
    power_plant_id = Column(String)
    source = Column(String)
    comment = Column(String)
    geom = Column(Geometry('POINT', 4326), index=True)
    voltage = Column(String)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)

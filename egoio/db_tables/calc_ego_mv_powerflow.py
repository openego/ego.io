# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column,  Float, ForeignKey, Integer, Numeric, Text, text
from sqlalchemy.dialects.postgresql.base import ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

Base = declarative_base()
metadata = Base.metadata


class Bus(Base):
    __tablename__ = 'bus'
    __table_args__ = {'schema': 'calc_ego_mv_powerflow'}

    bus_id = Column(BigInteger, primary_key=True)
    v_nom = Column(Float(53))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT'))


# class BusVMagSet(Base):
#     __tablename__ = 'bus_v_mag_set'
#     __table_args__ = {'schema': 'calc_ego_mv_powerflow'}
#
#     bus_id = Column(ForeignKey('calc_ego_mv_powerflow.bus.bus_id'), primary_key=True, nullable=False)
#     temp_id = Column(ForeignKey('calc_ego_mv_powerflow.temp_resolution.temp_id'), primary_key=True, nullable=False)
#     v_mag_pu_set = Column(ARRAY(Float(53)))
#
#     bus = relationship('Bus')
#     temp = relationship('TempResolution')


class Generator(Base):
    __tablename__ = 'generator'
    __table_args__ = {'schema': 'calc_ego_mv_powerflow'}

    generator_id = Column(BigInteger, primary_key=True)
    bus = Column(ForeignKey('calc_ego_mv_powerflow.bus.bus_id'))

    control = Column(Text, server_default=text("'PQ'::text"))
    p_nom = Column(Float(53), server_default=text("0"))
    p_min_pu_fixed = Column(Float(53), server_default=text("0"))
    p_max_pu_fixed = Column(Float(53), server_default=text("1"))
    sign = Column(Float(53), server_default=text("1"))

    bu = relationship('Bus')
    source1 = relationship('Source')


# class GeneratorPqSet(Base):
#     __tablename__ = 'generator_pq_set'
#     __table_args__ = {'schema': 'calc_ego_mv_powerflow'}
#
#     generator_id = Column(ForeignKey('calc_ego_mv_powerflow.generator.generator_id'), primary_key=True, nullable=False)
#     temp_id = Column(ForeignKey('calc_ego_mv_powerflow.temp_resolution.temp_id'), primary_key=True, nullable=False)
#     p_set = Column(ARRAY(Float(53)))
#     q_set = Column(ARRAY(Float(53)))
#     p_min_pu = Column(ARRAY(Float(53)))
#     p_max_pu = Column(ARRAY(Float(53)))
#
#     generator = relationship('Generator')
#     temp = relationship('TempResolution')


class Line(Base):
    __tablename__ = 'line'
    __table_args__ = {'schema': 'calc_ego_mv_powerflow'}

    line_id = Column(BigInteger, primary_key=True)
    bus0 = Column(ForeignKey('calc_ego_mv_powerflow.bus.bus_id'))
    bus1 = Column(ForeignKey('calc_ego_mv_powerflow.bus.bus_id'))
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Numeric, server_default=text("0"))
    length = Column(Float(53))
    cables = Column(Integer)
    geom = Column(Geometry('MULTILINESTRING'))

    bu = relationship('Bus', primaryjoin='Line.bus0 == Bus.bus_id')
    bu1 = relationship('Bus', primaryjoin='Line.bus1 == Bus.bus_id')


class Load(Base):
    __tablename__ = 'load'
    __table_args__ = {'schema': 'calc_ego_mv_powerflow'}

    load_id = Column(BigInteger, primary_key=True)
    bus = Column(ForeignKey('calc_ego_mv_powerflow.bus.bus_id'))
    sign = Column(Float(53), server_default=text("'-1'::integer"))

    bu = relationship('Bus')


# class LoadPqSet(Base):
#     __tablename__ = 'load_pq_set'
#     __table_args__ = {'schema': 'calc_ego_mv_powerflow'}
#
#     load_id = Column(ForeignKey('calc_ego_mv_powerflow.load.load_id'), primary_key=True, nullable=False)
#     temp_id = Column(ForeignKey('calc_ego_mv_powerflow.temp_resolution.temp_id'), primary_key=True, nullable=False)
#     p_set = Column(ARRAY(Float(53)))
#     q_set = Column(ARRAY(Float(53)))
#
#     load = relationship('Load')
#     temp = relationship('TempResolution')


# class Source(Base):
#     __tablename__ = 'source'
#     __table_args__ = {'schema': 'calc_ego_mv_powerflow'}
#
#     source_id = Column(BigInteger, primary_key=True)
#     name = Column(Text)
#     co2_emissions = Column(Float(53))
#     commentary = Column(Text)


# class Storage(Base):
#     __tablename__ = 'storage'
#     __table_args__ = {'schema': 'calc_ego_mv_powerflow'}
#
#     storage_id = Column(BigInteger, primary_key=True)
#     bus = Column(ForeignKey('calc_ego_mv_powerflow.bus.bus_id'))
#     dispatch = Column(Text, server_default=text("'flexible'::text"))
#     control = Column(Text, server_default=text("'PQ'::text"))
#     p_nom = Column(Float(53), server_default=text("0"))
#     p_nom_extendable = Column(Boolean, server_default=text("false"))
#     p_nom_min = Column(Float(53), server_default=text("0"))
#     p_nom_max = Column(Float(53))
#     p_min_pu_fixed = Column(Float(53), server_default=text("0"))
#     p_max_pu_fixed = Column(Float(53), server_default=text("1"))
#     sign = Column(Float(53), server_default=text("1"))
#     source = Column(ForeignKey('calc_ego_mv_powerflow.source.source_id'), index=True)
#     marginal_cost = Column(Float(53))
#     capital_cost = Column(Float(53))
#     efficiency = Column(Float(53))
#     soa_initial = Column(Float(53))
#     soa_cyclic = Column(Boolean, server_default=text("false"))
#     max_hours = Column(Float(53))
#     efficiency_store = Column(Float(53))
#     efficiency_dispatch = Column(Float(53))
#     standing_loss = Column(Float(53))
#
#     bu = relationship('Bus')
#     source1 = relationship('Source')


# class StoragePqSet(Base):
#     __tablename__ = 'storage_pq_set'
#     __table_args__ = {'schema': 'calc_ego_mv_powerflow'}
#
#     storage_id = Column(ForeignKey('calc_ego_mv_powerflow.storage.storage_id'), primary_key=True, nullable=False)
#     temp_id = Column(ForeignKey('calc_ego_mv_powerflow.temp_resolution.temp_id'), primary_key=True, nullable=False)
#     p_set = Column(ARRAY(Float(53)))
#     q_set = Column(ARRAY(Float(53)))
#     p_min_pu = Column(ARRAY(Float(53)))
#     p_max_pu = Column(ARRAY(Float(53)))
#     soa_set = Column(ARRAY(Float(53)))
#     inflow = Column(ARRAY(Float(53)))
#
#     storage = relationship('Storage')
#     temp = relationship('TempResolution')


class TempResolution(Base):
    __tablename__ = 'temp_resolution'
    __table_args__ = {'schema': 'calc_ego_mv_powerflow'}

    temp_id = Column(BigInteger, primary_key=True)
    timesteps = Column(BigInteger, nullable=False)
    resolution = Column(Text)
    commentary = Column(Text)
    start_time = Column(Text)


class Transformer(Base):
    __tablename__ = 'transformer'
    __table_args__ = {'schema': 'calc_ego_mv_powerflow'}

    trafo_id = Column(BigInteger, primary_key=True)
    bus0 = Column(ForeignKey('calc_ego_mv_powerflow.bus.bus_id'), index=True)
    bus1 = Column(ForeignKey('calc_ego_mv_powerflow.bus.bus_id'), index=True)
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Float(53), server_default=text("0"))
    tap_ratio = Column(Float(53))
    phase_shift = Column(Float(53))
    geom = Column(Geometry('MULTILINESTRING'))

    bu = relationship('Bus', primaryjoin='Transformer.bus0 == Bus.bus_id')
    bu1 = relationship('Bus', primaryjoin='Transformer.bus1 == Bus.bus_id')

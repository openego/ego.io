# coding: utf-8
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class DestatisGvaPerDistrict(Base):
    __tablename__ = 'destatis_gva_per_districts'
    __table_args__ = {'schema': 'orig_consumption_znes'}

    eu_code = Column(String(7), primary_key=True)
    district = Column(String, nullable=False)
    total_gva = Column(Float(53), nullable=False)
    gva_industry = Column(Float(53), nullable=False)
    gva_tertiary_sector = Column(Float(53), nullable=False)


class LakConsumptionPerDistrict(Base):
    __tablename__ = 'lak_consumption_per_district'
    __table_args__ = {'schema': 'orig_consumption_znes'}

    eu_code = Column(String(7), primary_key=True)
    district = Column(String)
    elec_consumption_industry = Column(Float(53))
    elec_consumption_tertiary_sector = Column(Float(53))
    area_industry = Column(Float(53))
    area_retail = Column(Float(53))
    area_agriculture = Column(Float(53))
    area_tertiary_sector = Column(Float(53))
    consumption_per_area_tertiary_sector = Column(Float(53))
    consumption_per_area_industry = Column(Float(53))


class LakConsumptionPerFederalstate(Base):
    __tablename__ = 'lak_consumption_per_federalstate'
    __table_args__ = {'schema': 'orig_consumption_znes'}

    eu_code = Column(String(7), primary_key=True)
    federal_states = Column(String, nullable=False)
    elec_consumption_households = Column(Float(53), nullable=False)
    elec_consumption_industry = Column(Float(53), nullable=False)
    elec_consumption_tertiary_sector = Column(Float(53), nullable=False)
    population = Column(Integer)
    elec_consumption_households_per_person = Column(Float(53))


class LakConsumptionPerFederalstatePerGva(Base):
    __tablename__ = 'lak_consumption_per_federalstate_per_gva'
    __table_args__ = {'schema': 'orig_consumption_znes'}

    eu_code = Column(String(7), primary_key=True)
    federal_state = Column(String)
    elec_consumption_industry = Column(Float(53))
    elec_consumption_tertiary_sector = Column(Float(53))

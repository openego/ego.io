# coding: utf-8
from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class ParameterElectricalPowerPlant(Base):
    __tablename__ = 'parameter_electrical_power_plant'
    __table_args__ = {'schema': 'ref_test'}

    fuel = Column(String, primary_key=True, nullable=False)
    type_of_generation = Column(String, primary_key=True, nullable=False)
    size = Column(ARRAY(NUMERIC()), primary_key=True, nullable=False)
    effnetto_el = Column(Numeric(5, 3))
    opex_fix = Column(Numeric(15, 3))
    opex_var = Column(Numeric(15, 3))
    ref_id = Column(Integer)

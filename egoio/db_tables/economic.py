# coding: utf-8
from sqlalchemy import Column, Float, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class DestatisGvaPerDistrict(Base):
    __tablename__ = 'destatis_gva_per_district'
    __table_args__ = {'schema': 'economic'}

    eu_code = Column(String(7), primary_key=True)
    district = Column(String, nullable=False)
    total_gva = Column(Float(53), nullable=False)
    gva_industry = Column(Float(53), nullable=False)
    gva_tertiary_sector = Column(Float(53), nullable=False)

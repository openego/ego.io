# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, Integer, Numeric, String, Table, Text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class BbsrRagCityAndMunTypesPerMun(Base):
    __tablename__ = 'bbsr_rag_city_and_mun_types_per_mun'
    __table_args__ = {'schema': 'social'}

    mun_id = Column(BigInteger, primary_key=True)
    mun_name = Column(Text)
    munassn_id = Column(BigInteger)
    munassn_name = Column(Text)
    pop_2013 = Column(Integer)
    area_sqm = Column(Numeric(5, 2))
    cm_typ = Column(Integer)
    cm_typ_name = Column(Text)
    cm_typ_d = Column(Integer)
    cm_typ_d_name = Column(Text)


class DestatisZensusPopulationPerBkgVg2506Gem(Base):
    __tablename__ = 'destatis_zensus_population_per_bkg_vg250_6_gem'
    __table_args__ = {'schema': 'social'}

    reference_date = Column(Date, primary_key=True, nullable=False)
    gem_id = Column(Integer, primary_key=True, nullable=False)
    ags_0 = Column(String(12))
    census_sum = Column(Integer)
    census_count = Column(Integer)
    census_density = Column(Integer)


class DestatisZensusPopulationPerHa(Base):
    __tablename__ = 'destatis_zensus_population_per_ha'
    __table_args__ = {'schema': 'social'}

    gid = Column(Integer, primary_key=True)
    grid_id = Column(String(254), nullable=False)
    x_mp = Column(Numeric(10, 0))
    y_mp = Column(Numeric(10, 0))
    population = Column(Numeric(10, 0))
    geom_point = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_destatis_zensus_population_per_ha_mview = Table(
    'destatis_zensus_population_per_ha_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('population', Numeric(10, 0)),
    Column('geom_point', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='social'
)

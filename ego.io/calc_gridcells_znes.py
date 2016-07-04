# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, ForeignKey, Integer, \
    SmallInteger, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class DeuVoronoi(Base):
    __tablename__ = 'deu_voronoi'
    __table_args__ = {'schema': 'calc_gridcells_znes'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry, index=True)


t_substations_deu_voronoi = Table(
    'substations_deu_voronoi', metadata,
    Column('lon', Float(53)),
    Column('lat', Float(53)),
    Column('voltage', Text),
    Column('power_typ', Text),
    Column('osm_id', BigInteger),
    Column('osm_typ', Text),
    Column('osm_www', Text),
    Column('frequency', Text),
    Column('name', Text),
    Column('ref', Text),
    Column('substation', Text),
    Column('operator', Text),
    Column('status', SmallInteger),
    Column('visible', SmallInteger),
    Column('geom', Geometry('POINT', 4326)),
    Column('subst_id', Integer),
    schema='calc_gridcells_znes'
)


class SubstationsDummy(Base):
    __tablename__ = 'substations_dummy'
    __table_args__ = {'schema': 'calc_gridcells_znes'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POINT', 4326))
    lon = Column(Float(53))
    lat = Column(Float(53))
    voltage = Column(String)
    power_typ = Column(String)
    osm_id = Column(BigInteger)
    osm_typ = Column(String)
    osm_www = Column(String)
    frequency = Column(String)
    name = Column(String)
    ref = Column(String)
    substation = Column(String)
    operator = Column(String)
    status = Column(Integer)
    visible = Column(Integer)


class Voronoi(Base):
    __tablename__ = 'voronoi'
    __table_args__ = {'schema': 'calc_gridcells_znes'}

    geom = Column(Geometry('POLYGON', 4326), index=True)
    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_gridcells_znes.voronoi_id_seq'::regclass)"))


class ZnesDeuGridcellsQgi(Base):
    __tablename__ = 'znes_deu_gridcells_qgis'
    __table_args__ = {'schema': 'calc_gridcells_znes'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_gridcells_znes.znes_deu_gridcells_qgis_id_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 4326), index=True)
    subst_id = Column(ForeignKey(
        'calc_gridcells_znes.znes_deu_substations_filtered.subst_id'))

    subst = relationship('ZnesDeuSubstationsFiltered')


class ZnesDeuSubstation(Base):
    __tablename__ = 'znes_deu_substations'
    __table_args__ = {'schema': 'calc_gridcells_znes'}

    id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_gridcells_znes.uw_id_seq'::regclass)"))
    lon = Column(Float(53), nullable=False)
    lat = Column(Float(53), nullable=False)
    voltage = Column(Text)
    power_typ = Column(Text)
    osm_id = Column(BigInteger, nullable=False)
    osm_typ = Column(Text, nullable=False)
    osm_www = Column(Text, nullable=False)
    frequency = Column(Text)
    name = Column(Text)
    ref = Column(Text)
    substation = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger, nullable=False)
    visible = Column(SmallInteger, nullable=False)
    geom = Column(Geometry('POINT', 4326))


class ZnesDeuSubstationsFiltered(Base):
    __tablename__ = 'znes_deu_substations_filtered'
    __table_args__ = {'schema': 'calc_gridcells_znes'}

    lon = Column(Float(53))
    lat = Column(Float(53))
    voltage = Column(Text)
    power_typ = Column(Text)
    osm_id = Column(BigInteger)
    osm_typ = Column(Text)
    osm_www = Column(Text)
    frequency = Column(Text)
    name = Column(Text)
    ref = Column(Text)
    substation = Column(Text)
    operator = Column(Text)
    status = Column(SmallInteger)
    visible = Column(SmallInteger)
    geom = Column(Geometry('POINT', 4326))
    subst_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('calc_gridcells_znes.znes_deu_substations_filtered_subst_id_seq'::regclass)"))

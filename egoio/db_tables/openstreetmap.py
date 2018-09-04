# coding: utf-8
from sqlalchemy import ARRAY, BigInteger, Boolean, Column, Float, Integer, SmallInteger, Table, Text, text
from sqlalchemy.dialects.postgresql.hstore import HSTORE
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class OsmDeuLine(Base):
    __tablename__ = 'osm_deu_line'
    __table_args__ = {'schema': 'openstreetmap'}

    osm_id = Column(BigInteger)
    access = Column(Text)
    addr_housename = Column('addr:housename', Text)
    addr_housenumber = Column('addr:housenumber', Text)
    addr_interpolation = Column('addr:interpolation', Text)
    admin_level = Column(Text)
    aerialway = Column(Text)
    aeroway = Column(Text)
    amenity = Column(Text)
    area = Column(Text)
    barrier = Column(Text)
    bicycle = Column(Text)
    brand = Column(Text)
    bridge = Column(Text)
    boundary = Column(Text)
    building = Column(Text)
    construction = Column(Text)
    covered = Column(Text)
    culvert = Column(Text)
    cutting = Column(Text)
    denomination = Column(Text)
    disused = Column(Text)
    embankment = Column(Text)
    foot = Column(Text)
    generator_source = Column('generator:source', Text)
    harbour = Column(Text)
    highway = Column(Text)
    historic = Column(Text)
    horse = Column(Text)
    intermittent = Column(Text)
    junction = Column(Text)
    landuse = Column(Text)
    layer = Column(Text)
    leisure = Column(Text)
    lock = Column(Text)
    man_made = Column(Text)
    military = Column(Text)
    motorcar = Column(Text)
    name = Column(Text)
    natural = Column(Text)
    office = Column(Text)
    oneway = Column(Text)
    operator = Column(Text)
    place = Column(Text)
    population = Column(Text)
    power = Column(Text)
    power_source = Column(Text)
    public_transport = Column(Text)
    railway = Column(Text)
    ref = Column(Text)
    religion = Column(Text)
    route = Column(Text)
    service = Column(Text)
    shop = Column(Text)
    sport = Column(Text)
    surface = Column(Text)
    toll = Column(Text)
    tourism = Column(Text)
    tower_type = Column('tower:type', Text)
    tracktype = Column(Text)
    tunnel = Column(Text)
    water = Column(Text)
    waterway = Column(Text)
    wetland = Column(Text)
    width = Column(Text)
    wood = Column(Text)
    z_order = Column(Integer)
    way_area = Column(Float)
    abandoned_aeroway = Column('abandoned:aeroway', Text)
    abandoned_amenity = Column('abandoned:amenity', Text)
    abandoned_building = Column('abandoned:building', Text)
    abandoned_landuse = Column('abandoned:landuse', Text)
    abandoned_power = Column('abandoned:power', Text)
    area_highway = Column('area:highway', Text)
    tags = Column(HSTORE(Text()), index=True)
    geom = Column(Geometry('LINESTRING', 900913), index=True)
    gid = Column(Integer, primary_key=True, server_default=text("nextval('openstreetmap.osm_deu_line_gid_seq'::regclass)"))


t_osm_deu_line_major_mview = Table(
    'osm_deu_line_major_mview', metadata,
    Column('osm_id', BigInteger),
    Column('geom', Geometry),
    Column('tags', HSTORE(Text())),
    schema='openstreetmap'
)


t_osm_deu_line_street_mview = Table(
    'osm_deu_line_street_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', BigInteger),
    Column('tags', HSTORE(Text())),
    Column('geom', Geometry, index=True),
    schema='openstreetmap'
)


class OsmDeuNode(Base):
    __tablename__ = 'osm_deu_nodes'
    __table_args__ = {'schema': 'openstreetmap'}

    id = Column(BigInteger, primary_key=True)
    lat = Column(Integer, nullable=False)
    lon = Column(Integer, nullable=False)
    tags = Column(ARRAY(Text()))


class OsmDeuPoint(Base):
    __tablename__ = 'osm_deu_point'
    __table_args__ = {'schema': 'openstreetmap'}

    osm_id = Column(BigInteger)
    access = Column(Text)
    addr_housename = Column('addr:housename', Text)
    addr_housenumber = Column('addr:housenumber', Text)
    addr_interpolation = Column('addr:interpolation', Text)
    admin_level = Column(Text)
    aerialway = Column(Text)
    aeroway = Column(Text)
    amenity = Column(Text)
    area = Column(Text)
    barrier = Column(Text)
    bicycle = Column(Text)
    brand = Column(Text)
    bridge = Column(Text)
    boundary = Column(Text)
    building = Column(Text)
    capital = Column(Text)
    construction = Column(Text)
    covered = Column(Text)
    culvert = Column(Text)
    cutting = Column(Text)
    denomination = Column(Text)
    disused = Column(Text)
    ele = Column(Text)
    embankment = Column(Text)
    foot = Column(Text)
    generator_source = Column('generator:source', Text)
    harbour = Column(Text)
    highway = Column(Text)
    historic = Column(Text)
    horse = Column(Text)
    intermittent = Column(Text)
    junction = Column(Text)
    landuse = Column(Text)
    layer = Column(Text)
    leisure = Column(Text)
    lock = Column(Text)
    man_made = Column(Text)
    military = Column(Text)
    motorcar = Column(Text)
    name = Column(Text)
    natural = Column(Text)
    office = Column(Text)
    oneway = Column(Text)
    operator = Column(Text)
    place = Column(Text)
    population = Column(Text)
    power = Column(Text)
    power_source = Column(Text)
    public_transport = Column(Text)
    railway = Column(Text)
    ref = Column(Text)
    religion = Column(Text)
    route = Column(Text)
    service = Column(Text)
    shop = Column(Text)
    sport = Column(Text)
    surface = Column(Text)
    toll = Column(Text)
    tourism = Column(Text)
    tower_type = Column('tower:type', Text)
    tunnel = Column(Text)
    water = Column(Text)
    waterway = Column(Text)
    wetland = Column(Text)
    width = Column(Text)
    wood = Column(Text)
    z_order = Column(Integer)
    tags = Column(HSTORE(Text()), index=True)
    geom = Column(Geometry('POINT', 900913), index=True)
    gid = Column(Integer, primary_key=True, server_default=text("nextval('openstreetmap.osm_deu_point_gid_seq'::regclass)"))


t_osm_deu_point_biogas_mview = Table(
    'osm_deu_point_biogas_mview', metadata,
    Column('osm_id', BigInteger),
    Column('gid', Integer),
    Column('tags', HSTORE(Text())),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='openstreetmap'
)


t_osm_deu_point_solar_mview = Table(
    'osm_deu_point_solar_mview', metadata,
    Column('osm_id', BigInteger),
    Column('gid', Integer),
    Column('tags', HSTORE(Text())),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='openstreetmap'
)


t_osm_deu_point_wind_mview = Table(
    'osm_deu_point_wind_mview', metadata,
    Column('osm_id', BigInteger),
    Column('gid', Integer),
    Column('tags', HSTORE(Text())),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='openstreetmap'
)


class OsmDeuPointWindpower(Base):
    __tablename__ = 'osm_deu_point_windpower'
    __table_args__ = {'schema': 'openstreetmap'}

    gid = Column(Integer, primary_key=True)
    osm_id = Column(BigInteger)
    building = Column(Text)
    tags = Column(HSTORE(Text()))
    geom = Column(Geometry, index=True)


class OsmDeuPolygon(Base):
    __tablename__ = 'osm_deu_polygon'
    __table_args__ = {'schema': 'openstreetmap'}

    osm_id = Column(BigInteger)
    access = Column(Text)
    addr_housename = Column('addr:housename', Text)
    addr_housenumber = Column('addr:housenumber', Text)
    addr_interpolation = Column('addr:interpolation', Text)
    admin_level = Column(Text)
    aerialway = Column(Text)
    aeroway = Column(Text)
    amenity = Column(Text)
    area = Column(Text)
    barrier = Column(Text)
    bicycle = Column(Text)
    brand = Column(Text)
    bridge = Column(Text)
    boundary = Column(Text)
    building = Column(Text)
    construction = Column(Text)
    covered = Column(Text)
    culvert = Column(Text)
    cutting = Column(Text)
    denomination = Column(Text)
    disused = Column(Text)
    embankment = Column(Text)
    foot = Column(Text)
    generator_source = Column('generator:source', Text)
    harbour = Column(Text)
    highway = Column(Text)
    historic = Column(Text)
    horse = Column(Text)
    intermittent = Column(Text)
    junction = Column(Text)
    landuse = Column(Text)
    layer = Column(Text)
    leisure = Column(Text)
    lock = Column(Text)
    man_made = Column(Text)
    military = Column(Text)
    motorcar = Column(Text)
    name = Column(Text)
    natural = Column(Text)
    office = Column(Text)
    oneway = Column(Text)
    operator = Column(Text)
    place = Column(Text)
    population = Column(Text)
    power = Column(Text)
    power_source = Column(Text)
    public_transport = Column(Text)
    railway = Column(Text)
    ref = Column(Text)
    religion = Column(Text)
    route = Column(Text)
    service = Column(Text)
    shop = Column(Text)
    sport = Column(Text)
    surface = Column(Text)
    toll = Column(Text)
    tourism = Column(Text)
    tower_type = Column('tower:type', Text)
    tracktype = Column(Text)
    tunnel = Column(Text)
    water = Column(Text)
    waterway = Column(Text)
    wetland = Column(Text)
    width = Column(Text)
    wood = Column(Text)
    z_order = Column(Integer)
    way_area = Column(Float)
    abandoned_aeroway = Column('abandoned:aeroway', Text)
    abandoned_amenity = Column('abandoned:amenity', Text)
    abandoned_building = Column('abandoned:building', Text)
    abandoned_landuse = Column('abandoned:landuse', Text)
    abandoned_power = Column('abandoned:power', Text)
    area_highway = Column('area:highway', Text)
    tags = Column(HSTORE(Text()), index=True)
    geom = Column(Geometry(srid=900913), index=True)
    gid = Column(Integer, primary_key=True, server_default=text("nextval('openstreetmap.osm_deu_polygon_gid_seq'::regclass)"))


t_osm_deu_polygon_building_mview = Table(
    'osm_deu_polygon_building_mview', metadata,
    Column('gid', Integer),
    Column('geom', Geometry, index=True),
    Column('building', Text),
    schema='openstreetmap'
)


t_osm_deu_polygon_landuse_mview = Table(
    'osm_deu_polygon_landuse_mview', metadata,
    Column('gid', Integer),
    Column('tags', HSTORE(Text())),
    Column('geom', Geometry(srid=900913), index=True),
    schema='openstreetmap'
)


class OsmDeuPolygonUrban(Base):
    __tablename__ = 'osm_deu_polygon_urban'
    __table_args__ = {'schema': 'openstreetmap'}

    gid = Column(Integer, primary_key=True)
    osm_id = Column(Integer)
    name = Column(Text)
    sector = Column(Integer)
    area_ha = Column(Float(53))
    tags = Column(HSTORE(Text()))
    vg250 = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_osm_deu_polygon_urban_error_geom_vg250_mview = Table(
    'osm_deu_polygon_urban_error_geom_vg250_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('name', Text),
    Column('sector', Integer),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE(Text())),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='openstreetmap'
)


t_osm_deu_polygon_urban_sector_1_residential_mview = Table(
    'osm_deu_polygon_urban_sector_1_residential_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('name', Text),
    Column('sector', Integer),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE(Text())),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='openstreetmap'
)


t_osm_deu_polygon_urban_sector_2_retail_mview = Table(
    'osm_deu_polygon_urban_sector_2_retail_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('name', Text),
    Column('sector', Integer),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE(Text())),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='openstreetmap'
)


t_osm_deu_polygon_urban_sector_3_industrial_mview = Table(
    'osm_deu_polygon_urban_sector_3_industrial_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('name', Text),
    Column('sector', Integer),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE(Text())),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='openstreetmap'
)


t_osm_deu_polygon_urban_sector_3_industrial_nolargescale_mview = Table(
    'osm_deu_polygon_urban_sector_3_industrial_nolargescale_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('name', Text),
    Column('sector', Integer),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE(Text())),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='openstreetmap'
)


t_osm_deu_polygon_urban_sector_4_agricultural_mview = Table(
    'osm_deu_polygon_urban_sector_4_agricultural_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('name', Text),
    Column('sector', Integer),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE(Text())),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='openstreetmap'
)


t_osm_deu_polygon_urban_vg250_clean_cut_multi_mview = Table(
    'osm_deu_polygon_urban_vg250_clean_cut_multi_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('name', Text),
    Column('sector', Integer),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE(Text())),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='openstreetmap'
)


t_osm_deu_polygon_urban_vg250_clean_cut_mview = Table(
    'osm_deu_polygon_urban_vg250_clean_cut_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('name', Text),
    Column('sector', Integer),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE(Text())),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035)),
    schema='openstreetmap'
)


t_osm_deu_polygon_urban_vg250_cut_mview = Table(
    'osm_deu_polygon_urban_vg250_cut_mview', metadata,
    Column('id', Integer),
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('name', Text),
    Column('sector', Integer),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE(Text())),
    Column('vg250', Text),
    Column('geom_type', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='openstreetmap'
)


class OsmDeuRel(Base):
    __tablename__ = 'osm_deu_rels'
    __table_args__ = {'schema': 'openstreetmap'}

    id = Column(BigInteger, primary_key=True, index=True)
    way_off = Column(SmallInteger)
    rel_off = Column(SmallInteger)
    parts = Column(ARRAY(BigInteger()), index=True)
    members = Column(ARRAY(Text()))
    tags = Column(ARRAY(Text()))
    pending = Column(Boolean, nullable=False)


class OsmDeuRoad(Base):
    __tablename__ = 'osm_deu_roads'
    __table_args__ = {'schema': 'openstreetmap'}

    osm_id = Column(BigInteger)
    access = Column(Text)
    addr_housename = Column('addr:housename', Text)
    addr_housenumber = Column('addr:housenumber', Text)
    addr_interpolation = Column('addr:interpolation', Text)
    admin_level = Column(Text)
    aerialway = Column(Text)
    aeroway = Column(Text)
    amenity = Column(Text)
    area = Column(Text)
    barrier = Column(Text)
    bicycle = Column(Text)
    brand = Column(Text)
    bridge = Column(Text)
    boundary = Column(Text)
    building = Column(Text)
    construction = Column(Text)
    covered = Column(Text)
    culvert = Column(Text)
    cutting = Column(Text)
    denomination = Column(Text)
    disused = Column(Text)
    embankment = Column(Text)
    foot = Column(Text)
    generator_source = Column('generator:source', Text)
    harbour = Column(Text)
    highway = Column(Text)
    historic = Column(Text)
    horse = Column(Text)
    intermittent = Column(Text)
    junction = Column(Text)
    landuse = Column(Text)
    layer = Column(Text)
    leisure = Column(Text)
    lock = Column(Text)
    man_made = Column(Text)
    military = Column(Text)
    motorcar = Column(Text)
    name = Column(Text)
    natural = Column(Text)
    office = Column(Text)
    oneway = Column(Text)
    operator = Column(Text)
    place = Column(Text)
    population = Column(Text)
    power = Column(Text)
    power_source = Column(Text)
    public_transport = Column(Text)
    railway = Column(Text)
    ref = Column(Text)
    religion = Column(Text)
    route = Column(Text)
    service = Column(Text)
    shop = Column(Text)
    sport = Column(Text)
    surface = Column(Text)
    toll = Column(Text)
    tourism = Column(Text)
    tower_type = Column('tower:type', Text)
    tracktype = Column(Text)
    tunnel = Column(Text)
    water = Column(Text)
    waterway = Column(Text)
    wetland = Column(Text)
    width = Column(Text)
    wood = Column(Text)
    z_order = Column(Integer)
    way_area = Column(Float)
    abandoned_aeroway = Column('abandoned:aeroway', Text)
    abandoned_amenity = Column('abandoned:amenity', Text)
    abandoned_building = Column('abandoned:building', Text)
    abandoned_landuse = Column('abandoned:landuse', Text)
    abandoned_power = Column('abandoned:power', Text)
    area_highway = Column('area:highway', Text)
    tags = Column(HSTORE(Text()), index=True)
    geom = Column(Geometry('LINESTRING', 900913), index=True)
    gid = Column(Integer, primary_key=True, server_default=text("nextval('openstreetmap.osm_deu_roads_gid_seq'::regclass)"))


class OsmDeuWay(Base):
    __tablename__ = 'osm_deu_ways'
    __table_args__ = {'schema': 'openstreetmap'}

    id = Column(BigInteger, primary_key=True, index=True)
    nodes = Column(ARRAY(BigInteger()), nullable=False, index=True)
    tags = Column(ARRAY(Text()))
    pending = Column(Boolean, nullable=False)

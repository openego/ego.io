# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Float, Integer, \
    SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.postgresql.hstore import HSTORE
from geoalchemy2.types import Geometry
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class OsmDeuLine(Base):
    __tablename__ = 'osm_deu_line'
    __table_args__ = {'schema': 'orig_osm'}

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
    tags = Column(HSTORE, index=True)
    geom = Column(Geometry('LINESTRING', 3857), index=True)
    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_osm.osm_deu_line_gid_seq'::regclass)"))


class OsmDeuNode(Base):
    __tablename__ = 'osm_deu_nodes'
    __table_args__ = {'schema': 'orig_osm'}

    id = Column(BigInteger, primary_key=True)
    lat = Column(Integer, nullable=False)
    lon = Column(Integer, nullable=False)
    tags = Column(ARRAY(TEXT()))


class OsmDeuPoint(Base):
    __tablename__ = 'osm_deu_point'
    __table_args__ = {'schema': 'orig_osm'}

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
    poi = Column(Text)
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
    tags = Column(HSTORE, index=True)
    geom = Column(Geometry('POINT', 3857), index=True)
    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_osm.osm_deu_point_gid_seq'::regclass)"))


t_osm_deu_point_power_substation_industrial_view = Table(
    'osm_deu_point_power_substation_industrial_view', metadata,
    Column('osm_id', BigInteger),
    Column('access', Text),
    Column('addr:housename', Text),
    Column('addr:housenumber', Text),
    Column('addr:interpolation', Text),
    Column('admin_level', Text),
    Column('aerialway', Text),
    Column('aeroway', Text),
    Column('amenity', Text),
    Column('area', Text),
    Column('barrier', Text),
    Column('bicycle', Text),
    Column('brand', Text),
    Column('bridge', Text),
    Column('boundary', Text),
    Column('building', Text),
    Column('capital', Text),
    Column('construction', Text),
    Column('covered', Text),
    Column('culvert', Text),
    Column('cutting', Text),
    Column('denomination', Text),
    Column('disused', Text),
    Column('ele', Text),
    Column('embankment', Text),
    Column('foot', Text),
    Column('generator:source', Text),
    Column('harbour', Text),
    Column('highway', Text),
    Column('historic', Text),
    Column('horse', Text),
    Column('intermittent', Text),
    Column('junction', Text),
    Column('landuse', Text),
    Column('layer', Text),
    Column('leisure', Text),
    Column('lock', Text),
    Column('man_made', Text),
    Column('military', Text),
    Column('motorcar', Text),
    Column('name', Text),
    Column('natural', Text),
    Column('office', Text),
    Column('oneway', Text),
    Column('operator', Text),
    Column('place', Text),
    Column('poi', Text),
    Column('population', Text),
    Column('power', Text),
    Column('power_source', Text),
    Column('public_transport', Text),
    Column('railway', Text),
    Column('ref', Text),
    Column('religion', Text),
    Column('route', Text),
    Column('service', Text),
    Column('shop', Text),
    Column('sport', Text),
    Column('surface', Text),
    Column('toll', Text),
    Column('tourism', Text),
    Column('tower:type', Text),
    Column('tunnel', Text),
    Column('water', Text),
    Column('waterway', Text),
    Column('wetland', Text),
    Column('width', Text),
    Column('wood', Text),
    Column('z_order', Integer),
    Column('tags', HSTORE),
    Column('geom', Geometry('POINT', 3857)),
    Column('gid', Integer),
    schema='orig_osm'
)


class OsmDeuPolygon(Base):
    __tablename__ = 'osm_deu_polygon'
    __table_args__ = {'schema': 'orig_osm'}

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
    tags = Column(HSTORE, index=True)
    geom = Column(Geometry('MULTIPOLYGON', 3857), index=True)
    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_osm.osm_deu_polygon_gid_seq'::regclass)"))


t_osm_deu_polygon_agriculture_view = Table(
    'osm_deu_polygon_agriculture_view', metadata,
    Column('osm_id', BigInteger),
    Column('access', Text),
    Column('addr:housename', Text),
    Column('addr:housenumber', Text),
    Column('addr:interpolation', Text),
    Column('admin_level', Text),
    Column('aerialway', Text),
    Column('aeroway', Text),
    Column('amenity', Text),
    Column('area', Text),
    Column('barrier', Text),
    Column('bicycle', Text),
    Column('brand', Text),
    Column('bridge', Text),
    Column('boundary', Text),
    Column('building', Text),
    Column('construction', Text),
    Column('covered', Text),
    Column('culvert', Text),
    Column('cutting', Text),
    Column('denomination', Text),
    Column('disused', Text),
    Column('embankment', Text),
    Column('foot', Text),
    Column('generator:source', Text),
    Column('harbour', Text),
    Column('highway', Text),
    Column('historic', Text),
    Column('horse', Text),
    Column('intermittent', Text),
    Column('junction', Text),
    Column('landuse', Text),
    Column('layer', Text),
    Column('leisure', Text),
    Column('lock', Text),
    Column('man_made', Text),
    Column('military', Text),
    Column('motorcar', Text),
    Column('name', Text),
    Column('natural', Text),
    Column('office', Text),
    Column('oneway', Text),
    Column('operator', Text),
    Column('place', Text),
    Column('population', Text),
    Column('power', Text),
    Column('power_source', Text),
    Column('public_transport', Text),
    Column('railway', Text),
    Column('ref', Text),
    Column('religion', Text),
    Column('route', Text),
    Column('service', Text),
    Column('shop', Text),
    Column('sport', Text),
    Column('surface', Text),
    Column('toll', Text),
    Column('tourism', Text),
    Column('tower:type', Text),
    Column('tracktype', Text),
    Column('tunnel', Text),
    Column('water', Text),
    Column('waterway', Text),
    Column('wetland', Text),
    Column('width', Text),
    Column('wood', Text),
    Column('z_order', Integer),
    Column('way_area', Float),
    Column('tags', HSTORE),
    Column('geom', Geometry('MULTIPOLYGON', 3857)),
    Column('gid', Integer),
    schema='orig_osm'
)

t_osm_deu_polygon_buildings_view = Table(
    'osm_deu_polygon_buildings_view', metadata,
    Column('osm_id', BigInteger),
    Column('access', Text),
    Column('addr:housename', Text),
    Column('addr:housenumber', Text),
    Column('addr:interpolation', Text),
    Column('admin_level', Text),
    Column('aerialway', Text),
    Column('aeroway', Text),
    Column('amenity', Text),
    Column('area', Text),
    Column('barrier', Text),
    Column('bicycle', Text),
    Column('brand', Text),
    Column('bridge', Text),
    Column('boundary', Text),
    Column('building', Text),
    Column('construction', Text),
    Column('covered', Text),
    Column('culvert', Text),
    Column('cutting', Text),
    Column('denomination', Text),
    Column('disused', Text),
    Column('embankment', Text),
    Column('foot', Text),
    Column('generator:source', Text),
    Column('harbour', Text),
    Column('highway', Text),
    Column('historic', Text),
    Column('horse', Text),
    Column('intermittent', Text),
    Column('junction', Text),
    Column('landuse', Text),
    Column('layer', Text),
    Column('leisure', Text),
    Column('lock', Text),
    Column('man_made', Text),
    Column('military', Text),
    Column('motorcar', Text),
    Column('name', Text),
    Column('natural', Text),
    Column('office', Text),
    Column('oneway', Text),
    Column('operator', Text),
    Column('place', Text),
    Column('population', Text),
    Column('power', Text),
    Column('power_source', Text),
    Column('public_transport', Text),
    Column('railway', Text),
    Column('ref', Text),
    Column('religion', Text),
    Column('route', Text),
    Column('service', Text),
    Column('shop', Text),
    Column('sport', Text),
    Column('surface', Text),
    Column('toll', Text),
    Column('tourism', Text),
    Column('tower:type', Text),
    Column('tracktype', Text),
    Column('tunnel', Text),
    Column('water', Text),
    Column('waterway', Text),
    Column('wetland', Text),
    Column('width', Text),
    Column('wood', Text),
    Column('z_order', Integer),
    Column('way_area', Float),
    Column('tags', HSTORE),
    Column('geom', Geometry('MULTIPOLYGON', 3857)),
    Column('gid', Integer),
    schema='orig_osm'
)

t_osm_deu_polygon_error_geom_mview = Table(
    'osm_deu_polygon_error_geom_mview', metadata,
    Column('id', Integer),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    schema='orig_osm'
)

t_osm_deu_polygon_landuse_view = Table(
    'osm_deu_polygon_landuse_view', metadata,
    Column('osm_id', BigInteger),
    Column('access', Text),
    Column('addr:housename', Text),
    Column('addr:housenumber', Text),
    Column('addr:interpolation', Text),
    Column('admin_level', Text),
    Column('aerialway', Text),
    Column('aeroway', Text),
    Column('amenity', Text),
    Column('area', Text),
    Column('barrier', Text),
    Column('bicycle', Text),
    Column('brand', Text),
    Column('bridge', Text),
    Column('boundary', Text),
    Column('building', Text),
    Column('construction', Text),
    Column('covered', Text),
    Column('culvert', Text),
    Column('cutting', Text),
    Column('denomination', Text),
    Column('disused', Text),
    Column('embankment', Text),
    Column('foot', Text),
    Column('generator:source', Text),
    Column('harbour', Text),
    Column('highway', Text),
    Column('historic', Text),
    Column('horse', Text),
    Column('intermittent', Text),
    Column('junction', Text),
    Column('landuse', Text),
    Column('layer', Text),
    Column('leisure', Text),
    Column('lock', Text),
    Column('man_made', Text),
    Column('military', Text),
    Column('motorcar', Text),
    Column('name', Text),
    Column('natural', Text),
    Column('office', Text),
    Column('oneway', Text),
    Column('operator', Text),
    Column('place', Text),
    Column('population', Text),
    Column('power', Text),
    Column('power_source', Text),
    Column('public_transport', Text),
    Column('railway', Text),
    Column('ref', Text),
    Column('religion', Text),
    Column('route', Text),
    Column('service', Text),
    Column('shop', Text),
    Column('sport', Text),
    Column('surface', Text),
    Column('toll', Text),
    Column('tourism', Text),
    Column('tower:type', Text),
    Column('tracktype', Text),
    Column('tunnel', Text),
    Column('water', Text),
    Column('waterway', Text),
    Column('wetland', Text),
    Column('width', Text),
    Column('wood', Text),
    Column('z_order', Integer),
    Column('way_area', Float),
    Column('tags', HSTORE),
    Column('geom', Geometry('MULTIPOLYGON', 3857)),
    Column('gid', Integer),
    schema='orig_osm'
)

t_osm_deu_polygon_nature_view = Table(
    'osm_deu_polygon_nature_view', metadata,
    Column('osm_id', BigInteger),
    Column('access', Text),
    Column('addr:housename', Text),
    Column('addr:housenumber', Text),
    Column('addr:interpolation', Text),
    Column('admin_level', Text),
    Column('aerialway', Text),
    Column('aeroway', Text),
    Column('amenity', Text),
    Column('area', Text),
    Column('barrier', Text),
    Column('bicycle', Text),
    Column('brand', Text),
    Column('bridge', Text),
    Column('boundary', Text),
    Column('building', Text),
    Column('construction', Text),
    Column('covered', Text),
    Column('culvert', Text),
    Column('cutting', Text),
    Column('denomination', Text),
    Column('disused', Text),
    Column('embankment', Text),
    Column('foot', Text),
    Column('generator:source', Text),
    Column('harbour', Text),
    Column('highway', Text),
    Column('historic', Text),
    Column('horse', Text),
    Column('intermittent', Text),
    Column('junction', Text),
    Column('landuse', Text),
    Column('layer', Text),
    Column('leisure', Text),
    Column('lock', Text),
    Column('man_made', Text),
    Column('military', Text),
    Column('motorcar', Text),
    Column('name', Text),
    Column('natural', Text),
    Column('office', Text),
    Column('oneway', Text),
    Column('operator', Text),
    Column('place', Text),
    Column('population', Text),
    Column('power', Text),
    Column('power_source', Text),
    Column('public_transport', Text),
    Column('railway', Text),
    Column('ref', Text),
    Column('religion', Text),
    Column('route', Text),
    Column('service', Text),
    Column('shop', Text),
    Column('sport', Text),
    Column('surface', Text),
    Column('toll', Text),
    Column('tourism', Text),
    Column('tower:type', Text),
    Column('tracktype', Text),
    Column('tunnel', Text),
    Column('water', Text),
    Column('waterway', Text),
    Column('wetland', Text),
    Column('width', Text),
    Column('wood', Text),
    Column('z_order', Integer),
    Column('way_area', Float),
    Column('tags', HSTORE),
    Column('geom', Geometry('MULTIPOLYGON', 3857)),
    Column('gid', Integer),
    schema='orig_osm'
)

t_osm_deu_polygon_population_view = Table(
    'osm_deu_polygon_population_view', metadata,
    Column('osm_id', BigInteger),
    Column('access', Text),
    Column('addr:housename', Text),
    Column('addr:housenumber', Text),
    Column('addr:interpolation', Text),
    Column('admin_level', Text),
    Column('aerialway', Text),
    Column('aeroway', Text),
    Column('amenity', Text),
    Column('area', Text),
    Column('barrier', Text),
    Column('bicycle', Text),
    Column('brand', Text),
    Column('bridge', Text),
    Column('boundary', Text),
    Column('building', Text),
    Column('construction', Text),
    Column('covered', Text),
    Column('culvert', Text),
    Column('cutting', Text),
    Column('denomination', Text),
    Column('disused', Text),
    Column('embankment', Text),
    Column('foot', Text),
    Column('generator:source', Text),
    Column('harbour', Text),
    Column('highway', Text),
    Column('historic', Text),
    Column('horse', Text),
    Column('intermittent', Text),
    Column('junction', Text),
    Column('landuse', Text),
    Column('layer', Text),
    Column('leisure', Text),
    Column('lock', Text),
    Column('man_made', Text),
    Column('military', Text),
    Column('motorcar', Text),
    Column('name', Text),
    Column('natural', Text),
    Column('office', Text),
    Column('oneway', Text),
    Column('operator', Text),
    Column('place', Text),
    Column('population', Text),
    Column('power', Text),
    Column('power_source', Text),
    Column('public_transport', Text),
    Column('railway', Text),
    Column('ref', Text),
    Column('religion', Text),
    Column('route', Text),
    Column('service', Text),
    Column('shop', Text),
    Column('sport', Text),
    Column('surface', Text),
    Column('toll', Text),
    Column('tourism', Text),
    Column('tower:type', Text),
    Column('tracktype', Text),
    Column('tunnel', Text),
    Column('water', Text),
    Column('waterway', Text),
    Column('wetland', Text),
    Column('width', Text),
    Column('wood', Text),
    Column('z_order', Integer),
    Column('way_area', Float),
    Column('tags', HSTORE),
    Column('geom', Geometry('MULTIPOLYGON', 3857)),
    Column('gid', Integer),
    schema='orig_osm'
)

t_osm_deu_polygon_power_substation_industrial_view = Table(
    'osm_deu_polygon_power_substation_industrial_view', metadata,
    Column('osm_id', BigInteger),
    Column('access', Text),
    Column('addr:housename', Text),
    Column('addr:housenumber', Text),
    Column('addr:interpolation', Text),
    Column('admin_level', Text),
    Column('aerialway', Text),
    Column('aeroway', Text),
    Column('amenity', Text),
    Column('area', Text),
    Column('barrier', Text),
    Column('bicycle', Text),
    Column('brand', Text),
    Column('bridge', Text),
    Column('boundary', Text),
    Column('building', Text),
    Column('construction', Text),
    Column('covered', Text),
    Column('culvert', Text),
    Column('cutting', Text),
    Column('denomination', Text),
    Column('disused', Text),
    Column('embankment', Text),
    Column('foot', Text),
    Column('generator:source', Text),
    Column('harbour', Text),
    Column('highway', Text),
    Column('historic', Text),
    Column('horse', Text),
    Column('intermittent', Text),
    Column('junction', Text),
    Column('landuse', Text),
    Column('layer', Text),
    Column('leisure', Text),
    Column('lock', Text),
    Column('man_made', Text),
    Column('military', Text),
    Column('motorcar', Text),
    Column('name', Text),
    Column('natural', Text),
    Column('office', Text),
    Column('oneway', Text),
    Column('operator', Text),
    Column('place', Text),
    Column('population', Text),
    Column('power', Text),
    Column('power_source', Text),
    Column('public_transport', Text),
    Column('railway', Text),
    Column('ref', Text),
    Column('religion', Text),
    Column('route', Text),
    Column('service', Text),
    Column('shop', Text),
    Column('sport', Text),
    Column('surface', Text),
    Column('toll', Text),
    Column('tourism', Text),
    Column('tower:type', Text),
    Column('tracktype', Text),
    Column('tunnel', Text),
    Column('water', Text),
    Column('waterway', Text),
    Column('wetland', Text),
    Column('width', Text),
    Column('wood', Text),
    Column('z_order', Integer),
    Column('way_area', Float),
    Column('tags', HSTORE),
    Column('geom', Geometry('MULTIPOLYGON', 3857)),
    Column('gid', Integer),
    schema='orig_osm'
)


class OsmDeuPolygonUrban(Base):
    __tablename__ = 'osm_deu_polygon_urban'
    __table_args__ = {'schema': 'orig_osm'}

    gid = Column(Integer, primary_key=True)
    osm_id = Column(Integer)
    landuse = Column(Text)
    man_made = Column(Text)
    aeroway = Column(Text)
    name = Column(Text)
    way_area = Column(Float(53))
    area_ha = Column(Float(53))
    tags = Column(HSTORE)
    vg250 = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_osm_deu_polygon_urban_buffer100_mview = Table(
    'osm_deu_polygon_urban_buffer100_mview', metadata,
    Column('id', Integer, unique=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='orig_osm'
)

t_osm_deu_polygon_urban_error_geom_mview = Table(
    'osm_deu_polygon_urban_error_geom_mview', metadata,
    Column('id', Integer),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    schema='orig_osm'
)

t_osm_deu_polygon_urban_error_geom_vg250_mview = Table(
    'osm_deu_polygon_urban_error_geom_vg250_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('landuse', Text),
    Column('man_made', Text),
    Column('aeroway', Text),
    Column('name', Text),
    Column('way_area', Float(53)),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_osm'
)

t_osm_deu_polygon_urban_sector_1_residential_mview = Table(
    'osm_deu_polygon_urban_sector_1_residential_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('landuse', Text),
    Column('man_made', Text),
    Column('aeroway', Text),
    Column('name', Text),
    Column('way_area', Float(53)),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_osm'
)

t_osm_deu_polygon_urban_sector_2_retail_mview = Table(
    'osm_deu_polygon_urban_sector_2_retail_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('landuse', Text),
    Column('man_made', Text),
    Column('aeroway', Text),
    Column('name', Text),
    Column('way_area', Float(53)),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_osm'
)

t_osm_deu_polygon_urban_sector_3_industrial_mview = Table(
    'osm_deu_polygon_urban_sector_3_industrial_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('landuse', Text),
    Column('man_made', Text),
    Column('aeroway', Text),
    Column('name', Text),
    Column('way_area', Float(53)),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_osm'
)

t_osm_deu_polygon_urban_sector_4_agricultural_mview = Table(
    'osm_deu_polygon_urban_sector_4_agricultural_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('landuse', Text),
    Column('man_made', Text),
    Column('aeroway', Text),
    Column('name', Text),
    Column('way_area', Float(53)),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_osm'
)

t_osm_deu_polygon_urban_sector_4_agricultural_mview_error_geom_vi = Table(
    'osm_deu_polygon_urban_sector_4_agricultural_mview_error_geom_vi', metadata,
    Column('id', Integer),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    schema='orig_osm'
)

t_osm_deu_polygon_urban_vg250_clean_cut_multi_mview = Table(
    'osm_deu_polygon_urban_vg250_clean_cut_multi_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('landuse', Text),
    Column('man_made', Text),
    Column('aeroway', Text),
    Column('name', Text),
    Column('way_area', Float(53)),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_osm'
)

t_osm_deu_polygon_urban_vg250_clean_cut_mview = Table(
    'osm_deu_polygon_urban_vg250_clean_cut_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('landuse', Text),
    Column('man_made', Text),
    Column('aeroway', Text),
    Column('name', Text),
    Column('way_area', Float(53)),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE),
    Column('vg250', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035)),
    schema='orig_osm'
)

t_osm_deu_polygon_urban_vg250_cut_mview = Table(
    'osm_deu_polygon_urban_vg250_cut_mview', metadata,
    Column('id', Integer),
    Column('gid', Integer, unique=True),
    Column('osm_id', Integer),
    Column('landuse', Text),
    Column('man_made', Text),
    Column('aeroway', Text),
    Column('name', Text),
    Column('way_area', Float(53)),
    Column('area_ha', Float(53)),
    Column('tags', HSTORE),
    Column('vg250', Text),
    Column('geom_type', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='orig_osm'
)


class OsmDeuRel(Base):
    __tablename__ = 'osm_deu_rels'
    __table_args__ = {'schema': 'orig_osm'}

    id = Column(BigInteger, primary_key=True, index=True)
    way_off = Column(SmallInteger)
    rel_off = Column(SmallInteger)
    parts = Column(ARRAY(BIGINT()), index=True)
    members = Column(ARRAY(TEXT()))
    tags = Column(ARRAY(TEXT()))
    pending = Column(Boolean, nullable=False)


class OsmDeuRoad(Base):
    __tablename__ = 'osm_deu_roads'
    __table_args__ = {'schema': 'orig_osm'}

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
    tags = Column(HSTORE, index=True)
    geom = Column(Geometry('LINESTRING', 3857), index=True)
    gid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_osm.osm_deu_roads_gid_seq'::regclass)"))


class OsmDeuSubstationsEhv(Base):
    __tablename__ = 'osm_deu_substations_ehv'
    __table_args__ = {'schema': 'orig_osm'}

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
    dbahn = Column(Text)
    status = Column(SmallInteger)
    visible = Column(SmallInteger)
    geom = Column(Geometry('POINT', 4326), nullable=False)
    subst_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_osm.osm_deu_substations_ehv_subst_id_seq'::regclass)"))


class OsmDeuWay(Base):
    __tablename__ = 'osm_deu_ways'
    __table_args__ = {'schema': 'orig_osm'}

    id = Column(BigInteger, primary_key=True, index=True)
    nodes = Column(ARRAY(BIGINT()), nullable=False, index=True)
    tags = Column(ARRAY(TEXT()))
    pending = Column(Boolean, nullable=False)

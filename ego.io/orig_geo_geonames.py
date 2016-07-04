# coding: utf-8
from sqlalchemy import Column, MetaData, Numeric, String, Table
from geoalchemy2.types import Geometry


metadata = MetaData()


t_postcode_germany = Table(
    'postcode_germany', metadata,
    Column('country_code', String(2)),
    Column('postalcode', String(20)),
    Column('placename', String(180)),
    Column('adminname1', String(100)),
    Column('admincode1', String(20)),
    Column('adminname2', String(100)),
    Column('admincode2', String(20)),
    Column('adminname3', String(100)),
    Column('admincode3', String(20)),
    Column('latitude', Numeric),
    Column('longitude', Numeric),
    Column('geom', Geometry('POINT', 4326), index=True),
    schema='orig_geo_geonames'
)

# coding: utf-8
from sqlalchemy import Column, DateTime, Integer
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class EgoDeuMvGridsVi(Base):
    __tablename__ = 'ego_deu_mv_grids_vis'
    __table_args__ = {'schema': 'calc_ego_grid'}

    grid_id = Column(Integer, primary_key=True, nullable=False)
    timestamp = Column(DateTime(True), primary_key=True, nullable=False)
    geom_mv_station = Column(Geometry('POINT', 4326))
    geom_mv_cable_dist = Column(Geometry('MULTIPOINT', 4326))
    geom_lv_stations = Column(Geometry('MULTIPOINT', 4326))
    geom_mv_lines = Column(Geometry('MULTILINESTRING', 4326))

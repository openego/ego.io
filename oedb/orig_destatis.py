# coding: utf-8
from sqlalchemy import BigInteger, Column, ForeignKey, Integer, Numeric, String, \
    Table, Text, text
from sqlalchemy.orm import relationship
from geoalchemy2.types import Geometry, Raster
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BbsrRagCityAndMunTypesPerMun(Base):
    __tablename__ = 'bbsr_rag_city_and_mun_types_per_mun'
    __table_args__ = {'schema': 'orig_destatis'}

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


class BbsrRagMunicipalityAndMunicipalAssociation(Base):
    __tablename__ = 'bbsr_rag_municipality_and_municipal_association'
    __table_args__ = {'schema': 'orig_destatis'}

    mun_id = Column(BigInteger, primary_key=True)
    mun_name = Column(Text)
    munassn_id = Column(BigInteger)
    munassn_name = Column(Text)
    munassn_location = Column(Text)
    area_sqm = Column(Numeric(5, 2))
    pop_2013 = Column(Integer)


class BbsrRagSpatialTypesPerMun(Base):
    __tablename__ = 'bbsr_rag_spatial_types_per_mun'
    __table_args__ = {'schema': 'orig_destatis'}

    mun_id = Column(BigInteger, primary_key=True)
    mun_name = Column(Text)
    munassn_id = Column(BigInteger)
    munassn_name = Column(Text)
    sp_typ_pop = Column(ForeignKey(
        'orig_destatis.bbsr_rag_spatial_types_per_mun_key_pop.sp_typ_pop'))
    sp_typ_loc = Column(ForeignKey(
        'orig_destatis.bbsr_rag_spatial_types_per_mun_key_loc.sp_typ_loc'))

    bbsr_rag_spatial_types_per_mun_key_loc = relationship(
        'BbsrRagSpatialTypesPerMunKeyLoc')
    bbsr_rag_spatial_types_per_mun_key_pop = relationship(
        'BbsrRagSpatialTypesPerMunKeyPop')


class BbsrRagSpatialTypesPerMunKeyLoc(Base):
    __tablename__ = 'bbsr_rag_spatial_types_per_mun_key_loc'
    __table_args__ = {'schema': 'orig_destatis'}

    sp_typ_loc = Column(Integer, primary_key=True)
    sp_typ_loc_name = Column(Text)
    sp_typ_loc_name_ger = Column(Text)


class BbsrRagSpatialTypesPerMunKeyPop(Base):
    __tablename__ = 'bbsr_rag_spatial_types_per_mun_key_pop'
    __table_args__ = {'schema': 'orig_destatis'}

    sp_typ_pop = Column(Integer, primary_key=True)
    sp_typ_pop_name = Column(Text)
    sp_typ_pop_name_ger = Column(Text)


class BbsrRop2035PopForecastByAgegroupsPerDist(Base):
    __tablename__ = 'bbsr_rop2035_pop_forecast_by_agegroups_per_dist'
    __table_args__ = {'schema': 'orig_destatis'}

    district_id = Column(BigInteger, primary_key=True, nullable=False)
    district_name = Column(Text)
    age_group = Column(Text, primary_key=True, nullable=False)
    pop_2012 = Column(Integer)
    pop_2013 = Column(Integer)
    pop_2014 = Column(Integer)
    pop_2015 = Column(Integer)
    pop_2016 = Column(Integer)
    pop_2017 = Column(Integer)
    pop_2018 = Column(Integer)
    pop_2019 = Column(Integer)
    pop_2020 = Column(Integer)
    pop_2021 = Column(Integer)
    pop_2022 = Column(Integer)
    pop_2023 = Column(Integer)
    pop_2024 = Column(Integer)
    pop_2025 = Column(Integer)
    pop_2026 = Column(Integer)
    pop_2027 = Column(Integer)
    pop_2028 = Column(Integer)
    pop_2029 = Column(Integer)
    pop_2030 = Column(Integer)
    pop_2031 = Column(Integer)
    pop_2032 = Column(Integer)
    pop_2033 = Column(Integer)
    pop_2034 = Column(Integer)
    pop_2035 = Column(Integer)


class BbsrRop2035PopForecastTotalPerDist(Base):
    __tablename__ = 'bbsr_rop2035_pop_forecast_total_per_dist'
    __table_args__ = {'schema': 'orig_destatis'}

    district_id = Column(BigInteger, primary_key=True)
    district_name = Column(Text)
    age_group = Column(Text)
    pop_2012 = Column(Integer)
    pop_2013 = Column(Integer)
    pop_2014 = Column(Integer)
    pop_2015 = Column(Integer)
    pop_2016 = Column(Integer)
    pop_2017 = Column(Integer)
    pop_2018 = Column(Integer)
    pop_2019 = Column(Integer)
    pop_2020 = Column(Integer)
    pop_2021 = Column(Integer)
    pop_2022 = Column(Integer)
    pop_2023 = Column(Integer)
    pop_2024 = Column(Integer)
    pop_2025 = Column(Integer)
    pop_2026 = Column(Integer)
    pop_2027 = Column(Integer)
    pop_2028 = Column(Integer)
    pop_2029 = Column(Integer)
    pop_2030 = Column(Integer)
    pop_2031 = Column(Integer)
    pop_2032 = Column(Integer)
    pop_2033 = Column(Integer)
    pop_2034 = Column(Integer)
    pop_2035 = Column(Integer)


class GenesisBldgWithHousingAndFlatsByBldgTypePerMun(Base):
    __tablename__ = 'genesis_bldg_with_housing_and_flats_by_bldg_type_per_mun'
    __table_args__ = {'schema': 'orig_destatis'}

    mun_id = Column(BigInteger, primary_key=True)
    mun_name = Column(Text)
    bldg_housing_total = Column(Integer)
    bldg_housing_house = Column(Integer)
    bldg_housing_reshome = Column(Integer)
    bldg_housing_other = Column(Integer)
    flat_housing_total = Column(Integer)
    flat_housing_house = Column(Integer)
    flat_housing_reshome = Column(Integer)
    flat_housing_other = Column(Integer)


class GenesisBldgWithHousingByNumberFlatsPerMun(Base):
    __tablename__ = 'genesis_bldg_with_housing_by_number_flats_per_mun'
    __table_args__ = {'schema': 'orig_destatis'}

    mun_id = Column(BigInteger, primary_key=True)
    mun_name = Column(Text)
    bldg_housing_total = Column(Integer)
    bldg_housing_flat_1 = Column(Integer)
    bldg_housing_flat_2 = Column(Integer)
    bldg_housing_flat_3_6 = Column('bldg_housing_flat_3-6', Integer)
    bldg_housing_flat_7_12 = Column('bldg_housing_flat_7-12', Integer)
    bldg_housing_flat_13_ = Column('bldg_housing_flat_13-', Integer)


class GenesisFlatsByLivingSpaceClassesPerMun(Base):
    __tablename__ = 'genesis_flats_by_living_space_classes_per_mun'
    __table_args__ = {'schema': 'orig_destatis'}

    mun_id = Column(BigInteger, primary_key=True)
    mun_name = Column(Text)
    flats_total = Column(Integer)
    flats_0_40 = Column('flats_0-40', Integer)
    flats_40_59 = Column('flats_40-59', Integer)
    flats_60_79 = Column('flats_60-79', Integer)
    flats_80_99 = Column('flats_80-99', Integer)
    flats_100_119 = Column('flats_100-119', Integer)
    flats_120_139 = Column('flats_120-139', Integer)
    flats_140_159 = Column('flats_140-159', Integer)
    flats_160_179 = Column('flats_160-179', Integer)
    flats_180_199 = Column('flats_180-199', Integer)
    flats_200_ = Column('flats_200-', Integer)


class GenesisPopDevByGenderPerMun(Base):
    __tablename__ = 'genesis_pop_dev_by_gender_per_mun'
    __table_args__ = {'schema': 'orig_destatis'}

    mun_id = Column(BigInteger, primary_key=True)
    mun_name = Column(Text)
    pop_2013_total = Column(Integer)
    pop_2013_male = Column(Integer)
    pop_2013_female = Column(Integer)
    pop_2012_total = Column(Integer)
    pop_2012_male = Column(Integer)
    pop_2012_female = Column(Integer)
    pop_2011_total = Column(Integer)
    pop_2011_male = Column(Integer)
    pop_2011_female = Column(Integer)
    pop_2010_total = Column(Integer)
    pop_2010_male = Column(Integer)
    pop_2010_female = Column(Integer)
    pop_2009_total = Column(Integer)
    pop_2009_male = Column(Integer)
    pop_2009_female = Column(Integer)
    pop_2008_total = Column(Integer)
    pop_2008_male = Column(Integer)
    pop_2008_female = Column(Integer)


class GenesisResidentialBldgByNumberFlatsPerMun(Base):
    __tablename__ = 'genesis_residential_bldg_by_number_flats_per_mun'
    __table_args__ = {'schema': 'orig_destatis'}

    mun_id = Column(BigInteger, primary_key=True)
    mun_name = Column(Text)
    r_bldg_total = Column(Integer)
    r_bldg_flat_1 = Column(Integer)
    r_bldg_flat_2 = Column(Integer)
    r_bldg_flat_3_6 = Column('r_bldg_flat_3-6', Integer)
    r_bldg_flat_7_12 = Column('r_bldg_flat_7-12', Integer)
    r_bldg_flat_13_ = Column('r_bldg_flat_13-', Integer)


class ZensusPopulationByGenderPerMun(Base):
    __tablename__ = 'zensus_population_by_gender_per_mun'
    __table_args__ = {'schema': 'orig_destatis'}

    state_id = Column(Integer)
    state_name = Column(Text)
    mun_id = Column(Integer, primary_key=True)
    mun_name = Column(Text)
    population = Column(Integer)
    pop_male = Column(Integer)
    pop_female = Column(Integer)
    population_old = Column(Integer)
    pop_male_old = Column(Integer)
    pop_female_old = Column(Integer)
    pop_diff = Column(Integer)
    pop_pct = Column(Numeric(4, 1))


class ZensusPopulationPerHa(Base):
    __tablename__ = 'zensus_population_per_ha'
    __table_args__ = {'schema': 'orig_destatis'}

    gid = Column(Integer, primary_key=True)
    grid_id = Column(String(254), nullable=False)
    x_mp = Column(Numeric(10, 0))
    y_mp = Column(Numeric(10, 0))
    population = Column(Numeric(10, 0), index=True)
    geom = Column(Geometry('POINT', 3035), index=True)


class ZensusPopulationPerHaGrid(Base):
    __tablename__ = 'zensus_population_per_ha_grid'
    __table_args__ = {'schema': 'orig_destatis'}

    gid = Column(Integer, primary_key=True)
    grid_id = Column(String(254), nullable=False)
    x_mp = Column(Numeric(10, 0))
    y_mp = Column(Numeric(10, 0))
    population = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class ZensusPopulationPerHaGridCluster(Base):
    __tablename__ = 'zensus_population_per_ha_grid_cluster'
    __table_args__ = {'schema': 'orig_destatis'}

    cid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_destatis.zensus_population_per_ha_grid_cluster_cid_seq'::regclass)"))
    population_sum = Column(Integer)
    area_ha = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_pts = Column(Geometry('MULTIPOINT', 3035), index=True)


t_zensus_population_per_ha_mview = Table(
    'zensus_population_per_ha_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('population', Numeric(10, 0)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='orig_destatis'
)


class ZensusPopulationPerHaRaster(Base):
    __tablename__ = 'zensus_population_per_ha_raster'
    __table_args__ = {'schema': 'orig_destatis'}

    rid = Column(Integer, primary_key=True)
    rast = Column(Raster)


class ZensusPopulationPerHaRasterTile100(Base):
    __tablename__ = 'zensus_population_per_ha_raster_tile100'
    __table_args__ = {'schema': 'orig_destatis'}

    rid = Column(Integer, primary_key=True, server_default=text(
        "nextval('orig_destatis.zensus_population_per_ha_raster_tile100_rid_seq'::regclass)"))
    rast = Column(Raster)


class ZensusStat(Base):
    __tablename__ = 'zensus_stats'
    __table_args__ = {'schema': 'orig_destatis'}

    scale = Column(Text, primary_key=True)
    summe_einwohner = Column(Numeric)
    anzahl_zellen = Column(BigInteger)


t_zensus_stats_view = Table(
    'zensus_stats_view', metadata,
    Column('summe_einwohner', Numeric),
    Column('anzahl_zellen', BigInteger),
    schema='orig_destatis'
)

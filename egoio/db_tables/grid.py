# coding: utf-8
from sqlalchemy import ARRAY, BigInteger, Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, Numeric, SmallInteger, String, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, JSON


Base = declarative_base()
metadata = Base.metadata


class BnetzaVorhabenBbplg(Base):
    __tablename__ = 'bnetza_vorhaben_bbplg'
    __table_args__ = {'schema': 'grid'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('grid.bnetza_vorhaben_bbplg_id_seq'::regclass)"))
    geom = Column(Geometry('MULTILINESTRING', 5652), index=True)
    object_id = Column(BigInteger)
    rechtsgrundlage = Column(String(5))
    vorhabennummer = Column(Integer)
    nova = Column(String(20))
    vorhabenbezeichnung = Column(String(200))
    zustaendigkeit = Column(String(4))
    technik = Column(String(2))
    abschnitt = Column(String(5))
    anfangspunkt = Column(String(50))
    endpunkt = Column(String(50))
    abschnittsbezeichnung = Column(String(150))
    art_der_geometrie = Column(String(20))
    status_der_geometrie = Column(String(20))
    luftlinie_km = Column(Float(53))
    erdkabelvorrang = Column(String(4))
    erdkabelpilot = Column(String(4))
    kennzeichnung = Column(String(10))
    kennzeichnung_a1 = Column(String(3))
    kennzeichnung_a2 = Column(String(3))
    kennzeichnung_b = Column(String(3))
    kennzeichnung_c = Column(String(3))
    kennzeichnung_d = Column(String(3))
    kennzeichnung_e = Column(String(3))
    kennzeichnung_f = Column(String(3))
    kennzeichnung_strich = Column(String(3))
    stand_des_vorhabens = Column(String(100))
    id_a = Column(String(10))
    vgi = Column(String(10))
    vgi_nr = Column(String(15))
    vorhabentraeger = Column(String(50))
    spannung = Column(String(20))
    shape_length = Column(Float(53))
    bezugsmassstab = Column(String(50))
    hinweis = Column(String(150))


class BnetzaVorhabenEnlag(Base):
    __tablename__ = 'bnetza_vorhaben_enlag'
    __table_args__ = {'schema': 'grid'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('grid.bnetza_vorhaben_enlag_id_seq'::regclass)"))
    geom = Column(Geometry('MULTILINESTRING', 5652), index=True)
    object_id = Column(BigInteger)
    rechtsgrundlage = Column(String(5))
    vorhabennummer = Column(Integer)
    nova = Column(String(20))
    vorhabenbezeichnung = Column(String(200))
    zustaendigkeit = Column(String(4))
    technik = Column(String(2))
    abschnitt = Column(String(5))
    anfangspunkt = Column(String(50))
    endpunkt = Column(String(50))
    abschnittsbezeichnung = Column(String(150))
    art_der_geometrie = Column(String(20))
    status_der_geometrie = Column(String(20))
    erdkabelvorrang = Column(String(4))
    erdkabelpilot = Column(String(4))
    kennzeichnung = Column(String(10))
    kennzeichnung_a1 = Column(String(3))
    kennzeichnung_a2 = Column(String(3))
    kennzeichnung_b = Column(String(3))
    kennzeichnung_c = Column(String(3))
    kennzeichnung_d = Column(String(3))
    kennzeichnung_e = Column(String(3))
    kennzeichnung_f = Column(String(3))
    kennzeichnung_strich = Column(String(3))
    stand_des_vorhabens = Column(String(100))
    id_a = Column(String(10))
    vgi = Column(String(10))
    vgi_nr = Column(String(15))
    vorhabentraeger = Column(String(50))
    spannung = Column(String(20))
    shape_length = Column(Float(53))
    bezugsmassstab = Column(String(50))
    hinweis = Column(String(150))


class BnetzaVorhabenpunkteBbplg(Base):
    __tablename__ = 'bnetza_vorhabenpunkte_bbplg'
    __table_args__ = {'schema': 'grid'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('grid.bnetza_vorhabenpunkte_bbplg_id_seq'::regclass)"))
    geom = Column(Geometry('POINT', 4647), index=True)
    object_id = Column(BigInteger)
    name = Column(String(50))


class BnetzaVorhabenpunkteEnlag(Base):
    __tablename__ = 'bnetza_vorhabenpunkte_enlag'
    __table_args__ = {'schema': 'grid'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('grid.bnetza_vorhabenpunkte_enlag_id_seq'::regclass)"))
    geom = Column(Geometry('POINT', 4647), index=True)
    object_id = Column(BigInteger)
    name = Column(String(50))


class EgoDpEhvGriddistrict(Base):
    __tablename__ = 'ego_dp_ehv_griddistrict'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    geom = Column(Geometry('POLYGON', 4326), index=True)
    subst_id = Column(Integer, primary_key=True, nullable=False)


class EgoDpEhvSubstation(Base):
    __tablename__ = 'ego_dp_ehv_substation'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    subst_id = Column(Integer, primary_key=True, nullable=False)
    lon = Column(Float(53))
    lat = Column(Float(53))
    point = Column(Geometry('POINT', 4326), index=True)
    polygon = Column(Geometry)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text)
    osm_www = Column(Text)
    frequency = Column(Text)
    subst_name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger)
    otg_id = Column(BigInteger)


class EgoDpHvmvSubstation(Base):
    __tablename__ = 'ego_dp_hvmv_substation'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    subst_id = Column(Integer, primary_key=True, nullable=False)
    lon = Column(Float(53))
    lat = Column(Float(53))
    point = Column(Geometry('POINT', 4326))
    polygon = Column(Geometry)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text)
    osm_www = Column(Text)
    frequency = Column(Text)
    subst_name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger)
    otg_id = Column(BigInteger)
    ags_0 = Column(Text)
    geom = Column(Geometry('POINT', 3035), index=True)


class EgoDpLvGriddistrict(Base):
    __tablename__ = 'ego_dp_lv_griddistrict'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    mvlv_subst_id = Column(Integer)
    subst_id = Column(Integer)
    la_id = Column(Integer)
    nn = Column(Boolean)
    subst_cnt = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Float(53))
    population_density = Column(Float(53))
    area_ha = Column(Float(53))
    sector_area_residential = Column(Float(53))
    sector_area_retail = Column(Float(53))
    sector_area_industrial = Column(Float(53))
    sector_area_agricultural = Column(Float(53))
    sector_area_sum = Column(Float(53))
    sector_share_residential = Column(Float(53))
    sector_share_retail = Column(Float(53))
    sector_share_industrial = Column(Float(53))
    sector_share_agricultural = Column(Float(53))
    sector_share_sum = Column(Float(53))
    sector_count_residential = Column(Integer)
    sector_count_retail = Column(Integer)
    sector_count_industrial = Column(Integer)
    sector_count_agricultural = Column(Integer)
    sector_count_sum = Column(Integer)
    sector_consumption_residential = Column(Float(53))
    sector_consumption_retail = Column(Float(53))
    sector_consumption_industrial = Column(Float(53))
    sector_consumption_agricultural = Column(Float(53))
    sector_consumption_sum = Column(Float(53))
    sector_peakload_residential = Column(Float(53))
    sector_peakload_retail = Column(Float(53))
    sector_peakload_industrial = Column(Float(53))
    sector_peakload_agricultural = Column(Float(53))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoDpMvGriddistrict(Base):
    __tablename__ = 'ego_dp_mv_griddistrict'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    subst_id = Column(Integer, primary_key=True, nullable=False)
    subst_sum = Column(Integer)
    type1 = Column(Integer)
    type1_cnt = Column(Integer)
    type2 = Column(Integer)
    type2_cnt = Column(Integer)
    type3 = Column(Integer)
    type3_cnt = Column(Integer)
    group = Column(String(1))
    gem = Column(Integer)
    gem_clean = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    population_density = Column(Numeric)
    la_count = Column(Integer)
    area_ha = Column(Numeric)
    la_area = Column(Numeric(10, 1))
    free_area = Column(Numeric(10, 1))
    area_share = Column(Numeric(4, 1))
    consumption = Column(Numeric)
    consumption_per_area = Column(Numeric)
    dea_cnt = Column(Integer)
    dea_capacity = Column(Numeric)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)
    mv_dea_cnt = Column(Integer)
    mv_dea_capacity = Column(Numeric)
    geom_type = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoDpMvlvSubstation(Base):
    __tablename__ = 'ego_dp_mvlv_substation'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    mvlv_subst_id = Column(Integer, primary_key=True, nullable=False)
    la_id = Column(Integer)
    subst_id = Column(Integer)
    geom = Column(Geometry('POINT', 3035), index=True)
    is_dummy = Column(Boolean)
    subst_cnt = Column(Integer)


class EgoPfHvBus(Base):
    __tablename__ = 'ego_pf_hv_bus'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    current_type = Column(Text, server_default=text("'AC'::text"))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326), index=True)


class EgoPfHvGenerator(Base):
    __tablename__ = 'ego_pf_hv_generator'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    dispatch = Column(Text, server_default=text("'flexible'::text"))
    control = Column(Text, server_default=text("'PQ'::text"))
    p_nom = Column(Float(53), server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    p_min_pu_fixed = Column(Float(53), server_default=text("0"))
    p_max_pu_fixed = Column(Float(53), server_default=text("1"))
    sign = Column(Float(53), server_default=text("1"))
    source = Column(BigInteger)
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))


class EgoPfHvGeneratorPqSet(Base):
    __tablename__ = 'ego_pf_hv_generator_pq_set'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(String(25), primary_key=True, nullable=False)
    temp_id = Column(Integer, primary_key=True, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_min_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_max_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))


class EgoPfHvLine(Base):
    __tablename__ = 'ego_pf_hv_line'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    line_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Numeric, server_default=text("0"))
    s_nom_extendable = Column(Boolean, server_default=text("false"))
    s_nom_min = Column(Float(53), server_default=text("0"))
    s_nom_max = Column(Float(53))
    capital_cost = Column(Float(53))
    length = Column(Float(53))
    cables = Column(Integer)
    frequency = Column(Numeric)
    terrain_factor = Column(Float(53), server_default=text("1"))
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))

class EgoPfHvLink(Base):
    __tablename__ = 'ego_pf_hv_link'
    __table_args__ = {'schema': 'grid'}

    version = version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'NEP'::character varying"))
    link_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    efficiency = Column(Float(53))
    p_nom = Column(Numeric, server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    capital_cost = Column(Float(53))
    length = Column(Float(53))
    terrain_factor = Column(Float(53), server_default=text("1"))
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))
    
class EgoPfHvLoad(Base):
    __tablename__ = 'ego_pf_hv_load'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    sign = Column(Float(53), server_default=text("'-1'::integer"))
    e_annual = Column(Float(53))


class EgoPfHvLoadPqSet(Base):
    __tablename__ = 'ego_pf_hv_load_pq_set'
    __table_args__ = {'schema': 'grid'}

    version = Column(ForeignKey('model_draft.ego_scenario.version'), primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(Integer, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))


class EgoPfHvResultBus(Base):
    __tablename__ = 'ego_pf_hv_result_bus'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    x = Column(Float(53))
    y = Column(Float(53))
    v_nom = Column(Float(53))
    current_type = Column(Text)
    v_mag_pu_min = Column(Float(53))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))
    
    
class EgoPfHvResultBusT(Base):
    __tablename__ = 'ego_pf_hv_result_bus_t'
    __table_args__ = {'schema': 'grid'}
    
    result_id = Column(BigInteger, primary_key=True, nullable=False)
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    p = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    v_mag_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    v_ang = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    marginal_price = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    

class EgoPfHvResultGenerator(Base):
    __tablename__ = 'ego_pf_hv_result_generator'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    generator_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    dispatch = Column(Text)
    control = Column(Text)
    p_nom = Column(Float(53))
    p_nom_extendable = Column(Boolean)
    p_nom_min = Column(Float(53))
    p_nom_max = Column(Float(53))
    p_min_pu_fixed = Column(Float(53))
    p_max_pu_fixed = Column(Float(53))
    sign = Column(Float(53))
    source = Column(BigInteger)
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))
    p_nom_opt= Column(Float(53))
    
    
class EgoPfHvResultGeneratorT(Base):
    __tablename__ = 'ego_pf_hv_result_generator_t'
    __table_args__ = {'schema': 'grid'}    
    
    result_id = Column(BigInteger, primary_key=True, nullable=False)
    generator_id = Column(BigInteger, primary_key=True, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_min_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_max_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    status = Column(ARRAY(BigInteger))
    

class EgoPfHvResultLine(Base):
    __tablename__ = 'ego_pf_hv_result_line'
    __table_args__ = {'schema': 'grid'}
    
    result_id = Column(BigInteger, primary_key=True, nullable=False)
    line_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    x = Column(Numeric)
    r = Column(Numeric)
    g = Column(Numeric)
    b = Column(Numeric)
    s_nom = Column(Numeric)
    s_nom_extendable = Column(Boolean)
    s_nom_min = Column(Float(53))
    s_nom_max = Column(Float(53))
    capital_cost = Column(Float(53))
    length = Column(Float(53))
    cables = Column(Integer)
    frequency = Column(Numeric)
    terrain_factor = Column(Float(53))
    x_pu = Column(Numeric)
    r_pu = Column(Numeric)
    g_pu = Column(Numeric)
    b_pu = Column(Numeric)
    s_nom_opt = Column(Numeric)
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))
    
    
class EgoPfHvResultLineT(Base):
    __tablename__ = 'ego_pf_hv_result_line_t'
    __table_args__ = {'schema': 'grid'}   
    
    result_id = Column(BigInteger, primary_key=True, nullable=False)
    line_id = Column(BigInteger, primary_key=True, nullable=False)
    p0 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q0 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p1 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q1 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    

class EgoPfHvResultLoad(Base):
    __tablename__ = 'ego_pf_hv_result_load'
    __table_args__ = {'schema': 'grid'}    
    
    result_id = Column(BigInteger, primary_key=True, nullable=False)
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    sign = Column(Float(53), server_default=text("(-1)"))
    e_annual = Column(Float(53))
    
    
class EgoPfHvResultLoadT(Base):
    __tablename__ = 'ego_pf_hv_result_load_t'
    __table_args__ = {'schema': 'grid'}    
    
    result_id = Column(BigInteger, primary_key=True, nullable=False)
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    
    
class EgoPfHvResultMeta(Base):
    __tablename__ = 'ego_pf_hv_result_meta'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    scn_name = Column(String)
    calc_date = Column(DateTime)
    user_name = Column(Text)
    method = Column(String)
    start_snapshot = Column(Integer)
    end_snapshot = Column(Integer)
    snapshots = Column(ARRAY(DateTime))
    solver = Column(String)
    settings = Column(JSON)

class EgoPfHvResultStorage(Base):
    __tablename__ = 'ego_pf_hv_result_storage'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    dispatch = Column(Text)
    control = Column(Text)
    p_nom = Column(Float(53), server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    p_min_pu_fixed = Column(Float(53), server_default=text("0"))
    p_max_pu_fixed = Column(Float(53), server_default=text("1"))
    sign = Column(Float(53), server_default=text("1"))
    source = Column(ForeignKey('grid.ego_pf_hv_source.source_id'), index=True)
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))
    soc_initial = Column(Float(53))
    soc_cyclic = Column(Boolean)
    max_hours = Column(Float(53))
    efficiency_store = Column(Float(53))
    efficiency_dispatch = Column(Float(53))
    standing_loss = Column(Float(53))
    p_nom_opt = Column(Float(53))


class EgoPfHvResultStorageT(Base):
    __tablename__ = 'ego_pf_hv_result_storage_t'
    __table_args__ = {'schema': 'grid'}
    
    result_id = Column(BigInteger, primary_key=True, nullable=False)
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_min_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_max_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    soc_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    inflow = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    state_of_charge = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    spill = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    

class EgoPfHvResultTransformer(Base):
    __tablename__ = 'ego_pf_hv_result_transformer'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    trafo_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger, index=True)
    bus1 = Column(BigInteger, index=True)
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Float(53), server_default=text("0"))
    s_nom_extendable = Column(Boolean, server_default=text("false"))
    s_nom_min = Column(Float(53), server_default=text("0"))
    s_nom_max = Column(Float(53))
    tap_ratio = Column(Float(53))
    phase_shift = Column(Float(53))
    capital_cost = Column(Float(53), server_default=text("0"))
    x_pu = Column(Numeric)
    r_pu = Column(Numeric)
    g_pu = Column(Numeric)
    b_pu = Column(Numeric)
    s_nom_opt = Column(Numeric)
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))


class EgoPfHvResultTransformerT(Base):
    __tablename__ = 'ego_pf_hv_result_transformer_t'
    __table_args__ = {'schema': 'grid'}
    
    result_id = Column(BigInteger, primary_key=True, nullable=False)
    trafo_id = Column(BigInteger, primary_key=True, nullable=False)
    p0 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q0 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p1 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q1 = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    

class EgoPfHvSource(Base):
    __tablename__ = 'ego_pf_hv_source'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    source_id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(Text)
    co2_emissions = Column(Float(53))
    commentary = Column(Text)


class EgoPfHvStorage(Base):
    __tablename__ = 'ego_pf_hv_storage'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    dispatch = Column(Text, server_default=text("'flexible'::text"))
    control = Column(Text, server_default=text("'PQ'::text"))
    p_nom = Column(Float(53), server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    p_min_pu_fixed = Column(Float(53), server_default=text("0"))
    p_max_pu_fixed = Column(Float(53), server_default=text("1"))
    sign = Column(Float(53), server_default=text("1"))
    source = Column(BigInteger)
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))
    soc_initial = Column(Float(53))
    soc_cyclic = Column(Boolean, server_default=text("false"))
    max_hours = Column(Float(53))
    efficiency_store = Column(Float(53))
    efficiency_dispatch = Column(Float(53))
    standing_loss = Column(Float(53))


class EgoPfHvStoragePqSet(Base):
    __tablename__ = 'ego_pf_hv_storage_pq_set'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(Integer, primary_key=True, nullable=False)
    p_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    q_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_min_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    p_max_pu = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    soc_set = Column(ARRAY(DOUBLE_PRECISION(precision=53)))
    inflow = Column(ARRAY(DOUBLE_PRECISION(precision=53)))


class EgoPfHvTempResolution(Base):
    __tablename__ = 'ego_pf_hv_temp_resolution'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    temp_id = Column(BigInteger, primary_key=True, nullable=False)
    timesteps = Column(BigInteger, nullable=False)
    resolution = Column(Text)
    start_time = Column(DateTime)


class EgoPfHvTransformer(Base):
    __tablename__ = 'ego_pf_hv_transformer'
    __table_args__ = {'schema': 'grid'}

    version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    trafo_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Float(53), server_default=text("0"))
    s_nom_extendable = Column(Boolean, server_default=text("false"))
    s_nom_min = Column(Float(53), server_default=text("0"))
    s_nom_max = Column(Float(53))
    tap_ratio = Column(Float(53))
    phase_shift = Column(Float(53))
    capital_cost = Column(Float(53), server_default=text("0"))
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))


class OtgEhvhvBranchDatum(Base):
    __tablename__ = 'otg_ehvhv_branch_data'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(ForeignKey('grid.otg_ehvhv_results_metadata.id', ondelete='CASCADE'))
    view_id = Column(Integer, primary_key=True, server_default=text("nextval('grid.otg_ehvhv_branch_data_view_id_seq'::regclass)"))
    branch_id = Column(BigInteger)
    f_bus = Column(BigInteger)
    t_bus = Column(BigInteger)
    br_r = Column(Numeric)
    br_x = Column(Numeric)
    br_b = Column(Numeric)
    rate_a = Column(Numeric)
    rate_b = Column(Numeric)
    rate_c = Column(Numeric)
    tap = Column(Numeric)
    shift = Column(Numeric)
    br_status = Column(Integer)
    link_type = Column(Text)
    branch_voltage = Column(Integer)
    cables = Column(Integer)
    frequency = Column(Numeric)
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))

    result = relationship('OtgEhvhvResultsMetadatum')


class OtgEhvhvBusDatum(Base):
    __tablename__ = 'otg_ehvhv_bus_data'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(ForeignKey('grid.otg_ehvhv_results_metadata.id', ondelete='CASCADE'))
    view_id = Column(Integer, primary_key=True, server_default=text("nextval('grid.otg_ehvhv_bus_data_view_id_seq'::regclass)"))
    bus_i = Column(BigInteger)
    bus_type = Column(Integer)
    pd = Column(Numeric)
    qd = Column(Numeric)
    gs = Column(Numeric)
    bs = Column(Numeric)
    bus_area = Column(Integer)
    vm = Column(Numeric)
    va = Column(Numeric)
    base_kv = Column(Numeric)
    zone = Column(Integer)
    vmax = Column(Numeric)
    vmin = Column(Numeric)
    osm_substation_id = Column(BigInteger)
    cntr_id = Column(String(2))
    frequency = Column(Numeric)
    geom = Column(Geometry('POINT', 4326))
    osm_name = Column(Text)

    result = relationship('OtgEhvhvResultsMetadatum')


class OtgEhvhvDclineDatum(Base):
    __tablename__ = 'otg_ehvhv_dcline_data'
    __table_args__ = {'schema': 'grid'}

    result_id = Column(ForeignKey('grid.otg_ehvhv_results_metadata.id', ondelete='CASCADE'))
    view_id = Column(Integer, primary_key=True, server_default=text("nextval('grid.otg_ehvhv_dcline_data_view_id_seq'::regclass)"))
    dcline_id = Column(BigInteger)
    f_bus = Column(BigInteger)
    t_bus = Column(BigInteger)
    br_status = Column(Integer)
    pf = Column(Numeric)
    pt = Column(Numeric)
    qf = Column(Numeric)
    qt = Column(Numeric)
    vf = Column(Numeric)
    vt = Column(Numeric)
    pmin = Column(Numeric)
    pmax = Column(Numeric)
    qminf = Column(Numeric)
    qmaxf = Column(Numeric)
    qmint = Column(Numeric)
    qmaxt = Column(Numeric)
    loss0 = Column(Numeric)
    loss1 = Column(Numeric)
    link_type = Column(Text)
    branch_voltage = Column(Integer)
    cables = Column(Integer)
    frequency = Column(Numeric)
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))

    result = relationship('OtgEhvhvResultsMetadatum')


class OtgEhvhvResultsMetadatum(Base):
    __tablename__ = 'otg_ehvhv_results_metadata'
    __table_args__ = {'schema': 'grid'}

    id = Column(Integer, primary_key=True)
    osm_date = Column(Date)
    abstraction_date = Column(Date)
    applied_plans = Column(Text)
    applied_year = Column(Integer)
    user_comment = Column(Text)


class EgoScenario(Base):
    __tablename__ = 'ego_scenario'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True)
    version_name = Column(Text)
    release = Column(Boolean)
    comment = Column(Text)
    timestamp = Column(DateTime)

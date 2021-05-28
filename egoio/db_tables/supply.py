# coding: utf-8
from sqlalchemy import ARRAY, BigInteger, Column, Date, DateTime, Float, Integer, Numeric, SmallInteger, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BnetzaEegAnlagenstammdaten(Base):
    __tablename__ = 'bnetza_eeg_anlagenstammdaten'
    __table_args__ = {'schema': 'supply'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('supply.bnetza_eeg_anlagenstammdaten_id_seq'::regclass)"))
    version = Column(Text)
    meldedatum = Column(Date)
    meldegrund = Column(Text)
    anlagennummer = Column(String(14))
    _1_8_eeg_anlagenschlüssel = Column('1.8_eeg-anlagenschl\xfcssel', Text)
    _3_1_genehmigungs_datum = Column('3.1_genehmigungs-datum', Date)
    _3_2_genehmigungs_behörde = Column('3.2_genehmigungs-beh\xf6rde', Text)
    _3_3_genehmigungs_aktenzeichen = Column('3.3_genehmigungs-aktenzeichen', Text)
    _3_4_geplantes_inbetriebnahme_datum = Column('3.4_geplantes_inbetriebnahme-datum', Date)
    _3_5_errichtungs_frist = Column('3.5_errichtungs-frist', Date)
    _4_1_energieträger = Column('4.1_energietr\xe4ger', Text)
    _4_2_installierte_leistung = Column('4.2_installierte_leistung', Float(53))
    _4_2_1_inst__leistung_vor_änderung = Column('4.2.1_inst._leistung_vor_\xe4nderung', Float(53))
    _4_2_2_inst__leistung_nach_änderung = Column('4.2.2_inst._leistung_nach_\xe4nderung', Float(53))
    _4_3_tatsächliche_inbetriebnahme = Column('4.3_tats\xe4chliche_inbetriebnahme', Date)
    _4_4_datum_leistungsänderung = Column('4.4_datum_leistungs\xe4nderung', Date)
    _4_5_stilllegungsdatum = Column('4.5_stilllegungsdatum', Date)
    _4_6_name_der_anlage = Column('4.6_name_der_anlage', Text)
    _4_7_strasse_bzw__flurstück = Column('4.7_strasse_bzw._flurst\xfcck', Text)
    _4_8_hausnummer = Column('4.8_hausnummer', Text)
    _4_9_postleitzahl = Column('4.9_postleitzahl', Text)
    _4_10_ort_bzw__gemarkung = Column('4.10_ort_bzw._gemarkung', Text)
    _4_10_1_gemeindeschlüssel = Column('4.10_1_gemeindeschl\xfcssel', Text)
    _4_11_bundesland = Column('4.11_bundesland', Text)
    _4_12_utm_zonenwert = Column('4.12_utm-zonenwert', Integer)
    _4_12_utm_east = Column('4.12_utm-east', Float(53))
    _4_12_utm_north = Column('4.12_utm-north', Float(53))
    _4_13_zugehörigkeit_anlagenpark = Column('4.13_zugeh\xf6rigkeit_anlagenpark', Text)
    _4_13_1_name_des_anlagenparks = Column('4.13.1_name_des_anlagenparks', Text)
    _4_14_spannungsebene = Column('4.14_spannungsebene', Text)
    _4_15_netzanschlusspunkt = Column('4.15_netzanschlusspunkt', Text)
    _4_15_1_zählpunktbezeichnung = Column('4.15.1_z\xe4hlpunktbezeichnung', Text)
    _4_16_name_des_netzbetreibers = Column('4.16_name_des_netzbetreibers', Text)
    _4_17_fernsteuerbarkeit_durch = Column('4.17_fernsteuerbarkeit_durch', Text)
    _4_18_gemeinsame_techn__einrichtung = Column('4.18_gemeinsame_techn._einrichtung', Text)
    _4_19_inanspruchnahme_finanzielle_Förderung = Column('4.19_inanspruchnahme_finanzielle_F\xf6rderung', Text)
    _4_20_Eigenverbrauch_geplant = Column('4.20_Eigenverbrauch_geplant', Text)
    _5_1_eingesetzte_biomasse = Column('5.1_eingesetzte_biomasse', Text)
    _5_2_ausschließlich_biomasse = Column('5.2_ausschlie\xdflich_biomasse', Text)
    _5_3_flexprämie_eeg = Column('5.3_flexpr\xe4mie_eeg', Text)
    _5_4_erstmalige_inanspruchnahme_flexprämie = Column('5.4_erstmalige_inanspruchnahme_flexpr\xe4mie', Date)
    _5_4_1_leistungserhöhung_flexprämie = Column('5.4.1_leistungserh\xf6hung_flexpr\xe4mie', Text)
    _5_4_2_datum_leistungserhöhung_flexprämie = Column('5.4.2_datum_leistungserh\xf6hung_flexpr\xe4mie', Date)
    _5_4_3_umfang_der_leistungserhöhung = Column('5.4.3_umfang_der_leistungserh\xf6hung', Text)
    _5_5_erstmalig_ausschließlich_biomethan = Column('5.5_erstmalig_ausschlie\xdflich_biomethan', Text)
    _5_6_zustimmung_gesonderte_veröffentlich = Column('5.6_zustimmung_gesonderte_ver\xf6ffentlich', Text)
    _6_1_kwk_anlage = Column('6.1_kwk-anlage', Text)
    _6_2_thermische_leistung = Column('6.2_thermische_leistung', Float(53))
    _6_3_andere_energieträger = Column('6.3_andere_energietr\xe4ger', Text)
    _6_4_eingesetzte_andere_energieträger = Column('6.4_eingesetzte_andere_energietr\xe4ger', Text)
    _6_5_erstmalige_stromerzeugung = Column('6.5_erstmalige_stromerzeugung', Date)
    _7_1_windanlagenhersteller = Column('7.1_windanlagenhersteller', Text)
    _7_2_anlagentyp = Column('7.2_anlagentyp', Text)
    _7_3_nabenhöhe = Column('7.3_nabenh\xf6he', Float(53))
    _7_4_rotordurch_messer = Column('7.4_rotordurch-messer', Float(53))
    _7_5_repowering = Column('7.5_repowering', Text)
    _7_6_stilllegung_gemeldet = Column('7.6_stilllegung_gemeldet', Text)
    _7_7_1_mittlere_windgeschwindigkeit = Column('7.7.1_mittlere_windgeschwindigkeit', Float(53))
    _7_7_2_formparameter_weibull_verteilung = Column('7.7.2_formparameter_weibull-verteilung', Float(53))
    _7_7_3_skalenparameter_weibull_verteilung = Column('7.7.3_skalenparameter_weibull-verteilung', Float(53))
    _7_7_4_ertrags_einschätzung = Column('7.7.4_ertrags-einsch\xe4tzung', Float(53))
    _7_7_5_ertragseinschätzung_referenzertrag = Column('7.7.5_ertragseinsch\xe4tzung/referenzertrag', Float(53))
    _7_8_1_seelage = Column('7.8.1_seelage', Text)
    _7_8_2_wassertiefe = Column('7.8.2_wassertiefe', Text)
    _7_8_3_küstenentfernung = Column('7.8.3_k\xfcstenentfernung', Text)
    _7_9_pilotwindanlage = Column('7.9_pilotwindanlage', Text)
    _8_1_ertüchtigung_wasserkraftanlage = Column('8.1_ert\xfcchtigung_wasserkraftanlage', Text)
    _8_2_art_der_ertüchtigung = Column('8.2_art_der_ert\xfcchtigung', Text)
    _8_3_zulassungspflichtige_maßnahme = Column('8.3_zulassungspflichtige_ma\xdfnahme', Text)
    _8_4__höhe_leistungssteigerung = Column('8.4._h\xf6he_leistungssteigerung', Float(53))
    _8_5_datum_der_ertüchtigung = Column('8.5_datum_der_ert\xfcchtigung', Date)
    _9_1_zuschlagnummer_pv_freifläche = Column('9.1_zuschlagnummer_pv-freifl\xe4che', Text)
    _9_2_fläche_pv_freiflächenanlage = Column('9.2_fl\xe4che_pv-freifl\xe4chenanlage', Float(53))
    _9_3_pv_freifläche_auf_ackerland = Column('9.3_pv-freifl\xe4che_auf_ackerland', Float(53))
    geom = Column(Geometry('POINT', 5652))


class EgoAggrWeather(Base):
    __tablename__ = 'ego_aggr_weather'
    __table_args__ = {'schema': 'supply'}

    version = Column(Text, primary_key=True, nullable=False)
    aggr_id = Column(BigInteger)
    w_id = Column(BigInteger)
    scn_name = Column(String)
    bus = Column(BigInteger)
    row_number = Column(BigInteger, primary_key=True, nullable=False)


class EgoConventionalPowerplant(Base):
    __tablename__ = 'ego_conventional_powerplant'
    __table_args__ = {'schema': 'supply'}

    gid = Column(Integer, primary_key=True)
    bnetza_id = Column(Text)
    company = Column(Text)
    name = Column(Text)
    postcode = Column(Text)
    city = Column(Text)
    street = Column(Text)
    state = Column(Text)
    block = Column(Text)
    commissioned_original = Column(Text)
    commissioned = Column(Float(53))
    retrofit = Column(Float(53))
    shutdown = Column(Float(53))
    status = Column(Text)
    fuel = Column(Text)
    technology = Column(Text)
    type = Column(Text)
    eeg = Column(Text)
    chp = Column(Text)
    capacity = Column(Float(53))
    capacity_uba = Column(Float(53))
    chp_capacity_uba = Column(Float(53))
    efficiency_data = Column(Float(53))
    efficiency_estimate = Column(Float(53))
    network_node = Column(Text)
    voltage = Column(Text)
    network_operator = Column(Text)
    name_uba = Column(Text)
    lat = Column(Float(53))
    lon = Column(Float(53))
    comment = Column(Text)
    geom = Column(Geometry('POINT', 4326))


class EgoDpConvPowerplant(Base):
    __tablename__ = 'ego_dp_conv_powerplant'
    __table_args__ = {'schema': 'supply'}

    version = Column(Text, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    bnetza_id = Column(Text)
    company = Column(Text)
    name = Column(Text)
    postcode = Column(Text)
    city = Column(Text)
    street = Column(Text)
    state = Column(Text)
    block = Column(Text)
    commissioned_original = Column(Text)
    commissioned = Column(Float(53))
    retrofit = Column(Float(53))
    shutdown = Column(Float(53))
    status = Column(Text)
    fuel = Column(Text)
    technology = Column(Text)
    type = Column(Text)
    eeg = Column(Text)
    chp = Column(Text)
    capacity = Column(Float(53))
    capacity_uba = Column(Float(53))
    chp_capacity_uba = Column(Float(53))
    efficiency_data = Column(Float(53))
    efficiency_estimate = Column(Float(53))
    network_node = Column(Text)
    voltage = Column(Text)
    network_operator = Column(Text)
    name_uba = Column(Text)
    lat = Column(Float(53))
    lon = Column(Float(53))
    comment = Column(Text)
    geom = Column(Geometry('POINT', 4326), index=True)
    voltage_level = Column(SmallInteger)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)
    preversion = Column(Text)
    la_id = Column(Integer)
    scenario = Column(Text, primary_key=True, nullable=False, server_default=text("'none'::text"))
    flag = Column(Text)
    nuts = Column(String)


t_ego_dp_conv_powerplant_ego100_mview = Table(
    'ego_dp_conv_powerplant_ego100_mview', metadata,
    Column('version', Text),
    Column('preversion', Text),
    Column('id', Integer),
    Column('bnetza_id', Text),
    Column('company', Text),
    Column('name', Text),
    Column('postcode', Text),
    Column('city', Text),
    Column('street', Text),
    Column('state', Text),
    Column('block', Text),
    Column('commissioned_original', Text),
    Column('commissioned', Float(53)),
    Column('retrofit', Float(53)),
    Column('shutdown', Float(53)),
    Column('status', Text),
    Column('fuel', Text),
    Column('technology', Text),
    Column('type', Text),
    Column('eeg', Text),
    Column('chp', Text),
    Column('capacity', Float(53)),
    Column('capacity_uba', Float(53)),
    Column('chp_capacity_uba', Float(53)),
    Column('efficiency_data', Float(53)),
    Column('efficiency_estimate', Float(53)),
    Column('network_node', Text),
    Column('voltage', Text),
    Column('network_operator', Text),
    Column('name_uba', Text),
    Column('lat', Float(53)),
    Column('lon', Float(53)),
    Column('comment', Text),
    Column('geom', Geometry('POINT', 4326)),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('la_id', Integer),
    Column('scenario', Text),
    Column('flag', Text),
    Column('nuts', String),
    schema='supply'
)


t_ego_dp_conv_powerplant_nep2035_mview = Table(
    'ego_dp_conv_powerplant_nep2035_mview', metadata,
    Column('version', Text),
    Column('id', Integer),
    Column('bnetza_id', Text),
    Column('company', Text),
    Column('name', Text),
    Column('postcode', Text),
    Column('city', Text),
    Column('street', Text),
    Column('state', Text),
    Column('block', Text),
    Column('commissioned_original', Text),
    Column('commissioned', Float(53)),
    Column('retrofit', Float(53)),
    Column('shutdown', Float(53)),
    Column('status', Text),
    Column('fuel', Text),
    Column('technology', Text),
    Column('type', Text),
    Column('eeg', Text),
    Column('chp', Text),
    Column('capacity', Float(53)),
    Column('capacity_uba', Float(53)),
    Column('chp_capacity_uba', Float(53)),
    Column('efficiency_data', Float(53)),
    Column('efficiency_estimate', Float(53)),
    Column('network_node', Text),
    Column('voltage', Text),
    Column('network_operator', Text),
    Column('name_uba', Text),
    Column('lat', Float(53)),
    Column('lon', Float(53)),
    Column('comment', Text),
    Column('geom', Geometry('POINT', 4326)),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('preversion', Text),
    Column('la_id', Integer),
    Column('scenario', Text),
    Column('flag', Text),
    Column('nuts', String),
    schema='supply'
)


t_ego_dp_conv_powerplant_sq_mview = Table(
    'ego_dp_conv_powerplant_sq_mview', metadata,
    Column('version', Text),
    Column('id', Integer),
    Column('bnetza_id', Text),
    Column('company', Text),
    Column('name', Text),
    Column('postcode', Text),
    Column('city', Text),
    Column('street', Text),
    Column('state', Text),
    Column('block', Text),
    Column('commissioned_original', Text),
    Column('commissioned', Float(53)),
    Column('retrofit', Float(53)),
    Column('shutdown', Float(53)),
    Column('status', Text),
    Column('fuel', Text),
    Column('technology', Text),
    Column('type', Text),
    Column('eeg', Text),
    Column('chp', Text),
    Column('capacity', Float(53)),
    Column('capacity_uba', Float(53)),
    Column('chp_capacity_uba', Float(53)),
    Column('efficiency_data', Float(53)),
    Column('efficiency_estimate', Float(53)),
    Column('network_node', Text),
    Column('voltage', Text),
    Column('network_operator', Text),
    Column('name_uba', Text),
    Column('lat', Float(53)),
    Column('lon', Float(53)),
    Column('comment', Text),
    Column('geom', Geometry('POINT', 4326)),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('preversion', Text),
    Column('la_id', Integer),
    Column('scenario', Text),
    Column('flag', Text),
    Column('nuts', String),
    schema='supply'
)


class EgoDpResPowerplant(Base):
    __tablename__ = 'ego_dp_res_powerplant'
    __table_args__ = {'schema': 'supply'}

    version = Column(Text, primary_key=True, nullable=False)
    id = Column(BigInteger, primary_key=True, nullable=False)
    start_up_date = Column(DateTime)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    thermal_capacity = Column(Numeric)
    city = Column(String)
    postcode = Column(String)
    address = Column(String)
    lon = Column(Numeric)
    lat = Column(Numeric)
    gps_accuracy = Column(String)
    validation = Column(String)
    notification_reason = Column(String)
    eeg_id = Column(String)
    tso = Column(Float(53))
    tso_eic = Column(String)
    dso_id = Column(String)
    dso = Column(String)
    voltage_level_var = Column(String)
    network_node = Column(String)
    power_plant_id = Column(String)
    source = Column(String)
    comment = Column(String)
    geom = Column(Geometry('POINT', 4326), index=True)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)
    voltage_level = Column(SmallInteger)
    la_id = Column(Integer)
    mvlv_subst_id = Column(Integer)
    rea_sort = Column(Integer)
    rea_flag = Column(String)
    rea_geom_line = Column(Geometry('LINESTRING', 3035))
    rea_geom_new = Column(Geometry('POINT', 3035), index=True)
    preversion = Column(Text)
    flag = Column(String)
    scenario = Column(String, primary_key=True, nullable=False, server_default=text("'none'::character varying"))
    nuts = Column(String)
    w_id = Column(BigInteger)


t_ego_dp_res_powerplant_ego100_mview = Table(
    'ego_dp_res_powerplant_ego100_mview', metadata,
    Column('version', Text),
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326)),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    Column('preversion', Text),
    Column('flag', String),
    Column('scenario', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    schema='supply'
)


t_ego_dp_res_powerplant_nep2035_mview = Table(
    'ego_dp_res_powerplant_nep2035_mview', metadata,
    Column('version', Text),
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326)),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    Column('preversion', Text),
    Column('flag', String),
    Column('scenario', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    schema='supply'
)


t_ego_dp_res_powerplant_sq_mview = Table(
    'ego_dp_res_powerplant_sq_mview', metadata,
    Column('version', Text),
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Float(53)),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Float(53)),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Float(53)),
    Column('lat', Float(53)),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level_var', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326)),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    Column('preversion', Text),
    Column('flag', String),
    Column('scenario', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    schema='supply'
)


class EgoPowerClas(Base):
    __tablename__ = 'ego_power_class'
    __table_args__ = {'schema': 'supply'}

    version = Column(Text, primary_key=True, nullable=False)
    power_class_id = Column(Integer, primary_key=True, nullable=False)
    lower_limit = Column(Float(53))
    upper_limit = Column(Float(53))
    wea = Column(Text)
    h_hub = Column(Float(53))
    d_rotor = Column(Float(53))


class EgoRenewableFeedin(Base):
    __tablename__ = 'ego_renewable_feedin'
    __table_args__ = {'schema': 'supply'}

    version = Column(Text, primary_key=True, nullable=False)
    weather_scenario_id = Column(Integer, primary_key=True, nullable=False)
    w_id = Column(Integer, primary_key=True, nullable=False)
    source = Column(Text, primary_key=True, nullable=False)
    weather_year = Column(Integer, primary_key=True, nullable=False)
    feedin = Column(ARRAY(Float(precision=53)))
    power_class = Column(Integer, primary_key=True, nullable=False)


t_ego_renewable_power_plants_germany_hydro_mview = Table(
    'ego_renewable_power_plants_germany_hydro_mview', metadata,
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level', String),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326), index=True),
    schema='supply'
)


t_ego_renewable_power_plants_germany_hydro_per_voltage_level_view = Table(
    'ego_renewable_power_plants_germany_hydro_per_voltage_level_view', metadata,
    Column('generation_type', Text),
    Column('voltage_level', String),
    Column('capacity', Numeric),
    Column('count', BigInteger),
    schema='supply'
)


class EgoRenewablePowerplant(Base):
    __tablename__ = 'ego_renewable_powerplant'
    __table_args__ = {'schema': 'supply'}

    id = Column(BigInteger, primary_key=True)
    start_up_date = Column(DateTime)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    thermal_capacity = Column(Numeric)
    city = Column(String)
    postcode = Column(String)
    address = Column(String)
    lon = Column(Numeric)
    lat = Column(Numeric)
    gps_accuracy = Column(String)
    validation = Column(String)
    notification_reason = Column(String)
    eeg_id = Column(String)
    tso = Column(Float(53))
    tso_eic = Column(String)
    dso_id = Column(String)
    dso = Column(String)
    voltage_level = Column(String)
    network_node = Column(String)
    power_plant_id = Column(String)
    source = Column(String)
    comment = Column(String)
    geom = Column(Geometry('POINT', 4326), index=True)


t_ego_res_powerplant_altmark_vg_mview = Table(
    'ego_res_powerplant_altmark_vg_mview', metadata,
    Column('id', BigInteger),
    Column('start_up_date', DateTime),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('thermal_capacity', Numeric),
    Column('city', String),
    Column('postcode', String),
    Column('address', String),
    Column('lon', Numeric),
    Column('lat', Numeric),
    Column('gps_accuracy', String),
    Column('validation', String),
    Column('notification_reason', String),
    Column('eeg_id', String),
    Column('tso', Float(53)),
    Column('tso_eic', String),
    Column('dso_id', String),
    Column('dso', String),
    Column('voltage_level', SmallInteger),
    Column('network_node', String),
    Column('power_plant_id', String),
    Column('source', String),
    Column('comment', String),
    Column('geom', Geometry('POINT', 4326)),
    schema='supply'
)


class ForwindOekoRenewableCapacityPerFederalstate(Base):
    __tablename__ = 'forwind_oeko_renewable_capacity_per_federalstate'
    __table_args__ = {'schema': 'supply'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('supply.forwind_oeko_renewable_capacity_per_federalstate_id_seq'::regclass)"))
    technology = Column(Text)
    year = Column(SmallInteger, nullable=False)
    federal_state = Column(Text)
    comment = Column(Text)
    capacity = Column(Integer)


class ForwindOekoRenewableFeedinPerFederalstate(Base):
    __tablename__ = 'forwind_oeko_renewable_feedin_per_federalstate'
    __table_args__ = {'schema': 'supply'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('supply.forwind_oeko_renewable_feedin_per_federalstate_id_seq'::regclass)"))
    technology = Column(Text)
    factor = Column(Text)
    year = Column(SmallInteger, nullable=False)
    federal_state = Column(Text)
    comment = Column(Text)
    time_series = Column(ARRAY(Float()))


t_fred_dp_conv_powerplant_hydro_mview = Table(
    'fred_dp_conv_powerplant_hydro_mview', metadata,
    Column('version', Text),
    Column('gid', Integer, unique=True),
    Column('bnetza_id', Text),
    Column('company', Text),
    Column('name', Text),
    Column('postcode', Text),
    Column('city', Text),
    Column('street', Text),
    Column('state', Text),
    Column('block', Text),
    Column('commissioned_original', Text),
    Column('commissioned', Float(53)),
    Column('retrofit', Float(53)),
    Column('shutdown', Float(53)),
    Column('status', Text),
    Column('fuel', Text),
    Column('technology', Text),
    Column('type', Text),
    Column('eeg', Text),
    Column('chp', Text),
    Column('capacity', Float(53)),
    Column('capacity_uba', Float(53)),
    Column('chp_capacity_uba', Float(53)),
    Column('efficiency_data', Float(53)),
    Column('efficiency_estimate', Float(53)),
    Column('network_node', Text),
    Column('voltage', Text),
    Column('network_operator', Text),
    Column('name_uba', Text),
    Column('lat', Float(53)),
    Column('lon', Float(53)),
    Column('comment', Text),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    schema='supply'
)


t_fred_dp_conv_powerplant_hydro_on_gaugeheight_mview = Table(
    'fred_dp_conv_powerplant_hydro_on_gaugeheight_mview', metadata,
    Column('gid', Integer),
    Column('id', Integer),
    Column('station_id', BigInteger),
    Column('station', String),
    Column('water', String),
    Column('geom', Geometry('POINT', 4326)),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_fred_dp_conv_powerplant_hydro_on_river_mview = Table(
    'fred_dp_conv_powerplant_hydro_on_river_mview', metadata,
    Column('gid', Integer),
    Column('gwk', String(30)),
    Column('nam', String(100)),
    Column('geom', Geometry('POINT', 4326)),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_fred_dp_res_powerplant_hydro_on_gauge_mview = Table(
    'fred_dp_res_powerplant_hydro_on_gauge_mview', metadata,
    Column('plant_id', BigInteger, unique=True),
    Column('gauge_id', Integer),
    Column('station_id', BigInteger),
    Column('station', String),
    Column('water', String),
    Column('source', Text),
    Column('dp_geom', Geometry, index=True),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_fred_dp_res_powerplant_hydro_on_river_mview = Table(
    'fred_dp_res_powerplant_hydro_on_river_mview', metadata,
    Column('id', BigInteger),
    Column('gwk', String(20)),
    Column('nam', String(100)),
    Column('orig_geom', Geometry('POINT', 4326)),
    Column('dp_geom', Geometry),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_fred_dp_res_powerplant_hydro_on_wg_mview = Table(
    'fred_dp_res_powerplant_hydro_on_wg_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('dp_geom', Geometry, index=True),
    Column('wg_id', Integer),
    schema='supply'
)


t_opsd_power_plants_germany_hydro_mview = Table(
    'opsd_power_plants_germany_hydro_mview', metadata,
    Column('gid', Integer),
    Column('bnetza_id', Text),
    Column('company', Text),
    Column('name', Text),
    Column('postcode', Text),
    Column('city', Text),
    Column('street', Text),
    Column('state', Text),
    Column('block', Text),
    Column('commissioned_original', Text),
    Column('commissioned', Float(53)),
    Column('retrofit', Float(53)),
    Column('shutdown', Float(53)),
    Column('status', Text),
    Column('fuel', Text),
    Column('technology', Text),
    Column('type', Text),
    Column('eeg', Text),
    Column('chp', Text),
    Column('capacity', Float(53)),
    Column('capacity_uba', Float(53)),
    Column('chp_capacity_uba', Float(53)),
    Column('efficiency_data', Float(53)),
    Column('efficiency_estimate', Float(53)),
    Column('network_node', Text),
    Column('voltage', Text),
    Column('network_operator', Text),
    Column('name_uba', Text),
    Column('lat', Float(53)),
    Column('lon', Float(53)),
    Column('comment', Text),
    Column('geom', Geometry('POINT', 4326), index=True),
    schema='supply'
)


t_temp_table_cl = Table(
    'temp_table_cl', metadata,
    Column('name', Text),
    Column('geom', Geometry),
    Column('num_turb', Integer),
    Column('dvn', Float(53)),
    Column('hn', Float(53)),
    Column('pn', Float(53)),
    Column('turb_type', Text),
    schema='supply'
)


t_temp_table_cl_gauge_mview = Table(
    'temp_table_cl_gauge_mview', metadata,
    Column('plant_id', Text),
    Column('gauge_id', Integer),
    Column('station_id', BigInteger),
    Column('station', String),
    Column('water', String),
    Column('source', Text),
    Column('dp_geom', Geometry),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_temp_table_cl_river_mview = Table(
    'temp_table_cl_river_mview', metadata,
    Column('name', Text),
    Column('gwk', String(20)),
    Column('nam', String(100)),
    Column('orig_geom', Geometry),
    Column('dp_geom', Geometry),
    Column('geom_line', Geometry('LINESTRING', 3035)),
    Column('st_distance', Float(53)),
    schema='supply'
)


t_temp_table_cl_wg_mview = Table(
    'temp_table_cl_wg_mview', metadata,
    Column('name', Text),
    Column('dp_geom', Geometry),
    Column('wg_id', Integer),
    schema='supply'
)


class VernetzenWindPotentialArea(Base):
    __tablename__ = 'vernetzen_wind_potential_area'
    __table_args__ = {'schema': 'supply'}

    region_key = Column(String, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 25832), index=True)

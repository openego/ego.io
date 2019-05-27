# coding: utf-8
from sqlalchemy import ARRAY, BigInteger, Boolean, CHAR, CheckConstraint, Column, Date, DateTime, Float, ForeignKey, ForeignKeyConstraint, Index, Integer, JSON, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from geoalchemy2.types import Geometry, Raster
from sqlalchemy.dialects.postgresql.hstore import HSTORE
from sqlalchemy.dialects.postgresql.base import OID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AEgoDemandLaOsm(Base):
    __tablename__ = 'a_ego_demand_la_osm'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.a_ego_demand_la_osm_id_seq'::regclass)"))
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class AaEgoDemandLaOsm(Base):
    __tablename__ = 'aa_ego_demand_la_osm'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.aa_ego_demand_la_osm_id_seq'::regclass)"))
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class BkgVg250201501011Sta(Base):
    __tablename__ = 'bkg_vg250_20150101_1_sta'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.bkg_vg250_20150101_1_sta_id_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 31467))
    ade = Column(BigInteger)
    gf = Column(BigInteger)
    bsg = Column(BigInteger)
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(BigInteger)
    bem = Column(String(75))
    nbd = Column(String(4))
    sn_l = Column(String(2))
    sn_r = Column(String(1))
    sn_k = Column(String(2))
    sn_v1 = Column(String(2))
    sn_v2 = Column(String(2))
    sn_g = Column(String(3))
    fk_s3 = Column(String(2))
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    wsk = Column(Date)
    debkg_id = Column(String(16))


class BkgVg250201601011Sta(Base):
    __tablename__ = 'bkg_vg250_20160101_1_sta'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.bkg_vg250_20160101_1_sta_id_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 31467))
    ade = Column(BigInteger)
    gf = Column(BigInteger)
    bsg = Column(BigInteger)
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(BigInteger)
    bem = Column(String(75))
    nbd = Column(String(4))
    sn_l = Column(String(2))
    sn_r = Column(String(1))
    sn_k = Column(String(2))
    sn_v1 = Column(String(2))
    sn_v2 = Column(String(2))
    sn_g = Column(String(3))
    fk_s3 = Column(String(2))
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    wsk = Column(Date)
    debkg_id = Column(String(16))


class BnetzaEegAnlagenstammdaten(Base):
    __tablename__ = 'bnetza_eeg_anlagenstammdaten'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.bnetza_eeg_anlagenstammdaten_registerdaten_id_seq'::regclass)"))
    geom = Column(Geometry('POINT', 5652), index=True)
    Meldedatum = Column(String)
    Meldegrund = Column(String)
    Anlagennummer = Column(String)
    _1_8_EEG_Anlagenschlüssel = Column('1.8 EEG-Anlagenschl\xfcssel', String)
    _3_1_Genehmigungs_datum = Column('3.1 Genehmigungs-datum', String)
    _3_2_Genehmigungs_behörde = Column('3.2 Genehmigungs-beh\xf6rde', String)
    _3_3_Genehmigungs_Aktenzeichen = Column('3.3 Genehmigungs-Aktenzeichen', String)
    _3_4_Geplantes_Inbetriebnahme_datum = Column('3.4 Geplantes Inbetriebnahme-datum', String)
    _3_5_Errichtungs_frist = Column('3.5 Errichtungs-frist', String)
    _4_1_Energieträger = Column('4.1 Energietr\xe4ger', String)
    _4_2_Installierte_Leistung__kW_ = Column('4.2 Installierte Leistung [kW]', String)
    _4_2_1_Inst__Leistung_vor_Leistungs_änderung__ohne_Flexprämie_ = Column('4.2.1 Inst. Leistung vor Leistungs-\xe4nderung (ohne Flexpr\xe4mie)', String)
    _4_2_2_Inst__Leistung_nach_Leistungs_änderung__ohne_Flexprämie = Column('4.2.2 Inst. Leistung nach Leistungs-\xe4nderung (ohne Flexpr\xe4mie', String)
    _4_3_Tatsächliche_Inbetrieb_nahme = Column('4.3 Tats\xe4chliche Inbetrieb-nahme', String)
    _4_4_Datum_Leistungs_änderung = Column('4.4 Datum Leistungs-\xe4nderung', String)
    _4_5_Stilllegungs_datum = Column('4.5 Stilllegungs-datum', String)
    _4_6_Name_der_Anlage = Column('4.6 Name der Anlage', String)
    _4_7_Strasse_bzw__Flurstück = Column('4.7 Strasse bzw. Flurst\xfcck', String)
    _4_8_Haus_nummer = Column('4.8 Haus-nummer', String)
    _4_9_Postleit_zahl = Column('4.9 Postleit-zahl', String)
    _4_10_Ort_bzw__Gemarkung = Column('4.10 Ort bzw. Gemarkung', String)
    Gemeinde_schlüssel = Column('Gemeinde-schl\xfcssel', String)
    _4_11_Bundesland = Column('4.11 Bundesland', String)
    UTM_Zonenwert = Column('UTM-Zonenwert', Integer)
    UTM_East = Column('UTM-East', Float(53))
    UTM_North = Column('UTM-North', Float(53))
    _4_13_Zugehörigkeit_Anlagenpark = Column('4.13 Zugeh\xf6rigkeit Anlagenpark', String)
    _4_13_1__Name_des_Anlagenparks = Column('4.13.1  Name des Anlagenparks', String)
    _4_14_Spannungsebene = Column('4.14 Spannungsebene', String)
    _4_15_Netzanschlusspunkt = Column('4.15 Netzanschlusspunkt', String)
    Zählpunktbezeichnung = Column(String)
    _4_16_Name_des_Netzbetreibers = Column('4.16 Name des Netzbetreibers', String)
    _4_17_Fernsteuerbarkeit_durch_ = Column('4.17 Fernsteuerbarkeit durch:', String)
    _4_18_Gemeinsame_techn__Einrichtung = Column('4.18 Gemeinsame techn. Einrichtung', String)
    _4_19_Inanspruchnahme_finanzielle_Förderung = Column('4.19 Inanspruchnahme finanzielle F\xf6rderung', String)
    _4_20_Eigenverbrauch_geplant = Column('4.20 Eigenverbrauch geplant', String)
    _5_1_Eingesetzte_Biomasse = Column('5.1 Eingesetzte Biomasse', String)
    _5_2_Ausschließlich_Biomasse = Column('5.2 Ausschlie\xdflich Biomasse', String)
    _5_3_Flexprämie = Column('5.3 Flexpr\xe4mie', String)
    _5_4_Erstmalige_Inanspruchnahme_Flexprämie = Column('5.4 Erstmalige Inanspruchnahme Flexpr\xe4mie', String)
    _5_4_1_Leistungserhöhung_Flexprämie = Column('5.4.1 Leistungserh\xf6hung Flexpr\xe4mie', String)
    _5_4_2_Datum_Leistungserhöhung_Flexprämie = Column('5.4.2 Datum Leistungserh\xf6hung Flexpr\xe4mie', String)
    _5_4_3_Umfang_der_Leistungserhöhung__kW_ = Column('5.4.3 Umfang der Leistungserh\xf6hung [kW]', String)
    _5_5_Erstmalig_ausschließlich_Biomethan = Column('5.5 Erstmalig ausschlie\xdflich Biomethan', String)
    _5_6__5_8_in_alter_Version__Zustimmung_gesonderte_Veröffentlich = Column('5.6 (5.8 in alter Version) Zustimmung gesonderte Ver\xf6ffentlich', String)
    _6_1_KWK_Anlage = Column('6.1 KWK-Anlage', String)
    _6_2_Thermische_Leistung__kW_ = Column('6.2 Thermische Leistung [kW]', String)
    _6_3_Andere_Energieträger_vor_01_08_2014 = Column('6.3 Andere Energietr\xe4ger vor 01.08.2014', String)
    _6_4_Eingesetzte_andere_Energieträger_vor_01_08_2014 = Column('6.4 Eingesetzte andere Energietr\xe4ger vor 01.08.2014', String)
    _6_5_Erstmalige_Stromerzeugung = Column('6.5 Erstmalige Stromerzeugung', String)
    _7_1_Windanlagenhersteller = Column('7.1 Windanlagenhersteller', String)
    _7_2_Anlagentyp = Column('7.2 Anlagentyp', String)
    _7_3_Nabenhöhe__m_ = Column('7.3 Nabenh\xf6he [m]', Float(53))
    _7_4_Rotordurch_messer__m_ = Column('7.4 Rotordurch-messer [m]', Float(53))
    _7_5_Repowering = Column('7.5 Repowering', String)
    _7_6_Stilllegung_gemeldet = Column('7.6 Stilllegung gemeldet', String)
    _7_7_1_Mittlere_Windge_schwindigkeit__m_s_ = Column('7.7.1 Mittlere Windge-schwindigkeit [m/s]', Float(53))
    _7_7_2_Formparameter_Weibull_Verteilung = Column('7.7.2 Formparameter Weibull-Verteilung', Float(53))
    _7_7_3_Skalenparameter_Weibull_Verteilung = Column('7.7.3 Skalenparameter Weibull-Verteilung', Float(53))
    _7_7_4_Ertrags_einschätzung__kWh_ = Column('7.7.4 Ertrags-einsch\xe4tzung [kWh]', Float(53))
    _7_7_5_Ertragseinschätzung_Referenzertrag____ = Column('7.7.5 Ertragseinsch\xe4tzung/Referenzertrag [%]', Float(53))
    _7_8_1_Seelage = Column('7.8.1 Seelage', String)
    _7_8_2_Wassertiefe__m_ = Column('7.8.2 Wassertiefe [m]', Float(53))
    _7_8_3_Küstenentfernung__km_ = Column('7.8.3 K\xfcstenentfernung [km]', Float(53))
    _7_9_Pilotwindanlage = Column('7.9 Pilotwindanlage', String)
    _8_1_Ertüchtigung_Wasserkraftanlage = Column('8.1 Ert\xfcchtigung Wasserkraftanlage', String)
    _8_2_Art_der_Ertüchtigung = Column('8.2 Art der Ert\xfcchtigung', String)
    _8_3_Zulassungspflichtige_Maßnahme = Column('8.3 Zulassungspflichtige Ma\xdfnahme', String)
    _8_4__HöheLeistungs_steigerung____ = Column('8.4. H\xf6heLeistungs-steigerung [%]', Float(53))
    _8_5_Datum_der_Ertüchtigung = Column('8.5 Datum der Ert\xfcchtigung', String)
    _9_1_Zuschlagnummer_PV_Freifläche = Column('9.1 Zuschlagnummer PV-Freifl\xe4che', String)
    _9_2_Wie_viel_Fläche_wird_durch_die_PV_Freiflächenanlage_in_An = Column('9.2 Wie viel Fl\xe4che wird durch die PV-Freifl\xe4chenanlage in An', Float(53))
    _9_3_Wie_viel_der_PV_Freifläche_ist_davon_Ackerland___ha_ = Column('9.3 Wie viel der PV-Freifl\xe4che ist davon Ackerland? [ha]', Float(53))


class BnetzaEegAnlagenstammdatenWindClassification(Base):
    __tablename__ = 'bnetza_eeg_anlagenstammdaten_wind_classification'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    version = Column(Text)
    meldegrund = Column(Text)
    anlagennummer = Column(String(14))
    _1_8_eeg_anlagenschlüssel = Column('1.8_eeg-anlagenschl\xfcssel', Text)
    _4_2_installierte_leistung = Column('4.2_installierte_leistung', Float(53))
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
    wea_manufacturer = Column(Text)
    wea_power_class = Column(Float(53))
    wea_power_revised = Column(Float(53))
    wea_rotor_area = Column(Float(53))
    wea_specific_power = Column(Float(53))
    wea_type = Column(Text)
    wea_type_comment = Column(Text)
    geom = Column(Geometry('POINT', 3035), index=True)


class BnetzaEegAnlagenstammdatenWindLttc(Base):
    __tablename__ = 'bnetza_eeg_anlagenstammdaten_wind_lttc'
    __table_args__ = {'schema': 'model_draft'}

    lttc_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.bnetza_eeg_anlagenstammdaten_wind_lttc_lttc_id_seq'::regclass)"))
    version = Column(Text)
    wea_count = Column(Integer)
    lttc_power_sum = Column(Float(53))
    lttc_area_ha = Column(Float(53))
    wea_manufacturer = Column(Text)
    wea_power_class = Column(Float(53))
    wea_power_avg = Column(Float(53))
    wea_hubhight_avg = Column(Float(53))
    wea_rotor_avg = Column(Float(53))
    wea_rotor_area_avg = Column(Float(53))
    wea_specific_power = Column(Float(53))
    wea_type = Column(Text)
    wea_group = Column(Text)
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class BuergenDistrictLandUse(Base):
    __tablename__ = 'buergen_district_land_use'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    year = Column(Integer)
    total_area = Column(Integer)
    building_associated_open_space_area_total = Column(Integer)
    building_aos_residential_area = Column(Integer)
    building_aos_commercial_area = Column(Integer)
    industrial_without_exploitation_area = Column(Integer)
    exploitation_area = Column(String(50))
    recreational_area_total = Column(Integer)
    recreational_area_green_area = Column(Integer)
    transport_infrastructure_total_area = Column(Integer)
    street_avenue_public_square_area = Column(Integer)
    agricultural_area_total = Column(Integer)
    agricultural_area_moor = Column(String(50))
    agricultural_area_heath = Column(String(50))
    forest_area = Column(Integer)
    water_area = Column(Integer)
    other_area = Column(String(50))
    other_area_unuseable_area = Column(String(50))
    cemetery_area = Column(Integer)
    settlement_and_traffic_area = Column(Integer)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_district_land_use_id_seq'::regclass)"))


class BuergenDistrictTourism(Base):
    __tablename__ = 'buergen_district_tourism'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    year = Column(Integer)
    tourist_accommodations = Column(Integer)
    beds = Column(Integer)
    overnight_stays = Column(Integer)
    guest_arrivals = Column(Integer)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_district_tourism_id_seq'::regclass)"))


class BuergenGeoDistrict(Base):
    __tablename__ = 'buergen_geo_district'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    ags = Column(String(50))
    name = Column(String(50))
    bez = Column(String(50))
    nuts = Column(String(50))
    debkg_id = Column(String(50))
    geom = Column(Geometry('MULTIPOLYGON'))
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_geo_district_id_seq'::regclass)"))


class BuergenGeoFederalState(Base):
    __tablename__ = 'buergen_geo_federal_state'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    ags = Column(String(50))
    name = Column(String(50))
    nuts = Column(String(50))
    debkg_id = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON'))
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_geo_federal_state_id_seq'::regclass)"))


class BuergenGeoMunicipality(Base):
    __tablename__ = 'buergen_geo_municipality'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    ags = Column(String(50))
    name = Column(String(50))
    bez = Column(String(50))
    nuts = Column(String(50))
    debkg_id = Column(String(50))
    geom = Column(Geometry('MULTIPOLYGON'))
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_geo_municipality_id_seq'::regclass)"))


class BuergenGridexpIfcEnergyTransitionDistrict(Base):
    __tablename__ = 'buergen_gridexp_ifc_energy_transition_district'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    qualitative_daten_vorhanden = Column(Boolean)
    energiekommune = Column(Text)
    hundert_prozent_ee_region = Column(Boolean)
    klimaschutzkonzept_nki_energiekonzept = Column(Text)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_gridexp_ifc_energy_transition_district_id_seq'::regclass)"))


class BuergenGridexpIfcGeneralInfoDistrict(Base):
    __tablename__ = 'buergen_gridexp_ifc_general_info_district'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    informationen_vorhanden = Column(Text)
    erklaerung_zum_netzaubau = Column(Text)
    initiative_vorhanden = Column(Text)
    quelle = Column(Text)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_gridexp_ifc_general_info_district_id_seq'::regclass)"))


class BuergenGridexpIfcGeneralInfoFedstate(Base):
    __tablename__ = 'buergen_gridexp_ifc_general_info_fedstate'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    umfangreiche_informationen_website = Column(Text)
    erklaerung_netzausbauvorhaben_allgemein = Column(Text)
    aktive_netzausbau_initiativen = Column(Text)
    quellen = Column(Text)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_gridexp_ifc_general_info_fedstate_id_seq'::regclass)"))


class BuergenGridexpIfcOperatorInfoMunicipality(Base):
    __tablename__ = 'buergen_gridexp_ifc_operator_info_municipality'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    netzbetreiber = Column(String(50))
    netzb_gibt_info_zu_hintergrund_von_energiewirtschaft_u_gesetzen = Column(Boolean)
    netzbetreiber_gibt_informationen_zum_vorgehen_beim_netzausbau = Column(Boolean)
    netzbetreiber_gibt_informationen_zu_konkreten_projekten = Column(Boolean)
    netzbetreiber_gibt_angebot_zu_aktuellen_projektinformationen = Column(Boolean)
    netzbetreiber_stellt_telefonisch_ansprechpartner_zu_projekt = Column(Boolean)
    netzbetreiber_stellt_buergersprechstunden_infomaerkte_bereit = Column(Text)
    netzbetreiber_stellt_staendige_ansprechpartner_vor_ort_bereit = Column(Text)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_gridexp_ifc_operator_info_municipality_id_seq'::regclass)"))


class BuergenGridexpIfcParticipationDistrict(Base):
    __tablename__ = 'buergen_gridexp_ifc_participation_district'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    format_beteiligung_am_planungsprozess = Column(String(50))
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_gridexp_ifc_participation_district_id_seq'::regclass)"))


class BuergenGridexpnIfpActionsDistrict(Base):
    __tablename__ = 'buergen_gridexpn_ifp_actions_district'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    tatsaechliche_protestaktionen = Column(Text)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_gridexpn_ifp_actions_district_id_seq'::regclass)"))


class BuergenGridexpnIfpReasonsDistrict(Base):
    __tablename__ = 'buergen_gridexpn_ifp_reasons_district'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    technische_planung_bauweise_trassenfuehrung = Column(Boolean)
    standort_entwicklung_der_region = Column(Boolean)
    verteilungsgerechtigkeit = Column(Boolean)
    verfahrensgerechtigkeit = Column(Boolean)
    bedarf_wird_infrage_gestellt = Column(Boolean)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_gridexpn_ifp_reasons_district_id_seq'::regclass)"))


class BuergenGridexpnIfpScopeMunicipality(Base):
    __tablename__ = 'buergen_gridexpn_ifp_scope_municipality'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    regional = Column(Text)
    lokal = Column(Text)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_gridexpn_ifp_scope_municipality_id_seq'::regclass)"))


class BuergenGridexpnIfpStakeholderDistrict(Base):
    __tablename__ = 'buergen_gridexpn_ifp_stakeholder_district'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    anwohner = Column(Boolean)
    buergerinitative = Column(Boolean)
    ngo_verband = Column(Boolean)
    kommunalpolitik = Column(Boolean)
    wissenschaft = Column(Boolean)
    unternehme_sonstige = Column(Boolean)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_gridexpn_ifp_stakeholder_district_id_seq'::regclass)"))


class BuergenGridexpnIfpStakeholderRegionalLvl(Base):
    __tablename__ = 'buergen_gridexpn_ifp_stakeholder_regional_lvl'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    akteur = Column(String(50))
    akteur_bezeichnung = Column(Text)
    akteur_ebene = Column(String(50))
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_gridexpn_ifp_stakeholder_regional_lvl_id_seq'::regclass)"))


class BuergenWindexpnSocialAcceptanceAnalysisDistrict(Base):
    __tablename__ = 'buergen_windexpn_social_acceptance_analysis_district'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    qualitative_information_wind = Column(Text)
    quellen = Column(Text)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_windexpn_social_acceptance_analysis_district_id_seq'::regclass)"))


class BuergenWindexpnSocialAcceptanceAnalysisFedstate(Base):
    __tablename__ = 'buergen_windexpn_social_acceptance_analysis_fedstate'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    gesellschaftliche_akzeptanz_wind_stromerzeugung_aus_ee = Column(Text)
    relevante_windregion_fuer_gesellschaftliche_akzeptanz = Column(Text)
    besonderheiten_umwelt_klima_energie = Column(Text)
    quellen = Column(Text)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_windexpn_social_acceptance_analysis_fedstate_id_seq'::regclass)"))


class BuergenWindexpnSocialAcceptanceAnalysisMunicipality(Base):
    __tablename__ = 'buergen_windexpn_social_acceptance_analysis_municipality'
    __table_args__ = {'schema': 'model_draft'}

    region_key = Column(String(50))
    name = Column(String(50))
    qualitative_information_wind = Column(Text)
    quelle = Column(Text)
    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.buergen_windexpn_social_acceptance_analysis_municipality_id_seq'::regclass)"))


t_corr_mv_bus_results = Table(
    'corr_mv_bus_results', metadata,
    Column('name', Text),
    Column('control', Text),
    Column('type', Text),
    Column('v_nom', Float(53)),
    Column('v', ARRAY(Float(precision=53))),
    Column('mv_grid', Integer),
    Column('result_id', Integer),
    Column('geom', Geometry('POINT', 4326)),
    Column('v_ang', ARRAY(Float(precision=53))),
    Column('p', ARRAY(Float(precision=53))),
    Column('q', ARRAY(Float(precision=53))),
    schema='model_draft'
)


t_corr_mv_lines_results = Table(
    'corr_mv_lines_results', metadata,
    Column('name', Text),
    Column('bus0', Text),
    Column('bus1', Text),
    Column('s_nom', Float(53)),
    Column('s', ARRAY(Float(precision=53))),
    Column('v_nom', Float(53)),
    Column('mv_grid', Integer),
    Column('result_id', Integer),
    Column('geom', Geometry('LINESTRING', 4326)),
    Column('x', Float(53)),
    Column('r', Float(53)),
    Column('length', Float(53)),
    schema='model_draft'
)


class CorrVisHvBus(Base):
    __tablename__ = 'corr_vis_hv_bus'
    __table_args__ = {'schema': 'model_draft'}

    bus_id = Column(BigInteger)
    v_nom = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))
    vis_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.corr_vis_hv_bus_vis_id_seq'::regclass)"))


class CorrVisHvLine(Base):
    __tablename__ = 'corr_vis_hv_lines'
    __table_args__ = {'schema': 'model_draft'}

    line_id = Column(BigInteger)
    v_nom = Column(Float(53))
    s_nom = Column(Numeric)
    topo = Column(Geometry('LINESTRING', 4326))
    cables = Column(Integer)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    result_id = Column(BigInteger)
    s_rel_max = Column(Float(53))
    rel_time_over = Column(Float(53))
    s_rel = Column(Float(53))
    snapshot = Column(Integer)
    vis_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.corr_vis_hv_lines_vis_id_seq'::regclass)"))
    max_srel = Column(Float(53))


class CorrVisMvBus(Base):
    __tablename__ = 'corr_vis_mv_bus'
    __table_args__ = {'schema': 'model_draft'}

    name = Column(Text)
    type = Column(Text)
    v_nom = Column(Float(53))
    mv_grid = Column(Integer)
    geom = Column(Geometry('POINT', 4326))
    result_id = Column(Integer)
    vis_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.corr_vis_mv_bus_vis_id_seq'::regclass)"))


class CorrVisMvLine(Base):
    __tablename__ = 'corr_vis_mv_lines'
    __table_args__ = {'schema': 'model_draft'}

    name = Column(Text)
    v_nom = Column(Float(53))
    s_nom = Column(Float(53))
    mv_grid = Column(Integer)
    geom = Column(Geometry('LINESTRING', 4326))
    result_id = Column(Integer)
    s_rel_max = Column(Float(53))
    rel_time_over = Column(Float(53))
    s_rel = Column(Float(53))
    snapshot = Column(Integer)
    vis_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.corr_vis_mv_lines_vis_id_seq'::regclass)"))
    max_srel = Column(Float(53))


class DataTypeTest(Base):
    __tablename__ = 'data_type_tests'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.data_type_tests_id_seq'::regclass)"))
    year = Column(Integer)
    x_r = Column(Float)
    x_dp = Column(Float(53))
    x_f = Column(Float(53))
    x_n = Column(Numeric)
    x_d = Column(Numeric)


class DeaGermanyPerLoadArea(Base):
    __tablename__ = 'dea_germany_per_load_area'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)


class DestatisZensusPopulationPerHaInside(Base):
    __tablename__ = 'destatis_zensus_population_per_ha_inside'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True)
    inside_borders = Column(Boolean)


t_destatis_zensus_population_per_ha_invg_mview = Table(
    'destatis_zensus_population_per_ha_invg_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('population', Numeric(10, 0)),
    Column('inside_borders', Boolean),
    Column('geom_point', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class DestatisZensusPopulationPerHaMvgdla(Base):
    __tablename__ = 'destatis_zensus_population_per_ha_mvgdla'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True)
    population = Column(Integer)
    inside = Column(Boolean)
    geom_point = Column(Geometry('POINT', 3035), index=True)


t_destatis_zensus_population_per_ha_outvg_mview = Table(
    'destatis_zensus_population_per_ha_outvg_mview', metadata,
    Column('gid', Integer, unique=True),
    Column('population', Numeric(10, 0)),
    Column('inside_borders', Boolean),
    Column('geom_point', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoBoundariesBkgVg2506GemClean(Base):
    __tablename__ = 'ego_boundaries_bkg_vg250_6_gem_clean'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_political_boundary_bkg_vg250_6_gem_clean_id_seq'::regclass)"))
    old_id = Column(Integer)
    gen = Column(Text)
    bez = Column(Text)
    bem = Column(Text)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    area_ha = Column(Numeric)
    count_hole = Column(Integer)
    path = Column(ARRAY(Integer()))
    is_hole = Column(Boolean)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoBoundariesHvmvSubstPerGem(Base):
    __tablename__ = 'ego_boundaries_hvmv_subst_per_gem'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    old_id = Column(Integer)
    gen = Column(Text)
    bez = Column(Text)
    bem = Column(Text)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    area_ha = Column(Numeric)
    count_hole = Column(Integer)
    path = Column(ARRAY(Integer()))
    is_hole = Column(Boolean)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)


t_ego_boundaries_hvmv_subst_per_gem_1_mview = Table(
    'ego_boundaries_hvmv_subst_per_gem_1_mview', metadata,
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='model_draft'
)


t_ego_boundaries_hvmv_subst_per_gem_2_mview = Table(
    'ego_boundaries_hvmv_subst_per_gem_2_mview', metadata,
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='model_draft'
)


t_ego_boundaries_hvmv_subst_per_gem_3_mview = Table(
    'ego_boundaries_hvmv_subst_per_gem_3_mview', metadata,
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='model_draft'
)


class EgoBoundariesHvmvSubstPerGem3Nn(Base):
    __tablename__ = 'ego_boundaries_hvmv_subst_per_gem_3_nn'
    __table_args__ = {'schema': 'model_draft'}

    mun_id = Column(Integer, primary_key=True)
    mun_ags_0 = Column(String(12))
    subst_ags_0 = Column(Text)
    subst_id = Column(Integer)
    subst_type = Column(Integer)
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    distance = Column(Float(53))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_ego_boundaries_hvmv_subst_per_gem_3_nn_line = Table(
    'ego_boundaries_hvmv_subst_per_gem_3_nn_line', metadata,
    Column('id', BigInteger, unique=True),
    Column('nn_id', Integer),
    Column('subst_id', Integer),
    Column('geom_centre', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='model_draft'
)


t_ego_boundaries_hvmv_subst_per_gem_3_nn_union = Table(
    'ego_boundaries_hvmv_subst_per_gem_3_nn_union', metadata,
    Column('subst_id', Integer, unique=True),
    Column('subst_type', Integer),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_conv_powerplant_costdat_gid = Table(
    'ego_conv_powerplant_costdat_gid', metadata,
    Column('id', Integer),
    Column('coastdat_gid', BigInteger),
    schema='model_draft'
)


class EgoDataProcessingCleanRun(Base):
    __tablename__ = 'ego_data_processing_clean_run'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_data_processing_clean_run_id_seq'::regclass)"))
    version = Column(Text)
    schema_name = Column(Text)
    table_name = Column(Text)
    script_name = Column(Text)
    entries = Column(Integer)
    status = Column(Text)
    timestamp = Column(DateTime)
    user_name = Column(Text)


class EgoDataProcessingResult(Base):
    __tablename__ = 'ego_data_processing_results'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_data_processing_results_id_seq'::regclass)"))
    version = Column(Text)
    schema_name = Column(Text)
    table_name = Column(Text)
    description = Column(Text)
    result = Column(Integer)
    unit = Column(Text)
    timestamp = Column(DateTime)


class EgoDataProcessingResultsMvgd(Base):
    __tablename__ = 'ego_data_processing_results_mvgd'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    type1 = Column(Integer)
    type1_cnt = Column(Integer)
    type2 = Column(Integer)
    type2_cnt = Column(Integer)
    type3 = Column(Integer)
    type3_cnt = Column(Integer)
    gem = Column(Integer)
    gem_clean = Column(Integer)
    la_count = Column(Integer)
    area_ha = Column(Numeric(10, 1))
    la_area = Column(Numeric(10, 1))
    free_area = Column(Numeric(10, 1))
    area_share = Column(Numeric(4, 1))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    timestamp = Column(DateTime)
    compound = Column(Text)
    group = Column(CHAR(1))
    consumption = Column(Numeric)
    consumption_per_area = Column(Numeric)


class EgoDeaAgriculturalSectorPerGridDistrict(Base):
    __tablename__ = 'ego_dea_agricultural_sector_per_grid_district'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_dea_agricultural_sector_per_grid_district_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDeaAllocation(Base):
    __tablename__ = 'ego_dea_allocation'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    sort = Column(Integer)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    postcode = Column(String)
    subst_id = Column(Integer)
    source = Column(String)
    la_id = Column(Integer)
    flag = Column(String)
    geom = Column(Geometry('POINT', 3035), index=True)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    geom_new = Column(Geometry('POINT', 3035), index=True)


t_ego_dea_allocation_m1_1_a_mview = Table(
    'ego_dea_allocation_m1_1_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m1_1_mview = Table(
    'ego_dea_allocation_m1_1_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m1_1_rest_mview = Table(
    'ego_dea_allocation_m1_1_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m1_2_a_mview = Table(
    'ego_dea_allocation_m1_2_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m1_2_mview = Table(
    'ego_dea_allocation_m1_2_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m1_2_rest_mview = Table(
    'ego_dea_allocation_m1_2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m2_a_mview = Table(
    'ego_dea_allocation_m2_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m2_mview = Table(
    'ego_dea_allocation_m2_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m2_rest_mview = Table(
    'ego_dea_allocation_m2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m3_a_mview = Table(
    'ego_dea_allocation_m3_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m3_mview = Table(
    'ego_dea_allocation_m3_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m3_rest_mview = Table(
    'ego_dea_allocation_m3_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m4_a_mview = Table(
    'ego_dea_allocation_m4_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m4_mview = Table(
    'ego_dea_allocation_m4_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m4_rest_mview = Table(
    'ego_dea_allocation_m4_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m5_a_mview = Table(
    'ego_dea_allocation_m5_a_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_m5_mview = Table(
    'ego_dea_allocation_m5_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_dea_allocation_m5_rest_mview = Table(
    'ego_dea_allocation_m5_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('subst_id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('flag', String),
    schema='model_draft'
)


t_ego_dea_allocation_out_mview = Table(
    'ego_dea_allocation_out_mview', metadata,
    Column('id', BigInteger),
    Column('sort', Integer),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', String),
    Column('postcode', String),
    Column('subst_id', Integer),
    Column('source', String),
    Column('la_id', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


class EgoDeaPerGenerationTypeAndVoltageLevel(Base):
    __tablename__ = 'ego_dea_per_generation_type_and_voltage_level'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(String)
    capacity = Column(Numeric)
    count = Column(BigInteger)


class EgoDeaPerGridDistrict(Base):
    __tablename__ = 'ego_dea_per_grid_district'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)
    mv_dea_cnt = Column(Integer)
    mv_dea_capacity = Column(Numeric)


class EgoDeaPerLoadArea(Base):
    __tablename__ = 'ego_dea_per_load_area'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)


class EgoDeaPerMethod(Base):
    __tablename__ = 'ego_dea_per_method'
    __table_args__ = {'schema': 'model_draft'}

    name = Column(Text, primary_key=True)
    capacity = Column(Numeric)
    count = Column(BigInteger)


class EgoDemandHvLargescaleconsumer(Base):
    __tablename__ = 'ego_demand_hv_largescaleconsumer'
    __table_args__ = {'schema': 'model_draft'}

    polygon_id = Column(Integer, primary_key=True)
    area_ha = Column(Float(53))
    powerplant_id = Column(Integer)
    voltage_level = Column(SmallInteger)
    subst_id = Column(Integer)
    otg_id = Column(Integer)
    un_id = Column(Integer)
    consumption = Column(Numeric)
    peak_load = Column(Numeric)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)


class EgoDemandHvmvDemand(Base):
    __tablename__ = 'ego_demand_hvmv_demand'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_hvmv_demand_id_seq'::regclass)"))
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))


class EgoDemandLaBufferbug(Base):
    __tablename__ = 'ego_demand_la_bufferbug'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    oid = Column(Integer)
    comment = Column(Text)
    part = Column(Text)
    geom = Column(Geometry('POLYGON', 3035))


class EgoDemandLaOsm(Base):
    __tablename__ = 'ego_demand_la_osm'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_la_osm_id_seq'::regclass)"))
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDemandLaZensu(Base):
    __tablename__ = 'ego_demand_la_zensus'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_la_zensus_id_seq'::regclass)"))
    gid = Column(Integer)
    population = Column(Integer)
    inside_la = Column(Boolean)
    geom_point = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDemandLaZensusCluster(Base):
    __tablename__ = 'ego_demand_la_zensus_cluster'
    __table_args__ = {'schema': 'model_draft'}

    cid = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_la_zensus_cluster_cid_seq'::regclass)"))
    zensus_sum = Column(Integer)
    area_ha = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_buffer = Column(Geometry('POLYGON', 3035))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)


class EgoDemandLoadCollect(Base):
    __tablename__ = 'ego_demand_load_collect'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_load_collect_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDemandLoadCollectBuffer100(Base):
    __tablename__ = 'ego_demand_load_collect_buffer100'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_load_collect_buffer100_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDemandLoadMelt(Base):
    __tablename__ = 'ego_demand_load_melt'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_load_melt_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoDemandLoadMelt99(Base):
    __tablename__ = 'ego_demand_load_melt_99'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_load_melt_99_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_demand_load_melt_error_2_geom_mview = Table(
    'ego_demand_load_melt_error_2_geom_mview', metadata,
    Column('id', Integer, unique=True),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_demand_load_melt_error_geom_fix_mview = Table(
    'ego_demand_load_melt_error_geom_fix_mview', metadata,
    Column('id', Integer, unique=True),
    Column('error', Boolean),
    Column('geom_type', Text),
    Column('area', Float(53)),
    Column('geom_buffer', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_demand_load_melt_error_geom_mview = Table(
    'ego_demand_load_melt_error_geom_mview', metadata,
    Column('id', Integer, unique=True),
    Column('error', Boolean),
    Column('error_reason', String),
    Column('error_location', Geometry('POINT', 3035)),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoDemandLoadarea(Base):
    __tablename__ = 'ego_demand_loadarea'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_loadarea_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    otg_id = Column(Integer)
    un_id = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    ioer_sum = Column(Numeric)
    ioer_count = Column(Integer)
    ioer_density = Column(Numeric)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_area_sum = Column(Numeric)
    sector_share_residential = Column(Numeric)
    sector_share_retail = Column(Numeric)
    sector_share_industrial = Column(Numeric)
    sector_share_agricultural = Column(Numeric)
    sector_share_sum = Column(Numeric)
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
    sector_peakload_retail = Column(Float(53))
    sector_peakload_residential = Column(Float(53))
    sector_peakload_industrial = Column(Float(53))
    sector_peakload_agricultural = Column(Float(53))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_demand_loadarea_error_noags_mview = Table(
    'ego_demand_loadarea_error_noags_mview', metadata,
    Column('id', Integer, unique=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoDemandLoadareaPeakLoad(Base):
    __tablename__ = 'ego_demand_loadarea_peak_load'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, index=True, server_default=text("nextval('model_draft.ego_demand_loadarea_peak_load_id_seq'::regclass)"))
    retail = Column(Float(53))
    residential = Column(Float(53))
    industrial = Column(Float(53))
    agricultural = Column(Float(53))


t_ego_demand_loadarea_smaller100m2_mview = Table(
    'ego_demand_loadarea_smaller100m2_mview', metadata,
    Column('id', Integer, unique=True),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoDemandLoadareaTemp(Base):
    __tablename__ = 'ego_demand_loadarea_temp'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    otg_id = Column(Integer)
    un_id = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    ioer_sum = Column(Numeric)
    ioer_count = Column(Integer)
    ioer_density = Column(Numeric)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_area_sum = Column(Numeric)
    sector_share_residential = Column(Numeric)
    sector_share_retail = Column(Numeric)
    sector_share_industrial = Column(Numeric)
    sector_share_agricultural = Column(Numeric)
    sector_share_sum = Column(Numeric)
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
    geom_centroid = Column(Geometry('POINT', 3035))
    geom_surfacepoint = Column(Geometry('POINT', 3035))
    geom_centre = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035))


class EgoDemandLoadareaVoi(Base):
    __tablename__ = 'ego_demand_loadarea_voi'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_loadarea_voi_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    otg_id = Column(Integer)
    un_id = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    ioer_sum = Column(Numeric)
    ioer_count = Column(Integer)
    ioer_density = Column(Numeric)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_area_sum = Column(Numeric)
    sector_share_residential = Column(Numeric)
    sector_share_retail = Column(Numeric)
    sector_share_industrial = Column(Numeric)
    sector_share_agricultural = Column(Numeric)
    sector_share_sum = Column(Numeric)
    sector_count_residential = Column(Integer)
    sector_count_retail = Column(Integer)
    sector_count_industrial = Column(Integer)
    sector_count_agricultural = Column(Integer)
    sector_count_sum = Column(Integer)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)
    sector_consumption_sum = Column(Numeric)
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_demand_loadarea_voi_error_noags_mview = Table(
    'ego_demand_loadarea_voi_error_noags_mview', metadata,
    Column('id', Integer, unique=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_demand_loadarea_voi_smaller100m2_mview = Table(
    'ego_demand_loadarea_voi_smaller100m2_mview', metadata,
    Column('id', Integer, unique=True),
    Column('area_ha', Numeric),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoDemandLoad(Base):
    __tablename__ = 'ego_demand_loads'
    __table_args__ = {'schema': 'model_draft'}

    un_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_demand_loads_un_id_seq'::regclass)"))
    ssc_id = Column(Integer)
    lsc_id = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoDemandPerDistrict(Base):
    __tablename__ = 'ego_demand_per_district'
    __table_args__ = {'schema': 'model_draft'}

    eu_code = Column(String(7), primary_key=True)
    district = Column(String)
    elec_consumption_industry = Column(Float(53))
    elec_consumption_tertiary_sector = Column(Float(53))
    area_industry = Column(Float(53))
    consumption_per_area_industry = Column(Float(53))
    area_retail = Column(Float(53))
    area_agriculture = Column(Float(53))
    area_tertiary_sector = Column(Float(53))


class EgoDemandPerGva(Base):
    __tablename__ = 'ego_demand_per_gva'
    __table_args__ = {'schema': 'model_draft'}

    eu_code = Column(String(7), primary_key=True)
    federal_states = Column(String)
    elec_consumption_industry = Column(Float(53))
    elec_consumption_tertiary_sector = Column(Float(53))


t_ego_demand_per_gva_test = Table(
    'ego_demand_per_gva_test', metadata,
    Column('eu_code', String(7)),
    Column('federal_states', String),
    Column('elec_consumption_industry', Float(53)),
    Column('elec_consumption_tertiary_sector', Float(53)),
    schema='model_draft'
)


class EgoDeuLoadsOsm(Base):
    __tablename__ = 'ego_deu_loads_osm'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_deu_loads_osm_id_seq'::regclass)"))
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_dp_res_powerplant_vg_enavan_mview = Table(
    'ego_dp_res_powerplant_vg_enavan_mview', metadata,
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
    Column('geom', Geometry('POINT', 4326), index=True),
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
    schema='model_draft'
)


t_ego_dp_scenario_log_version_view = Table(
    'ego_dp_scenario_log_version_view', metadata,
    Column('id', Integer),
    Column('version', Text),
    Column('io', Text),
    Column('schema_name', Text),
    Column('table_name', Text),
    Column('script_name', Text),
    Column('entries', Integer),
    Column('status', Text),
    Column('user_name', Text),
    Column('timestamp', DateTime),
    Column('meta_data', Text),
    schema='model_draft'
)


class EgoDpSupplyConvPowerplant(Base):
    __tablename__ = 'ego_dp_supply_conv_powerplant'
    __table_args__ = {'schema': 'model_draft'}

    preversion = Column(Text, primary_key=True, nullable=False)
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
    la_id = Column(Integer)
    scenario = Column(Text, primary_key=True, nullable=False)
    flag = Column(Text)
    nuts = Column(String)


class EgoDpSupplyResPowerplant(Base):
    __tablename__ = 'ego_dp_supply_res_powerplant'
    __table_args__ = {'schema': 'model_draft'}

    preversion = Column(Text, primary_key=True, nullable=False)
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
    scenario = Column(String, primary_key=True, nullable=False)
    flag = Column(String)
    nuts = Column(String)
    w_id = Column(BigInteger)
    la_id = Column(Integer)
    mvlv_subst_id = Column(Integer)
    rea_sort = Column(Integer)
    rea_flag = Column(String)
    rea_geom_line = Column(Geometry('LINESTRING', 3035))
    rea_geom_new = Column(Geometry('POINT', 3035), index=True)


t_ego_dp_supply_res_powerplant_out_mview = Table(
    'ego_dp_supply_res_powerplant_out_mview', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


class EgoDpSupplyResPowerplantV030(Base):
    __tablename__ = 'ego_dp_supply_res_powerplant_v030'
    __table_args__ = {'schema': 'model_draft'}

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
    geom = Column(Geometry('POINT', 4326))
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)
    voltage_level = Column(SmallInteger)
    la_id = Column(Integer)
    mvlv_subst_id = Column(Integer)
    rea_sort = Column(Integer)
    rea_flag = Column(String)
    rea_geom_line = Column(Geometry('LINESTRING', 3035))
    rea_geom_new = Column(Geometry('POINT', 3035))
    preversion = Column(Text)
    flag = Column(String)
    scenario = Column(String, primary_key=True, nullable=False, server_default=text("'none'::character varying"))
    nuts = Column(String)
    w_id = Column(BigInteger)


class EgoGridDing0HvmvTransformer(Base):
    __tablename__ = 'ego_grid_ding0_hvmv_transformer'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_hvmv_transformer_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326), index=True)
    name = Column(String(100))
    voltage_op = Column(Float)
    s_nom = Column(Float)
    x = Column(Float)
    r = Column(Float)


class EgoGridDing0Line(Base):
    __tablename__ = 'ego_grid_ding0_line'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_line_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    edge_name = Column(String(100))
    grid_name = Column(String(100))
    node1 = Column(String(100))
    node2 = Column(String(100))
    type_kind = Column(String(20))
    type_name = Column(String(30))
    length = Column(Float)
    u_n = Column(Float)
    c = Column(Float)
    l = Column(Float)
    r = Column(Float)
    i_max_th = Column(Float)
    geom = Column(Geometry('LINESTRING', 4326), index=True)


class EgoGridDing0LvBranchtee(Base):
    __tablename__ = 'ego_grid_ding0_lv_branchtee'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_lv_branchtee_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326), index=True)
    name = Column(String(100))


class EgoGridDing0LvGenerator(Base):
    __tablename__ = 'ego_grid_ding0_lv_generator'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_lv_generator_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    la_id = Column(BigInteger)
    name = Column(String(100))
    lv_grid_id = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326), index=True)
    type = Column(String(22))
    subtype = Column(String(22))
    v_level = Column(Integer)
    nominal_capacity = Column(Float)
    weather_cell_id = Column(BigInteger)
    is_aggregated = Column(Boolean)


class EgoGridDing0LvGrid(Base):
    __tablename__ = 'ego_grid_ding0_lv_grid'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_lv_grid_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    name = Column(String(100))
    geom = Column(Geometry('MULTIPOLYGON', 4326), index=True)
    population = Column(BigInteger)
    voltage_nom = Column(Float)


class EgoGridDing0LvLoad(Base):
    __tablename__ = 'ego_grid_ding0_lv_load'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_lv_load_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    name = Column(String(100))
    lv_grid_id = Column(Integer)
    geom = Column(Geometry('POINT', 4326), index=True)
    consumption = Column(String(100))


class EgoGridDing0LvStation(Base):
    __tablename__ = 'ego_grid_ding0_lv_station'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_lv_station_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326), index=True)
    name = Column(String(100))


class EgoGridDing0MvBranchtee(Base):
    __tablename__ = 'ego_grid_ding0_mv_branchtee'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_mv_branchtee_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326), index=True)
    name = Column(String(100))


class EgoGridDing0MvCircuitbreaker(Base):
    __tablename__ = 'ego_grid_ding0_mv_circuitbreaker'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_mv_circuitbreaker_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326), index=True)
    name = Column(String(100))
    status = Column(String(10))


class EgoGridDing0MvGenerator(Base):
    __tablename__ = 'ego_grid_ding0_mv_generator'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_mv_generator_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    name = Column(String(100))
    geom = Column(Geometry('POINT', 4326), index=True)
    type = Column(String(22))
    subtype = Column(String(22))
    v_level = Column(Integer)
    nominal_capacity = Column(Float)
    weather_cell_id = Column(BigInteger)
    is_aggregated = Column(Boolean)


class EgoGridDing0MvGrid(Base):
    __tablename__ = 'ego_grid_ding0_mv_grid'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_mv_grid_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    geom = Column(Geometry('MULTIPOLYGON', 4326), index=True)
    name = Column(String(100))
    population = Column(BigInteger)
    voltage_nom = Column(Float)


class EgoGridDing0MvLoad(Base):
    __tablename__ = 'ego_grid_ding0_mv_load'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_mv_load_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    name = Column(String(100))
    geom = Column(Geometry(srid=4326), index=True)
    is_aggregated = Column(Boolean)
    consumption = Column(String(100))


class EgoGridDing0MvStation(Base):
    __tablename__ = 'ego_grid_ding0_mv_station'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_mv_station_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326), index=True)
    name = Column(String(100))


class EgoGridDing0MvlvMapping(Base):
    __tablename__ = 'ego_grid_ding0_mvlv_mapping'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_mvlv_mapping_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    lv_grid_id = Column(BigInteger)
    lv_grid_name = Column(String(100))
    mv_grid_id = Column(BigInteger)
    mv_grid_name = Column(String(100))


class EgoGridDing0MvlvTransformer(Base):
    __tablename__ = 'ego_grid_ding0_mvlv_transformer'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_mvlv_transformer_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False)
    id_db = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326), index=True)
    name = Column(String(100))
    voltage_op = Column(Float)
    s_nom = Column(Float)
    x = Column(Float)
    r = Column(Float)


class EgoGridDing0Versioning(Base):
    __tablename__ = 'ego_grid_ding0_versioning'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_ding0_versioning_id_seq'::regclass)"))
    run_id = Column(BigInteger, nullable=False, unique=True)
    description = Column(String(3000))


class EgoGridEhvSubstation(Base):
    __tablename__ = 'ego_grid_ehv_substation'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, nullable=False, unique=True, server_default=text("nextval('model_draft.ego_grid_ehv_substation_subst_id_seq'::regclass)"))
    lon = Column(Float(53), nullable=False)
    lat = Column(Float(53), nullable=False)
    point = Column(Geometry('POINT', 4326), nullable=False)
    polygon = Column(Geometry, nullable=False)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text, primary_key=True)
    osm_www = Column(Text, nullable=False)
    frequency = Column(Text)
    subst_name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger, nullable=False)
    otg_id = Column(BigInteger)


class EgoGridEhvSubstationVoronoi(EgoGridEhvSubstation):
    __tablename__ = 'ego_grid_ehv_substation_voronoi'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry('POLYGON', 4326), index=True)
    subst_id = Column(ForeignKey('model_draft.ego_grid_ehv_substation.subst_id'), primary_key=True)


t_ego_grid_hv_electrical_neighbours_bus = Table(
    'ego_grid_hv_electrical_neighbours_bus', metadata,
    Column('scn_name', String, nullable=False, server_default=text("'Status Quo'::character varying")),
    Column('bus_id', BigInteger),
    Column('central_bus', Boolean, server_default=text("false")),
    Column('v_nom', Float(53)),
    Column('cntr_id', Text),
    Column('current_type', Text, server_default=text("'AC'::text")),
    Column('v_mag_pu_min', Float(53), server_default=text("0")),
    Column('v_mag_pu_max', Float(53)),
    Column('geom', Geometry('POINT', 4326)),
    schema='model_draft'
)


class EgoGridHvElectricalNeighboursLine(Base):
    __tablename__ = 'ego_grid_hv_electrical_neighbours_line'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    line_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    cntr_id_1 = Column(Text)
    cntr_id_2 = Column(Text)
    v_nom = Column(BigInteger)
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


t_ego_grid_hv_electrical_neighbours_link = Table(
    'ego_grid_hv_electrical_neighbours_link', metadata,
    Column('scn_name', String, nullable=False, server_default=text("'Status Quo'::character varying")),
    Column('link_id', BigInteger, nullable=False),
    Column('bus0', BigInteger),
    Column('bus1', BigInteger),
    Column('cntr_id_1', String),
    Column('cntr_id_2', String),
    Column('v_nom', BigInteger),
    Column('efficiency', Float(53), server_default=text("1")),
    Column('p_nom', Numeric, server_default=text("0")),
    Column('p_nom_extendable', Boolean, server_default=text("false")),
    Column('p_nom_min', Float(53), server_default=text("0")),
    Column('p_min_pu', Float(53)),
    Column('p_max_pu', Float(53)),
    Column('p_nom_max', Float(53)),
    Column('capital_cost', Float(53)),
    Column('length', Float(53)),
    Column('terrain_factor', Float(53), server_default=text("1")),
    Column('geom', Geometry('MULTILINESTRING', 4326)),
    Column('topo', Geometry('LINESTRING', 4326)),
    schema='model_draft'
)


class EgoGridHvElectricalNeighboursTransformer(Base):
    __tablename__ = 'ego_grid_hv_electrical_neighbours_transformer'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    trafo_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    cntr_id = Column(Text)
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
    geom_point = Column(Geometry('POINT', 4326))
    topo = Column(Geometry('LINESTRING', 4326))
    v1 = Column(Float(53), server_default=text("0"))
    v2 = Column(Float(53), server_default=text("0"))
    s1 = Column(Float(53), server_default=text("0"))
    s2 = Column(Float(53), server_default=text("0"))
    s_min = Column(Float(53), server_default=text("0"))


class EgoGridHvmvSubstation(Base):
    __tablename__ = 'ego_grid_hvmv_substation'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, nullable=False, server_default=text("nextval('model_draft.ego_grid_hvmv_substation_subst_id_seq'::regclass)"))
    lon = Column(Float(53), nullable=False)
    lat = Column(Float(53), nullable=False)
    point = Column(Geometry('POINT', 4326), nullable=False)
    polygon = Column(Geometry, nullable=False)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text, primary_key=True)
    osm_www = Column(Text, nullable=False)
    frequency = Column(Text)
    subst_name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger, nullable=False)
    otg_id = Column(BigInteger)
    ags_0 = Column(Text)
    geom = Column(Geometry('POINT', 3035), index=True)


class EgoGridHvmvSubstationDummy(Base):
    __tablename__ = 'ego_grid_hvmv_substation_dummy'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    geom = Column(Geometry('POINT', 3035), index=True)


t_ego_grid_hvmv_substation_mun_2_mview = Table(
    'ego_grid_hvmv_substation_mun_2_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('subst_name', Text),
    Column('subst_type', Integer),
    Column('geom', Geometry('POINT', 3035)),
    schema='model_draft'
)


class EgoGridHvmvSubstationV030(Base):
    __tablename__ = 'ego_grid_hvmv_substation_v030'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, nullable=False, server_default=text("nextval('model_draft.ego_grid_hvmv_substation_v030_subst_id_seq'::regclass)"))
    lon = Column(Float(53), nullable=False)
    lat = Column(Float(53), nullable=False)
    point = Column(Geometry('POINT', 4326), nullable=False)
    polygon = Column(Geometry, nullable=False)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text, primary_key=True)
    osm_www = Column(Text, nullable=False)
    frequency = Column(Text)
    subst_name = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger, nullable=False)
    otg_id = Column(BigInteger)
    ags_0 = Column(Text)
    geom = Column(Geometry('POINT', 3035))


class EgoGridHvmvSubstationVoronoi(Base):
    __tablename__ = 'ego_grid_hvmv_substation_voronoi'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry('POLYGON', 3035), index=True)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_hvmv_substation_voronoi_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_sum = Column(Integer)


class EgoGridHvmvSubstationVoronoiCut(Base):
    __tablename__ = 'ego_grid_hvmv_substation_voronoi_cut'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_hvmv_substation_voronoi_cut_id_seq'::regclass)"))
    subst_id = Column(Integer)
    mun_id = Column(Integer)
    voi_id = Column(Integer)
    ags_0 = Column(String(12))
    subst_type = Column(Integer)
    subst_sum = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_sub = Column(Geometry('POINT', 3035), index=True)


t_ego_grid_hvmv_substation_voronoi_cut_0subst_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_0subst_mview', metadata,
    Column('id', Integer, unique=True),
    Column('subst_id', Integer),
    Column('mun_id', Integer),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_cut_0subst_nn_line_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_0subst_nn_line_mview', metadata,
    Column('id', BigInteger, unique=True),
    Column('voi_id', Integer),
    Column('subst_id', Integer),
    Column('geom_centre', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_cut_0subst_nn_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_0subst_nn_mview', metadata,
    Column('voi_id', Integer, unique=True),
    Column('voi_ags_0', String(12)),
    Column('geom_voi', Geometry('POLYGON', 3035), index=True),
    Column('subst_id', Integer),
    Column('ags_0', String(12)),
    Column('geom_sub', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_cut_0subst_nn_union_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_0subst_nn_union_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_cut_1subst_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_1subst_mview', metadata,
    Column('id', Integer, unique=True),
    Column('subst_id', Integer),
    Column('mun_id', Integer),
    Column('voi_id', Integer),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('subst_sum', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    Column('geom_sub', Geometry('POINT', 3035)),
    schema='model_draft'
)


class EgoGridHvmvSubstationVoronoiCutNnCollect(Base):
    __tablename__ = 'ego_grid_hvmv_substation_voronoi_cut_nn_collect'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_hvmv_substation_voronoi_cut_nn_collect_id_seq'::regclass)"))
    subst_id = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_ego_grid_hvmv_substation_voronoi_cut_nn_mview = Table(
    'ego_grid_hvmv_substation_voronoi_cut_nn_mview', metadata,
    Column('subst_id', Integer, unique=True),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='model_draft'
)


t_ego_grid_hvmv_substation_voronoi_mview = Table(
    'ego_grid_hvmv_substation_voronoi_mview', metadata,
    Column('id', Integer, unique=True),
    Column('subst_id', Integer),
    Column('subst_sum', Integer),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoGridLineExpansionCost(Base):
    __tablename__ = 'ego_grid_line_expansion_costs'
    __table_args__ = {'schema': 'model_draft'}

    cost_id = Column(BigInteger, primary_key=True)
    voltage_level = Column(Text)
    component = Column(Text)
    measure = Column(Text)
    investment_cost = Column(Float(53))
    unit = Column(Text)
    comment = Column(Text)
    source = Column(Text)
    capital_costs_pypsa = Column(Float(53))


class EgoGridLvBuildingConn(Base):
    __tablename__ = 'ego_grid_lv_building_conn'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_building_conn_id_seq'::regclass)"))
    building_id = Column(Integer)
    street_id = Column(Integer)
    la_id = Column(Integer)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    distance = Column(Float(53))


class EgoGridLvBuilding(Base):
    __tablename__ = 'ego_grid_lv_buildings'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_buildings_id_seq'::regclass)"))
    polygon_id = Column(Integer)
    la_id = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridLvCandidatepoint(Base):
    __tablename__ = 'ego_grid_lv_candidatepoints'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_candidatepoints_id_seq'::regclass)"))
    geom = Column(Geometry('POINT', 3035))
    la_id = Column(Integer)
    pop50 = Column(Integer)
    pop100 = Column(Integer)
    diststreet = Column(Integer)
    distcrossroad = Column(Integer)
    buildingsnr50 = Column(Integer)
    buildingsarea100 = Column(Integer)
    buildingsarea250 = Column(Integer)


class EgoGridLvGriddistrict(Base):
    __tablename__ = 'ego_grid_lv_griddistrict'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
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


class EgoGridLvGriddistrictCut(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_griddistrict_cut_id_seq'::regclass)"))
    la_id = Column(Integer)
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridLvGriddistrictCut0subst(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut_0subst'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    la_id = Column(Integer)
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridLvGriddistrictCut1subst(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut_1subst'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    la_id = Column(Integer)
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridLvGriddistrictCutNn(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut_nn'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_griddistrict_cut_nn_id_seq'::regclass)"))
    a_id = Column(Integer)
    b_id = Column(Integer)
    subst_id = Column(Integer)
    la_id = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    distance = Column(Float(53))


class EgoGridLvGriddistrictCutNnCollect(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut_nn_collect'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    mvlv_subst_id = Column(Integer)
    subst_id = Column(Integer)
    la_id = Column(Integer)
    nn = Column(Boolean)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridLvGriddistrictCutXsubst(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_cut_xsubst'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    la_id = Column(Integer)
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridLvGriddistrictPaper(Base):
    __tablename__ = 'ego_grid_lv_griddistrict_paper'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POINT', 3035), index=True)
    la_id = Column(Integer)
    ont_count = Column(Integer)
    ont_id = Column(Integer)
    merge_id = Column(Integer)
    mvlv_subst_id = Column(Integer)


class EgoGridLvGriddistrictsvoronoi(Base):
    __tablename__ = 'ego_grid_lv_griddistrictsvoronoi'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_griddistrictsvoronoi_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    subst_id = Column(Integer)


class EgoGridLvGriddistrictwithoutpop(Base):
    __tablename__ = 'ego_grid_lv_griddistrictwithoutpop'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_griddistrictwithoutpop_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    load_area_id = Column(Integer)


class EgoGridLvLoadareaRest(Base):
    __tablename__ = 'ego_grid_lv_loadarea_rest'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_loadarea_rest_id_seq'::regclass)"))
    la_id = Column(Integer)
    geom_point = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_grid_lv_loadareas = Table(
    'ego_grid_lv_loadareas', metadata,
    Column('version', Text),
    Column('id', Integer),
    Column('area_ha', Numeric),
    Column('zensus_sum', Integer),
    Column('zensus_count', Integer),
    Column('zensus_density', Numeric),
    Column('geom', Geometry('POLYGON', 3035)),
    Column('ontnumber', Numeric),
    schema='model_draft'
)


t_ego_grid_lv_ons = Table(
    'ego_grid_lv_ons', metadata,
    Column('geom', Geometry('POINT', 3035)),
    schema='model_draft'
)


class EgoGridLvStreet(Base):
    __tablename__ = 'ego_grid_lv_streets'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_streets_id_seq'::regclass)"))
    line_id = Column(Integer)
    la_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)


class EgoGridLvTestGriddistrict(Base):
    __tablename__ = 'ego_grid_lv_test_griddistrict'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035))
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_test_griddistrict_id_seq'::regclass)"))


class EgoGridLvTestStreet(Base):
    __tablename__ = 'ego_grid_lv_test_streets'
    __table_args__ = {'schema': 'model_draft'}

    osm_id = Column(BigInteger)
    geom = Column(Geometry)
    gid = Column(Integer)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_test_streets_id_seq'::regclass)"))


class EgoGridLvZensusdaten(Base):
    __tablename__ = 'ego_grid_lv_zensusdaten'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_lv_zensusdaten_id_seq'::regclass)"))
    la_id = Column(Integer)
    population = Column(Numeric(10, 0))
    geom_point = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035))


class EgoGridMvGriddistrict(Base):
    __tablename__ = 'ego_grid_mv_griddistrict'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    subst_sum = Column(Integer)
    type1 = Column(Integer)
    type1_cnt = Column(Integer)
    type2 = Column(Integer)
    type2_cnt = Column(Integer)
    type3 = Column(Integer)
    type3_cnt = Column(Integer)
    group = Column(CHAR(1))
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


t_ego_grid_mv_griddistrict_2035 = Table(
    'ego_grid_mv_griddistrict_2035', metadata,
    Column('subst_id', Integer),
    Column('subst_sum', Integer),
    Column('type1', Integer),
    Column('type1_cnt', Integer),
    Column('type2', Integer),
    Column('type2_cnt', Integer),
    Column('type3', Integer),
    Column('type3_cnt', Integer),
    Column('group', CHAR(1)),
    Column('gem', Integer),
    Column('gem_clean', Integer),
    Column('zensus_sum', Integer),
    Column('zensus_count', Integer),
    Column('zensus_density', Numeric),
    Column('population_density', Numeric),
    Column('la_count', Integer),
    Column('area_ha', Numeric),
    Column('la_area', Numeric(10, 1)),
    Column('free_area', Numeric(10, 1)),
    Column('area_share', Numeric(4, 1)),
    Column('consumption', Numeric),
    Column('consumption_per_area', Numeric),
    Column('dea_cnt', Integer),
    Column('dea_capacity', Numeric),
    Column('lv_dea_cnt', Integer),
    Column('lv_dea_capacity', Numeric),
    Column('mv_dea_cnt', Integer),
    Column('mv_dea_capacity', Numeric),
    Column('geom_type', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035)),
    schema='model_draft'
)


t_ego_grid_mv_griddistrict_2050 = Table(
    'ego_grid_mv_griddistrict_2050', metadata,
    Column('subst_id', Integer),
    Column('subst_sum', Integer),
    Column('type1', Integer),
    Column('type1_cnt', Integer),
    Column('type2', Integer),
    Column('type2_cnt', Integer),
    Column('type3', Integer),
    Column('type3_cnt', Integer),
    Column('group', CHAR(1)),
    Column('gem', Integer),
    Column('gem_clean', Integer),
    Column('zensus_sum', Integer),
    Column('zensus_count', Integer),
    Column('zensus_density', Numeric),
    Column('population_density', Numeric),
    Column('la_count', Integer),
    Column('area_ha', Numeric),
    Column('la_area', Numeric(10, 1)),
    Column('free_area', Numeric(10, 1)),
    Column('area_share', Numeric(4, 1)),
    Column('consumption', Numeric),
    Column('consumption_per_area', Numeric),
    Column('dea_cnt', Integer),
    Column('dea_capacity', Numeric),
    Column('lv_dea_cnt', Integer),
    Column('lv_dea_capacity', Numeric),
    Column('mv_dea_cnt', Integer),
    Column('mv_dea_capacity', Numeric),
    Column('geom_type', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035)),
    schema='model_draft'
)


class EgoGridMvGriddistrictCollect(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_collect'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_collect_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictDump(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_dump_id_seq1'::regclass)"))
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom_point = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridMvGriddistrictDump0sub(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_0sub'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_dump_0sub_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom_point = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridMvGriddistrictDump1sub(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_1sub'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_dump_1sub_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridMvGriddistrictDumpNn(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_nn'
    __table_args__ = {'schema': 'model_draft'}

    a_id = Column(Integer, primary_key=True)
    a_geom_point = Column(Geometry('POINT', 3035))
    a_geom = Column(Geometry('POLYGON', 3035))
    b_id = Column(Integer)
    subst_id = Column(Integer)
    b_subst_cnt = Column(Integer)
    b_geom = Column(Geometry('POLYGON', 3035))
    distance = Column(Float(53))


class EgoGridMvGriddistrictDumpNnCollect(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_nn_collect'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_dump_nn_collect_id_seq'::regclass)"))
    subst_id = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridMvGriddistrictDumpNnCollectUnion(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_nn_collect_union'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictDumpNnLine(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_nn_line'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_dump_nn_line_id_seq'::regclass)"))
    a_id = Column(Integer)
    subst_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)


class EgoGridMvGriddistrictDumpNnUnion(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_dump_nn_union'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictNew(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_new'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictNewDump(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_new_dump'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_griddistrict_new_dump_id_seq'::regclass)"))
    subst_id = Column(Integer)
    subst_cnt = Column(Integer)
    geom_point = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridMvGriddistrictType1(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_type1'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictType2(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_type2'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictType3(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_type3'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    subst_name = Column(Text)
    ags_0 = Column(String(12))
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvGriddistrictUnion(Base):
    __tablename__ = 'ego_grid_mv_griddistrict_union'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoGridMvVisualizationBranch(Base):
    __tablename__ = 'ego_grid_mv_visualization_branches'
    __table_args__ = {'schema': 'model_draft'}

    branch_id = Column(String(25), primary_key=True)
    grid_id = Column(Integer)
    type_name = Column(String(25))
    type_kind = Column(String(5))
    type_v_nom = Column(Integer)
    type_s_nom = Column(Float(53))
    length = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 4326), index=True)
    s_res0 = Column(Float(53))
    s_res1 = Column(Float(53))


class EgoGridMvVisualizationBranchesJa(Base):
    __tablename__ = 'ego_grid_mv_visualization_branches_ja'
    __table_args__ = {'schema': 'model_draft'}

    branch_id = Column(String(25), primary_key=True)
    grid_id = Column(Integer)
    type_name = Column(String(25))
    type_kind = Column(String(5))
    type_v_nom = Column(Integer)
    type_s_nom = Column(Float(53))
    length = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 4326), index=True)
    s_res0 = Column(Float(53))
    s_res1 = Column(Float(53))


class EgoGridMvVisualizationBunch(Base):
    __tablename__ = 'ego_grid_mv_visualization_bunch'
    __table_args__ = {'schema': 'model_draft'}

    grid_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_visualization_bunch_grid_id_seq'::regclass)"))
    geom_mv_station = Column(Geometry('POINT', 4326), index=True)
    geom_mv_cable_dists = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_circuit_breakers = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_lv_load_area_centres = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_lv_stations = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_generators = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_lines = Column(Geometry('MULTILINESTRING', 4326), index=True)


class EgoGridMvVisualizationBunchJa(Base):
    __tablename__ = 'ego_grid_mv_visualization_bunch_ja'
    __table_args__ = {'schema': 'model_draft'}

    grid_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_visualization_bunch_grid_id_seq'::regclass)"))
    geom_mv_station = Column(Geometry('POINT', 4326), index=True)
    geom_mv_cable_dists = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_circuit_breakers = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_lv_load_area_centres = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_lv_stations = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_generators = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_lines = Column(Geometry('MULTILINESTRING', 4326), index=True)


class EgoGridMvVisualizationBunchPaper1(Base):
    __tablename__ = 'ego_grid_mv_visualization_bunch_paper1'
    __table_args__ = {'schema': 'model_draft'}

    grid_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mv_visualization_bunch_paper1_grid_id_seq'::regclass)"))
    geom_mv_station = Column(Geometry('POINT', 4326), index=True)
    geom_mv_cable_dists = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_circuit_breakers = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_lv_load_area_centres = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_lv_stations = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_generators = Column(Geometry('MULTIPOINT', 4326), index=True)
    geom_mv_lines = Column(Geometry('MULTILINESTRING', 4326), index=True)


class EgoGridMvVisualizationNode(Base):
    __tablename__ = 'ego_grid_mv_visualization_nodes'
    __table_args__ = {'schema': 'model_draft'}

    node_id = Column(String(100), primary_key=True)
    grid_id = Column(Integer)
    v_nom = Column(Integer)
    geom = Column(Geometry('POINT', 4326), index=True)
    v_res0 = Column(Float(53))
    v_res1 = Column(Float(53))


class EgoGridMvVisualizationNodesJa(Base):
    __tablename__ = 'ego_grid_mv_visualization_nodes_ja'
    __table_args__ = {'schema': 'model_draft'}

    node_id = Column(String(100), primary_key=True)
    grid_id = Column(Integer)
    v_nom = Column(Integer)
    geom = Column(Geometry('POINT', 4326), index=True)
    v_res0 = Column(Float(53))
    v_res1 = Column(Float(53))


t_ego_grid_mvlv_referenceontpoints = Table(
    'ego_grid_mvlv_referenceontpoints', metadata,
    Column('id', Integer),
    Column('geom', Geometry('POINT', 3035)),
    Column('pop50', Integer),
    Column('pop100', Integer),
    Column('pop250', Integer),
    Column('pop500', Integer),
    Column('pop1000', Integer),
    Column('diststreet', Integer),
    Column('distcrossroad', Integer),
    Column('buildingsnr50', Integer),
    Column('buildingsnr100', Integer),
    Column('buildingsnr250', Integer),
    Column('buildingsnr500', Integer),
    Column('buildingsnr1000', Integer),
    Column('buildingsarea50', Integer),
    Column('buildingsarea100', Integer),
    Column('buildingsarea250', Integer),
    Column('buildingsarea500', Integer),
    Column('buildingsarea1000', Integer),
    schema='model_draft'
)


class EgoGridMvlvSubstation(Base):
    __tablename__ = 'ego_grid_mvlv_substation'
    __table_args__ = {'schema': 'model_draft'}

    mvlv_subst_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mvlv_substation_mvlv_subst_id_seq'::regclass)"))
    la_id = Column(Integer)
    subst_id = Column(Integer)
    geom = Column(Geometry('POINT', 3035), index=True)
    is_dummy = Column(Boolean)


class EgoGridMvlvSubstationPaper(Base):
    __tablename__ = 'ego_grid_mvlv_substation_paper'
    __table_args__ = {'schema': 'model_draft'}

    mvlv_subst_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mvlv_substation_paper_mvlv_subst_id_seq'::regclass)"))
    la_id = Column(Integer)
    subst_id = Column(Integer)
    geom = Column(Geometry('POINT', 3035), index=True)
    is_dummy = Column(Boolean)


class EgoGridMvlvSubstationVoronoi(Base):
    __tablename__ = 'ego_grid_mvlv_substation_voronoi'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_grid_mvlv_substation_voronoi_id_seq'::regclass)"))
    subst_id = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoGridPfHvBus(Base):
    __tablename__ = 'ego_grid_pf_hv_bus'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    current_type = Column(Text, server_default=text("'AC'::text"))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))


class EgoGridPfHvBusV030(Base):
    __tablename__ = 'ego_grid_pf_hv_bus_v030'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    current_type = Column(Text, server_default=text("'AC'::text"))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))


class EgoGridPfHvBusmap(Base):
    __tablename__ = 'ego_grid_pf_hv_busmap'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(Text, primary_key=True, nullable=False)
    version = Column(Text, primary_key=True, nullable=False)
    bus0 = Column(Text, primary_key=True, nullable=False)
    bus1 = Column(Text, primary_key=True, nullable=False)
    path_length = Column(Numeric)


class EgoGridPfHvDataCheck(Base):
    __tablename__ = 'ego_grid_pf_hv_data_check'
    __table_args__ = {'schema': 'model_draft'}

    test_id = Column(Integer, nullable=False, server_default=text("nextval('model_draft.ego_grid_pf_hv_data_check_test_id_seq'::regclass)"))
    version = Column(String, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False)
    test = Column(String, primary_key=True, nullable=False)
    table_name = Column(String)
    count = Column(Integer)



class EgoGridPfHvExtensionBus(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_bus'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    current_type = Column(Text, server_default=text("'AC'::text"))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326), index=True)
    project = Column(String)
    bus_name = Column(String)

class EgoGridPfHvExtensionLine(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_line'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, nullable=False, server_default=text("'extension_nep2035_confirmed'::character varying"))
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
    v_nom = Column(BigInteger)
    project = Column(String)
    project_id = Column(BigInteger)
    segment = Column(BigInteger),
    cable = Column(Boolean, server_default=text("false")),
    nova = Column(String)


class EgoGridPfHvExtensionLink(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_link'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'extension_nep2035_confirmed'::character varying"))
    link_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    efficiency = Column(Float(53), server_default=text("1"))
    p_nom = Column(Numeric, server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    capital_cost = Column(Float(53))
    marginal_cost = Column(Float(53))
    length = Column(Float(53))
    terrain_factor = Column(Float(53), server_default=text("1"))
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))
    project = Column(Text)
    project_id = Column(BigInteger)
    segment = Column(String)
    v_nom = Column(BigInteger)


class EgoGridPfHvExtensionLoad(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_load'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'BE and NO'::character varying"))
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    sign = Column(Float(53), server_default=text("'-1'::integer"))
    e_annual = Column(Float(53))



class EgoGridPfHvExtensionSource(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_source'
    __table_args__ = {'schema': 'model_draft'}

    source_id = Column(BigInteger,primary_key=True, nullable=False)
    name = Column(Text)
    co2_emissions = Column(Float(53))
    commentary = Column(Text)



class EgoGridPfHvExtensionStorage(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_storage'
    __table_args__ = {'schema': 'model_draft'}

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


class EgoGridPfHvExtensionStoragePqSet(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_storage_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(Integer, primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))
    p_min_pu = Column(ARRAY(Float(precision=53)))
    p_max_pu = Column(ARRAY(Float(precision=53)))
    soc_set = Column(ARRAY(Float(precision=53)))
    inflow = Column(ARRAY(Float(precision=53)))



class EgoGridPfHvExtensionTempResolution(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_temp_resolution'
    __table_args__ = {'schema': 'model_draft'}

    temp_id = Column(BigInteger, primary_key=True, nullable=False)
    timesteps = Column(BigInteger)
    resolution = Column(Text)
    start_time = Column(DateTime)



class EgoGridPfHvExtensionTransformer(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_transformer'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'extension_nep2035_confirmed'::character varying"))
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
    project = Column(String)
    v0 = Column(Float(53), server_default=text("0"))
    v1 = Column(Float(53), server_default=text("0"))
    s0 = Column(Float(53), server_default=text("0"))
    s1 = Column(Float(53), server_default=text("0"))
    s_min = Column(Float(53), server_default=text("0"))


class EgoGridPfHvLine(Base):
    __tablename__ = 'ego_grid_pf_hv_line'
    __table_args__ = {'schema': 'model_draft'}

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


class EgoGridPfHvLink(Base):
    __tablename__ = 'ego_grid_pf_hv_link'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    link_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    efficiency = Column(Float(53), server_default=text("1"))
    marginal_cost = Column(Float(53), server_default=text("0"))
    p_nom = Column(Numeric, server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    capital_cost = Column(Float(53))
    length = Column(Float(53))
    terrain_factor = Column(Float(53), server_default=text("1"))
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))


class EgoGridPfHvLoad(Base):
    __tablename__ = 'ego_grid_pf_hv_load'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    sign = Column(Float(53), server_default=text("'-1'::integer"))
    e_annual = Column(Float(53))


t_ego_grid_pf_hv_nep2035_bus = Table(
    'ego_grid_pf_hv_nep2035_bus', metadata,
    Column('scn_name', String, nullable=False, server_default=text("'Exogene Netzszenarien'::character varying")),
    Column('bus_id', BigInteger, nullable=False),
    Column('v_nom', Float(53)),
    Column('current_type', Text, server_default=text("'AC'::text")),
    Column('v_mag_pu_min', Float(53), server_default=text("0")),
    Column('v_mag_pu_max', Float(53)),
    Column('geom', Geometry('POINT', 4326)),
    schema='model_draft'
)


class EgoGridPfHvNep2035Link(Base):
    __tablename__ = 'ego_grid_pf_hv_nep2035_link'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Exogene Netzszenarien'::character varying"))
    link_id = Column(BigInteger, primary_key=True, nullable=False)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    efficency = Column(BigInteger, server_default=text("1"))
    p_nom = Column(Numeric, server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    capital_cost = Column(Float(53))
    length = Column(Float(53))
    terrain_factor = Column(Float(53), server_default=text("1"))
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))


class EgoGridPfHvResultBus(Base):
    __tablename__ = 'ego_grid_pf_hv_result_bus'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    x = Column(Float(53))
    y = Column(Float(53))
    v_nom = Column(Float(53))
    current_type = Column(Text)
    v_mag_pu_min = Column(Float(53))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))


class EgoGridPfHvResultBusT(Base):
    __tablename__ = 'ego_grid_pf_hv_result_bus_t'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    v_mag_pu_set = Column(ARRAY(Float(precision=53)))
    p = Column(ARRAY(Float(precision=53)))
    q = Column(ARRAY(Float(precision=53)))
    v_mag_pu = Column(ARRAY(Float(precision=53)))
    v_ang = Column(ARRAY(Float(precision=53)))
    marginal_price = Column(ARRAY(Float(precision=53)))


class EgoGridPfHvResultGenerator(Base):
    __tablename__ = 'ego_grid_pf_hv_result_generator'
    __table_args__ = {'schema': 'model_draft'}

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
    p_nom_opt = Column(Float(53))


class EgoGridPfHvResultGeneratorT(Base):
    __tablename__ = 'ego_grid_pf_hv_result_generator_t'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    generator_id = Column(BigInteger, primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))
    p_min_pu = Column(ARRAY(Float(precision=53)))
    p_max_pu = Column(ARRAY(Float(precision=53)))
    p = Column(ARRAY(Float(precision=53)))
    q = Column(ARRAY(Float(precision=53)))
    status = Column(ARRAY(BigInteger()))


class EgoGridPfHvResultLine(Base):
    __tablename__ = 'ego_grid_pf_hv_result_line'
    __table_args__ = {'schema': 'model_draft'}

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
    terrain_factor = Column(Float(53), server_default=text("1"))
    x_pu = Column(Numeric)
    r_pu = Column(Numeric)
    g_pu = Column(Numeric)
    b_pu = Column(Numeric)
    s_nom_opt = Column(Numeric)
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))


class EgoGridPfHvResultLineT(Base):
    __tablename__ = 'ego_grid_pf_hv_result_line_t'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    line_id = Column(BigInteger, primary_key=True, nullable=False)
    p0 = Column(ARRAY(Float(precision=53)))
    q0 = Column(ARRAY(Float(precision=53)))
    p1 = Column(ARRAY(Float(precision=53)))
    q1 = Column(ARRAY(Float(precision=53)))


class EgoGridPfHvResultLoad(Base):
    __tablename__ = 'ego_grid_pf_hv_result_load'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    sign = Column(Float(53))
    e_annual = Column(Float(53))


class EgoGridPfHvResultLoadT(Base):
    __tablename__ = 'ego_grid_pf_hv_result_load_t'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))
    p = Column(ARRAY(Float(precision=53)))
    q = Column(ARRAY(Float(precision=53)))


class EgoGridPfHvResultMeta(Base):
    __tablename__ = 'ego_grid_pf_hv_result_meta'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True)
    scn_name = Column(String)
    calc_date = Column(DateTime)
    user_name = Column(String)
    method = Column(String)
    start_snapshot = Column(Integer)
    end_snapshot = Column(Integer)
    snapshots = Column(ARRAY(DateTime()))
    solver = Column(String)
    settings = Column(JSON)
    safe_results = Column(Boolean, server_default=text("false"))


class EgoGridPfHvResultStorage(Base):
    __tablename__ = 'ego_grid_pf_hv_result_storage'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
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
    soc_initial = Column(Float(53))
    soc_cyclic = Column(Boolean, server_default=text("false"))
    max_hours = Column(Float(53))
    efficiency_store = Column(Float(53))
    efficiency_dispatch = Column(Float(53))
    standing_loss = Column(Float(53))
    p_nom_opt = Column(Float(53))


class EgoGridPfHvResultStorageT(Base):
    __tablename__ = 'ego_grid_pf_hv_result_storage_t'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))
    p_min_pu = Column(ARRAY(Float(precision=53)))
    p_max_pu = Column(ARRAY(Float(precision=53)))
    soc_set = Column(ARRAY(Float(precision=53)))
    inflow = Column(ARRAY(Float(precision=53)))
    p = Column(ARRAY(Float(precision=53)))
    q = Column(ARRAY(Float(precision=53)))
    state_of_charge = Column(ARRAY(Float(precision=53)))
    spill = Column(ARRAY(Float(precision=53)))


class EgoGridPfHvResultTransformer(Base):
    __tablename__ = 'ego_grid_pf_hv_result_transformer'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    trafo_id = Column(BigInteger, primary_key=True, nullable=False)
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
    tap_ratio = Column(Float(53))
    phase_shift = Column(Float(53))
    capital_cost = Column(Float(53))
    x_pu = Column(Numeric)
    r_pu = Column(Numeric)
    g_pu = Column(Numeric)
    b_pu = Column(Numeric)
    s_nom_opt = Column(Numeric)
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))


class EgoGridPfHvResultTransformerT(Base):
    __tablename__ = 'ego_grid_pf_hv_result_transformer_t'
    __table_args__ = {'schema': 'model_draft'}

    result_id = Column(BigInteger, primary_key=True, nullable=False)
    trafo_id = Column(BigInteger, primary_key=True, nullable=False)
    p0 = Column(ARRAY(Float(precision=53)))
    q0 = Column(ARRAY(Float(precision=53)))
    p1 = Column(ARRAY(Float(precision=53)))
    q1 = Column(ARRAY(Float(precision=53)))


class EgoGridPfHvScenarioSetting(Base):
    __tablename__ = 'ego_grid_pf_hv_scenario_settings'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, server_default=text("'Status Quo'::character varying"))
    bus = Column(String)
    bus_v_mag_set = Column(String)
    generator = Column(String)
    generator_pq_set = Column(String)
    line = Column(String)
    load = Column(String)
    load_pq_set = Column(String)
    storage = Column(String)
    storage_pq_set = Column(String)
    temp_resolution = Column(String)
    transformer = Column(String)


class EgoGridPfHvSource(Base):
    __tablename__ = 'ego_grid_pf_hv_source'
    __table_args__ = {'schema': 'model_draft'}

    source_id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    co2_emissions = Column(Float(53))
    commentary = Column(Text)


t_ego_grid_pf_hv_storage_eins = Table(
    'ego_grid_pf_hv_storage_eins', metadata,
    Column('scn_name', String, nullable=False, server_default=text("'Status Quo'::character varying")),
    Column('storage_id', BigInteger, nullable=False),
    Column('bus', BigInteger),
    Column('dispatch', Text, server_default=text("'flexible'::text")),
    Column('control', Text, server_default=text("'PQ'::text")),
    Column('p_nom', Float(53), server_default=text("0")),
    Column('p_nom_extendable', Boolean, server_default=text("false")),
    Column('p_nom_min', Float(53), server_default=text("0")),
    Column('p_nom_max', Float(53)),
    Column('p_min_pu_fixed', Float(53), server_default=text("0")),
    Column('p_max_pu_fixed', Float(53), server_default=text("1")),
    Column('sign', Float(53), server_default=text("1")),
    Column('source', BigInteger),
    Column('marginal_cost', Float(53)),
    Column('capital_cost', Float(53)),
    Column('efficiency', Float(53)),
    Column('soc_initial', Float(53)),
    Column('soc_cyclic', Boolean, server_default=text("false")),
    Column('max_hours', Float(53)),
    Column('efficiency_store', Float(53)),
    Column('efficiency_dispatch', Float(53)),
    Column('standing_loss', Float(53)),
    schema='model_draft'
)


class EgoGridPfHvTempResolution(Base):
    __tablename__ = 'ego_grid_pf_hv_temp_resolution'
    __table_args__ = {'schema': 'model_draft'}

    temp_id = Column(BigInteger, primary_key=True)
    timesteps = Column(BigInteger, nullable=False)
    resolution = Column(Text)
    start_time = Column(DateTime)


class EgoGridPfHvTransformer(Base):
    __tablename__ = 'ego_grid_pf_hv_transformer'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
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
    geom = Column(Geometry('MULTILINESTRING', 4326))
    topo = Column(Geometry('LINESTRING', 4326))


class EgoGridPfMvBus(Base):
    __tablename__ = 'ego_grid_pf_mv_bus'
    __table_args__ = {'schema': 'model_draft'}

    bus_id = Column(String(25), primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    grid_id = Column(Integer)


class EgoGridPfMvBusVMagSet(Base):
    __tablename__ = 'ego_grid_pf_mv_bus_v_mag_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(String(25), primary_key=True, nullable=False)
    temp_id = Column(Integer, primary_key=True, nullable=False)
    v_mag_pu_set = Column(ARRAY(Float(precision=53)))
    grid_id = Column(Integer)


class EgoGridPfMvGenerator(Base):
    __tablename__ = 'ego_grid_pf_mv_generator'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(String(25), primary_key=True, nullable=False)
    bus = Column(String(25))
    control = Column(Text, server_default=text("'PQ'::text"))
    p_nom = Column(Float(53), server_default=text("0"))
    p_min_pu_fixed = Column(Float(53), server_default=text("0"))
    p_max_pu_fixed = Column(Float(53), server_default=text("1"))
    sign = Column(Float(53), server_default=text("1"))
    grid_id = Column(Integer)


class EgoGridPfMvGeneratorPqSet(Base):
    __tablename__ = 'ego_grid_pf_mv_generator_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(String(25), primary_key=True, nullable=False)
    temp_id = Column(Integer, primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))
    p_min_pu = Column(ARRAY(Float(precision=53)))
    p_max_pu = Column(ARRAY(Float(precision=53)))
    grid_id = Column(Integer)


class EgoGridPfMvLine(Base):
    __tablename__ = 'ego_grid_pf_mv_line'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    line_id = Column(String(25), primary_key=True, nullable=False)
    bus0 = Column(String(25))
    bus1 = Column(String(25))
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Numeric, server_default=text("0"))
    length = Column(Float(53))
    cables = Column(Integer)
    geom = Column(Geometry('LINESTRING', 4326))
    grid_id = Column(Integer)


class EgoGridPfMvLoad(Base):
    __tablename__ = 'ego_grid_pf_mv_load'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(String(25), primary_key=True, nullable=False)
    bus = Column(String(25))
    sign = Column(Float(53), server_default=text("'-1'::integer"))
    grid_id = Column(Integer)


class EgoGridPfMvLoadPqSet(Base):
    __tablename__ = 'ego_grid_pf_mv_load_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(String(25), primary_key=True, nullable=False)
    temp_id = Column(Integer, primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))
    grid_id = Column(Integer)


class EgoGridPfMvResBus(Base):
    __tablename__ = 'ego_grid_pf_mv_res_bus'
    __table_args__ = {'schema': 'model_draft'}

    bus_id = Column(String(25), primary_key=True)
    v_mag_pu = Column(ARRAY(Float(precision=53)))


class EgoGridPfMvResLine(Base):
    __tablename__ = 'ego_grid_pf_mv_res_line'
    __table_args__ = {'schema': 'model_draft'}

    line_id = Column(String(25), primary_key=True)
    p0 = Column(ARRAY(Float(precision=53)))
    p1 = Column(ARRAY(Float(precision=53)))
    q0 = Column(ARRAY(Float(precision=53)))
    q1 = Column(ARRAY(Float(precision=53)))


class EgoGridPfMvResTransformer(Base):
    __tablename__ = 'ego_grid_pf_mv_res_transformer'
    __table_args__ = {'schema': 'model_draft'}

    trafo_id = Column(String(25), primary_key=True)
    p0 = Column(ARRAY(Float(precision=53)))
    p1 = Column(ARRAY(Float(precision=53)))
    q0 = Column(ARRAY(Float(precision=53)))
    q1 = Column(ARRAY(Float(precision=53)))


class EgoGridPfMvScenarioSetting(Base):
    __tablename__ = 'ego_grid_pf_mv_scenario_settings'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, server_default=text("'Status Quo'::character varying"))
    bus = Column(String)
    bus_v_mag_set = Column(String)
    generator = Column(String)
    generator_pq_set = Column(String)
    line = Column(String)
    load = Column(String)
    load_pq_set = Column(String)
    storage = Column(String)
    storage_pq_set = Column(String)
    temp_resolution = Column(String)
    transformer = Column(String)


class EgoGridPfMvSource(Base):
    __tablename__ = 'ego_grid_pf_mv_source'
    __table_args__ = {'schema': 'model_draft'}

    source_id = Column(String(25), primary_key=True)
    name = Column(Text)
    co2_emissions = Column(Float(53))
    commentary = Column(Text)


class EgoGridPfMvTempResolution(Base):
    __tablename__ = 'ego_grid_pf_mv_temp_resolution'
    __table_args__ = {'schema': 'model_draft'}

    temp_id = Column(BigInteger, primary_key=True)
    timesteps = Column(BigInteger, nullable=False)
    resolution = Column(Text)
    start_time = Column(DateTime)
    grid_id = Column(Integer)


class EgoGridPfMvTransformer(Base):
    __tablename__ = 'ego_grid_pf_mv_transformer'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    trafo_id = Column(String(25), primary_key=True, nullable=False)
    bus0 = Column(String(25))
    bus1 = Column(String(25))
    x = Column(Numeric, server_default=text("0"))
    r = Column(Numeric, server_default=text("0"))
    g = Column(Numeric, server_default=text("0"))
    b = Column(Numeric, server_default=text("0"))
    s_nom = Column(Float(53), server_default=text("0"))
    tap_ratio = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))
    grid_id = Column(Integer)


class EgoGridPpEntsoeBus(Base):
    __tablename__ = 'ego_grid_pp_entsoe_bus'
    __table_args__ = {'schema': 'model_draft'}

    bus_id = Column(BigInteger, primary_key=True)
    station_id = Column(BigInteger)
    voltage = Column(Float(53))
    dc = Column(Boolean)
    symbol = Column(String)
    country = Column(Text)
    under_construction = Column(Boolean)
    geom = Column(Geometry('POINT'))


class EgoGridPpEntsoeLine(Base):
    __tablename__ = 'ego_grid_pp_entsoe_line'
    __table_args__ = {'schema': 'model_draft'}

    link_id = Column(BigInteger, primary_key=True)
    bus0 = Column(BigInteger)
    bus1 = Column(BigInteger)
    voltage = Column(Float(53))
    circiuts = Column(BigInteger)
    dc = Column(Boolean)
    underground = Column(Boolean)
    under_construction = Column(Boolean)
    country1 = Column(String)
    country2 = Column(String)
    geom = Column(Geometry('LINESTRING'))


class EgoHvmvSubstation(Base):
    __tablename__ = 'ego_hvmv_substation'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True, nullable=False)
    subst_id = Column(SmallInteger, primary_key=True, nullable=False)
    subst_name = Column(Text)
    ags_0 = Column(Text)
    voltage = Column(Text)
    power_type = Column(Text)
    substation = Column(Text)
    osm_id = Column(Text)
    osm_www = Column(Text)
    frequency = Column(Text)
    ref = Column(Text)
    operator = Column(Text)
    dbahn = Column(Text)
    status = Column(SmallInteger)
    otg_id = Column(BigInteger)
    lat = Column(Float(53))
    lon = Column(Float(53))
    point = Column(Geometry('POINT', 4326))
    polygon = Column(Geometry)
    geom = Column(Geometry('POINT', 3035))


class EgoLanduseIndustry(Base):
    __tablename__ = 'ego_landuse_industry'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True)
    osm_id = Column(Integer)
    name = Column(Text)
    sector = Column(Integer)
    area_ha = Column(Float(53))
    tags = Column(HSTORE(Text()))
    vg250 = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)
    nuts = Column(String(5))
    consumption = Column(Numeric)
    peak_load = Column(Numeric)


class EgoLattice1km(Base):
    __tablename__ = 'ego_lattice_1km'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POINT', 3035))
    subst_id = Column(BigInteger)


class EgoLattice2km(Base):
    __tablename__ = 'ego_lattice_2km'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POINT', 3035))
    subst_id = Column(BigInteger)


class EgoLattice2pt5km(Base):
    __tablename__ = 'ego_lattice_2pt5km'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POINT', 3035))
    subst_id = Column(BigInteger)


class EgoLattice360mLv(Base):
    __tablename__ = 'ego_lattice_360m_lv'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_lattice_360m_lv_id_seq'::regclass)"))
    la_id = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoLattice500m(Base):
    __tablename__ = 'ego_lattice_500m'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_lattice_500m_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_type = Column(Text)
    geom_box = Column(Geometry('POLYGON', 3035), index=True)
    geom = Column(Geometry('POINT', 3035), index=True)


t_ego_lattice_500m_la_mview = Table(
    'ego_lattice_500m_la_mview', metadata,
    Column('id', Integer),
    Column('subst_id', Integer),
    Column('area_type', Text),
    Column('geom_box', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_lattice_500m_out_mview = Table(
    'ego_lattice_500m_out_mview', metadata,
    Column('id', Integer),
    Column('subst_id', Integer),
    Column('area_type', Text),
    Column('geom_box', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_lattice_500m_wpa_mview = Table(
    'ego_lattice_500m_wpa_mview', metadata,
    Column('id', Integer),
    Column('subst_id', Integer),
    Column('area_type', Text),
    Column('geom_box', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_lattice_500m_x_mview = Table(
    'ego_lattice_500m_x_mview', metadata,
    Column('id', Integer),
    Column('subst_id', Integer),
    Column('area_type', Text),
    Column('geom_box', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


class EgoLattice50m(Base):
    __tablename__ = 'ego_lattice_50m'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_lattice_50m_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_type = Column(Text)
    geom_box = Column(Geometry('POLYGON', 3035), index=True)
    geom = Column(Geometry('POINT', 3035), index=True)


t_ego_lattice_50m_la_mview = Table(
    'ego_lattice_50m_la_mview', metadata,
    Column('id', Integer),
    Column('subst_id', Integer),
    Column('area_type', Text),
    Column('geom_box', Geometry('POLYGON', 3035)),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


class EgoLoadarea(Base):
    __tablename__ = 'ego_loadarea'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    otg_id = Column(Integer)
    un_id = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    ioer_sum = Column(Numeric)
    ioer_count = Column(Integer)
    ioer_density = Column(Numeric)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_area_sum = Column(Numeric)
    sector_share_residential = Column(Numeric)
    sector_share_retail = Column(Numeric)
    sector_share_industrial = Column(Numeric)
    sector_share_agricultural = Column(Numeric)
    sector_share_sum = Column(Numeric)
    sector_count_residential = Column(Integer)
    sector_count_retail = Column(Integer)
    sector_count_industrial = Column(Integer)
    sector_count_agricultural = Column(Integer)
    sector_count_sum = Column(Integer)
    sector_consumption_residential = Column(Numeric)
    sector_consumption_retail = Column(Numeric)
    sector_consumption_industrial = Column(Numeric)
    sector_consumption_agricultural = Column(Numeric)
    sector_consumption_sum = Column(Numeric)
    geom_centroid = Column(Geometry('POINT', 3035))
    geom_surfacepoint = Column(Geometry('POINT', 3035))
    geom_centre = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035))


class EgoMvGriddistrict(Base):
    __tablename__ = 'ego_mv_griddistrict'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True, nullable=False)
    subst_id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('model_draft.ego_mv_griddistrict_subst_id_seq'::regclass)"))
    subst_sum = Column(Text)
    area_ha = Column(Numeric)
    geom_type = Column(Text)
    geom = Column(Geometry('MULTIPOLYGON', 3035))


class EgoNeighboursOffshorePoint(Base):
    __tablename__ = 'ego_neighbours_offshore_point'
    __table_args__ = {'schema': 'model_draft'}

    cntr_id = Column(Text, primary_key=True)
    coastdat_id = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326))


class EgoOsmAgriculturePerMvgd(Base):
    __tablename__ = 'ego_osm_agriculture_per_mvgd'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_agriculture_per_mvgd_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmDeuStreetStreetcrossing(Base):
    __tablename__ = 'ego_osm_deu_street_streetcrossing'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry, index=True)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_deu_street_streetcrossing_id_seq'::regclass)"))


class EgoOsmSectorPerGriddistrict1Residential(Base):
    __tablename__ = 'ego_osm_sector_per_griddistrict_1_residential'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_griddistrict_1_residential_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerGriddistrict2Retail(Base):
    __tablename__ = 'ego_osm_sector_per_griddistrict_2_retail'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_griddistrict_2_retail_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerGriddistrict3Industrial(Base):
    __tablename__ = 'ego_osm_sector_per_griddistrict_3_industrial'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_griddistrict_3_industrial_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerGriddistrict4Agricultural(Base):
    __tablename__ = 'ego_osm_sector_per_griddistrict_4_agricultural'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_griddistrict_4_agricultural_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)
    subst_id = Column(Integer)
    area_ha = Column(Float(53))


class EgoOsmSectorPerLvgd1Residential(Base):
    __tablename__ = 'ego_osm_sector_per_lvgd_1_residential'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_lvgd_1_residential_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerLvgd2Retail(Base):
    __tablename__ = 'ego_osm_sector_per_lvgd_2_retail'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_lvgd_2_retail_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerLvgd3Industrial(Base):
    __tablename__ = 'ego_osm_sector_per_lvgd_3_industrial'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_lvgd_3_industrial_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoOsmSectorPerLvgd4Agricultural(Base):
    __tablename__ = 'ego_osm_sector_per_lvgd_4_agricultural'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_osm_sector_per_lvgd_4_agricultural_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_political_boundary_bkg_vg250_6_gem_hole_mview = Table(
    'ego_political_boundary_bkg_vg250_6_gem_hole_mview', metadata,
    Column('id', Integer, unique=True),
    Column('old_id', Integer),
    Column('gen', Text),
    Column('bez', Text),
    Column('bem', Text),
    Column('nuts', String(5)),
    Column('rs_0', String(12)),
    Column('ags_0', String(12)),
    Column('area_ha', Numeric),
    Column('count_hole', Integer),
    Column('path', ARRAY(Integer())),
    Column('is_hole', Boolean),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoPoliticalBoundaryHvmvSubstPerGem(Base):
    __tablename__ = 'ego_political_boundary_hvmv_subst_per_gem'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    old_id = Column(Integer)
    gen = Column(Text)
    bez = Column(Text)
    bem = Column(Text)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    area_ha = Column(Numeric)
    count_hole = Column(Integer)
    path = Column(ARRAY(Integer()))
    is_hole = Column(Boolean)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    subst_sum = Column(Integer)
    subst_type = Column(Integer)


t_ego_political_boundary_hvmv_subst_per_gem_1_mview = Table(
    'ego_political_boundary_hvmv_subst_per_gem_1_mview', metadata,
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='model_draft'
)


t_ego_political_boundary_hvmv_subst_per_gem_2_mview = Table(
    'ego_political_boundary_hvmv_subst_per_gem_2_mview', metadata,
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='model_draft'
)


t_ego_political_boundary_hvmv_subst_per_gem_3_mview = Table(
    'ego_political_boundary_hvmv_subst_per_gem_3_mview', metadata,
    Column('id', Integer, unique=True),
    Column('gen', Text),
    Column('bez', Text),
    Column('ags_0', String(12)),
    Column('subst_type', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    schema='model_draft'
)


class EgoPoliticalBoundaryHvmvSubstPerGem3Nn(Base):
    __tablename__ = 'ego_political_boundary_hvmv_subst_per_gem_3_nn'
    __table_args__ = {'schema': 'model_draft'}

    mun_id = Column(Integer, primary_key=True)
    mun_ags_0 = Column(String(12))
    subst_ags_0 = Column(Text)
    subst_id = Column(Integer)
    subst_type = Column(Integer)
    geom_sub = Column(Geometry('POINT', 3035), index=True)
    distance = Column(Float(53))
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


t_ego_political_boundary_hvmv_subst_per_gem_3_nn_line = Table(
    'ego_political_boundary_hvmv_subst_per_gem_3_nn_line', metadata,
    Column('id', BigInteger, unique=True),
    Column('nn_id', Integer),
    Column('subst_id', Integer),
    Column('geom_centre', Geometry('POINT', 3035), index=True),
    Column('geom', Geometry('LINESTRING', 3035), index=True),
    schema='model_draft'
)


t_ego_political_boundary_hvmv_subst_per_gem_3_nn_union = Table(
    'ego_political_boundary_hvmv_subst_per_gem_3_nn_union', metadata,
    Column('subst_id', Integer, unique=True),
    Column('subst_type', Integer),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    schema='model_draft'
)


class EgoPowerClas(Base):
    __tablename__ = 'ego_power_class'
    __table_args__ = {'schema': 'model_draft'}

    power_class_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_power_class_power_class_id_seq'::regclass)"))
    lower_limit = Column(Float(53))
    upper_limit = Column(Float(53))
    wea = Column(Text)
    h_hub = Column(Float(53))
    d_rotor = Column(Float(53))


class EgoRenewableFeedin(Base):
    __tablename__ = 'ego_renewable_feedin'
    __table_args__ = {'schema': 'model_draft'}

    weather_scenario_id = Column(Integer, primary_key=True, nullable=False)
    w_id = Column(Integer, primary_key=True, nullable=False)
    source = Column(Text, primary_key=True, nullable=False)
    weather_year = Column(Integer, primary_key=True, nullable=False)
    power_class = Column(Integer, primary_key=True, nullable=False)
    feedin = Column(ARRAY(Float(precision=53)))


class EgoRenewableFeedinV031(Base):
    __tablename__ = 'ego_renewable_feedin_v031'
    __table_args__ = {'schema': 'model_draft'}

    weather_scenario_id = Column(Integer, primary_key=True, nullable=False)
    w_id = Column(Integer, primary_key=True, nullable=False)
    source = Column(Text, primary_key=True, nullable=False)
    weather_year = Column(Integer, primary_key=True, nullable=False)
    power_class = Column(Integer, primary_key=True, nullable=False)
    feedin = Column(ARRAY(Float(precision=53)))


t_ego_renewable_powerplant_eaa_mview = Table(
    'ego_renewable_powerplant_eaa_mview', metadata,
    Column('id', BigInteger, unique=True),
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
    schema='model_draft'
)


t_ego_renpassgis_simple_feedin_mview = Table(
    'ego_renpassgis_simple_feedin_mview', metadata,
    Column('hour', BigInteger),
    Column('generation_type', Text),
    Column('scenario', Text),
    Column('total_cap_feedin', Numeric),
    schema='model_draft'
)


t_ego_res_powerplant_costdat_gid = Table(
    'ego_res_powerplant_costdat_gid', metadata,
    Column('id', Integer),
    Column('coastdat_gid', BigInteger),
    schema='model_draft'
)


class EgoScenario(Base):
    __tablename__ = 'ego_scenario'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('model_draft.ego_scenario_id_seq'::regclass)"))
    model = Column(Text)
    version = Column(Text, primary_key=True, nullable=False)
    version_name = Column(Text)
    release = Column(Boolean)
    comment = Column(Text)
    timestamp = Column(DateTime)


class EgoScenarioInput(Base):
    __tablename__ = 'ego_scenario_input'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_scenario_input_id_seq'::regclass)"))
    version = Column(Text)
    oid = Column(OID)
    database = Column(String)
    table_schema = Column(String)
    table_name = Column(String)
    path = Column(Text)
    metadata_title = Column(Text)
    metadata_reference_date = Column(Text)
    meta_data = Column(Text)


class EgoScenarioOverview(Base):
    __tablename__ = 'ego_scenario_overview'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_scenario_overview_id_seq'::regclass)"))
    name = Column(Text)
    version = Column(Text)
    cnt = Column(Integer)


class EgoSimpleFeedinFull(Base):
    __tablename__ = 'ego_simple_feedin_full'
    __table_args__ = (
        Index('ego_simple_feedin_full_idx', 'scenario', 'sub_id'),
        {'schema': 'model_draft'}
    )

    hour = Column(BigInteger, primary_key=True, nullable=False)
    coastdat_id = Column(BigInteger, primary_key=True, nullable=False)
    sub_id = Column(BigInteger, primary_key=True, nullable=False)
    generation_type = Column(Text, primary_key=True, nullable=False)
    feedin = Column(Numeric(23, 20))
    scenario = Column(Text, primary_key=True, nullable=False)
    weighted_feedin = Column(Numeric(23, 20))


class EgoSmallChpPlantGermany(Base):
    __tablename__ = 'ego_small_chp_plant_germany'
    __table_args__ = {'schema': 'model_draft'}

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
    geom = Column(Geometry('POINT', 4326))


class EgoSocialZensusLoad(Base):
    __tablename__ = 'ego_social_zensus_load'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_social_zensus_load_id_seq'::regclass)"))
    gid = Column(Integer)
    population = Column(Integer)
    inside_la = Column(Boolean)
    geom_point = Column(Geometry('POINT', 3035), index=True)
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoSocialZensusLoadCluster(Base):
    __tablename__ = 'ego_social_zensus_load_cluster'
    __table_args__ = {'schema': 'model_draft'}

    cid = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_social_zensus_load_cluster_cid_seq'::regclass)"))
    zensus_sum = Column(Integer)
    area_ha = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035), index=True)
    geom_buffer = Column(Geometry('POLYGON', 3035))
    geom_centroid = Column(Geometry('POINT', 3035), index=True)
    geom_surfacepoint = Column(Geometry('POINT', 3035), index=True)


t_ego_society_zensus_per_la_mview = Table(
    'ego_society_zensus_per_la_mview', metadata,
    Column('name', Text),
    Column('sum', Numeric),
    Column('census_count', BigInteger),
    schema='model_draft'
)


class EgoStorageH2AreasDe(Base):
    __tablename__ = 'ego_storage_h2_areas_de'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_storage_h2_areas_de_gid_seq'::regclass)"))
    objectid = Column(Numeric(10, 0))
    bezeichnun = Column(String(50))
    salzstrukt = Column(String(50))
    id = Column(Integer)
    shape_star = Column(Numeric)
    shape_stle = Column(Numeric)
    geom = Column(Geometry('MULTIPOLYGON', 4326), index=True)


t_ego_supply_aggr_weather = Table(
    'ego_supply_aggr_weather', metadata,
    Column('aggr_id', BigInteger),
    Column('w_id', BigInteger),
    Column('scn_name', String),
    Column('bus', BigInteger),
    Column('row_number', BigInteger),
    schema='model_draft'
)


t_ego_supply_conv_nep2035_temp = Table(
    'ego_supply_conv_nep2035_temp', metadata,
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('la_id', Integer),
    Column('scenario', Text),
    Column('flag', Text),
    Column('nuts', String),
    schema='model_draft'
)


t_ego_supply_conv_powerplant = Table(
    'ego_supply_conv_powerplant', metadata,
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
    schema='model_draft'
)


t_ego_supply_conv_powerplant_2035 = Table(
    'ego_supply_conv_powerplant_2035', metadata,
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('la_id', Integer),
    Column('scenario', Text),
    Column('flag', Text),
    Column('nuts', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    schema='model_draft'
)


t_ego_supply_conv_powerplant_ego100_mview = Table(
    'ego_supply_conv_powerplant_ego100_mview', metadata,
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
    schema='model_draft'
)


t_ego_supply_conv_powerplant_nep2035_mview = Table(
    'ego_supply_conv_powerplant_nep2035_mview', metadata,
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
    schema='model_draft'
)


t_ego_supply_conv_powerplant_sq_mview = Table(
    'ego_supply_conv_powerplant_sq_mview', metadata,
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
    schema='model_draft'
)


class EgoSupplyGenerator(Base):
    __tablename__ = 'ego_supply_generator'
    __table_args__ = {'schema': 'model_draft'}

    un_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_generator_un_id_seq'::regclass)"))
    re_id = Column(Integer)
    conv_id = Column(Integer)
    aggr_id_pf = Column(Integer)
    aggr_id_ms = Column(Integer)
    geom = Column(Geometry('POINT', 4326), index=True)


class EgoSupplyGeneratorNep2035(Base):
    __tablename__ = 'ego_supply_generator_nep2035'
    __table_args__ = {'schema': 'model_draft'}

    un_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_generator_nep2035_un_id_seq'::regclass)"))
    re_id = Column(BigInteger)
    conv_id = Column(BigInteger)
    aggr_id_pf = Column(BigInteger)
    aggr_id_ms = Column(BigInteger)
    geom = Column(Geometry('POINT', 4326), index=True)


class EgoSupplyGeneratorTest(Base):
    __tablename__ = 'ego_supply_generator_test'
    __table_args__ = {'schema': 'model_draft'}

    un_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_generator_test_un_id_seq'::regclass)"))
    re_id = Column(Integer)
    conv_id = Column(Integer)
    aggr_id_pf = Column(Integer)
    aggr_id_ms = Column(Integer)
    geom = Column(Geometry('POINT', 4326), index=True)


class EgoSupplyRea(Base):
    __tablename__ = 'ego_supply_rea'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    electrical_capacity = Column(Numeric)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(SmallInteger)
    postcode = Column(String)
    source = Column(String)
    subst_id = Column(BigInteger)
    la_id = Column(Integer)
    sort = Column(Integer)
    flag = Column(String)
    geom = Column(Geometry('POINT', 3035), index=True)
    geom_line = Column(Geometry('LINESTRING', 3035), index=True)
    geom_new = Column(Geometry('POINT', 3035), index=True)


t_ego_supply_rea_m1_1_mview = Table(
    'ego_supply_rea_m1_1_mview', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m1_1_rest_mview = Table(
    'ego_supply_rea_m1_1_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m1_2_mview = Table(
    'ego_supply_rea_m1_2_mview', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m1_2_rest_mview = Table(
    'ego_supply_rea_m1_2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m2_mview = Table(
    'ego_supply_rea_m2_mview', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m2_rest_mview = Table(
    'ego_supply_rea_m2_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


class EgoSupplyReaM2Windfarm(Base):
    __tablename__ = 'ego_supply_rea_m2_windfarm'
    __table_args__ = {'schema': 'model_draft'}

    farm_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_rea_m2_windfarm_farm_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    dea_cnt = Column(Integer)
    electrical_capacity_sum = Column(Numeric)
    rea_geom_new = Column(Geometry('POLYGON', 3035))
    rea_geom_line = Column(Geometry('LINESTRING', 3035))
    geom = Column(Geometry('POLYGON', 3035), index=True)


t_ego_supply_rea_m3_mview = Table(
    'ego_supply_rea_m3_mview', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m3_rest_mview = Table(
    'ego_supply_rea_m3_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m4_mview = Table(
    'ego_supply_rea_m4_mview', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m4_rest_mview = Table(
    'ego_supply_rea_m4_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m5_mview = Table(
    'ego_supply_rea_m5_mview', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_rea_m5_rest_2_mview = Table(
    'ego_supply_rea_m5_rest_2_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_m5_rest_mview = Table(
    'ego_supply_rea_m5_rest_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('subst_id', BigInteger),
    Column('geom', Geometry, index=True),
    Column('rea_flag', String),
    schema='model_draft'
)


t_ego_supply_rea_out_mview = Table(
    'ego_supply_rea_out_mview', metadata,
    Column('id', BigInteger),
    Column('electrical_capacity', Numeric),
    Column('generation_type', Text),
    Column('generation_subtype', String),
    Column('voltage_level', SmallInteger),
    Column('postcode', String),
    Column('source', String),
    Column('subst_id', BigInteger),
    Column('la_id', Integer),
    Column('sort', Integer),
    Column('flag', String),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


class EgoSupplyReaPerGentypeAndVoltlevel(Base):
    __tablename__ = 'ego_supply_rea_per_gentype_and_voltlevel'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True)
    generation_type = Column(Text)
    generation_subtype = Column(String)
    voltage_level = Column(SmallInteger)
    capacity = Column(Numeric)
    count = Column(BigInteger)


class EgoSupplyReaPerLoadarea(Base):
    __tablename__ = 'ego_supply_rea_per_loadarea'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    subst_id = Column(Integer)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)


class EgoSupplyReaPerMethod(Base):
    __tablename__ = 'ego_supply_rea_per_method'
    __table_args__ = {'schema': 'model_draft'}

    name = Column(Text, primary_key=True)
    capacity = Column(Numeric)
    count = Column(BigInteger)


class EgoSupplyReaPerMvgd(Base):
    __tablename__ = 'ego_supply_rea_per_mvgd'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(Integer, primary_key=True)
    dea_cnt = Column(Integer)
    dea_capacity = Column(Numeric)
    lv_dea_cnt = Column(Integer)
    lv_dea_capacity = Column(Numeric)
    mv_dea_cnt = Column(Integer)
    mv_dea_capacity = Column(Numeric)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)


class EgoSupplyRenewableBnetzaFullAttribute(Base):
    __tablename__ = 'ego_supply_renewable_bnetza_full_attribute'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True)
    meldedatum = Column(String(254))
    meldegrund = Column(String(254))
    anlagennummer = Column(String(254))
    eeg_anlagenschluessel = Column(String(254))
    genehmigungs_datum = Column(String(254))
    genehmigungs_behoerde = Column(String(254))
    genehmigungs_aktenzeichen = Column(String(254))
    geplantes_inbetriebnahme_datum = Column(String(254))
    errichtungs_frist = Column(String(254))
    energietraeger = Column(String(254))
    installierte_leistung = Column(String(254))
    inst_leistung_vor_leistungs_aenderung = Column(Numeric)
    inst_leistung_nach_leistungs_aenderung = Column(Numeric)
    tatsächliche_inbetriebnahme = Column(String(254))
    datum_leistungs_aenderung = Column(String(254))
    stilllegungs_datum = Column(String(254))
    name_der_anlage = Column(String(254))
    strasse = Column(String(254))
    hausnummer = Column(String(254))
    plz = Column(String(254))
    ort = Column(String(254))
    gemeinde_schluessel = Column('gemeinde-schluessel', String(254))
    bundesland = Column(String(254))
    utm_zonenwert = Column('utm-zonenwert', String(254))
    utm_east = Column('utm-east', Numeric)
    utm_east_neu = Column('utm-east_neu', Numeric)
    utm_north = Column('utm-north', Numeric)
    zugehoehrigkeit_anlagenpark = Column(String(254))
    name_des_anlagenparks = Column(String(254))
    spannungsebene = Column(String(254))
    netzanschlusspunkt = Column(String(254))
    zaehlpunktbezeichnung = Column(String(254))
    name_des_netzbetreibers = Column(String(254))
    fernsteuerbarkeit_durch = Column(String(254))
    gemeinsame_techn_einrichtung = Column(String(254))
    inanspruchnahme_finanzieller_foerderung = Column(String(254))
    eigenverbrauch_geplant = Column(String(254))
    eingesetzte_biomasse = Column(String(254))
    ausschliesslich_Biomasse = Column(String(254))
    flexpraemie = Column(String(254))
    erstmalige_inanspruchnahme_flexpraemie = Column(String(254))
    leistungserhoehung_flexpraemie = Column(String(254))
    datum_leistungserhoehung_flexpraemie = Column(String(254))
    umfang_der_leistungserhoehung = Column(String(254))
    erstmalig_ausschliesslich_biomethan = Column(String(254))
    zustimmung_gesonderte_veröeffentlichung_biomethanstilllegung = Column(String(254))
    kwk_anlage = Column(String(254))
    thermische_leistung = Column(String(254))
    andere_energietraeger = Column(String(254))
    eingesetzte_andere_energietraeger = Column(String(254))
    erstmalige_stromerzeugung = Column(String(254))
    windanlagenhersteller = Column(String(254))
    anlagentyp = Column(String(254))
    nabenhoehe = Column(String(254))
    rotordurchmesser = Column(String(254))
    repowering = Column(String(254))
    stillgelegt = Column(String(254))
    _7_7_1_mitt = Column('7_7_1_mitt', String(254))
    _7_7_2_form = Column('7_7_2_form', String(254))
    _7_7_3_skal = Column('7_7_3_skal', Numeric)
    _7_7_4_ertr = Column('7_7_4_ertr', Numeric)
    _7_7_5_ertr = Column('7_7_5_ertr', Numeric)
    _7_8_1_seel = Column('7_8_1_seel', String(254))
    _7_8_2_wass = Column('7_8_2_wass', String(254))
    _7_8_3_küs = Column('7_8_3_k\xfcs', String(254))
    _8_1_ertüc = Column('8_1_ert\xfcc', String(254))
    _8_2_art_de = Column('8_2_art_de', String(254))
    _8_3_zulass = Column('8_3_zulass', String(254))
    _8_4_höhe = Column('8_4_h\xf6he', String(254))
    _8_5_datum = Column('8_5_datum', String(254))
    _9_1_zuschl = Column('9_1_zuschl', String(254))
    _9_2_wie_vi = Column('9_2_wie_vi', String(254))
    _9_3_wie_vi = Column('9_3_wie_vi', String(254))
    field_74 = Column(Numeric)
    field_75 = Column(Numeric)
    field_76 = Column(String(254))
    field_77 = Column(String(254))
    field_78 = Column(String(254))
    field_79 = Column(String(254))
    field_80 = Column(String(254))
    field_81 = Column(String(254))
    field_82 = Column(String(254))
    field_83 = Column(String(254))
    field_84 = Column(String(254))
    field_85 = Column(Numeric)
    field_86 = Column(Numeric(10, 0))
    field_87 = Column(String(254))
    field_88 = Column(String(254))
    geom = Column(Geometry('POINT', 25832), index=True)


t_ego_supply_res_biomass_2035_temp = Table(
    'ego_supply_res_biomass_2035_temp', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry, index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Text),
    Column('rea_geom_new', Text),
    Column('scenario', Text),
    Column('flag', Text),
    Column('nuts', String),
    schema='model_draft'
)


t_ego_supply_res_biomass_2050_temp = Table(
    'ego_supply_res_biomass_2050_temp', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 3035), index=True),
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
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    schema='model_draft'
)


t_ego_supply_res_chp_2050_temp = Table(
    'ego_supply_res_chp_2050_temp', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 3035), index=True),
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
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    schema='model_draft'
)


t_ego_supply_res_hydro_2035_temp = Table(
    'ego_supply_res_hydro_2035_temp', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Text),
    Column('rea_geom_new', Text),
    Column('scenario', Text),
    Column('flag', Text),
    Column('nuts', String),
    schema='model_draft'
)


t_ego_supply_res_hydro_2050_temp = Table(
    'ego_supply_res_hydro_2050_temp', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 3035), index=True),
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
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    schema='model_draft'
)


class EgoSupplyResPowerplant(Base):
    __tablename__ = 'ego_supply_res_powerplant'
    __table_args__ = {'schema': 'model_draft'}

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
    rea_geom_new = Column(Geometry('POINT', 3035))


t_ego_supply_res_powerplant_ego100_mview = Table(
    'ego_supply_res_powerplant_ego100_mview', metadata,
    Column('preversion', Text),
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
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    schema='model_draft'
)


t_ego_supply_res_powerplant_nep2035_mview = Table(
    'ego_supply_res_powerplant_nep2035_mview', metadata,
    Column('preversion', Text),
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
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    schema='model_draft'
)


t_ego_supply_res_powerplant_out_mview = Table(
    'ego_supply_res_powerplant_out_mview', metadata,
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('rea_geom_new', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ego_supply_res_powerplant_sq_mview = Table(
    'ego_supply_res_powerplant_sq_mview', metadata,
    Column('preversion', Text),
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
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('w_id', BigInteger),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    schema='model_draft'
)


class EgoSupplyResPv2035GermanyMunTemp(Base):
    __tablename__ = 'ego_supply_res_pv_2035_germany_mun_temp'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.ego_supply_pv_dev_2035_germany_mun_id_seq'::regclass)"))
    pv_units = Column(Integer)
    pv_cap_2014 = Column(Integer)
    pv_add_cap_2035 = Column(Integer)
    voltage_level = Column(SmallInteger)
    rs = Column(String(12))
    pv_avg_cap = Column(Integer)
    pv_new_units = Column(Integer)


class EgoSupplyResPv2050GermanyMunTemp(Base):
    __tablename__ = 'ego_supply_res_pv_2050_germany_mun_temp'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.ego_supply_res_pv_2050_germany_mun_id_seq'::regclass)"))
    pv_units = Column(Integer)
    pv_cap_2035 = Column(Integer)
    pv_add_cap_2050 = Column(Integer)
    voltage_level = Column(SmallInteger)
    rs = Column(String(12))
    pv_avg_cap = Column(Integer)
    pv_new_units = Column(Integer)


class EgoSupplyResPvToRegionTemp(Base):
    __tablename__ = 'ego_supply_res_pv_to_region_temp'
    __table_args__ = {'schema': 'model_draft'}

    re_id = Column(BigInteger, primary_key=True)
    subst_id = Column(BigInteger)
    otg_id = Column(BigInteger)
    un_id = Column(BigInteger)
    nuts = Column(String(5))
    rs = Column(String(12))
    id_vg250 = Column(BigInteger)


class EgoSupplyResWo2035GermanyMunTemp(Base):
    __tablename__ = 'ego_supply_res_wo_2035_germany_mun_temp'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.ego_supply_res_wo_2035_germany_mun_id_seq'::regclass)"))
    wo_units = Column(Integer)
    wo_cap_2014 = Column(Integer)
    wo_add_cap_2035 = Column(Integer)
    voltage_level = Column(SmallInteger)
    rs = Column(String(12))
    wo_avg_cap = Column(Integer)
    wo_new_units = Column(Integer)


class EgoSupplyResWo2050GermanyMunTemp(Base):
    __tablename__ = 'ego_supply_res_wo_2050_germany_mun_temp'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.ego_supply_res_wo_2050_germany_mun_id_seq'::regclass)"))
    wo_units = Column(Integer)
    wo_cap_2035 = Column(Integer)
    wo_add_cap_2050 = Column(Integer)
    voltage_level = Column(SmallInteger)
    rs = Column(String(12))
    wo_avg_cap = Column(Integer)
    wo_new_units = Column(Integer)


t_ego_supply_res_woff_2035_temp = Table(
    'ego_supply_res_woff_2035_temp', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 4326), index=True),
    Column('subst_id', BigInteger),
    Column('otg_id', BigInteger),
    Column('un_id', BigInteger),
    Column('voltage_level', SmallInteger),
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    Column('la_id', Integer),
    Column('mvlv_subst_id', Integer),
    Column('rea_sort', Integer),
    Column('rea_flag', String),
    Column('rea_geom_line', Geometry('LINESTRING', 3035)),
    Column('rea_geom_new', Geometry('POINT', 3035)),
    schema='model_draft'
)


t_ego_supply_res_woff_2050_temp = Table(
    'ego_supply_res_woff_2050_temp', metadata,
    Column('preversion', Text),
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
    Column('geom', Geometry('POINT', 3035), index=True),
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
    Column('scenario', String),
    Column('flag', String),
    Column('nuts', String),
    schema='model_draft'
)


class EgoSupplyScenarioCapacity(Base):
    __tablename__ = 'ego_supply_scenario_capacities'
    __table_args__ = {'schema': 'model_draft'}

    state = Column(CHAR(50), nullable=False)
    generation_type = Column(CHAR(25), primary_key=True, nullable=False)
    capacity = Column(Numeric(15, 0))
    nuts = Column(CHAR(12), primary_key=True, nullable=False)
    scenario_name = Column(CHAR(50), primary_key=True, nullable=False)


class EgoSupplyWpaPerMvgd(Base):
    __tablename__ = 'ego_supply_wpa_per_mvgd'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ego_supply_wpa_per_mvgd_id_seq'::regclass)"))
    subst_id = Column(Integer)
    area_ha = Column(Float(53))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class EgoWeatherMeasurementPoint(Base):
    __tablename__ = 'ego_weather_measurement_point'
    __table_args__ = {'schema': 'model_draft'}

    coastdat_id = Column(BigInteger, primary_key=True, nullable=False)
    type_of_generation = Column(Text, primary_key=True, nullable=False)
    geom = Column(Geometry('POINT', 4326))


t_ev_charging_berlin_parking_poly = Table(
    'ev_charging_berlin_parking_poly', metadata,
    Column('osm_id', BigInteger),
    Column('tags', HSTORE(Text())),
    Column('geom', Geometry, index=True),
    schema='model_draft'
)


t_ev_charging_berlin_parking_pts = Table(
    'ev_charging_berlin_parking_pts', metadata,
    Column('osm_id', BigInteger),
    Column('tags', HSTORE(Text())),
    Column('geom', Geometry),
    schema='model_draft'
)


t_ev_charging_berlin_shops_pts = Table(
    'ev_charging_berlin_shops_pts', metadata,
    Column('osm_id', BigInteger),
    Column('tags', HSTORE(Text())),
    Column('geom', Geometry),
    schema='model_draft'
)


t_ev_charging_bonn_poi_points = Table(
    'ev_charging_bonn_poi_points', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('amenity', String(50)),
    Column('weight', Integer),
    schema='model_draft'
)


t_ev_charging_bonn_shops = Table(
    'ev_charging_bonn_shops', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POINT', 3035)),
    Column('amenity', String(50)),
    schema='model_draft'
)


t_ev_charging_bonn_shops_clusters = Table(
    'ev_charging_bonn_shops_clusters', metadata,
    Column('npoints', Integer),
    Column('geom', Geometry),
    schema='model_draft'
)


class EvChargingBrandenburgStreetseg(Base):
    __tablename__ = 'ev_charging_brandenburg_streetsegs'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_brandenburg_streetsegs_id_seq'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Numeric)


t_ev_charging_buildings_berlin = Table(
    'ev_charging_buildings_berlin', metadata,
    Column('gid', Integer, unique=True),
    Column('geom', Geometry, index=True),
    schema='model_draft'
)


class EvChargingCandidatepoint(Base):
    __tablename__ = 'ev_charging_candidatepoints'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_candidatepoints_id_seq'::regclass)"))
    geom = Column(Geometry('POINT', 3035), index=True)


class EvChargingCensusblocksSpiekeroog(Base):
    __tablename__ = 'ev_charging_censusblocks_spiekeroog'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_censusblocks_spiekeroog_id_seq'::regclass)"))
    population = Column(Integer)
    geom = Column(Geometry('POLYGON', 3035))


t_ev_charging_chosenpoints = Table(
    'ev_charging_chosenpoints', metadata,
    Column('id', Integer),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('current_cp', Boolean),
    schema='model_draft'
)


t_ev_charging_coverage_bundesland = Table(
    'ev_charging_coverage_bundesland', metadata,
    Column('osm_id', BigInteger),
    Column('geom', Geometry),
    schema='model_draft'
)


class EvChargingDistrict(Base):
    __tablename__ = 'ev_charging_districts'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_districts_id_seq'::regclass)"))
    district_name = Column(String(50))
    geom = Column(Geometry('MULTIPOLYGON', 4326))


t_ev_charging_essen_charging_points = Table(
    'ev_charging_essen_charging_points', metadata,
    Column('ge_id', Text),
    Column('lat', Float(53)),
    Column('lng', Float(53)),
    Column('charger_count', Integer),
    Column('power_kwh', Float(53)),
    Column('charger_type', Text),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_ev_charging_essen_districtdata = Table(
    'ev_charging_essen_districtdata', metadata,
    Column('index', BigInteger, index=True),
    Column('Name', Text),
    Column('geom', Geometry('MULTIPOLYGON', 3035), index=True),
    Column('Wohnungsbezogene Charakterisierung', Text),
    Column('Sozialraeumliche Charakterisierung', Text),
    Column('Mietspiegel', Float(53)),
    Column('Flaeche [m2]', BigInteger),
    Column('bebaute Flaeche', BigInteger),
    Column('Bevoelkerung', BigInteger),
    Column('Anteil 18-25', Float(53)),
    Column('Anteil 25-45', Float(53)),
    Column('Anteil 45-65', Float(53)),
    Column('Durchschnittsalter [a]', Float(53)),
    Column('Privathaushalte', BigInteger),
    Column('Einpersonenhaushalte', BigInteger),
    Column('Haushalte mit minderj. Kindern', BigInteger),
    Column('durchschn. Haushaltsgroe\xdfe', Float(53)),
    Column('Geb/Sterb', BigInteger),
    Column('Wanderung', BigInteger),
    Column('Wohnungen je Gebaeude', Float(53)),
    Column('Wohnflaeche [m2]', BigInteger),
    Column('Pkw', BigInteger),
    Column('Pkw natuerlicher Personen', BigInteger),
    Column('sozpflichtig beschaeftigte', BigInteger),
    Column('Arbeitslose', BigInteger),
    Column('Gruenwaehler', BigInteger),
    schema='model_draft'
)


t_ev_charging_geom_essen = Table(
    'ev_charging_geom_essen', metadata,
    Column('geom', Geometry),
    schema='model_draft'
)


t_ev_charging_geom_essen2 = Table(
    'ev_charging_geom_essen2', metadata,
    Column('geom', Geometry('MULTIPOLYGON', 31467)),
    schema='model_draft'
)


t_ev_charging_geom_potsdam = Table(
    'ev_charging_geom_potsdam', metadata,
    Column('geom', Geometry('MULTIPOLYGON', 31467)),
    schema='model_draft'
)


t_ev_charging_geom_spiekeroog = Table(
    'ev_charging_geom_spiekeroog', metadata,
    Column('geom', Geometry),
    schema='model_draft'
)


t_ev_charging_giessen_poi_points_ = Table(
    'ev_charging_giessen_poi_points_', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('amenity', String(50)),
    Column('weight', Integer),
    schema='model_draft'
)


t_ev_charging_giessen_poi_points__clusters = Table(
    'ev_charging_giessen_poi_points__clusters', metadata,
    Column('npoints', Integer),
    Column('geom', Geometry, index=True),
    schema='model_draft'
)


class EvChargingGiessenStreet(Base):
    __tablename__ = 'ev_charging_giessen_streets'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.\"ev_charging_gießen_streets_id_seq\"'::regclass)"))
    osm_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Numeric)
    highway = Column(HSTORE(Text()))


class EvChargingGiessenStreetsSegmented(Base):
    __tablename__ = 'ev_charging_giessen_streets_segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.\"ev_charging_gießen_streets_segmented_id_seq\"'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Float(53))


t_ev_charging_nodebetweenness = Table(
    'ev_charging_nodebetweenness', metadata,
    Column('node_id', Integer),
    Column('x', Float(53)),
    Column('node_betweenness', Float(53)),
    Column('y', Float(53)),
    Column('geom', Geometry('POINT', 3035)),
    schema='model_draft'
)


t_ev_charging_nxcoverage_ = Table(
    'ev_charging_nxcoverage_', metadata,
    Column('index', BigInteger, index=True),
    Column('status', Text),
    Column('weight', Float(53)),
    Column('x1', Float(53)),
    Column('x2', Float(53)),
    Column('y1', Float(53)),
    Column('y2', Float(53)),
    Column('geom', Geometry('LINESTRING', 3035)),
    schema='model_draft'
)


t_ev_charging_nxcoverage_Friedland = Table(
    'ev_charging_nxcoverage_Friedland', metadata,
    Column('index', BigInteger, index=True),
    Column('status', Text),
    Column('weight', Float(53)),
    Column('x1', Float(53)),
    Column('x2', Float(53)),
    Column('y1', Float(53)),
    Column('y2', Float(53)),
    Column('geom', Geometry('LINESTRING', 3035)),
    schema='model_draft'
)


t_ev_charging_nxcoverage_Gießen = Table(
    'ev_charging_nxcoverage_Gie\xdfen', metadata,
    Column('index', BigInteger, index=True),
    Column('status', Text),
    Column('weight', Float(53)),
    Column('x1', Float(53)),
    Column('x2', Float(53)),
    Column('y1', Float(53)),
    Column('y2', Float(53)),
    schema='model_draft'
)


t_ev_charging_nxcoverage_friedland = Table(
    'ev_charging_nxcoverage_friedland', metadata,
    Column('index', BigInteger, index=True),
    Column('status', Text),
    Column('weight', Float(53)),
    Column('x1', Float(53)),
    Column('x2', Float(53)),
    Column('y1', Float(53)),
    Column('y2', Float(53)),
    Column('geom', Geometry('LINESTRING', 3035)),
    schema='model_draft'
)


t_ev_charging_nxcoverage_gießen = Table(
    'ev_charging_nxcoverage_gie\xdfen', metadata,
    Column('index', BigInteger, index=True),
    Column('status', Text),
    Column('weight', Float(53)),
    Column('x1', Float(53)),
    Column('x2', Float(53)),
    Column('y1', Float(53)),
    Column('y2', Float(53)),
    Column('geom', Geometry('LINESTRING', 3035)),
    schema='model_draft'
)


t_ev_charging_nxcoverage_winterberg = Table(
    'ev_charging_nxcoverage_winterberg', metadata,
    Column('index', BigInteger, index=True),
    Column('status', Text),
    Column('weight', Float(53)),
    Column('x1', Float(53)),
    Column('x2', Float(53)),
    Column('y1', Float(53)),
    Column('y2', Float(53)),
    Column('geom', Geometry('LINESTRING', 3035)),
    schema='model_draft'
)


t_ev_charging_parking_points_berlin = Table(
    'ev_charging_parking_points_berlin', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POINT', 3035)),
    Column('amenity', String(50)),
    schema='model_draft'
)


t_ev_charging_parking_polygons_berlin = Table(
    'ev_charging_parking_polygons_berlin', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POLYGON', 3035)),
    Column('amenity', String(50)),
    schema='model_draft'
)


t_ev_charging_poi = Table(
    'ev_charging_poi', metadata,
    Column('osm_id', BigInteger),
    Column('geom', Geometry('POINT', 3035)),
    Column('amenity', Text),
    Column('weight', Integer),
    schema='model_draft'
)


class EvChargingPoiCluster(Base):
    __tablename__ = 'ev_charging_poi_clusters'
    __table_args__ = {'schema': 'model_draft'}

    npoints = Column(Integer)
    geom = Column(Geometry)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_poi_clusters_id_seq'::regclass)"))


t_ev_charging_poi_point = Table(
    'ev_charging_poi_point', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POINT', 3035)),
    Column('amenity', String(50)),
    schema='model_draft'
)


t_ev_charging_poi_points_berlin = Table(
    'ev_charging_poi_points_berlin', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POINT', 3035)),
    Column('amenity', String(50)),
    Column('weight', Integer),
    schema='model_draft'
)


class EvChargingPoiPointsBerlinCluster(Base):
    __tablename__ = 'ev_charging_poi_points_berlin_clusters'
    __table_args__ = {'schema': 'model_draft'}

    npoints = Column(Integer)
    geom = Column(Geometry)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_poi_points_berlin_clusters_id_seq'::regclass)"))


t_ev_charging_poi_points_essen = Table(
    'ev_charging_poi_points_essen', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POINT', 3035)),
    Column('amenity', String(50)),
    schema='model_draft'
)


t_ev_charging_poi_points_giessen = Table(
    'ev_charging_poi_points_giessen', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POINT', 3035)),
    Column('amenity', String(50)),
    schema='model_draft'
)


t_ev_charging_poi_points_potsdam = Table(
    'ev_charging_poi_points_potsdam', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POINT', 3035)),
    Column('amenity', String(50)),
    Column('weight', Integer),
    schema='model_draft'
)


class EvChargingPoiPointsPotsdamCluster(Base):
    __tablename__ = 'ev_charging_poi_points_potsdam_clusters'
    __table_args__ = {'schema': 'model_draft'}

    npoints = Column(Integer)
    geom = Column(Geometry)
    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_poi_points_potsdam_clusters_id_seq'::regclass)"))


t_ev_charging_poi_polygon = Table(
    'ev_charging_poi_polygon', metadata,
    Column('id', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    Column('amenity', String(50)),
    schema='model_draft'
)


t_ev_charging_poi_polygon_essen = Table(
    'ev_charging_poi_polygon_essen', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry('POLYGON', 3035)),
    Column('amenity', String(50)),
    schema='model_draft'
)


t_ev_charging_poi_test = Table(
    'ev_charging_poi_test', metadata,
    Column('osm_id', BigInteger),
    Column('geom', Geometry('POINT', 3035)),
    Column('amenity', Text),
    schema='model_draft'
)


t_ev_charging_population_per_ha_berlin = Table(
    'ev_charging_population_per_ha_berlin', metadata,
    Column('gid', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    Column('population', Numeric(10, 0)),
    Column('perc_builtup_ha', Float(53)),
    Column('builtup_m2_per_person', Float(53)),
    schema='model_draft'
)


t_ev_charging_preprocess_segments = Table(
    'ev_charging_preprocess_segments', metadata,
    Column('id', BigInteger),
    Column('geom', Text),
    schema='model_draft'
)


t_ev_charging_saarland_streets_ = Table(
    'ev_charging_saarland_streets_', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry, index=True),
    schema='model_draft'
)


class EvChargingSaarlandStreetsSegmented(Base):
    __tablename__ = 'ev_charging_saarland_streets__segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_saarland_streets__segmented_id_seq'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Float(53))


class EvChargingStreetSegment(Base):
    __tablename__ = 'ev_charging_street_segments'
    __table_args__ = {'schema': 'model_draft'}

    geom_startpt = Column(Geometry)
    geom_endpt = Column(Geometry)
    geom = Column(Geometry)
    length = Column(Float(53))
    startpt_id = Column(Integer, nullable=False, server_default=text("nextval('model_draft.ev_charging_street_segments_startpt_id_seq'::regclass)"))
    endpt_id = Column(Integer, nullable=False, server_default=text("nextval('model_draft.ev_charging_street_segments_endpt_id_seq'::regclass)"))
    line_id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_street_segments_line_id_seq'::regclass)"))


class EvChargingStreet(Base):
    __tablename__ = 'ev_charging_streets'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_id_seq'::regclass)"))
    osm_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Numeric)


class EvChargingStreetsBerlin(Base):
    __tablename__ = 'ev_charging_streets_berlin'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_berlin_id_seq'::regclass)"))
    osm_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Numeric)
    highway = Column(HSTORE(Text()))


class EvChargingStreetsBerlinSegmented(Base):
    __tablename__ = 'ev_charging_streets_berlin_segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_berlin_segmented_id_seq'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Float(53))


t_ev_charging_streets_brandenburg = Table(
    'ev_charging_streets_brandenburg', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry),
    schema='model_draft'
)


class EvChargingStreetsBrandenburgSegmented(Base):
    __tablename__ = 'ev_charging_streets_brandenburg_segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_brandenburg_segmented_id_seq'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Float(53))


class EvChargingStreetsDittwar(Base):
    __tablename__ = 'ev_charging_streets_dittwar'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_dittwar_id_seq'::regclass)"))
    osm_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Numeric)
    highway = Column(HSTORE(Text()))


class EvChargingStreetsDittwarSegmented(Base):
    __tablename__ = 'ev_charging_streets_dittwar_segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_dittwar_segmented_id_seq'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Float(53))


class EvChargingStreetsEssen(Base):
    __tablename__ = 'ev_charging_streets_essen'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_essen_id_seq'::regclass)"))
    osm_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Numeric)
    highway = Column(HSTORE(Text()))


class EvChargingStreetsEssenSegmented(Base):
    __tablename__ = 'ev_charging_streets_essen_segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_essen_segmented_id_seq'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Float(53))


class EvChargingStreetsFriedland(Base):
    __tablename__ = 'ev_charging_streets_friedland'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_friedland_id_seq'::regclass)"))
    osm_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Numeric)
    highway = Column(HSTORE(Text()))


class EvChargingStreetsFriedlandSegmented(Base):
    __tablename__ = 'ev_charging_streets_friedland_segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_friedland_segmented_id_seq'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Float(53))


class EvChargingStreetsGiessen(Base):
    __tablename__ = 'ev_charging_streets_giessen'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.\"ev_charging_streets_gießen_id_seq\"'::regclass)"))
    osm_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Numeric)
    highway = Column(HSTORE(Text()))


class EvChargingStreetsGiessenSegmented(Base):
    __tablename__ = 'ev_charging_streets_giessen_segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.\"ev_charging_streets_gießen_segmented_id_seq\"'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Float(53))


t_ev_charging_streets_hessen = Table(
    'ev_charging_streets_hessen', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry),
    schema='model_draft'
)


class EvChargingStreetsHessenSegmented(Base):
    __tablename__ = 'ev_charging_streets_hessen_segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_hessen_segmented_id_seq'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Float(53))


t_ev_charging_streets_saarland = Table(
    'ev_charging_streets_saarland', metadata,
    Column('id', BigInteger),
    Column('geom', Geometry),
    schema='model_draft'
)


class EvChargingStreetsSaarlandSegmented(Base):
    __tablename__ = 'ev_charging_streets_saarland_segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_saarland_segmented_id_seq'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Float(53))


class EvChargingStreetsSpiekeroog(Base):
    __tablename__ = 'ev_charging_streets_spiekeroog'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_spiekeroog_id_seq'::regclass)"))
    osm_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Numeric)
    highway = Column(HSTORE(Text()))


class EvChargingStreetsSpiekeroogSegmented(Base):
    __tablename__ = 'ev_charging_streets_spiekeroog_segmented'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streets_spiekeroog_segmented_id_seq'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Float(53))


t_ev_charging_streetsbrandenburg = Table(
    'ev_charging_streetsbrandenburg', metadata,
    Column('osm_id', BigInteger),
    Column('geom', Geometry),
    schema='model_draft'
)


class EvChargingStreetseg(Base):
    __tablename__ = 'ev_charging_streetsegs'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streetsegs_id_seq1'::regclass)"))
    x1 = Column(Float(53))
    y1 = Column(Float(53))
    x2 = Column(Float(53))
    y2 = Column(Float(53))
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Numeric)


class EvChargingStreetsegsBrandenburg(Base):
    __tablename__ = 'ev_charging_streetsegs_brandenburg'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_streetsegs_id_seq'::regclass)"))
    x1 = Column(Numeric)
    y1 = Column(Numeric)
    x2 = Column(Numeric)
    y2 = Column(Numeric)
    geom = Column(Geometry('LINESTRING', 3035))
    length = Column(Numeric)


class EvChargingTestInsertWitha(Base):
    __tablename__ = 'ev_charging_test_insert_withas'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_test_insert_withas_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON', 3035))


t_ev_charging_testpandasupload = Table(
    'ev_charging_testpandasupload', metadata,
    Column('index', BigInteger, index=True),
    Column('Name', Text),
    Column('Koordinaten', Text),
    schema='model_draft'
)


t_ev_charging_top_censusblocks = Table(
    'ev_charging_top_censusblocks', metadata,
    Column('cb_id', Integer),
    Column('district_name', String(50)),
    Column('population', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    Column('lng', Float(53)),
    Column('lat', Float(53)),
    schema='model_draft'
)


t_ev_charging_top_censusblocks_giessen = Table(
    'ev_charging_top_censusblocks_giessen', metadata,
    Column('cb_id', Integer),
    Column('district_name', String(50)),
    Column('population', Integer),
    Column('geom', Geometry('POLYGON', 3035)),
    Column('lng', Float(53)),
    Column('lat', Float(53)),
    schema='model_draft'
)


class EvChargingWinterbergStreet(Base):
    __tablename__ = 'ev_charging_winterberg_streets'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ev_charging_winterberg_streets_id_seq'::regclass)"))
    osm_id = Column(Integer)
    geom = Column(Geometry('LINESTRING', 3035), index=True)
    length = Column(Numeric)
    highway = Column(HSTORE(Text()))


t_ev_charging_x2test_graphtotable = Table(
    'ev_charging_x2test_graphtotable', metadata,
    Column('node_id', Integer),
    Column('x', Float(53)),
    Column('y', Float(53)),
    schema='model_draft'
)


t_ev_charging_xtest_graphtotable = Table(
    'ev_charging_xtest_graphtotable', metadata,
    Column('node_id1', Integer),
    Column('node_id2', Integer),
    Column('weight', Float(53)),
    schema='model_draft'
)


t_ev_charging_xxtestedges = Table(
    'ev_charging_xxtestedges', metadata,
    Column('node_id1', Integer),
    Column('node_id2', Integer),
    Column('edge_betweenness', Float(53)),
    Column('y1', Float(53)),
    Column('x2', Float(53)),
    Column('weight', Float(53)),
    Column('y2', Float(53)),
    Column('x1', Float(53)),
    Column('geom', Geometry('LINESTRING', 3035)),
    schema='model_draft'
)


t_ev_charging_xxtestnodes = Table(
    'ev_charging_xxtestnodes', metadata,
    Column('node_id', Integer),
    Column('x', Float(53)),
    Column('y', Float(53)),
    Column('node_betweenness', Float(53)),
    Column('geom', Geometry('POINT', 3035)),
    schema='model_draft'
)


t_ev_charging_xxxx = Table(
    'ev_charging_xxxx', metadata,
    Column('node_id', Integer),
    Column('var2', Integer),
    Column('betweenness', Float(53)),
    Column('var3', Float(53)),
    Column('var4', Integer),
    schema='model_draft'
)


t_ev_charging_xxxx_edges = Table(
    'ev_charging_xxxx_edges', metadata,
    Column('node_id1', Integer),
    Column('nodeid2', Integer),
    schema='model_draft'
)


class ExampleApiTable(Base):
    __tablename__ = 'example_api_table'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.example_api_table_id_seq'::regclass)"))
    name = Column(String(50))
    type = Column(String(20))
    capacity = Column(Numeric)
    lat = Column(Numeric)
    lon = Column(Numeric)


t_feasability_check = Table(
    'feasability_check', metadata,
    Column('results', String),
    schema='model_draft'
)


t_fred_dp_hydropower_mview = Table(
    'fred_dp_hydropower_mview', metadata,
    Column('hydropower_id', BigInteger, unique=True),
    Column('postcode', Text),
    Column('city', Text),
    Column('capacity', Float(53)),
    Column('voltage_level', SmallInteger),
    Column('source', Text),
    Column('geom', Geometry('POINT', 3035), index=True),
    schema='model_draft'
)


t_fred_dp_hydropower_on_river_mview = Table(
    'fred_dp_hydropower_on_river_mview', metadata,
    Column('hydropower_id', BigInteger, unique=True),
    Column('postcode', Text),
    Column('city', Text),
    Column('capacity', Float(53)),
    Column('voltage_level', SmallInteger),
    Column('source', Text),
    Column('river_id', Integer),
    Column('riversystem_id', Integer),
    Column('gwk', String),
    Column('nam', String(100)),
    Column('geom', Geometry('POINT', 3035), index=True),
    Column('geom_line', Geometry('LINESTRING', 3035), index=True),
    Column('distance', Float(53)),
    schema='model_draft'
)


t_fred_dp_river_mview = Table(
    'fred_dp_river_mview', metadata,
    Column('river_id', Integer, unique=True),
    Column('riversystem_id', Integer),
    Column('gwk', String),
    Column('nam', String(100)),
    Column('geom', Geometry('MULTILINESTRING', 3035), index=True),
    schema='model_draft'
)


t_fred_dp_river_systems_mview = Table(
    'fred_dp_river_systems_mview', metadata,
    Column('riversystem_id', Integer, unique=True),
    Column('riversystem_name', Text),
    Column('river_cnt', BigInteger),
    Column('river_lenght', Float(53)),
    Column('geom', Geometry('MULTILINESTRING', 3035), index=True),
    schema='model_draft'
)


t_fred_dp_river_with_hydropower_mview = Table(
    'fred_dp_river_with_hydropower_mview', metadata,
    Column('river_id', Integer, unique=True),
    Column('capacity_sum', Float(53)),
    Column('count', BigInteger),
    Column('gwk', String),
    Column('riversystem_id', Integer),
    Column('riversystem_name', Text),
    Column('nam', String(100)),
    Column('geom', Geometry('MULTILINESTRING', 3035), index=True),
    schema='model_draft'
)


class IoerUrbanShareIndustrial(Base):
    __tablename__ = 'ioer_urban_share_industrial'
    __table_args__ = (
        CheckConstraint('(public.st_scalex(rast))::numeric(16,10) = (100)::numeric(16,10)'),
        CheckConstraint("(public.st_scaley(rast))::numeric(16,10) = ('-100'::integer)::numeric(16,10)"),
        CheckConstraint("public._raster_constraint_out_db(rast) = '{f}'::boolean[]"),
        CheckConstraint("public._raster_constraint_pixel_types(rast) = '{32BF}'::text[]"),
        CheckConstraint('public.st_height(rast) = 500'),
        CheckConstraint('public.st_numbands(rast) = 1'),
        CheckConstraint('public.st_srid(rast) = 3035'),
        CheckConstraint('public.st_width(rast) = 500'),
        CheckConstraint("ublic.st_coveredby(public.st_convexhull(rast), '0103000020DB0B000001000000430000000000000028E64E4100000000C83744410000000080844E4100000000C83744410000000080844E4100000000709944410000000080844E410000000018FB44410000000080844E4100000000C05C45410000000080844E410000000068BE45410000000080844E4100000000102046410000000080844E4100000000B88146410000000080844E410000000060E346410000000080844E4100000000084547410000000080844E4100000000B0A647410000000080844E4100000000580848410000000080844E4100000000006A48410000000080844E4100000000A8CB48410000000080844E4100000000502D49410000000080844E4100000000F88E49410000000080844E4100000000A0F049410000000080844E410000000048524A410000000080844E4100000000F0B34A410000000080844E410000000098154B410000000080844E410000000040774B410000000028E64E410000000040774B4100000000D0474F410000000040774B410000000078A94F410000000040774B4100000000900550410000000040774B4100000000643650410000000040774B4100000000386750410000000040774B41000000000C9850410000000040774B4100000000E0C850410000000040774B4100000000B4F950410000000040774B4100000000882A51410000000040774B41000000005C5B51410000000040774B4100000000308C51410000000040774B410000000004BD51410000000040774B4100000000D8ED51410000000040774B4100000000D8ED51410000000098154B4100000000D8ED514100000000F0B34A4100000000D8ED51410000000048524A4100000000D8ED514100000000A0F0494100000000D8ED514100000000F88E494100000000D8ED514100000000502D494100000000D8ED514100000000A8CB484100000000D8ED514100000000006A484100000000D8ED5141000000005808484100000000D8ED514100000000B0A6474100000000D8ED5141000000000845474100000000D8ED51410000000060E3464100000000D8ED514100000000B881464100000000D8ED5141000000001020464100000000D8ED51410000000068BE454100000000D8ED514100000000C05C454100000000D8ED51410000000018FB444100000000D8ED5141000000007099444100000000D8ED514100000000C83744410000000004BD514100000000C837444100000000308C514100000000C8374441000000005C5B514100000000C837444100000000882A514100000000C837444100000000B4F9504100000000C837444100000000E0C8504100000000C8374441000000000C98504100000000C8374441000000003867504100000000C8374441000000006436504100000000C8374441000000009005504100000000C83744410000000078A94F4100000000C837444100000000D0474F4100000000C83744410000000028E64E4100000000C8374441'::public.geometry"),
        CheckConstraint("ublic.st_iscoveragetile(rast, '0100000000000000000000594000000000000059C00000000080844E410000000040774B4100000000000000000000000000000000DB0B0000581B1C25'::public.raster, 500, 500"),
        CheckConstraint("ublic.st_samealignment(rast, '0100000000000000000000594000000000000059C00000000080844E410000000040774B4100000000000000000000000000000000DB0B000001000100'::public.raster"),
        {'schema': 'model_draft'}
    )

    rid = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ioer_urban_share_industrial_rid_seq'::regclass)"))
    rast = Column(Raster)


class IoerUrbanShareIndustrialCentroid(Base):
    __tablename__ = 'ioer_urban_share_industrial_centroid'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.ioer_urban_share_industrial_centroid_id_seq'::regclass)"))
    rid = Column(Integer)
    ioer_share = Column(Numeric)
    geom = Column(Geometry('POINT', 3035), index=True)


class LanduseCalc(Base):
    __tablename__ = 'landuse_calc'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True)
    source = Column(Text)
    attribute = Column(Text)
    count_int = Column(Integer)
    area_ha = Column(Numeric(15, 1))


class LisCharging(Base):
    __tablename__ = 'lis_charging'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.lis_charging_id_seq'::regclass)"))
    geom = Column(Geometry('POINT', 3035), index=True)
    desc = Column(String)


class LisChargingGe(Base):
    __tablename__ = 'lis_charging_ge'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.lis_charging_ge_id_seq'::regclass)"))
    ge_id = Column(BigInteger)
    geom = Column(Geometry('POINT', 3035), index=True)
    name = Column(String)
    street = Column(String)
    postcode = Column(String)
    city = Column(String)
    count = Column(Integer)
    power = Column(Float(53))
    type = Column(String)
    desc = Column(String)


class LisChargingPoi(Base):
    __tablename__ = 'lis_charging_poi'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.lis_charging_poi_id_seq'::regclass)"))
    geom = Column(Geometry('POINT', 3035), index=True)
    osm_id = Column(BigInteger)
    amenity = Column(String)
    name = Column(String)
    category = Column(SmallInteger)
    grid_id = Column(BigInteger)
    potential = Column(Float(53))
    covered_by = Column(BigInteger)
    region = Column(BigInteger)


class LisChargingStreet(Base):
    __tablename__ = 'lis_charging_streets'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.lis_charging_streets_id_seq'::regclass)"))
    geom = Column(Geometry('MULTILINESTRING', 3035), index=True)
    geom_string = Column(String)
    desc = Column(String)


class NepSupplyConvPowerplantNep2015(Base):
    __tablename__ = 'nep_supply_conv_powerplant_nep2015'
    __table_args__ = {'schema': 'model_draft'}

    bnetza_id = Column(String)
    tso = Column(String)
    power_plant_name = Column(String)
    unit_name = Column(String)
    postcode = Column(String)
    state = Column(String)
    commissioning = Column(Integer)
    chp = Column(String)
    fuel = Column(String)
    rated_power = Column(Numeric)
    rated_power_a2025 = Column(Numeric)
    rated_power_b2025 = Column(Numeric)
    rated_power_b2035 = Column(Numeric)
    rated_power_c2025 = Column(Numeric)
    lat = Column(Float(53))
    lon = Column(Float(53))
    location_checked = Column(Text)
    geom = Column(Geometry('POINT', 4326))
    gid = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.nep_supply_conv_powerplant_nep2015_seq'::regclass)"))


class OepMetadataTableExampleV13(Base):
    __tablename__ = 'oep_metadata_table_example_v13'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.oep_metadata_table_example_v13_id_seq'::regclass)"))
    year = Column(Integer)
    value = Column(Float(53))
    geom = Column(Geometry('POINT', 4326), index=True)


class OepMetadataTableExampleV14(Base):
    __tablename__ = 'oep_metadata_table_example_v14'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.oep_metadata_table_example_v14_id_seq'::regclass)"))
    year = Column(Integer)
    value = Column(Float(53))
    geom = Column(Geometry('POINT', 4326), index=True)


t_offshore_feedin_foreign = Table(
    'offshore_feedin_foreign', metadata,
    Column('generator_id', BigInteger),
    Column('scn_name', String),
    Column('feedin', ARRAY(Float(precision=53))),
    schema='model_draft'
)


class OpenfredLocation(Base):
    __tablename__ = 'openfred_locations'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.openfred_locations_id_seq'::regclass)"))
    point = Column(Geometry('POINT', 4326), unique=True)


class OpenfredTimestamp(Base):
    __tablename__ = 'openfred_timestamps'
    __table_args__ = (
        CheckConstraint('(id = 1) OR ((start IS NOT NULL) AND (stop IS NOT NULL))'),
        UniqueConstraint('start', 'stop'),
        {'schema': 'model_draft'}
    )

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.openfred_timestamps_id_seq'::regclass)"))
    start = Column(DateTime)
    stop = Column(DateTime)


class OpenfredVariable(Base):
    __tablename__ = 'openfred_variables'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.openfred_variables_id_seq'::regclass)"))
    name = Column(String(255), nullable=False, unique=True)
    type = Column(String(37))
    aggregation = Column(String(255))
    description = Column(Text)
    standard_name = Column(String(255))


class OpenfredFlag(OpenfredVariable):
    __tablename__ = 'openfred_flags'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(ForeignKey('model_draft.openfred_variables.id'), primary_key=True)
    flag_ks = Column(ARRAY(Integer()), nullable=False)
    flag_vs = Column(ARRAY(String(length=37)), nullable=False)


class Openfredgrid(Base):
    __tablename__ = 'openfredgrid'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.openfredgrid_gid_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 4326), index=True)


t_opsd_hourly_timeseries = Table(
    'opsd_hourly_timeseries', metadata,
    Column('timestamp', DateTime),
    Column('load_at', Numeric(12, 2)),
    Column('load_ba', Numeric(12, 2)),
    Column('load_be', Numeric(12, 2)),
    Column('load_bg', Numeric(12, 2)),
    Column('load_ch', Numeric(12, 2)),
    Column('load_cs', Numeric(12, 2)),
    Column('load_cy', Numeric(12, 2)),
    Column('load_cz', Numeric(12, 2)),
    Column('load_de', Numeric(12, 2)),
    Column('load_dk', Numeric(12, 2)),
    Column('load_dkw', Numeric(12, 2)),
    Column('load_ee', Numeric(12, 2)),
    Column('load_es', Numeric(12, 2)),
    Column('load_fi', Numeric(12, 2)),
    Column('load_fr', Numeric(12, 2)),
    Column('load_gb', Numeric(12, 2)),
    Column('load_gr', Numeric(12, 2)),
    Column('load_hr', Numeric(12, 2)),
    Column('load_hu', Numeric(12, 2)),
    Column('load_ie', Numeric(12, 2)),
    Column('load_is', Numeric(12, 2)),
    Column('load_it', Numeric(12, 2)),
    Column('load_lt', Numeric(12, 2)),
    Column('load_lu', Numeric(12, 2)),
    Column('load_lv', Numeric(12, 2)),
    Column('load_me', Numeric(12, 2)),
    Column('load_mk', Numeric(12, 2)),
    Column('load_ni', Numeric(12, 2)),
    Column('load_nl', Numeric(12, 2)),
    Column('load_no', Numeric(12, 2)),
    Column('load_pl', Numeric(12, 2)),
    Column('load_pt', Numeric(12, 2)),
    Column('load_ro', Numeric(12, 2)),
    Column('load_rs', Numeric(12, 2)),
    Column('load_se', Numeric(12, 2)),
    Column('load_si', Numeric(12, 2)),
    Column('load_sk', Numeric(12, 2)),
    Column('load_uaw', Numeric(12, 2)),
    Column('solar_de_capacity', Numeric(12, 2)),
    Column('solar_de_forecast', Numeric(12, 2)),
    Column('solar_de_generation', Numeric(12, 2)),
    Column('solar_de_profile', Numeric(12, 2)),
    Column('solar_de50hertz_forecast', Numeric(12, 2)),
    Column('solar_de50hertz_generation', Numeric(12, 2)),
    Column('solar_deamprion_forecast', Numeric(12, 2)),
    Column('solar_deamprion_generation', Numeric(12, 2)),
    Column('solar_detennet_forecast', Numeric(12, 2)),
    Column('solar_detennet_generation', Numeric(12, 2)),
    Column('solar_detransnetbw_forecast', Numeric(12, 2)),
    Column('solar_detransnetbw_generation', Numeric(12, 2)),
    Column('wind_de_capacity', Numeric(12, 2)),
    Column('wind_de_forecast', Numeric(12, 2)),
    Column('wind_de_generation', Numeric(12, 2)),
    Column('wind_de_profile', Numeric(12, 2)),
    Column('wind_de50hertz_forecast', Numeric(12, 2)),
    Column('wind_de50hertz_generation', Numeric(12, 2)),
    Column('wind_deamprion_forecast', Numeric(12, 2)),
    Column('wind_deamprion_generation', Numeric(12, 2)),
    Column('wind_detennet_forecast', Numeric(12, 2)),
    Column('wind_detennet_generation', Numeric(12, 2)),
    Column('wind_detransnetbw_forecast', Numeric(12, 2)),
    Column('wind_detransnetbw_generation', Numeric(12, 2)),
    schema='model_draft'
)


t_osm_deu_polygon_urban_buffer100_mview = Table(
    'osm_deu_polygon_urban_buffer100_mview', metadata,
    Column('id', Integer, unique=True),
    Column('geom', Geometry('POLYGON', 3035), index=True),
    schema='model_draft'
)


t_ren_feedin_by_gen_id = Table(
    'ren_feedin_by_gen_id', metadata,
    Column('generator_id', BigInteger),
    Column('feedin', ARRAY(Float(precision=53))),
    schema='model_draft'
)


t_ren_feedin_foreign = Table(
    'ren_feedin_foreign', metadata,
    Column('generator_id', BigInteger),
    Column('feedin', ARRAY(Float(precision=53))),
    schema='model_draft'
)


class RenpassGisEconomicScenario(Base):
    __tablename__ = 'renpass_gis_economic_scenario'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_economic_scenario_id_seq'::regclass)"))
    name = Column(String(250), nullable=False, unique=True)


class RenpassGisParameterRegion(Base):
    __tablename__ = 'renpass_gis_parameter_region'
    __table_args__ = {'schema': 'model_draft'}

    gid = Column(Integer, primary_key=True)
    u_region_id = Column(String(14), nullable=False)
    stat_level = Column(Integer)
    geom = Column(Geometry('MULTIPOLYGON', 4326))
    geom_point = Column(Geometry('POINT', 4326))


class RenpassgisEconomicWeatherpointVoronoi(Base):
    __tablename__ = 'renpassgis_economic_weatherpoint_voronoi'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry('POLYGON', 4326), index=True)
    id = Column(Integer, primary_key=True)


class RenpassgisEconomyClimatepointVoronoi(Base):
    __tablename__ = 'renpassgis_economy_climatepoint_voronoi'
    __table_args__ = {'schema': 'model_draft'}

    geom = Column(Geometry('POLYGON', 4326), index=True)
    id = Column(Integer, primary_key=True)


class RliResearchInstitute(Base):
    __tablename__ = 'rli_research_institute'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.rli_research_institute_id_seq'::regclass)"))
    name = Column(Text)
    short_name = Column(Text)
    country_name = Column(Text)
    country_code = Column(Text)
    city = Column(Text)
    project_id = Column(Text)
    website = Column(Text)
    osm_id = Column(BigInteger)
    updated = Column(DateTime(True))
    source = Column(Text)
    lon = Column(Float(53))
    lat = Column(Float(53))
    geom = Column(Geometry('POINT', 3035), index=True)


class ScenarioLog(Base):
    __tablename__ = 'scenario_log'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.scenario_log_id_seq'::regclass)"))
    project = Column(Text)
    version = Column(Text)
    io = Column(Text)
    schema_name = Column(Text)
    table_name = Column(Text)
    script_name = Column(Text)
    entries = Column(Integer)
    comment = Column(Text)
    user_name = Column(Text)
    timestamp = Column(DateTime)
    meta_data = Column(Text)


t_scn_nep2035_b2_line = Table(
    'scn_nep2035_b2_line', metadata,
    Column('scn_name', String, nullable=False, server_default=text("'Status Quo'::character varying")),
    Column('project', String),
    Column('project_id', BigInteger),
    Column('startpunkt', String),
    Column('endpunkt', String),
    Column('spannung', BigInteger),
    Column('s_nom', Numeric, server_default=text("0")),
    Column('cables', BigInteger),
    Column('nova', String),
    Column('geom', Geometry('MULTILINESTRING', 4326)),
    schema='model_draft'
)


class SqlalchemyLinestring(Base):
    __tablename__ = 'sqlalchemy_linestring'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.sqlalchemy_linestring_id_seq'::regclass)"))
    geom = Column(Geometry('LINESTRING'))


class SqlalchemyPoint(Base):
    __tablename__ = 'sqlalchemy_point'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.sqlalchemy_point_id_seq'::regclass)"))
    geom = Column(Geometry('POINT'))


class SqlalchemyPolygon(Base):
    __tablename__ = 'sqlalchemy_polygon'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.sqlalchemy_polygon_id_seq'::regclass)"))
    geom = Column(Geometry('POLYGON'))


class SupplyWriWorldpowerwatch(Base):
    __tablename__ = 'supply_wri_worldpowerwatch'
    __table_args__ = {'schema': 'model_draft'}

    pw_idnr = Column(String, primary_key=True)
    geom = Column(Geometry('POINT', 4326))
    name = Column(String)
    capacity_mw = Column(Float(53))
    year_of_capacity_data = Column(String)
    annual_generation_gwh = Column(String)
    year_of_generation_data = Column(String)
    country = Column(String)
    owner = Column(String)
    source = Column(String)
    url = Column(String)
    latitude = Column(Float(53))
    longitude = Column(Float(53))
    fuel1 = Column(String)
    fuel2 = Column(String)
    fuel3 = Column(String)
    fuel4 = Column(String)
    field_17 = Column(String)
    field_18 = Column(String)


t_temp_supply_aggr_weather = Table(
    'temp_supply_aggr_weather', metadata,
    Column('aggr_id', BigInteger),
    Column('w_id', BigInteger),
    Column('scn_name', String),
    Column('bus', BigInteger),
    Column('power_class', BigInteger),
    Column('row_number', BigInteger),
    schema='model_draft'
)


class TemplateTable(Base):
    __tablename__ = 'template_table'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.template_table_id_seq'::regclass)"))
    base_id = Column(Integer)
    area_type = Column(Text)
    geom_poly = Column(Geometry('POLYGON', 3035), index=True)
    geom = Column(Geometry('POINT', 3035), index=True)


t_template_table_mview = Table(
    'template_table_mview', metadata,
    Column('id', Integer),
    Column('base_id', Integer),
    Column('area_type', Text),
    Column('geom', Geometry, index=True),
    schema='model_draft'
)


t_test_ego_supply_res_powerplant_nep2035_mview = Table(
    'test_ego_supply_res_powerplant_nep2035_mview', metadata,
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
    schema='model_draft'
)


class TestTable(Base):
    __tablename__ = 'test_table'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.test_table_id_seq'::regclass)"))
    year = Column(Integer)
    value = Column(Float(53))
    geom = Column(Geometry('POINT', 4326))


t_way_substations_test = Table(
    'way_substations_test', metadata,
    Column('id', BigInteger),
    Column('tags', ARRAY(Text())),
    Column('geom', Geometry),
    schema='model_draft'
)


class WnAbwBkgVg2504Kr(Base):
    __tablename__ = 'wn_abw_bkg_vg250_4_krs'
    __table_args__ = {'schema': 'model_draft'}

    reference_date = Column(Date, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('model_draft.wn_abw_bkg_vg250_4_krs_id_seq'::regclass)"))
    ade = Column(Float(53))
    gf = Column(Float(53))
    bsg = Column(Float(53))
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(Float(53))
    bem = Column(String(75))
    nbd = Column(String(4))
    sn_l = Column(String(2))
    sn_r = Column(String(1))
    sn_k = Column(String(2))
    sn_v1 = Column(String(2))
    sn_v2 = Column(String(2))
    sn_g = Column(String(3))
    fk_s3 = Column(String(2))
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    wsk = Column(Date)
    debkg_id = Column(String(16))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class WnAbwBkgVg2506Gem(Base):
    __tablename__ = 'wn_abw_bkg_vg250_6_gem'
    __table_args__ = {'schema': 'model_draft'}

    reference_date = Column(Date, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, server_default=text("nextval('model_draft.wn_abw_bkg_vg250_6_gem_id_seq'::regclass)"))
    ade = Column(Float(53))
    gf = Column(Float(53))
    bsg = Column(Float(53))
    rs = Column(String(12))
    ags = Column(String(12))
    sdv_rs = Column(String(12))
    gen = Column(String(50))
    bez = Column(String(50))
    ibz = Column(Float(53))
    bem = Column(String(75))
    nbd = Column(String(4))
    sn_l = Column(String(2))
    sn_r = Column(String(1))
    sn_k = Column(String(2))
    sn_v1 = Column(String(2))
    sn_v2 = Column(String(2))
    sn_g = Column(String(3))
    fk_s3 = Column(String(2))
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    wsk = Column(Date)
    debkg_id = Column(String(16))
    geom = Column(Geometry('MULTIPOLYGON', 31467), index=True)


class WnAbwDemandElT(Base):
    __tablename__ = 'wn_abw_demand_el_ts'
    __table_args__ = {'schema': 'model_draft'}

    load_id = Column(BigInteger, primary_key=True)
    bus = Column(BigInteger)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))
    subst_id = Column(Integer)


class WnAbwEgoDemandHvLargescaleconsumer(Base):
    __tablename__ = 'wn_abw_ego_demand_hv_largescaleconsumer'
    __table_args__ = {'schema': 'model_draft'}

    polygon_id = Column(Integer, primary_key=True)
    area_ha = Column(Float(53))
    powerplant_id = Column(Integer)
    voltage_level = Column(SmallInteger)
    subst_id = Column(Integer)
    otg_id = Column(Integer)
    un_id = Column(Integer)
    consumption = Column(Numeric)
    peak_load = Column(Numeric)
    geom = Column(Geometry('MULTIPOLYGON', 3035), index=True)
    geom_centre = Column(Geometry('POINT', 3035), index=True)
    hvmv_subst_id = Column(Integer)


class WnAbwEgoDpConvPowerplant(Base):
    __tablename__ = 'wn_abw_ego_dp_conv_powerplant'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True, nullable=False)
    gid = Column(Integer, primary_key=True, nullable=False)
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


class WnAbwEgoDpHvmvSubstation(Base):
    __tablename__ = 'wn_abw_ego_dp_hvmv_substation'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, nullable=False)
    subst_id = Column(Integer, primary_key=True)
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


class WnAbwEgoDpLoadarea(Base):
    __tablename__ = 'wn_abw_ego_dp_loadarea'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    subst_id = Column(Integer)
    area_ha = Column(Numeric)
    nuts = Column(String(5))
    rs_0 = Column(String(12))
    ags_0 = Column(String(12))
    otg_id = Column(Integer)
    un_id = Column(Integer)
    zensus_sum = Column(Integer)
    zensus_count = Column(Integer)
    zensus_density = Column(Numeric)
    ioer_sum = Column(Numeric)
    ioer_count = Column(Integer)
    ioer_density = Column(Numeric)
    sector_area_residential = Column(Numeric)
    sector_area_retail = Column(Numeric)
    sector_area_industrial = Column(Numeric)
    sector_area_agricultural = Column(Numeric)
    sector_area_sum = Column(Numeric)
    sector_share_residential = Column(Numeric)
    sector_share_retail = Column(Numeric)
    sector_share_industrial = Column(Numeric)
    sector_share_agricultural = Column(Numeric)
    sector_share_sum = Column(Numeric)
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
    sector_peakload_retail = Column(Float(53))
    sector_peakload_residential = Column(Float(53))
    sector_peakload_industrial = Column(Float(53))
    sector_peakload_agricultural = Column(Float(53))
    geom_centroid = Column(Geometry('POINT', 3035))
    geom_surfacepoint = Column(Geometry('POINT', 3035))
    geom_centre = Column(Geometry('POINT', 3035))
    geom = Column(Geometry('POLYGON', 3035), index=True)


class WnAbwEgoDpMvGriddistrict(Base):
    __tablename__ = 'wn_abw_ego_dp_mv_griddistrict'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, nullable=False)
    subst_id = Column(Integer, primary_key=True)
    subst_sum = Column(Integer)
    type1 = Column(Integer)
    type1_cnt = Column(Integer)
    type2 = Column(Integer)
    type2_cnt = Column(Integer)
    type3 = Column(Integer)
    type3_cnt = Column(Integer)
    group = Column(CHAR(1))
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
    consumption_total = Column(Integer)


class WnAbwEgoDpResPowerplant(Base):
    __tablename__ = 'wn_abw_ego_dp_res_powerplant'
    __table_args__ = {'schema': 'model_draft'}

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


class WnAbwEgoPfHvBus(Base):
    __tablename__ = 'wn_abw_ego_pf_hv_bus'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    v_nom = Column(Float(53))
    current_type = Column(Text, server_default=text("'AC'::text"))
    v_mag_pu_min = Column(Float(53), server_default=text("0"))
    v_mag_pu_max = Column(Float(53))
    geom = Column(Geometry('POINT', 4326), index=True)
    hvmv_subst_id = Column(Integer)
    region_bus = Column(Boolean, server_default=text("false"))


class WnAbwEgoPfHvLine(Base):
    __tablename__ = 'wn_abw_ego_pf_hv_line'
    __table_args__ = {'schema': 'model_draft'}

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


class WnAbwEgoPfHvTransformer(Base):
    __tablename__ = 'wn_abw_ego_pf_hv_transformer'
    __table_args__ = {'schema': 'model_draft'}

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


class WnAbwLauProtectedLandscapeElement(Base):
    __tablename__ = 'wn_abw_lau_protected_landscape_elements'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('model_draft.wn_abw_lau_protected_landscape_elements_id_seq'::regclass)"))
    geom = Column(Geometry('MULTIPOLYGON', 3035))


class WnAbwPowerplantT(Base):
    __tablename__ = 'wn_abw_powerplant_ts'
    __table_args__ = {'schema': 'model_draft'}

    generator_id = Column(BigInteger, primary_key=True)
    bus = Column(BigInteger)
    dispatch = Column(Text)
    control = Column(Text)
    p_nom = Column(Float(53), server_default=text("0"))
    generation_type = Column(Text)
    p_set = Column(ARRAY(Float(precision=53)))
    subst_id = Column(Integer)


t_wn_abw_results_line = Table(
    'wn_abw_results_line', metadata,
    Column('line_id', BigInteger),
    Column('loading_mean', Float(53)),
    Column('loading_max', Float(53)),
    schema='model_draft'
)


class WnAbwResultsLineEgo(Base):
    __tablename__ = 'wn_abw_results_line_ego'
    __table_args__ = {'schema': 'model_draft'}

    line_id = Column(BigInteger, primary_key=True)
    loading_max = Column(Float(53), server_default=text("0"))
    loading_mean = Column(Float(53), server_default=text("0"))


class WnAbwStatsResPowerplantsPerMvgd(Base):
    __tablename__ = 'wn_abw_stats_res_powerplants_per_mvgd'
    __table_args__ = {'schema': 'model_draft'}

    subst_id = Column(BigInteger, primary_key=True, nullable=False)
    generation_type = Column(Text, primary_key=True, nullable=False)
    count = Column(Integer)
    capacity_mw = Column(Numeric)
    annual_energy_gwh = Column(Numeric)


class EgoDemandPfLoadSingle(Base):
    __tablename__ = 'ego_demand_pf_load_single'
    __table_args__ = (
        ForeignKeyConstraint(['bus', 'scn_name'], ['model_draft.ego_grid_pf_hv_bus.bus_id', 'model_draft.ego_grid_pf_hv_bus.scn_name']),
        {'schema': 'model_draft'}
    )

    scn_name = Column(String, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True)
    bus = Column(BigInteger)
    sign = Column(Float(53), server_default=text("'-1'::integer"))
    e_annual = Column(Float(53))

    ego_grid_pf_hv_bus = relationship('EgoGridPfHvBus')


class EgoGridPfHvBusVMagSet(Base):
    __tablename__ = 'ego_grid_pf_hv_bus_v_mag_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    bus_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('model_draft.ego_grid_pf_hv_temp_resolution.temp_id'), primary_key=True, nullable=False)
    v_mag_pu_set = Column(ARRAY(Float(precision=53)))

    temp = relationship('EgoGridPfHvTempResolution')



class EgoGridPfHvExtensionGenerator(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_generator'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False)
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


class EgoGridPfHvExtensionGeneratorPqSet(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_generator_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    version = Column(Text, primary_key=True, nullable=False)
    scn_name = Column(String, primary_key=True, nullable=False)
    generator_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(Integer, primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))
    p_min_pu = Column(ARRAY(Float(precision=53)))
    p_max_pu = Column(ARRAY(Float(precision=53)))



class EgoGridPfHvExtensionLoadPqSet(Base):
    __tablename__ = 'ego_grid_pf_hv_extension_load_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('model_draft.ego_grid_pf_hv_temp_resolution.temp_id'), primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))

    temp = relationship('EgoGridPfHvTempResolution')


class EgoGridPfHvGenerator(Base):
    __tablename__ = 'ego_grid_pf_hv_generator'
    __table_args__ = {'schema': 'model_draft'}

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
    source = Column(ForeignKey('model_draft.ego_grid_pf_hv_source.source_id'), index=True)
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))

    ego_grid_pf_hv_source = relationship('EgoGridPfHvSource')


class EgoGridPfHvGeneratorPqSet(Base):
    __tablename__ = 'ego_grid_pf_hv_generator_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    generator_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('model_draft.ego_grid_pf_hv_temp_resolution.temp_id'), primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))
    p_min_pu = Column(ARRAY(Float(precision=53)))
    p_max_pu = Column(ARRAY(Float(precision=53)))

    temp = relationship('EgoGridPfHvTempResolution')


class EgoGridPfHvLoadPqSet(Base):
    __tablename__ = 'ego_grid_pf_hv_load_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    load_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('model_draft.ego_grid_pf_hv_temp_resolution.temp_id'), primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))

    temp = relationship('EgoGridPfHvTempResolution')


class EgoGridPfHvStorage(Base):
    __tablename__ = 'ego_grid_pf_hv_storage'
    __table_args__ = {'schema': 'model_draft'}

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
    source = Column(ForeignKey('model_draft.ego_grid_pf_hv_source.source_id'), index=True)
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))
    soc_initial = Column(Float(53))
    soc_cyclic = Column(Boolean, server_default=text("false"))
    max_hours = Column(Float(53))
    efficiency_store = Column(Float(53))
    efficiency_dispatch = Column(Float(53))
    standing_loss = Column(Float(53))

    ego_grid_pf_hv_source = relationship('EgoGridPfHvSource')


class EgoGridPfHvStoragePqSet(Base):
    __tablename__ = 'ego_grid_pf_hv_storage_pq_set'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    temp_id = Column(ForeignKey('model_draft.ego_grid_pf_hv_temp_resolution.temp_id'), primary_key=True, nullable=False)
    p_set = Column(ARRAY(Float(precision=53)))
    q_set = Column(ARRAY(Float(precision=53)))
    p_min_pu = Column(ARRAY(Float(precision=53)))
    p_max_pu = Column(ARRAY(Float(precision=53)))
    soc_set = Column(ARRAY(Float(precision=53)))
    inflow = Column(ARRAY(Float(precision=53)))

    temp = relationship('EgoGridPfHvTempResolution')


class EgoSupplyPfGeneratorSingle(Base):
    __tablename__ = 'ego_supply_pf_generator_single'
    __table_args__ = {'schema': 'model_draft'}

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
    source = Column(ForeignKey('model_draft.ego_grid_pf_hv_source.source_id'))
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))
    w_id = Column(BigInteger)
    aggr_id = Column(BigInteger)
    power_class = Column(BigInteger)
    voltage_level = Column(SmallInteger)

    ego_grid_pf_hv_source = relationship('EgoGridPfHvSource')


class EgoSupplyPfStorageSingle(Base):
    __tablename__ = 'ego_supply_pf_storage_single'
    __table_args__ = {'schema': 'model_draft'}

    scn_name = Column(String, primary_key=True, nullable=False, server_default=text("'Status Quo'::character varying"))
    storage_id = Column(BigInteger, primary_key=True, nullable=False)
    bus = Column(BigInteger)
    dispatch = Column(Text, server_default=text("'flexible'::text"))
    control = Column(Text, server_default=text("'PQ'::text"))
    p_nom = Column(Float(53), server_default=text("0"))
    p_nom_extendable = Column(Boolean, server_default=text("false"))
    p_nom_min = Column(Float(53), server_default=text("0"))
    p_nom_max = Column(Float(53))
    p_min_pu_fixed = Column(Float(53), server_default=text("'-1'::integer"))
    p_max_pu_fixed = Column(Float(53), server_default=text("1"))
    sign = Column(Float(53), server_default=text("1"))
    source = Column(ForeignKey('model_draft.ego_grid_pf_hv_source.source_id'))
    marginal_cost = Column(Float(53))
    capital_cost = Column(Float(53))
    efficiency = Column(Float(53))
    soc_initial = Column(Float(53))
    soc_cyclic = Column(Boolean, server_default=text("true"))
    max_hours = Column(Float(53))
    efficiency_store = Column(Float(53))
    efficiency_dispatch = Column(Float(53))
    standing_loss = Column(Float(53))
    aggr_id = Column(Integer)

    ego_grid_pf_hv_source = relationship('EgoGridPfHvSource')


class OpenfredValue(Base):
    __tablename__ = 'openfred_values'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.openfred_values_id_seq'::regclass)"))
    v = Column(Float(53), nullable=False)
    altitude = Column(Float(53))
    timestamp_id = Column(ForeignKey('model_draft.openfred_timestamps.id'), nullable=False, server_default=text("1"))
    location_id = Column(ForeignKey('model_draft.openfred_locations.id'), nullable=False)
    variable_id = Column(ForeignKey('model_draft.openfred_variables.id'), nullable=False)

    location = relationship('OpenfredLocation')
    timestamp = relationship('OpenfredTimestamp')
    variable = relationship('OpenfredVariable')


class RenpassGisEconomicLinearTransformer(Base):
    __tablename__ = 'renpass_gis_economic_linear_transformer'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_economic_linear_transformer_id_seq'::regclass)"))
    scenario_id = Column(ForeignKey('model_draft.renpass_gis_economic_scenario.id'))
    label = Column(String(250))
    source = Column(String(250))
    target = Column(String(250))
    conversion_factors = Column(ARRAY(Numeric()))
    summed_min = Column(ARRAY(Numeric()))
    nominal_value = Column(ARRAY(Numeric()))
    actual_value = Column(ARRAY(Numeric()))
    fixed = Column(Boolean)
    variable_costs = Column(ARRAY(Numeric()))
    fixed_costs = Column(ARRAY(Numeric()))

    scenario = relationship('RenpassGisEconomicScenario')


class RenpassGisEconomicSink(Base):
    __tablename__ = 'renpass_gis_economic_sink'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_economic_sink_id_seq'::regclass)"))
    scenario_id = Column(ForeignKey('model_draft.renpass_gis_economic_scenario.id'))
    label = Column(String(250))
    source = Column(String(250))
    target = Column(String(250))
    nominal_value = Column(ARRAY(Numeric()))
    actual_value = Column(ARRAY(Numeric()))
    fixed = Column(Boolean)

    scenario = relationship('RenpassGisEconomicScenario')


class RenpassGisEconomicSource(Base):
    __tablename__ = 'renpass_gis_economic_source'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_economic_source_id_seq'::regclass)"))
    scenario_id = Column(ForeignKey('model_draft.renpass_gis_economic_scenario.id'))
    label = Column(String(250))
    source = Column(String(250))
    target = Column(String(250))
    nominal_value = Column(ARRAY(Numeric()))
    actual_value = Column(ARRAY(Numeric()))
    variable_costs = Column(ARRAY(Numeric()))
    fixed = Column(Boolean)

    scenario = relationship('RenpassGisEconomicScenario')


class RenpassGisEconomicStorage(Base):
    __tablename__ = 'renpass_gis_economic_storage'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_economic_storage_id_seq'::regclass)"))
    scenario_id = Column(ForeignKey('model_draft.renpass_gis_economic_scenario.id'))
    label = Column(String(250))
    source = Column(String(250))
    target = Column(String(250))
    conversion_factors = Column(ARRAY(Numeric()))
    summed_min = Column(ARRAY(Numeric()))
    nominal_value = Column(ARRAY(Numeric()))
    min = Column(ARRAY(Numeric()))
    max = Column(ARRAY(Numeric()))
    actual_value = Column(ARRAY(Numeric()))
    fixed = Column(Boolean)
    variable_costs = Column(ARRAY(Numeric()))
    fixed_costs = Column(ARRAY(Numeric()))
    nominal_capacity = Column(ARRAY(Numeric()))
    capacity_loss = Column(ARRAY(Numeric()))
    inflow_conversion_factor = Column(ARRAY(Numeric()))
    outflow_conversion_factor = Column(ARRAY(Numeric()))
    initial_capacity = Column(ARRAY(Numeric()))
    capacity_min = Column(ARRAY(Numeric()))
    capacity_max = Column(ARRAY(Numeric()))

    scenario = relationship('RenpassGisEconomicScenario')


class RenpassGisScenarioResult(Base):
    __tablename__ = 'renpass_gis_scenario_results'
    __table_args__ = {'schema': 'model_draft'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('model_draft.renpass_gis_scenario_results_id_seq'::regclass)"))
    scenario_id = Column(ForeignKey('model_draft.renpass_gis_economic_scenario.id'))
    bus_label = Column(String(250))
    type = Column(String(250))
    obj_label = Column(String(250))
    datetime = Column(DateTime)
    val = Column(Numeric)

    scenario = relationship('RenpassGisEconomicScenario')

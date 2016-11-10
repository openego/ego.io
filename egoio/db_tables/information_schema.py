# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, text
from sqlalchemy.dialects.postgresql import ARRAY, OID

metadata = MetaData()

t__pg_foreign_data_wrappers = Table(
    '_pg_foreign_data_wrappers', metadata,
    Column('oid', OID),
    Column('fdwowner', OID),
    Column('fdwoptions', ARRAY(TEXT())),
    Column('foreign_data_wrapper_catalog', String),
    Column('foreign_data_wrapper_name', String),
    Column('authorization_identifier', String),
    Column('foreign_data_wrapper_language', String),
    schema='information_schema'
)

t__pg_foreign_servers = Table(
    '_pg_foreign_servers', metadata,
    Column('oid', OID),
    Column('srvoptions', ARRAY(TEXT())),
    Column('foreign_server_catalog', String),
    Column('foreign_server_name', String),
    Column('foreign_data_wrapper_catalog', String),
    Column('foreign_data_wrapper_name', String),
    Column('foreign_server_type', String),
    Column('foreign_server_version', String),
    Column('authorization_identifier', String),
    schema='information_schema'
)

t__pg_foreign_table_columns = Table(
    '_pg_foreign_table_columns', metadata,
    Column('nspname', String),
    Column('relname', String),
    Column('attname', String),
    Column('attfdwoptions', ARRAY(TEXT())),
    schema='information_schema'
)

t__pg_foreign_tables = Table(
    '_pg_foreign_tables', metadata,
    Column('foreign_table_catalog', String),
    Column('foreign_table_schema', String),
    Column('foreign_table_name', String),
    Column('ftoptions', ARRAY(TEXT())),
    Column('foreign_server_catalog', String),
    Column('foreign_server_name', String),
    Column('authorization_identifier', String),
    schema='information_schema'
)

t__pg_user_mappings = Table(
    '_pg_user_mappings', metadata,
    Column('oid', OID),
    Column('umoptions', ARRAY(TEXT())),
    Column('umuser', OID),
    Column('authorization_identifier', String),
    Column('foreign_server_catalog', String),
    Column('foreign_server_name', String),
    Column('srvowner', String),
    schema='information_schema'
)

t_administrable_role_authorizations = Table(
    'administrable_role_authorizations', metadata,
    Column('grantee', String),
    Column('role_name', String),
    Column('is_grantable', String),
    schema='information_schema'
)

t_applicable_roles = Table(
    'applicable_roles', metadata,
    Column('grantee', String),
    Column('role_name', String),
    Column('is_grantable', String),
    schema='information_schema'
)

t_attributes = Table(
    'attributes', metadata,
    Column('udt_catalog', String),
    Column('udt_schema', String),
    Column('udt_name', String),
    Column('attribute_name', String),
    Column('ordinal_position', Integer),
    Column('attribute_default', String),
    Column('is_nullable', String),
    Column('data_type', String),
    Column('character_maximum_length', Integer),
    Column('character_octet_length', Integer),
    Column('character_set_catalog', String),
    Column('character_set_schema', String),
    Column('character_set_name', String),
    Column('collation_catalog', String),
    Column('collation_schema', String),
    Column('collation_name', String),
    Column('numeric_precision', Integer),
    Column('numeric_precision_radix', Integer),
    Column('numeric_scale', Integer),
    Column('datetime_precision', Integer),
    Column('interval_type', String),
    Column('interval_precision', Integer),
    Column('attribute_udt_catalog', String),
    Column('attribute_udt_schema', String),
    Column('attribute_udt_name', String),
    Column('scope_catalog', String),
    Column('scope_schema', String),
    Column('scope_name', String),
    Column('maximum_cardinality', Integer),
    Column('dtd_identifier', String),
    Column('is_derived_reference_attribute', String),
    schema='information_schema'
)

t_character_sets = Table(
    'character_sets', metadata,
    Column('character_set_catalog', String),
    Column('character_set_schema', String),
    Column('character_set_name', String),
    Column('character_repertoire', String),
    Column('form_of_use', String),
    Column('default_collate_catalog', String),
    Column('default_collate_schema', String),
    Column('default_collate_name', String),
    schema='information_schema'
)

t_check_constraint_routine_usage = Table(
    'check_constraint_routine_usage', metadata,
    Column('constraint_catalog', String),
    Column('constraint_schema', String),
    Column('constraint_name', String),
    Column('specific_catalog', String),
    Column('specific_schema', String),
    Column('specific_name', String),
    schema='information_schema'
)

t_check_constraints = Table(
    'check_constraints', metadata,
    Column('constraint_catalog', String),
    Column('constraint_schema', String),
    Column('constraint_name', String),
    Column('check_clause', String),
    schema='information_schema'
)

t_collation_character_set_applicability = Table(
    'collation_character_set_applicability', metadata,
    Column('collation_catalog', String),
    Column('collation_schema', String),
    Column('collation_name', String),
    Column('character_set_catalog', String),
    Column('character_set_schema', String),
    Column('character_set_name', String),
    schema='information_schema'
)

t_collations = Table(
    'collations', metadata,
    Column('collation_catalog', String),
    Column('collation_schema', String),
    Column('collation_name', String),
    Column('pad_attribute', String),
    schema='information_schema'
)

t_column_domain_usage = Table(
    'column_domain_usage', metadata,
    Column('domain_catalog', String),
    Column('domain_schema', String),
    Column('domain_name', String),
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('column_name', String),
    schema='information_schema'
)

t_column_options = Table(
    'column_options', metadata,
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('column_name', String),
    Column('option_name', String),
    Column('option_value', String),
    schema='information_schema'
)

t_column_privileges = Table(
    'column_privileges', metadata,
    Column('grantor', String),
    Column('grantee', String),
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('column_name', String),
    Column('privilege_type', String),
    Column('is_grantable', String),
    schema='information_schema'
)

t_column_udt_usage = Table(
    'column_udt_usage', metadata,
    Column('udt_catalog', String),
    Column('udt_schema', String),
    Column('udt_name', String),
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('column_name', String),
    schema='information_schema'
)

t_columns = Table(
    'columns', metadata,
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('column_name', String),
    Column('ordinal_position', Integer),
    Column('column_default', String),
    Column('is_nullable', String),
    Column('data_type', String),
    Column('character_maximum_length', Integer),
    Column('character_octet_length', Integer),
    Column('numeric_precision', Integer),
    Column('numeric_precision_radix', Integer),
    Column('numeric_scale', Integer),
    Column('datetime_precision', Integer),
    Column('interval_type', String),
    Column('interval_precision', Integer),
    Column('character_set_catalog', String),
    Column('character_set_schema', String),
    Column('character_set_name', String),
    Column('collation_catalog', String),
    Column('collation_schema', String),
    Column('collation_name', String),
    Column('domain_catalog', String),
    Column('domain_schema', String),
    Column('domain_name', String),
    Column('udt_catalog', String),
    Column('udt_schema', String),
    Column('udt_name', String),
    Column('scope_catalog', String),
    Column('scope_schema', String),
    Column('scope_name', String),
    Column('maximum_cardinality', Integer),
    Column('dtd_identifier', String),
    Column('is_self_referencing', String),
    Column('is_identity', String),
    Column('identity_generation', String),
    Column('identity_start', String),
    Column('identity_increment', String),
    Column('identity_maximum', String),
    Column('identity_minimum', String),
    Column('identity_cycle', String),
    Column('is_generated', String),
    Column('generation_expression', String),
    Column('is_updatable', String),
    schema='information_schema'
)

t_constraint_column_usage = Table(
    'constraint_column_usage', metadata,
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('column_name', String),
    Column('constraint_catalog', String),
    Column('constraint_schema', String),
    Column('constraint_name', String),
    schema='information_schema'
)

t_constraint_table_usage = Table(
    'constraint_table_usage', metadata,
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('constraint_catalog', String),
    Column('constraint_schema', String),
    Column('constraint_name', String),
    schema='information_schema'
)

t_data_type_privileges = Table(
    'data_type_privileges', metadata,
    Column('object_catalog', String),
    Column('object_schema', String),
    Column('object_name', String),
    Column('object_type', String),
    Column('dtd_identifier', String),
    schema='information_schema'
)

t_domain_constraints = Table(
    'domain_constraints', metadata,
    Column('constraint_catalog', String),
    Column('constraint_schema', String),
    Column('constraint_name', String),
    Column('domain_catalog', String),
    Column('domain_schema', String),
    Column('domain_name', String),
    Column('is_deferrable', String),
    Column('initially_deferred', String),
    schema='information_schema'
)

t_domain_udt_usage = Table(
    'domain_udt_usage', metadata,
    Column('udt_catalog', String),
    Column('udt_schema', String),
    Column('udt_name', String),
    Column('domain_catalog', String),
    Column('domain_schema', String),
    Column('domain_name', String),
    schema='information_schema'
)

t_domains = Table(
    'domains', metadata,
    Column('domain_catalog', String),
    Column('domain_schema', String),
    Column('domain_name', String),
    Column('data_type', String),
    Column('character_maximum_length', Integer),
    Column('character_octet_length', Integer),
    Column('character_set_catalog', String),
    Column('character_set_schema', String),
    Column('character_set_name', String),
    Column('collation_catalog', String),
    Column('collation_schema', String),
    Column('collation_name', String),
    Column('numeric_precision', Integer),
    Column('numeric_precision_radix', Integer),
    Column('numeric_scale', Integer),
    Column('datetime_precision', Integer),
    Column('interval_type', String),
    Column('interval_precision', Integer),
    Column('domain_default', String),
    Column('udt_catalog', String),
    Column('udt_schema', String),
    Column('udt_name', String),
    Column('scope_catalog', String),
    Column('scope_schema', String),
    Column('scope_name', String),
    Column('maximum_cardinality', Integer),
    Column('dtd_identifier', String),
    schema='information_schema'
)

t_element_types = Table(
    'element_types', metadata,
    Column('object_catalog', String),
    Column('object_schema', String),
    Column('object_name', String),
    Column('object_type', String),
    Column('collection_type_identifier', String),
    Column('data_type', String),
    Column('character_maximum_length', Integer),
    Column('character_octet_length', Integer),
    Column('character_set_catalog', String),
    Column('character_set_schema', String),
    Column('character_set_name', String),
    Column('collation_catalog', String),
    Column('collation_schema', String),
    Column('collation_name', String),
    Column('numeric_precision', Integer),
    Column('numeric_precision_radix', Integer),
    Column('numeric_scale', Integer),
    Column('datetime_precision', Integer),
    Column('interval_type', String),
    Column('interval_precision', Integer),
    Column('domain_default', String),
    Column('udt_catalog', String),
    Column('udt_schema', String),
    Column('udt_name', String),
    Column('scope_catalog', String),
    Column('scope_schema', String),
    Column('scope_name', String),
    Column('maximum_cardinality', Integer),
    Column('dtd_identifier', String),
    schema='information_schema'
)

t_enabled_roles = Table(
    'enabled_roles', metadata,
    Column('role_name', String),
    schema='information_schema'
)

t_foreign_data_wrapper_options = Table(
    'foreign_data_wrapper_options', metadata,
    Column('foreign_data_wrapper_catalog', String),
    Column('foreign_data_wrapper_name', String),
    Column('option_name', String),
    Column('option_value', String),
    schema='information_schema'
)

t_foreign_data_wrappers = Table(
    'foreign_data_wrappers', metadata,
    Column('foreign_data_wrapper_catalog', String),
    Column('foreign_data_wrapper_name', String),
    Column('authorization_identifier', String),
    Column('library_name', String),
    Column('foreign_data_wrapper_language', String),
    schema='information_schema'
)

t_foreign_server_options = Table(
    'foreign_server_options', metadata,
    Column('foreign_server_catalog', String),
    Column('foreign_server_name', String),
    Column('option_name', String),
    Column('option_value', String),
    schema='information_schema'
)

t_foreign_servers = Table(
    'foreign_servers', metadata,
    Column('foreign_server_catalog', String),
    Column('foreign_server_name', String),
    Column('foreign_data_wrapper_catalog', String),
    Column('foreign_data_wrapper_name', String),
    Column('foreign_server_type', String),
    Column('foreign_server_version', String),
    Column('authorization_identifier', String),
    schema='information_schema'
)

t_foreign_table_options = Table(
    'foreign_table_options', metadata,
    Column('foreign_table_catalog', String),
    Column('foreign_table_schema', String),
    Column('foreign_table_name', String),
    Column('option_name', String),
    Column('option_value', String),
    schema='information_schema'
)

t_foreign_tables = Table(
    'foreign_tables', metadata,
    Column('foreign_table_catalog', String),
    Column('foreign_table_schema', String),
    Column('foreign_table_name', String),
    Column('foreign_server_catalog', String),
    Column('foreign_server_name', String),
    schema='information_schema'
)

t_information_schema_catalog_name = Table(
    'information_schema_catalog_name', metadata,
    Column('catalog_name', String),
    schema='information_schema'
)

t_key_column_usage = Table(
    'key_column_usage', metadata,
    Column('constraint_catalog', String),
    Column('constraint_schema', String),
    Column('constraint_name', String),
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('column_name', String),
    Column('ordinal_position', Integer),
    Column('position_in_unique_constraint', Integer),
    schema='information_schema'
)

t_parameters = Table(
    'parameters', metadata,
    Column('specific_catalog', String),
    Column('specific_schema', String),
    Column('specific_name', String),
    Column('ordinal_position', Integer),
    Column('parameter_mode', String),
    Column('is_result', String),
    Column('as_locator', String),
    Column('parameter_name', String),
    Column('data_type', String),
    Column('character_maximum_length', Integer),
    Column('character_octet_length', Integer),
    Column('character_set_catalog', String),
    Column('character_set_schema', String),
    Column('character_set_name', String),
    Column('collation_catalog', String),
    Column('collation_schema', String),
    Column('collation_name', String),
    Column('numeric_precision', Integer),
    Column('numeric_precision_radix', Integer),
    Column('numeric_scale', Integer),
    Column('datetime_precision', Integer),
    Column('interval_type', String),
    Column('interval_precision', Integer),
    Column('udt_catalog', String),
    Column('udt_schema', String),
    Column('udt_name', String),
    Column('scope_catalog', String),
    Column('scope_schema', String),
    Column('scope_name', String),
    Column('maximum_cardinality', Integer),
    Column('dtd_identifier', String),
    schema='information_schema'
)

t_referential_constraints = Table(
    'referential_constraints', metadata,
    Column('constraint_catalog', String),
    Column('constraint_schema', String),
    Column('constraint_name', String),
    Column('unique_constraint_catalog', String),
    Column('unique_constraint_schema', String),
    Column('unique_constraint_name', String),
    Column('match_option', String),
    Column('update_rule', String),
    Column('delete_rule', String),
    schema='information_schema'
)

t_role_column_grants = Table(
    'role_column_grants', metadata,
    Column('grantor', String),
    Column('grantee', String),
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('column_name', String),
    Column('privilege_type', String),
    Column('is_grantable', String),
    schema='information_schema'
)

t_role_routine_grants = Table(
    'role_routine_grants', metadata,
    Column('grantor', String),
    Column('grantee', String),
    Column('specific_catalog', String),
    Column('specific_schema', String),
    Column('specific_name', String),
    Column('routine_catalog', String),
    Column('routine_schema', String),
    Column('routine_name', String),
    Column('privilege_type', String),
    Column('is_grantable', String),
    schema='information_schema'
)

t_role_table_grants = Table(
    'role_table_grants', metadata,
    Column('grantor', String),
    Column('grantee', String),
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('privilege_type', String),
    Column('is_grantable', String),
    Column('with_hierarchy', String),
    schema='information_schema'
)

t_role_udt_grants = Table(
    'role_udt_grants', metadata,
    Column('grantor', String),
    Column('grantee', String),
    Column('udt_catalog', String),
    Column('udt_schema', String),
    Column('udt_name', String),
    Column('privilege_type', String),
    Column('is_grantable', String),
    schema='information_schema'
)

t_role_usage_grants = Table(
    'role_usage_grants', metadata,
    Column('grantor', String),
    Column('grantee', String),
    Column('object_catalog', String),
    Column('object_schema', String),
    Column('object_name', String),
    Column('object_type', String),
    Column('privilege_type', String),
    Column('is_grantable', String),
    schema='information_schema'
)

t_routine_privileges = Table(
    'routine_privileges', metadata,
    Column('grantor', String),
    Column('grantee', String),
    Column('specific_catalog', String),
    Column('specific_schema', String),
    Column('specific_name', String),
    Column('routine_catalog', String),
    Column('routine_schema', String),
    Column('routine_name', String),
    Column('privilege_type', String),
    Column('is_grantable', String),
    schema='information_schema'
)

t_routines = Table(
    'routines', metadata,
    Column('specific_catalog', String),
    Column('specific_schema', String),
    Column('specific_name', String),
    Column('routine_catalog', String),
    Column('routine_schema', String),
    Column('routine_name', String),
    Column('routine_type', String),
    Column('module_catalog', String),
    Column('module_schema', String),
    Column('module_name', String),
    Column('udt_catalog', String),
    Column('udt_schema', String),
    Column('udt_name', String),
    Column('data_type', String),
    Column('character_maximum_length', Integer),
    Column('character_octet_length', Integer),
    Column('character_set_catalog', String),
    Column('character_set_schema', String),
    Column('character_set_name', String),
    Column('collation_catalog', String),
    Column('collation_schema', String),
    Column('collation_name', String),
    Column('numeric_precision', Integer),
    Column('numeric_precision_radix', Integer),
    Column('numeric_scale', Integer),
    Column('datetime_precision', Integer),
    Column('interval_type', String),
    Column('interval_precision', Integer),
    Column('type_udt_catalog', String),
    Column('type_udt_schema', String),
    Column('type_udt_name', String),
    Column('scope_catalog', String),
    Column('scope_schema', String),
    Column('scope_name', String),
    Column('maximum_cardinality', Integer),
    Column('dtd_identifier', String),
    Column('routine_body', String),
    Column('routine_definition', String),
    Column('external_name', String),
    Column('external_language', String),
    Column('parameter_style', String),
    Column('is_deterministic', String),
    Column('sql_data_access', String),
    Column('is_null_call', String),
    Column('sql_path', String),
    Column('schema_level_routine', String),
    Column('max_dynamic_result_sets', Integer),
    Column('is_user_defined_cast', String),
    Column('is_implicitly_invocable', String),
    Column('security_type', String),
    Column('to_sql_specific_catalog', String),
    Column('to_sql_specific_schema', String),
    Column('to_sql_specific_name', String),
    Column('as_locator', String),
    Column('created', DateTime,
           server_default=text("('now'::text)::timestamp(2) with time zone")),
    Column('last_altered', DateTime,
           server_default=text("('now'::text)::timestamp(2) with time zone")),
    Column('new_savepoint_level', String),
    Column('is_udt_dependent', String),
    Column('result_cast_from_data_type', String),
    Column('result_cast_as_locator', String),
    Column('result_cast_char_max_length', Integer),
    Column('result_cast_char_octet_length', Integer),
    Column('result_cast_char_set_catalog', String),
    Column('result_cast_char_set_schema', String),
    Column('result_cast_character_set_name', String),
    Column('result_cast_collation_catalog', String),
    Column('result_cast_collation_schema', String),
    Column('result_cast_collation_name', String),
    Column('result_cast_numeric_precision', Integer),
    Column('result_cast_numeric_precision_radix', Integer),
    Column('result_cast_numeric_scale', Integer),
    Column('result_cast_datetime_precision', Integer),
    Column('result_cast_interval_type', String),
    Column('result_cast_interval_precision', Integer),
    Column('result_cast_type_udt_catalog', String),
    Column('result_cast_type_udt_schema', String),
    Column('result_cast_type_udt_name', String),
    Column('result_cast_scope_catalog', String),
    Column('result_cast_scope_schema', String),
    Column('result_cast_scope_name', String),
    Column('result_cast_maximum_cardinality', Integer),
    Column('result_cast_dtd_identifier', String),
    schema='information_schema'
)

t_schemata = Table(
    'schemata', metadata,
    Column('catalog_name', String),
    Column('schema_name', String),
    Column('schema_owner', String),
    Column('default_character_set_catalog', String),
    Column('default_character_set_schema', String),
    Column('default_character_set_name', String),
    Column('sql_path', String),
    schema='information_schema'
)

t_sequences = Table(
    'sequences', metadata,
    Column('sequence_catalog', String),
    Column('sequence_schema', String),
    Column('sequence_name', String),
    Column('data_type', String),
    Column('numeric_precision', Integer),
    Column('numeric_precision_radix', Integer),
    Column('numeric_scale', Integer),
    Column('start_value', String),
    Column('minimum_value', String),
    Column('maximum_value', String),
    Column('increment', String),
    Column('cycle_option', String),
    schema='information_schema'
)

t_sql_features = Table(
    'sql_features', metadata,
    Column('feature_id', String),
    Column('feature_name', String),
    Column('sub_feature_id', String),
    Column('sub_feature_name', String),
    Column('is_supported', String),
    Column('is_verified_by', String),
    Column('comments', String),
    schema='information_schema'
)

t_sql_implementation_info = Table(
    'sql_implementation_info', metadata,
    Column('implementation_info_id', String),
    Column('implementation_info_name', String),
    Column('integer_value', Integer),
    Column('character_value', String),
    Column('comments', String),
    schema='information_schema'
)

t_sql_languages = Table(
    'sql_languages', metadata,
    Column('sql_language_source', String),
    Column('sql_language_year', String),
    Column('sql_language_conformance', String),
    Column('sql_language_integrity', String),
    Column('sql_language_implementation', String),
    Column('sql_language_binding_style', String),
    Column('sql_language_programming_language', String),
    schema='information_schema'
)

t_sql_packages = Table(
    'sql_packages', metadata,
    Column('feature_id', String),
    Column('feature_name', String),
    Column('is_supported', String),
    Column('is_verified_by', String),
    Column('comments', String),
    schema='information_schema'
)

t_sql_parts = Table(
    'sql_parts', metadata,
    Column('feature_id', String),
    Column('feature_name', String),
    Column('is_supported', String),
    Column('is_verified_by', String),
    Column('comments', String),
    schema='information_schema'
)

t_sql_sizing = Table(
    'sql_sizing', metadata,
    Column('sizing_id', Integer),
    Column('sizing_name', String),
    Column('supported_value', Integer),
    Column('comments', String),
    schema='information_schema'
)

t_sql_sizing_profiles = Table(
    'sql_sizing_profiles', metadata,
    Column('sizing_id', Integer),
    Column('sizing_name', String),
    Column('profile_id', String),
    Column('required_value', Integer),
    Column('comments', String),
    schema='information_schema'
)

t_table_constraints = Table(
    'table_constraints', metadata,
    Column('constraint_catalog', String),
    Column('constraint_schema', String),
    Column('constraint_name', String),
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('constraint_type', String),
    Column('is_deferrable', String),
    Column('initially_deferred', String),
    schema='information_schema'
)

t_table_privileges = Table(
    'table_privileges', metadata,
    Column('grantor', String),
    Column('grantee', String),
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('privilege_type', String),
    Column('is_grantable', String),
    Column('with_hierarchy', String),
    schema='information_schema'
)

t_tables = Table(
    'tables', metadata,
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('table_type', String),
    Column('self_referencing_column_name', String),
    Column('reference_generation', String),
    Column('user_defined_type_catalog', String),
    Column('user_defined_type_schema', String),
    Column('user_defined_type_name', String),
    Column('is_insertable_into', String),
    Column('is_typed', String),
    Column('commit_action', String),
    schema='information_schema'
)

t_triggered_update_columns = Table(
    'triggered_update_columns', metadata,
    Column('trigger_catalog', String),
    Column('trigger_schema', String),
    Column('trigger_name', String),
    Column('event_object_catalog', String),
    Column('event_object_schema', String),
    Column('event_object_table', String),
    Column('event_object_column', String),
    schema='information_schema'
)

t_triggers = Table(
    'triggers', metadata,
    Column('trigger_catalog', String),
    Column('trigger_schema', String),
    Column('trigger_name', String),
    Column('event_manipulation', String),
    Column('event_object_catalog', String),
    Column('event_object_schema', String),
    Column('event_object_table', String),
    Column('action_order', Integer),
    Column('action_condition', String),
    Column('action_statement', String),
    Column('action_orientation', String),
    Column('action_timing', String),
    Column('action_reference_old_table', String),
    Column('action_reference_new_table', String),
    Column('action_reference_old_row', String),
    Column('action_reference_new_row', String),
    Column('created', DateTime,
           server_default=text("('now'::text)::timestamp(2) with time zone")),
    schema='information_schema'
)

t_udt_privileges = Table(
    'udt_privileges', metadata,
    Column('grantor', String),
    Column('grantee', String),
    Column('udt_catalog', String),
    Column('udt_schema', String),
    Column('udt_name', String),
    Column('privilege_type', String),
    Column('is_grantable', String),
    schema='information_schema'
)

t_usage_privileges = Table(
    'usage_privileges', metadata,
    Column('grantor', String),
    Column('grantee', String),
    Column('object_catalog', String),
    Column('object_schema', String),
    Column('object_name', String),
    Column('object_type', String),
    Column('privilege_type', String),
    Column('is_grantable', String),
    schema='information_schema'
)

t_user_defined_types = Table(
    'user_defined_types', metadata,
    Column('user_defined_type_catalog', String),
    Column('user_defined_type_schema', String),
    Column('user_defined_type_name', String),
    Column('user_defined_type_category', String),
    Column('is_instantiable', String),
    Column('is_final', String),
    Column('ordering_form', String),
    Column('ordering_category', String),
    Column('ordering_routine_catalog', String),
    Column('ordering_routine_schema', String),
    Column('ordering_routine_name', String),
    Column('reference_type', String),
    Column('data_type', String),
    Column('character_maximum_length', Integer),
    Column('character_octet_length', Integer),
    Column('character_set_catalog', String),
    Column('character_set_schema', String),
    Column('character_set_name', String),
    Column('collation_catalog', String),
    Column('collation_schema', String),
    Column('collation_name', String),
    Column('numeric_precision', Integer),
    Column('numeric_precision_radix', Integer),
    Column('numeric_scale', Integer),
    Column('datetime_precision', Integer),
    Column('interval_type', String),
    Column('interval_precision', Integer),
    Column('source_dtd_identifier', String),
    Column('ref_dtd_identifier', String),
    schema='information_schema'
)

t_user_mapping_options = Table(
    'user_mapping_options', metadata,
    Column('authorization_identifier', String),
    Column('foreign_server_catalog', String),
    Column('foreign_server_name', String),
    Column('option_name', String),
    Column('option_value', String),
    schema='information_schema'
)

t_user_mappings = Table(
    'user_mappings', metadata,
    Column('authorization_identifier', String),
    Column('foreign_server_catalog', String),
    Column('foreign_server_name', String),
    schema='information_schema'
)

t_view_column_usage = Table(
    'view_column_usage', metadata,
    Column('view_catalog', String),
    Column('view_schema', String),
    Column('view_name', String),
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('column_name', String),
    schema='information_schema'
)

t_view_routine_usage = Table(
    'view_routine_usage', metadata,
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('specific_catalog', String),
    Column('specific_schema', String),
    Column('specific_name', String),
    schema='information_schema'
)

t_view_table_usage = Table(
    'view_table_usage', metadata,
    Column('view_catalog', String),
    Column('view_schema', String),
    Column('view_name', String),
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    schema='information_schema'
)

t_views = Table(
    'views', metadata,
    Column('table_catalog', String),
    Column('table_schema', String),
    Column('table_name', String),
    Column('view_definition', String),
    Column('check_option', String),
    Column('is_updatable', String),
    Column('is_insertable_into', String),
    Column('is_trigger_updatable', String),
    Column('is_trigger_deletable', String),
    Column('is_trigger_insertable_into', String),
    schema='information_schema'
)

import os
from oemof.db import connection as oemof_connection


def grant_db_access(conn, schema, table, role):
    r"""Gives access to database users/ groups

    Parameters
    ----------
    conn : sqlalchemy connection object
        A valid connection to a database
    schema : str
        The database schema
    table : str
        The database table
    role : str
        database role that access is granted to

    """
    grant_str = """GRANT ALL ON TABLE {schema}.{table}
    TO {role} WITH GRANT OPTION;""".format(schema=schema, table=table,
                                           role=role)

    conn.execute(grant_str)


def add_primary_key(conn, schema, table, pk_col):
    r"""Adds primary key to database table

    Parameters
    ----------
    conn : sqlalchemy connection object
        A valid connection to a database
    schema : str
        The database schema
    table : str
        The database table
    pk_col : str
        Column that primary key is applied to

    """
    sql_str = """alter table {schema}.{table} add primary key ({col})""".format(
        schema=schema, table=table, col=pk_col)

    conn.execute(sql_str)


def change_owner_to(conn, schema, table, role):
    r"""Changes table's ownership to role

    Parameters
    ----------
    conn : sqlalchemy connection object
        A valid connection to a database
    schema : str
        The database schema
    table : str
        The database table
    role : str
        database role that access is granted to

    """
    sql_str = """ALTER TABLE {schema}.{table}
        OWNER TO {role};""".format(schema=schema,
                                   table=table,
                                   role=role)

    conn.execute(sql_str)


def create_oedb_config_file(filepath, section='oep'):
    """

    Parameters
    ----------
    filepath : str
        Absolute path of config file including the filename itself
    section : str
        Section in config file which contains connection details
    """

    # create egoio dir if not existent
    base_path = os.path.split(filepath)[0]
    if not os.path.isdir(base_path):
        os.mkdir(base_path)
        print('The directory {path} was created.'.format(path=base_path))

    # if not, ask to create with user input
    print('DB config file {} not found. '
          'This might be the first run of the tool. '
          'Do you want me to create this file?'
          .format(filepath))

    choice = ''
    while choice not in ['y', 'n']:
        choice = input('(y/n): ')

    if choice == 'y':
        username = input('Enter value for `username`: ')
        database = input('Enter value for `database`: ')
        host = input('Enter value for `host`: ')
        port = input('Enter value for `port` (default: 5432): ')

        file = open(filepath, 'w')
        template = '[{0}]\n' \
                   'username = {1}\n' \
                   'database = {2}\n' \
                   'host     = {3}\n' \
                   'port     = {4}\n'.format(section,
                                             username,
                                             database,
                                             host,
                                             '5432' if not port else port)
        file.write(template)
        file.close()

        print('Template {0} with section `{1}` created.\n You can manually edit'
              ' the config file.'
                    .format(filepath,
                            section))

        config_file = filepath

    # fallback: use oemof's config.ini
    else:
        print('No DB config file created, I\'ll try to use oemof\'s config.ini')
        config_file=None

    return config_file


def connection(filepath=None, section='oep'):
    """
    Instantiate a database connection (for the use with SQLAlchemy) based on
    oemof.db.

    The keyword argument `filepath` specifies the location of the config file
    that contains database connection information. If not given, the default
    of `~/.egoio/config.ini` applies.

    Parameters
    ----------
    filepath : str
        Absolute path of config file including the filename itself
    """

    # define default filepath if not provided
    if filepath is None:
        filepath = os.path.join(os.path.expanduser("~"), '.egoio', 'config.ini')

    # does the file exist?
    if not os.path.isfile(filepath):
        config_file = create_oedb_config_file(filepath, section=section)
    else:
        config_file = filepath

    # establish connection and return it
    conn = oemof_connection(section=section, config_file=config_file)

    return conn
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
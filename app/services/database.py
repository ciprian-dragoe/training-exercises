from data.configuration import CONFIGURATION


import psycopg2
import psycopg2.extras
from enum import Enum


class DbConnection(Enum):
    admin = 1
    language_pg = 2


def get_db_connection(connection_type: DbConnection):
    """
    Create a database connection based on the :connection_data: parameter
    :connection_data: Connection string attributes
    :returns: psycopg2.connection
    """
    if connection_type == DbConnection.admin:
        connection_string = f"dbname={CONFIGURATION['ADMIN_DBNAME']} user={CONFIGURATION['ADMIN_USER']} host={CONFIGURATION['ADMIN_HOST']} password={CONFIGURATION['ADMIN_PASS']} port={CONFIGURATION['ADMIN_PORT']}"
    else:
        connection_string = f"dbname={CONFIGURATION['PRACTICE_DBNAME']} user={CONFIGURATION['PRACTICE_USER']} host={CONFIGURATION['PRACTICE_HOST']} password={CONFIGURATION['PRACTICE_PASS']} port={CONFIGURATION['PRACTICE_PORT']}"
    try:
        conn = psycopg2.connect(connection_string)
        conn.autocommit = True
        return conn
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)


def execute_select(statement, connection, variables=None, fetchall=True):
    """
    Execute SELECT statement optionally parameterized.
    Use fetchall=False to get back one value (fetchone)

    Example:
    > execute_select('SELECT %(title)s; FROM shows', variables={'title': 'Codecool'})

    statement: SELECT statement

    variables:  optional parameter dict, optional parameter fetchall"""
    with connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement, variables)
            result_set = cursor.fetchall() if fetchall else cursor.fetchone()
    return result_set

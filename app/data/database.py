from data.configuration import CONFIGURATION


import psycopg2
import psycopg2.extras
from enum import Enum


class DbConnection(Enum):
    admin = 1
    language_pg = 2


def admin_connection(func):
    def get_connection_wrapper(*args, **kwargs):
        connection = get_db_connection(DbConnection.admin)
        return func(connection, *args, **kwargs)

    return get_connection_wrapper()


def playground_connection(func):
    def get_connection_wrapper(*args, **kwargs):
        connection = get_db_connection(DbConnection.language_pg)
        return func(connection, *args, **kwargs)

    return get_connection_wrapper()


def get_db_connection(connection_type):
    if connection_type == DbConnection.admin:
        connection_string = f"dbname={CONFIGURATION['ADMIN_DBNAME']} user={CONFIGURATION['ADMIN_USER']} host={CONFIGURATION['ADMIN_HOST']} password={CONFIGURATION['ADMIN_PASS']} port={CONFIGURATION['ADMIN_PORT']}"
    else:
        connection_string = f"dbname={CONFIGURATION['PRACTICE_DBNAME']} user={CONFIGURATION['PRACTICE_USER']} host={CONFIGURATION['PRACTICE_HOST']} password={CONFIGURATION['PRACTICE_PASS']} port={CONFIGURATION['PRACTICE_PORT']}"
    try:
        print(f'DEBUG connecting to: {connection_string}')
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
        return connection
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)


def execute(connection, statement, variables=None):
    with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute(statement, variables)
        if cursor.pgresult_ptr is not None:
            return cursor.fetchall()

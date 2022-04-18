from enum import Enum
import pymssql
import psycopg2
import psycopg2.extras


from data.configuration import CONFIGURATION


class DbConnection(Enum):
    admin = 1
    language_pg = 2


def connection_callback_builder(connection_type):
    if connection_type == DbConnection.admin:
        if CONFIGURATION["ADMIN_SERVER_TYPE"] == "sql-server":
            connection_service = pymssql
        else:
            connection_service = psycopg2
        return lambda: connection_service.connect(server=CONFIGURATION['ADMIN_HOST'], port=CONFIGURATION['ADMIN_PORT'], user=CONFIGURATION['ADMIN_USER'], password=CONFIGURATION['ADMIN_PASS'], database=CONFIGURATION['ADMIN_DBNAME'])
    else:
        if CONFIGURATION["PRACTICE_SERVER_TYPE"] == "sql-server":
            connection_service = pymssql
        else:
            connection_service = psycopg2
        return lambda: connection_service.connect(server=CONFIGURATION['PRACTICE_HOST'], port=CONFIGURATION['PRACTICE_PORT'], user=CONFIGURATION['PRACTICE_USER'], password=CONFIGURATION['PRACTICE_PASS'], database=CONFIGURATION['PRACTICE_DBNAME'])


def get_db_connection(connection_type):
    connection_builder = connection_callback_builder(connection_type)
    try:
        connection = connection_builder()
        connection.autocommit = True
        return connection
    except:
        print("Cannot connect to database.")


def execute(connection, statement, variables=None):
    with connection.cursor() as cursor:
        cursor.execute(statement, variables)
        if cursor.pgresult_ptr is not None:
            return cursor.fetchall()

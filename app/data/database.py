from enum import Enum
import pymssql
import psycopg2
import psycopg2.extras


from data.configuration import CONFIGURATION


class DbConnection(Enum):
    admin = 1
    language_pg = 2


def execute_sql_server_query(host, port, user, password, db, statement, variables):
    try:
        connection = pymssql.connect(server=host, port=port, user=user, password=password, database=db)
        with connection.cursor() as cursor:
            cursor.execute(statement, variables)
            return cursor.fetchall()
    except:
        print("Cannot connect to database.")


def execute_postgres_query(host, port, user, password, db, statement, variables):
    try:
        connection = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
        connection.autocommit = True
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement, variables)
            if cursor.pgresult_ptr is not None:
                return cursor.fetchall()
    except:
        print("Cannot connect to database.")


CONNECTION_HANDLER_FACTORY = {
    "sql-server": execute_sql_server_query,
    "postgres": execute_postgres_query,
}


def execute(connection_type, statement, variables=None):
    if connection_type == DbConnection.admin:
        connection_handler = CONNECTION_HANDLER_FACTORY[CONFIGURATION["ADMIN_SERVER_TYPE"]]
        return connection_handler(CONFIGURATION['ADMIN_HOST'], CONFIGURATION['ADMIN_PORT'],
                                  CONFIGURATION['ADMIN_USER'], CONFIGURATION['ADMIN_PASS'],
                                  CONFIGURATION['ADMIN_DBNAME'], statement, variables)
    elif connection_type == DbConnection.language_pg:
        connection_handler = CONNECTION_HANDLER_FACTORY[CONFIGURATION["PRACTICE_SERVER_TYPE"]]
        return connection_handler(CONFIGURATION['PRACTICE_HOST'], CONFIGURATION['PRACTICE_PORT'],
                                  CONFIGURATION['PRACTICE_USER'], CONFIGURATION['PRACTICE_PASS'],
                                  CONFIGURATION['PRACTICE_DBNAME'], statement, variables)

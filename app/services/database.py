from data.configuration import CONFIGURATION

import os
import psycopg2
import psycopg2.extras


def establish_connection(connection_data=None):
    """
    Create a database connection based on the :connection_data: parameter

    :connection_data: Connection string attributes

    :returns: psycopg2.connection
    """
    if connection_data is None:
        connection_data = get_connection_data()
    try:
        connect_str = "dbname={} user={} host={} password={} port={}".format(
            connection_data["dbname"],
            connection_data["user"],
            connection_data["host"],
            connection_data["password"],
            connection_data["port"],
        )
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        return conn

    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)


def get_connection_data():
    return {
        "dbname": CONFIGURATION['PRACTICE_DBNAME'],
        "user": CONFIGURATION['PRACTICE_USER'],
        "host": CONFIGURATION["PRACTICE_HOST"],
        "password": CONFIGURATION["PRACTICE_PASS"],
        "port": CONFIGURATION["PRACTICE_PORT"],
    }


def execute_script_file(file_path):
    """
    Execute script file based on the given file path.
    Print the result of the execution to console.

    Example:
    > execute_script_file('db_schema/01_create_schema.sql')

    :file_path: Relative path of the file to be executed.
    """
    package_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(package_directory, file_path)
    with open(full_path) as script_file:
        with establish_connection() as conn, conn.cursor() as cursor:
            try:
                sql_to_run = script_file.read()
                cursor.execute(sql_to_run)
                print("{} script executed successfully.".format(file_path))
            except Exception as ex:
                print("Execution of {} failed".format(file_path))
                print(ex.args)


def execute_select(statement, variables=None, fetchall=True):
    """
    Execute SELECT statement optionally parameterized.
    Use fetchall=False to get back one value (fetchone)

    Example:
    > execute_select('SELECT %(title)s; FROM shows', variables={'title': 'Codecool'})

    statement: SELECT statement

    variables:  optional parameter dict, optional parameter fetchall"""
    with establish_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement, variables)
            result_set = cursor.fetchall() if fetchall else cursor.fetchone()
    return result_set

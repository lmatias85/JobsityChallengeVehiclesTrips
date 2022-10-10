import mysql.connector as connector
from mysql.connector import Error


def connect_to_db(database, user, password):
    try:
        conn = connector.connect(host='localhost',
                                 database=database,
                                 user=user,
                                 password=password)
        return conn
    except Error as e:
        print("Error getting db connection. {}".format(e))
        if conn.is_connected():
            conn.close()
        raise


def get_sql_statements_from_file(path):
    try:
        db_file = open(path, 'r')
        db_sql = db_file.read()
        db_file.close()
        db_sql_statements = db_sql.split(';')
        return db_sql_statements
    except IOError as e:
        print('Error while opening file. {}'.format(e))
        raise


def execute_sql_statements(db_connector, sql_statements):
    cursor = db_connector.cursor()
    for statement in sql_statements:
        cursor.execute(statement)
    cursor.close()


def execute_sql_report(db_connector, sql_statements):
    cursor = db_connector.cursor()
    for statement in sql_statements:
        cursor.execute(statement)
    return cursor

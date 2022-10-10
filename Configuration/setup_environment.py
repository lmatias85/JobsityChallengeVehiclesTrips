import os
from Services.db_services import *


def execute_on_db(sql_file_path):
    conn = connect_to_db(database='mysql',
                         user='root',
                         password='root')
    if conn.is_connected():
        execute_sql_statements(conn, get_sql_statements_from_file(sql_file_path))
    else:
        print('Database connection lost. Pleas try again.')


if __name__ == '__main__':
    ''' Database configuration'''
    execute_on_db(os.path.abspath(os.getcwd())+'/SQLScripts/00_create_db_and_user.sql')
    print('Database configuration set up')
    ''' Database structure definition'''
    print('Database structure set up')
    execute_on_db(os.path.abspath(os.getcwd()) + '/SQLScripts/01_create_db_structure.sql')

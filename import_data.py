import os
import csv
import sys
from Services.db_services import *


def get_lines(filename):
    with open(filename, 'r') as csv_file:
        data_reader = csv.reader(csv_file)
        for row in data_reader:
            yield row


def insert_data(sql_conn, rows_to_insert):
    cursor = sql_conn.cursor()
    sql_insert = get_sql_statements_from_file(os.path.abspath(os.getcwd()) + '/SQLScripts/03_insert_raw_data.sql')
    cursor.executemany(sql_insert[0], rows_to_insert)
    return cursor.rowcount


def execute_sql(sql_conn, sql_path):
    sql_statements = get_sql_statements_from_file(os.path.abspath(os.getcwd()) + sql_path)
    execute_sql_statements(sql_conn, sql_statements)


def import_trips_data():
    rows = []
    rows_per_block = 0
    block_of_lines = 0
    rows_processed = 0
    header = True
    conn = connect_to_db("jobsity_db", "jobsity_user", "jobsity_user")
    csv_path = os.path.abspath(os.getcwd()) + '/DataSources/trips.csv'
    file = open(csv_path, 'r')
    rows_count = sum(1 for row in csv.reader(file))
    rows_per_block = int(rows_count / 10)
    print('Total number of rows to be processed: {}'.format(str(rows_count)))
    try:
        execute_sql(conn, '/SQLScripts/02_create_raw_table.sql')
        for i in get_lines(csv_path):
            if block_of_lines < rows_per_block:
                block_of_lines += 1
                rows.append(i)
            else:
                if header:
                    rows_inserted = insert_data(conn, rows[1:])
                    header = False
                else:
                    rows_inserted = insert_data(conn, rows)
                rows_processed = rows_processed + rows_inserted
                block_of_lines = 0
                rows.clear()
                rows.append(i)
                print('Number of rows already processed: {}'.format(rows_processed))
        if rows:
            rows_inserted = insert_data(conn, rows)
            rows_processed = rows_processed + rows_inserted
            print('Number of rows already processed: {}'.format(rows_processed))
        print("Done")
        print("Retrieving and inserting not duplicate data")
        execute_sql(conn, '/SQLScripts/04_insert_trips_data.sql')
        conn.commit()
        print("Done")
    except Exception as e:
        conn.rollback()
        print('Error while ingesting data. {}'.format(e))
    finally:
        if conn.is_connected():
            conn.close()


if __name__ == '__main__':
    import_trips_data()

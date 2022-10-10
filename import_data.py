import os
import csv
from Services.db_services import *


def get_lines(filename):
    with open(filename, 'r') as csv_file:
        data_reader = csv.reader(csv_file)
        for row in data_reader:
            yield row


def insert_data(connector, rows_to_insert):
    cursor = connector.cursor()
    sql_insert = """INSERT INTO test (id, region) values (%s, %s)"""
    cursor.executemany(sql_insert, rows_to_insert)


def create_raw_table(connector):


if __name__ == '__main__':
    rows = []
    block_of_lines = 0
    header = True
    conn = connect_to_db("jobsity_db", "jobsity_user", "jobsity_user")
    try:
        for i in get_lines(os.path.abspath(os.getcwd()) + '/DataSources/prueba.csv'):
            if block_of_lines < 1000:
                block_of_lines += 1
                rows.append(i)
            else:
                if header:
                    insert_data(conn, rows[1:])
                    header = False
                else:
                    insert_data(conn, rows)
                block_of_lines = 0
                rows.clear()
                rows.append(i)
        if rows:
            insert_data(conn, rows)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print('Error while ingesting data. {}'.format(e))


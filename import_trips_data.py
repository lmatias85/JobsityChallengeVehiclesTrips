import os
from Services.db_services import *
import pymysql


def file_block(fp, number_of_blocks, block):
    assert 0 <= block < number_of_blocks
    assert 0 < number_of_blocks
    fp.seek(0, 2)
    file_size = fp.tell()
    ini = file_size * block / number_of_blocks
    end = file_size * (1 + block) / number_of_blocks
    if ini <= 0:
        fp.seek(0)
    else:
        fp.seek(ini - 1)
        fp.readline()
    while fp.tell() < end:
        yield fp.readline()


if __name__ == '__main__':
    iteration = 0
    fp = open(os.path.abspath(os.getcwd()) + '/DataSources/trips.csv')
    fp.seek(1)
    number_of_chunks = 1000
    for chunk_number in range(number_of_chunks):
        print(chunk_number, 100 * '=')
        for line in file_block(fp, number_of_chunks, chunk_number):
            print(line)

import os
from Services.db_services import *


def gen_avg_weekly_trips_by_region_report(region):
    conn = connect_to_db("jobsity_db", "jobsity_user", "jobsity_user")
    sql_report = get_sql_statements_from_file(os.path.abspath(os.getcwd()) + '/SQLScripts/05_trips_per_week_by_region.sql')
    sql_report_new = []
    for i in sql_report:
        sql_report_new.append(i.replace("@param_region", "'"+region+"'"))
    cursor = execute_sql_report(conn, sql_report_new)
    print("\n\n")
    print("Weekly trips by region")
    print("----------------------\n")
    print(f"Week\t\tFrom\t\t\tTo\t\t\t\tTrips")
    for (number_of_week, week_from, week_to, avg_number_of_trips) in cursor:
        print("{:4}\t\t{}\t\t{}\t\t{:5}".format(number_of_week,week_from, week_to, avg_number_of_trips))
    cursor.close()
    conn.close()

def gen_avg_weekly_trips_by_area_report(x1, y2):
    conn = connect_to_db("jobsity_db", "jobsity_user", "jobsity_user")
    sql_report = get_sql_statements_from_file(os.path.abspath(os.getcwd()) + '/SQLScripts/06_trips_per_week_by_area.sql')
    sql_report_new = []
    for i in sql_report:
        sql = i.replace("@param_x1", str(x1))
        sql = sql.replace("@param_y2", str(y2))
        sql_report_new.append(sql)
    cursor = execute_sql_report(conn, sql_report_new)
    print("\n\n")
    print("Weekly trips by area")
    print("----------------------\n")
    print(f"Week\t\tFrom\t\t\tTo\t\t\t\tTrips")
    for (number_of_week, week_from, week_to, avg_number_of_trips) in cursor:
        print("{:4}\t\t{}\t\t{}\t\t{:5}".format(number_of_week,week_from, week_to, avg_number_of_trips))
    cursor.close()
    conn.close()

if __name__ == "__main__":
    gen_avg_weekly_trips_by_region_report("Turin")
    gen_avg_weekly_trips_by_area_report(9, 60)

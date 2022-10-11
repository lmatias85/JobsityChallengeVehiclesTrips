import os
from Services.db_services import *

''' 
    This function generates and prints the report for the weekly average number of trips by region. The core of the 
    report logic is set up in the /SQLScripts/05_trips_per_week_by_region.sql script.
    It receives the region by parameter.
'''
def gen_avg_weekly_trips_by_region_report(region):
    conn = connect_to_db("jobsity_db", "jobsity_user", "jobsity_user")
    sql_report = get_sql_statements_from_file(
        os.path.abspath(os.getcwd()) + '/SQLScripts/05_trips_per_week_by_region.sql')
    sql_report_new = []
    for i in sql_report:
        sql_report_new.append(i.replace("@param_region", "'" + region + "'"))
    cursor = execute_sql_report(conn, sql_report_new)
    print("\n\n")
    print("Weekly trips by region")
    print("----------------------\n")
    print(f"Week\t\tFrom\t\t\tTo\t\t\t\tTrips")
    for (number_of_week, week_from, week_to, avg_number_of_trips) in cursor:
        print("{:4}\t\t{}\t\t{}\t\t{:5}".format(number_of_week, week_from, week_to, avg_number_of_trips))
    cursor.close()
    conn.close()


'''
    This function generates and prints the report for weekly average number of trips by area. 
    The core of the report logic is set up in the /SQLScripts/06_trips_per_week_by_area.sql script.
    The main idea is to receive two point coords, but we are interested that either the origin or destiny
    point are greater than the first x coord and lower than the second y coord.
'''
def gen_avg_weekly_trips_by_area_report(x1, y2):
    conn = connect_to_db("jobsity_db", "jobsity_user", "jobsity_user")
    sql_report = get_sql_statements_from_file(
        os.path.abspath(os.getcwd()) + '/SQLScripts/06_trips_per_week_by_area.sql')
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
        print("{:4}\t\t{}\t\t{}\t\t{:5}".format(number_of_week, week_from, week_to, avg_number_of_trips))
    cursor.close()
    conn.close()


''' 
    This is a function to test the reports.
'''
if __name__ == "__main__":
    gen_avg_weekly_trips_by_region_report("Turin")
    gen_avg_weekly_trips_by_area_report(9, 60)

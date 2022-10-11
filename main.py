from import_data import *
from reports import *

if __name__ == '__main__':
    while(True):
        print("1) Ingest Trips Data")
        print("2) Weekly average trips by region")
        print("3) Weekly average trips for a bounding box")
        print("4) Quit")

        try:
            option = int(input("Select your option: "))
        except Exception as e:
            print("Must choose a numeric option from 1 to 3")

        if option == 1:
            import_trips_data()
        elif option == 2:
            region = str(input("Please insert the region name: "))
            gen_avg_weekly_trips_by_region_report(region)
        elif option == 3:
            x1 = (input("Please insert value for the first X coord "))
            y1 = (input("Please insert value for the first Y coord "))
            x2 = (input("Please insert value for the second X coord "))
            y2 = (input("Please insert value for the second Y coord "))
            gen_avg_weekly_trips_by_area_report(x1, y2)
        elif option == 4:
            break
        else:
            print("Invalid option, please try again.")





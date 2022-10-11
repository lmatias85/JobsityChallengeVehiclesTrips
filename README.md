# JobsityChallengeVehiclesTrips

### Technical Environment and Platform Settings:

The application has been developed using the following technologies:

- Operating System: Linux Ubuntu 20.04
- SDK: Python 3.9
- Database: MySQL 8.0.30 / localhost 


### Considerations

There is a file that set up the database environment for developing purposes.
The file **setup_environment.py** has a main executable function that calls the following scripts:

- 00_create_db_and_user.sql: located in the Configuration folder. This script connect to the MySQL database as root and generates a database called **"Jobsity_db"**. Also, it will create a user called "**jobsity_user**" which will be the user to perform all database operations.
- 01_create_db_structure.sql: located in the Configuration folder. this script creates the main trips table which stores the data. It is a partitioned table and only 2018 partitions are created.
- Database: Jobsity_db
- User: Jobsity_user
- Password: Jobsity_user
- Services: this folder contains a script that performs the mains database operations.
- SQLScripts: this folder contains all sql statements used by the application. It also contains two queries to retrieve the regions with "**cheap_mobile**" datasource, and the last datasource of the most commonly appearing regions.

### Run application

The main file called "**main.py**" shows all the options the application can perform.





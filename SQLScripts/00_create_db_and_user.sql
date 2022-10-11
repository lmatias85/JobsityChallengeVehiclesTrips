USE mysql;
CREATE DATABASE jobsity_db;
USE jobsity_db;
CREATE USER 'jobsity_user'@'localhost' IDENTIFIED BY 'jobsity_user';
GRANT ALL PRIVILEGES ON  jobsity_db.* TO 'jobsity_user'@'localhost' WITH GRANT OPTION;
GRANT CREATE, INSERT, DELETE, SELECT ON jobsity_db.* TO 'jobsity_user'@'localhost';
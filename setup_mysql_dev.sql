CREATE DATABASE IF NOT EXISTS guidehub_dev_db;

CREATE USER IF NOT EXISTS 'guidehub_dev'@'localhost' IDENTIFIED BY 'guidehub_dev_pwd';

GRANT ALL PRIVILEGES ON guidehub_dev_db.* TO 'guidehub_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'guidehub_dev'@'localhost';
CREATE DATABASE IF NOT EXISTS guidehub_test_db;

CREATE USER IF NOT EXISTS 'guidehub_test'@'localhost' IDENTIFIED BY 'guidehub_test_pwd';

GRANT ALL PRIVILEGES ON guidehub_test_db.* TO 'guidehub_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'guidehub_test'@'localhost';
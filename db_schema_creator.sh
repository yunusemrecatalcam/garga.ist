#!/usr/bin/env bash

Q1="CREATE DATABASE IF NOT EXISTS garga CHARACTER SET utf8 COLLATE utf8_general_ci;"
Q2="USE garga;"
Q3="CREATE TABLE IF NOT EXISTS texts ( \
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, \
    textname TINYTEXT NOT NULL, \
    text TEXT NOT NULL,  \
    mahlas TINYTEXT,  \
    reg_date TIMESTAMP );"
Q4="CREATE TABLE IF NOT EXISTS users ( \
    mahlas TINYTEXT NOT NULL, \
    passwords TINYTEXT NOT NULL);"
Q9="CREATE TABLE IF NOT EXISTS votes ( \
    id INT(6),\
    admin TINYTEXT NOT NULL,\
    vote boolean);"

Q5="CREATE USER IF NOT EXISTS 'api'@'localhost' IDENTIFIED BY 'pass';"
Q6="GRANT ALL PRIVILEGES ON * . * TO 'api'@'localhost';"
Q7="FLUSH PRIVILEGES;"
Q8="GRANT DELETE,INSERT,SELECT,UPDATE ON garga.* TO 'api'@'localhost';"

SQL="${Q1}${Q2}${Q3}${Q4}${Q5}${Q6}${Q7}${Q8}"

mysql -u root -p -e "$SQL"
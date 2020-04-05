#!/bin/bash
mysql_ip="$1"
mysql -uroot -pmypassword -h "$mysql_ip" -v << EOF
CREATE DATABASE IF NOT EXISTS proj2db;
CREATE TABLE IF NOT EXISTS proj2db.prize(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    prize INTEGER NOT NULL
);
EOF

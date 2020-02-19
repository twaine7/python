# pylint: disable=no-member

## Event Generator - creates new event object and adds to db table as record

import boto3
import logging
import rds_config
import socket
import mysql.connector as mariadb

# -- for MariaDB RDS instance in AWS
# uses 'rds_config.py' file to define rds connection / table info
rds_host = rds_config.db_host
name = rds_config.db_user
password = rds_config.db_pass
db_name = rds_config.db_name


# Connection Info
conn = mariadb.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
cur = conn.cursor(buffered=True)

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

records_to_insert = (host_name, host_ip)
records_to_find = (host_name, host_ip)

print(records_to_find)

find_query = """select hostname, hostip from configitem"""



cur.execute(find_query)

query = cur.fetchall()

i = 0
found = 0
for record in query:
    print(host_name)
    print(query[i][0])

    if host_name == query[i][0]:
        found = 1
    i += 1

if found == 0:
    print("not found, inserting record")
    insert_query = """insert into configitem (hostname, hostip) VALUES (%s, %s)"""
    cur.execute(insert_query, records_to_insert)

conn.commit()

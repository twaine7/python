# pylint: disable=no-member

## Event Generator - Host info-gather method (not currently in use)
import boto3
import logging
import rds_config
import mysql.connector as mariadb
import socket

# -- for MariaDB RDS instance in AWS
# uses 'rds_config.py' file to define rds connection / table info
rds_host = rds_config.db_host
name = rds_config.db_user
password = rds_config.db_pass
db_name = rds_config.db_name


class Newhost(object):

    def __init__(self, host_name, host_ip):
        self.host_name = host_name
        self.host_ip = host_ip

    def createhost(self):
        conn = mariadb.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
        cur = conn.cursor()

        ci_info = (self.host_name, self.host_ip)

        find_query = """select hostname, hostip from configitem"""

        cur.execute(find_query)

        query = cur.fetchall()

        i = 0
        found = 0

        # Checks to see if CI exists in database
        for record in query:
            if self.host_name == query[i][0]:
                print(record, "exists in db")
                found = 1
            i += 1

        # Inserts CI record into database if does not already exist
        if found == 0:
            print("not found, inserting record: ", record)
            insert_query = """insert into configitem (hostname, hostip) VALUES (%s, %s)"""
            cur.execute(insert_query, ci_info)

        conn.commit()
# pylint: disable=no-member

## Event Generator - creates new event object and adds to db table as record

import boto3
import logging
import rds_config
import mysql.connector as mariadb

# -- for MariaDB RDS instance in AWS
# uses 'rds_config.py' file to define rds connection / table info
rds_host = rds_config.db_host
name = rds_config.db_user
password = rds_config.db_pass
db_name = rds_config.db_name


# Class object for each event
class Newevent(object):

    def __init__(self, uid, time_stamp, host_name, host_ip, used_cpu_per, used_mem, used_mem_per):
        self.uid = uid
        self.time_stamp = time_stamp
        self.host_name = host_name
        self.host_ip = host_ip
        self.used_cpu_per = used_cpu_per
        self.used_mem = used_mem
        self.used_mem_per = used_mem_per


    def createrecord(self):
        # Connection Info
        conn = mariadb.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
        cur = conn.cursor()

        records_to_insert = (self.uid, self.time_stamp, self.host_name, self.host_ip, self.used_cpu_per, self.used_mem, self.used_mem_per)

        insert_query = """insert into events (uid, timestamp, hostname, hostip, usedcpupercent, usedmem, usedmempercent) VALUES (%s, %s,%s,%s,%s,%s,%s)"""

        cur.execute(insert_query, records_to_insert)
        conn.commit()
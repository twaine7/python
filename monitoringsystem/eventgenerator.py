# pylint: disable=no-member

## Event Generator - main

# Import python modules
import boto3
import time
import datetime
import socket
import psutil
import os
import subprocess
import rds_config # <--- need to create file "rds_config.py" with RDS connection info (username, password, hostname, dbname)
import mysql.connector as mariadb

# class to create event objects
import createnewevent
import createnewci

#RDS Connection Info
rds_host = rds_config.db_host
name = rds_config.db_user
password = rds_config.db_pass
db_name = rds_config.db_name

# Sets MariaDB connection variables
conn = mariadb.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
cur = conn.cursor(buffered=True)

def generateuid():
    # Finds last UID in Events DB Table
    find_query = """select uid from events order by uid desc limit 1"""
    cur.execute(find_query)
    query = cur.fetchall()
    conn.commit()
    lastuid = query[0][0]

    print("Last UID:", lastuid)

    # Gets integer from UID, increments by 1, returns new UID
    intfromlastuid = int("".join(s for s in lastuid if s.isdigit()))
    nexti = intfromlastuid + 1  

    nextuid ="id" + str(format(nexti, '04d'))
    print("Next UID:", nextuid)
    return nextuid
    
def findhostinfo():
    # Finds IP and Hostname of localhost
    host_name = socket.gethostname()
    return host_name, socket.gethostbyname(host_name)

def gettimestamp():
    # Assign timestamp to event entry
    return str(datetime.datetime.now().time())

def gethostresourceinfo():
    # Get localhost's memory and cpu utilization info
    vir_mem = psutil.virtual_memory()
    return vir_mem, vir_mem.used, int(vir_mem.percent), int(psutil.cpu_percent())

while True:
    # Iterates iterator for UID ('id000' + i) & creates new uid
    uid = generateuid()
    
    # Ping application
    #application = "twitch.tv"
#   type_, min_, avg_, max_, mdev_, total_, loss_ = ping(application)

#    print(application, type_, min_, avg_, max_, mdev_, total_, loss_)

    # Get local host info
    host_name, host_ip = findhostinfo()

    # Enter hostname into configitem db table
    new_ci = createnewci.Newhost(host_name, host_ip)
    createnewci.Newhost.createhost(new_ci)

    # Get resource info
    vir_mem, used_mem, used_mem_per, used_cpu_per = gethostresourceinfo()

    # Get timestamp
    time_stamp = gettimestamp()

    # Creates new event instancen
    new_event = createnewevent.Newevent(uid, time_stamp, host_name, host_ip, used_cpu_per, used_mem, used_mem_per)
    
    # Calls 'newevent' class to enter event into DB
    createnewevent.Newevent.createrecord(new_event)
  
    # Increments each iteration by 1 second
    time.sleep(1)
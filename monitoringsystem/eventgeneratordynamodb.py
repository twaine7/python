# pylint: disable=no-member

import boto3
import psutil
import datetime
import time
import putitem
import socket

# Get the service resource.  Later, this can be brought into a seperate functionality depending on the database table being referenced
# 'dynamodb' is the aws service being used
dynamodb = boto3.resource('dynamodb')

# 'monitor' is the database table being referenced
table = dynamodb.Table('monitor')

# Start UID count number (will increment in following 'while' statement)
uid = 1

# While statement to continuously generate events, iterates each second
while True:

    # All the following should be in a class-- as more event types are added, a class shall be configured for each

    # Finds IP and Hostname of localhost
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)

    # Create unique identifer (table index)
    new_uid = "id" + str(format(uid, '04d'))
    
    # Assign timestamp to event entry
    time_stamp = str(datetime.datetime.now().time())

    # categorizes event as value_type
    value_type = 'mem'

    # Get localhost's memory utilization info
    vir_mem = psutil.virtual_memory()
    used_mem = vir_mem.used
    used_mem_per = int(vir_mem.percent)

    # Increments UID value each iteration
    uid += 1

    # Calls 'newevent' class to enter event into DB
    putitem.newevent(new_uid, time_stamp, host_name, host_ip, value_type, used_mem, used_mem_per)

    # Debug / confirmation that the UIDs are incrementing, and the entries are current
    print(new_uid, time_stamp, host_name, host_ip, value_type, used_mem, used_mem_per)
    
    time.sleep(1)
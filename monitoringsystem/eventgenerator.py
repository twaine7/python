# pylint: disable=no-member

## Event Generator - main


# Import python modules
import boto3
import time
import datetime
import socket
import psutil
import pickle
import os
import subprocess

# class to create event objects
import createnewevent
import createnewci


# Get the service resource.  Later, this can be brought into a seperate functionality depending on the database table being referenced
# 'dynamodb' is the aws service being used
dynamodb = boto3.resource('dynamodb')

# 'monitor' is the database table being referenced
table = dynamodb.Table('monitoring')

# Define Variables
i = 1

def generateuid(i):
    # Generates new event UID
    return "id" + str(format(i, '04d'))
    

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

def load():  
    # Load variables from last script run (current_uid, uid, prev_uid)
    print("Loading i")
    i = pickle.load(open('store.pckle', 'rb'))
    return i

def save(i):  
    # Store variables for use in subsequent script runs (uid, i, prev_uid)
    print("Saving i", i)
    f = open('store.pckle', 'wb')
    pickle.dump(i,f)
    f.close()

def load_save():
    choice = ""
    while choice != 'N' and choice != 'L':
        
        choice = input("Load or New? l/n").upper()
        if choice == 'N':
            print("Starting new count")
            i = 1
            print("i = ", i)
            return i
        if choice == 'L':
            print("Loading from store.pckle")
            i = load()
            print("Starting count at", i)
            return i
i = load_save()

while True:
    # Iterates iterator for UID ('id000' + i) & creates new uid
    uid = generateuid(i)
    i += 1

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
    
    # Saves current UID, iterator, and previous UID to store.pckle
    save(i)
    # Debug / confirmation that the UIDs are incrementing, and the entries are current
    
    # Increments each iteration by 1 second
    time.sleep(1)
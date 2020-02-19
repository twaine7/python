# pylint: disable=no-member

## Event Generator - creates new event object and adds to db table as record

import boto3

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
        # Get the service resource:
        # 'dynamodb' is the aws service being used
        dynamodb = boto3.resource('dynamodb')

        # 'monitor' is the database table being referenced
        table = dynamodb.Table('monitoring')

         # Creates new table record and populates event information
        table.put_item(
                Item={
                    'uid': self.uid,
                    'timestamp': self.time_stamp,
                    'hostname': self.host_name,
                    'hostip': self.host_ip,
                    'usedcpupercent': self.used_cpu_per,
                    'usedmem': self.used_mem,
                    'usedmempercent': self.used_mem_per,
                }
        )




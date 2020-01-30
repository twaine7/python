# pylint: disable=no-member

import boto3


class Createevent:


    def __init__(self, prev_uid, new_uid, time_stamp, host_name, host_ip, value_type, used_mem, used_mem_per):
        self.prev_uid = prev_uid
        self.new_uid = new_uid
        self.time_stamp = time_stamp
        self.host_name = host_name
        self.host_ip = host_ip
        self.value_type = value_type
        self.used_mem = used_mem
        self.used_mem_per = used_mem_per
        
        # Sets "lastrecord" indicator flag to 1
        self.last_record = int(1)

    def createrecord(self, prev_uid):
        # Get the service resource:
        # 'dynamodb' is the aws service being used
        dynamodb = boto3.resource('dynamodb')

        # 'monitor' is the database table being referenced
        table = dynamodb.Table('monitor')

        # Creates new table record and populates event information
        table.put_item(
                Item={
                    'uid': self.new_uid,
                    'timestamp': self.time_stamp,
                    'hostname': self.host_name,
                    'hostip': self.host_ip,
                    'type': self.value_type,
                    'value': self.used_mem,
                    'percent': self.used_mem_per,
                    'lastrecord': self.last_record
                }
        )
        
        # Find previous "lastrecord" and changes flag from 1 to 0
        if prev_uid != "id0000":
            table.update_item(
                Key={
                    'uid': self.prev_uid,
                },
                UpdateExpression="SET lastrecord = :l",
                ExpressionAttributeValues={
                    ':l': 0
                }
            )
        
        print("Created Record: ", self.new_uid)  
        print("Updated Record: ", self.prev_uid)   


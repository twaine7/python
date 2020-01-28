import boto3


# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('monitor')

class newevent:

    def __init__(self,new_uid,time_stamp, host_name, host_ip, value_type, used_mem, used_mem_per):
        self.new_uid = new_uid
        self.time_stamp = time_stamp
        self.host_name = host_name
        self.host_ip = host_ip
        self.value_type = value_type
        self.used_mem = used_mem
        self.used_mem_per = used_mem_per
    
        # Creates new table record and populates event information
        table.put_item(
                Item={
                    'uid': self.new_uid,
                    'timestamp': self.time_stamp,
                    'hostname': self.host_name,
                    'hostip': self.host_ip,
                    'type': self.value_type,
                    'value': self.used_mem,
                    'percent': self.used_mem_per
                }
        )

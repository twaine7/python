
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
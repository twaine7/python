        

                
        # Sets "lastrecord" indicator flag to 1
        self.last_record = int(1)

        
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



        
def createuid(uid, current_uid, prev_uid):
    # Create unique identifer (table index)
    current_uid = "id" + str(format(uid, '04d'))
    prev_uid = "id" + str(format(uid-1,'04d'))
    # Increments UID value each iteration

    print(uid, current_uid, prev_uid)
    return


    
while not new_or_existing == 'N' and not new_or_existing == 'E':
    new_or_existing = input('New table or Existing table? (n, e) >').upper()
    
    if new_or_existing == 'E':
        load_state = (uid, i, prev_uid)
        saveloadstate.Saveload.load(load_state)
        print(uid, i, prev_uid)

    elif new_or_existing == 'N':
        i = 1

    else:
        print("Invalid Selection.")

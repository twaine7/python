import pickle

class Saveload:

    def __init__(self, uid, i, prev_uid):
        self.uid = uid
        self.i = i 
        self.prev_uid = prev_uid

    def load(self):  
        # Load variables from last script run (current_uid, uid, prev_uid)
        f = open('store.pckle', 'rb')
        self.uid, self.i, self.prev_uid = pickle.load(f)
        f.close()
        print("Loading: " + self.uid, self.i, self.prev_uid)

    def save(self):  
        # Store variables for use in subsequent script runs (uid, i, prev_uid)
        print("Saving: " + self.uid, self.i, self.prev_uid)
        f = open('store.pckle', 'wb')
        pickle.dump([self.uid, self.i, self.prev_uid],f)
        f.close()


import pickle
import time

i = 0

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

choice = ""
while choice != 'N' and choice != 'L':
    
    choice = input("Load or New? l/n").upper()
    if choice == 'N':
        print("Starting new count")
        i = 1
        print("i = ", i)
    if choice == 'L':
        print("Loading from store.pckle")
        i = load()
        print("Starting count at", i)


while True:
    print(i)
    i += 1
    save(i)
    time.sleep(1)

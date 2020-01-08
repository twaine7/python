#Imported modules
import sys
import os
import struct
import random

## variables:
# player backpack 
backpack = []
founditems = []

## determine random locations for items
xloc = []
yloc = []

##define list to create "user added" item(s)
useradded = []

# starting location
locationx = 1
locationy = 1
level = "2"

# itemsearch
takeable = "false"
found = "false"

# items in game  ### --- maybe onsolidate all items, include "Level" field ---- ###

############################################ Level 1 ############################################

## Items available during Level 1
##     Name of Item 0 / Visibility 1 / Interaction 2 / xloc 3 / yloc 4 / Taken 5 /   State 6 /    Interacts with 7 / interacts at 8 (xloc) / interacts at 9 (yloc) / Interaction Message 10 
level1items =[["Paperclip",    "visible",   "take",            "1",   "3",   "nottaken",  "unlocked", "Lockbox",     "7", "9",  "Using the paperclip, you pick the lock on the lockbox.  Inside the lockbox, you find a key."],
              ["Screwdriver",  "visible",   "take",            "5",   "7",   "nottaken",  "unlocked", "Cabinet",     "7", "9",  "Using the screwdriver, you pry open the cabinet door.  Within the cabinet, you find a small lockbox."],
              ["Cabinet",      "visible",   "interact",        "7",   "9",   "nottaken",  "locked",   "Screwdriver", "0", "0",  "You try to open the cabinet, but it is locked."],
              ["Lockbox",      "hidden",    "interact",        "7",   "9",   "nottaken",  "locked",   "Paperclip",   "0", "0",  "You try to open the lockbox, but it is locked (shocker)."],
              ["Key",          "hidden",    "take",            "7",   "9",   "nottaken",  "unlocked", "Door",        "9", "10", "You insert the key into the door lock.  Turning the key, you hear a click as the door is unlocked."],
              ["Door",         "visible",   "interact",        "9",   "10",  "nottaken",  "locked",   "Key",         "0", "0",  "You attempt to turn the doorknob. Unfortunately, the door is locked."],
              ["Map",          "visible",   "take",            "1",   "2",   "nottaken",  "unlocked", "nothing",     "0", "0",  ""]]
#################################################################################################

############################################ Level 2 ############################################

for c in range(0,2):

    for i in range(1,10):
        n = random.randint(1,10)
        xloc.append(n)

    for i in range(1,10):
        n = random.randint(1,10)
        yloc.append(n) 


## Items available during Level 2
##     Name of Item 0 / Visibility 1 / Interaction 2 / xloc 3 / yloc 4 / Taken 5 /   State 6 /    Interacts with 7 / interacts at 8 (xloc) / interacts at 9 (yloc) / Interaction Message 10 
level2items = [ ["Lever",               "visible",    "interact",    str(xloc[0]),  str(yloc[0]), "nottaken",   "unlocked",   "nothing",   "0", "0",  "You pull the lever, nothing appears to happen."],
                ["Hidden Door",         "hidden",     "interact",    str(xloc[1]),  "10",         "nottaken",   "locked",     "nothing",   "0", "0",  "You have found a door, hidden the panels of the north wall."],  ##Need to "interact" with "wall" (neither prompted).  Once unhidden, can move "F" through wall.  Next position is somewhere else in room.
                ["Hidden Passageway",   "hidden",     "interact",    "8",           str(yloc[1]), "nottaken",   "locked",     "nothing",   "0", "0",  "You cannot go back this way."]]
               # [useradded[0],          useradded[1], useradded[2],  useradded[3],  useradded[4], useradded[5], useradded[6], useradded[7], useradded[8], useradded[9], useradded[10] ] ]

#################################################################################################


# functions:
# main menu for player to control game
def mainmenu(level1items, locationx, locationy, level, founditems, backpack, found):
    print("Main Menu")
    while True:
        print("Please select option:")
        
        option = input("(S)earch, (L)ocation, (M)ove, (I)nventory, (Q)uit:")
        option = option.upper()
        
        if option == 'S':
            search(level1items, level2items, locationx, locationy, level, founditems, backpack, found)
        elif option == 'L':
            location(locationx, locationy, level)
        elif option == 'M':
            move(locationx, locationy, level)
        elif option == 'I':
            inventory(backpack, locationx, locationy, level)
        elif option == 'Q':
            quitgame()
        elif option == 'LEVEL':
            #level2(locationx, locationy, level)
            level = input("Enter Level to Warp: ")
        elif option == "COORDS":
            locationx = input("X:")
            locationy = input("Y:")
        elif option == 'PRINTITEMS':
            if level == "1":
                for t in level1items:
                    print(t)
            if level == "2":
                for t in level2items:
                    print(t)


#action menu
def action(level1items, level2items, locationx, locationy, level, founditems, backpack, found):
    while True:
        option = input("Action? (I)nteract, (T)ake, (M)ove, (S)earch, i(N)ventory, (E)xit to main:")
        option = option.upper()
        
        if option == 'I':
            interact(level1items, level2items, locationx, locationy, level, founditems, backpack, found)
        elif option == 'T':
            take(level1items, locationx, locationy, founditems, backpack, takeable, found)
        elif option == 'M':
            move(locationx, locationy, level)
        elif option == 'S':
            search(level1items, level2items, locationx, locationy, level, founditems, backpack, found)
        elif option == 'E':
            mainmenu(level1items, locationx, locationy, level, founditems, backpack, found)
        elif option == 'N':
            inventory(backpack, locationx, locationy, level)
        elif option == 'PRINTITEMS':
            if level == "1":
                for t in level1items:
                    print(t)
            if level == "2":
                for t in level2items:
                    print(t)


# open inventory / backpack
def inventory(backpack, locationx, locationy, level):
    if backpack == []:
        print("Backpack is empty!")
    elif not backpack == []:
        print("Backpack Contents:", backpack)
    
    print("Please select option:")

    option = input("(U)se item, (S)earch, (L)ocation, (M)ove, (E)xit to main:")
    option = option.upper()
    
    if option == 'U':
        useitem(level1items, locationx, locationy, backpack)
    elif option == 'S':
        search(level1items, level2items, locationx, locationy, level, founditems, backpack, found)
    elif option == 'L':
        location(locationx, locationy, level)
    elif option == 'M':
        move(locationx, locationy, level)
    elif option == 'E':
        mainmenu(level1items, locationx, locationy, level, founditems, backpack, found)
    elif option == 'PRINTITEMS':
        if level == "1":
            for t in level1items:
                print(t)
        if level == "2":
            for t in level2items:
                print(t)

# investigate current location
def search(level1items, level2items, locationx, locationy, level, founditems, backpack, found):
    print("Search")
    if not level == "1":
        print("Level:", level)
    founditems = []
    x = str(locationx)
    y = str(locationy)
    i = 0
    found = 0

    print("You see: ")
   
    #search itemlist to see if items exist at coordinates and adds to founditems[]
    ## Level 1 ##
    if level == "1":
        i = 0
        for n in level1items:
            if level1items[i][3] == x and level1items[i][4] == y:
                if level1items[i][1] == 'visible' and level1items[i][5] == 'nottaken':
                    print(level1items[i][0])
                    if not level1items[i][0] in founditems:
                        founditems.append(level1items[i][0])
                    found += 1
            i += 1
    
    ## Level 2 ##
    if level == "2":
        i = 0
        for n in level2items:
            if level2items[i][3] == x and level2items[i][4] == y:
                if level2items[i][1] == 'visible' and level2items[i][5] == 'nottaken':
                    print(level2items[i][0])
                    if not level2items[i][0] in founditems:
                        founditems.append(level2items[i][0])
                    found += 1
            i += 1

    ## Nothing Found ##
    if found == 0:
        print("Nothing")
    action(level1items, level2items, locationx, locationy, level, founditems, backpack, found)

#take found takeable items and add to backpack
def take(level1items, locationx, locationy, founditems, backpack, takeable, found):
    i = 0
    takeitem = ""
    found = "false"
    
    for n in founditems:
        print(founditems[i])
        i += 1
    takeitem = input("Items to take: ")
    #checks if item is in location
    checktakeable(level1items, locationx, locationy, founditems, backpack, takeable, takeitem, found)

#check if item is take-able  ### need to add level 2 ###
def checktakeable(level1items, locationx, locationy, founditems, backpack, takeable, takeitem, found):
    i = 0
    x = locationx
    y = locationy
    takeable = "false"
    found = "false"
    if takeitem in founditems:
            found = "true"
    elif not takeitem in founditems:
        print(takeitem, "not a valid choice!")

    for n in level1items:
        if level1items[i][0] == takeitem and level1items[i][2] == "take": # and items[i][3] == x and items[i][4] == y:
            takeable = "true"
            found = "true"
            checkbackpack(level1items, locationx, locationy, founditems, backpack, takeable, takeitem, found)
        i += 1
    if not takeable == "true":
        print(takeitem, "cannot be taken.")
    
    action(level1items, level2items, locationx, locationy, level, founditems, backpack, found)
    
#check whether item is already in backpack and adds if able
def checkbackpack(level1items, locationx, locationy, founditems, backpack, takeable, takeitem, found):
    if takeitem in founditems and takeable == "true":
        if not takeitem in backpack:
            print(takeitem, "added to backpack.")
            backpack.append(takeitem)
            j = 0
            for n in level1items:
                if level1items[j][0] == takeitem:
                    level1items[j][1] = "hidden"
                    level1items[j][5] = "taken"
                    inventory(backpack, locationx, locationy, level)
                j += 1
        elif takeitem in backpack:
            print(takeitem, "is already in your backpack!")
    
    action(level1items, level2items, locationx, locationy, level, founditems, backpack, found)

#use item in inventory (change "locked" to "unlocked")
def useitem(level1items, locationx, locationy, backpack):
    x = str(locationx)
    y = str(locationy)
    i = 0
    
    print("Use Item")   
    itemtouse = input("Which item do you wish to use? ")

    #check if item is in backpack
    if itemtouse in backpack:
        for n in level1items:
            #check if item is usable at this location
            if level1items[i][0] == itemtouse:# and items[i][8] == x and items[i][9] == y:
                print(level1items[i][10])
            #check if game complete condition (key used at door location)
                if itemtouse == "Key":# and items[i][8] == x and items[i][9] == y:
                        print("You turn the knob, slowly opening the door.")
                        gamecompleted()
                if itemtouse == "Screwdriver":
                    level1items[3][1] = "visible" 
                elif itemtouse == "Paperclip":
                    level1items[4][1] = "visible"
            i += 1
    elif not itemtouse in backpack:
        print("Item not in backpack.")
    
    action(level1items, level2items, locationx, locationy, level, founditems, backpack, found)

#interact with found items that cannot be 'taken'
def interact(level1items, level2items, locationx, locationy, level, founditems, backpack, found):
    interactwith = ""
    i = 0
    x = str(locationx)
    y = str(locationy)
    print("Level:", level)
    interactwith = input("Interact with: ")
    
    ### Level 1 ###
    if level == "1":
        #check if item is interactable  
        for n in level1items:
            if level1items[i][0] == interactwith and level1items[i][1] == "visible" and level1items[i][2] == "interact" and level1items[i][6] == "locked":
                print(level1items[i][10])
            elif level1items[i][0] == interactwith and level1items[i][1] == "hidden":
                print("Item not found at this location.")
            i += 1
    
    ### Level 2 ###
    if level == "2":
        #interact with hidden door
        if interactwith == "Hidden Door":
            for n in level2items:
                if level2items[i][0] == interactwith and x == level2items[i][3] and y == level2items[i][4]:
                    print("You have found the Hidden Door!")
                    j = 0
                    print(level2items[i],[10])
                    for n in level2items:
                        ## Move player to new coordinates ("Hidden Passageway" is other side of "Hidden Door")
                        if level2items[j][0] == "Hidden Passageway":
                            locationx = int(level2items[j][3])
                            locationy = int(level2items[j][4])
                i +=  1

        #check if item is visible, interactible and locked (return message if "yes")
        if not interactwith == "Hidden Door":
            for n in level2items:
                if level2items[i][0] == interactwith and level2items[i][1] == "visible" and level2items[i][2] == "interact" and x == level2items[i][3] and y == level2items[i][4] and level1items[i][6] == "locked":
                    print(level2items[i][10])
                    break
                elif level2items[i][0] == interactwith and level2items[i][1] == "hidden":
                    print("Item not found at this location.")
                    break
                elif level2items[i][0] == interactwith and level2items[i][1] == "visible" and level2items[i][2] == "interact" and x == level2items[i][3] and y == level2items[i][4] and level1items[i][6] == "unlocked":
                    if interactwith == "Lever":
                        print("You hear the sound of something scraping.")
                        j = 0
                        #interacting with "Lever" changes the "locked" variable of the "Hidden Door" (Unlocked becomes locked, vice versa)
                        for m in level2items:
                            if level2items[j][0] == "Hidden Door" and level2items[j][6] == "locked":
                                level2items[j][6] = "unlocked"
                                break
                            elif level2items[j][0] == "Hidden Door" and level2items[j][6] == "unlocked":
                                level2items[j][6] = "locked"
                            j += 1
                i += 1    

    action(level1items, level2items, locationx, locationy, level, founditems, backpack, found)        


# check current map coordinates
def location(locationx, locationy, level):

    print("Player Location: ", locationx, locationy)

    if not level == "1":
        print("Level: ", level)

    if "Map" in backpack:    
        for y in range(1,11):
            for x in range(1,11):
                if x == locationx and y == locationy:
                    print("O", end = " ")
                else:
                    print("#", end = " ")
            print(" ")

# move player through map by changing x, y location
def move(locationx, locationy, level):
    while True:
        print("Player Location: ", locationx, locationy)
        option = input("Move? (S)earch, (F)orward, (B)ackward, (L)eft, (R)ight), (E)xit to main:")
        option = option.upper()

        ## if player breaks location coordinates by entering null, they are trapped.  
        acceptible = [1,2,3,4,5,6,7,8,9,10]
        if not locationx in acceptible or not locationy in acceptible:
            trapped(locationx, locationy, level)

        ## player movement, changes coords based on input and assigns outer limits
        if option == 'F' and locationy >= 1 and locationy <= 10:
            if locationy == 10:
                print("Limit Reached, Not Moving")
            if not locationy == 10:
                print("Moving Forward")
                locationy = locationy + 1
        elif option == 'B' and locationy >= 1 and locationy <= 10:
            if locationy == 1:
                print("Limit Reached, Not Moving")
            if not locationy == 1:
                print("Moving Backward")
                locationy = locationy - 1
        elif option == 'R' and locationx >= 1 and locationx <= 10:
            if locationx == 10:
                print("Limit Reached, Not Moving")
            if not locationx == 10:
                print("Moving Rightward")
                locationx = locationx + 1
        elif option == 'L' and locationx >= 1 and locationx <= 10:
            if locationx == 1:
                print("Limit Reached, Not Moving")
            if not locationx == 1:
                print("Moving Leftward")
                locationx = locationx - 1
        elif option == 'S':
            search(level1items, level2items, locationx, locationy, level, founditems, backpack, found)
        elif option == 'E':
            mainmenu(level1items, locationx, locationy, level, founditems, backpack, found)
        elif option == 'PRINTITEMS':
            if level == "1":
                for t in level1items:
                    print(t)
            if level == "2":
                for t in level1items:
                    print(t)

#saves progress
def saveprogress():
    print("Save")

#loads progress
def loadprogress():
    print("Load")

#game completed
def gamecompleted():
    print("You have escaped! Congratulations!")
    print("Please choose:")
    choice = input("(E)xit, (P)lay again")
    choice = choice.upper()   
    
    if not choice == 'Leave':
        print("You didn't think it would be that easy, did you?")
        level2(locationx, locationy, level)
    elif choice == 'Leave':
        print("Good bye... For now.")
        os._exit(0)

#trap countdown
def trapped(locationx, locationy, level):
    escape = ""
    hp = 15
    print("You are trapped!")
    while not escape == "escape" and hp > 0:
        escape = input("")
        if escape == "escape":
            locationx = 5
            locationy = 5
            print("You have escaped the trap.")
            move(locationx, locationy, level)
        else:
            hp -= 1

        if hp == 14:
            print("Trapped!")
        elif hp == 13:
            print("You did this...")
        elif hp == 12:
            print("Prove yourself worthy.")    
        elif hp == 11:
            print("Escape is unlickely")
        elif hp == 9:
            print("Erm")
        elif hp == 8:
            print("Shucks.")
        elif hp == 7:
            print("Crying won't help.")    
        elif hp == 6:
            print("All over soon.")
        elif hp == 5:
            print("Pretty sure this is it.")
        elif hp == 4:
            print("End is nigh.")
        elif hp == 0:
            print("You failed to escape the trap.  You are dead.")
            diedinatrap(locationx, locationy, level)


#died in a trap
def diedinatrap(locationx, locationy, level):
    print("You died in a trap that you caused because you cheated.")
    respawn = input("I bet you would like to respawn...")
    respawn = respawn.upper()
    if respawn == "RESPAWN":
        locationx = 7
        locationy = 7
        level = 1
        move(locationx, locationy, level)


#exit game
def quitgame():
    quitconfirm = 'N'
    quitconfirm = input("Exit? Are you sure? (Y / N)")
    quitconfirm = quitconfirm.upper()
   
    if quitconfirm == 'N':
        mainmenu(level1items, locationx, locationy, level, founditems, backpack, found)
    elif quitconfirm == 'Y':
        print("Exiting...")
        os._exit(0)

def level2(locationx, locationy, level):
    level = "2"
    while True:
        print("You have entered Level", level)
        print("Player Location: ", locationx, locationy)
        
        option = input("(F)orward, (B)ackward, (L)eft, (R)ight)")
        option = option.upper()
        
        if option == 'F' and locationy >= 1 and locationy <= 10:
            if locationy == 10:
                print("Limit Reached, Not Moving")
            if not locationy == 10:
                print("Moving Forward")
                locationy = locationy + 1
        elif option == 'B' and locationy >= 1 and locationy <= 10:
            if locationy == 1:
                print("Limit Reached, Not Moving")
            if not locationy == 1:
                print("Moving Backward")
                locationy = locationy - 1
        elif option == 'R' and locationx >= 1 and locationx <= 10:
            if locationx == 10:
                print("Limit Reached, Not Moving")
            if not locationx == 10:
                print("Moving Rightward")
                locationx = locationx + 1
        elif option == 'L' and locationx >= 1 and locationx <= 10:
            if locationx == 1:
                print("Limit Reached, Not Moving")
            if not locationx == 1:
                print("Moving Leftward")
                locationx = locationx - 1
        elif option == 'Q':
            quitgame()

def hiddenpassage(level2items, locationx, locationy, level):
    print("You have found a Hidden Passage")
    
    for i in level2items:
        if level2items[i][0] == "Hidden Passageway":
            locationx = level2items[i][3]
            locationy = level2items[i][4]
        i += 1
    print("Location:", locationx, locationy)



mainmenu(level1items, locationx, locationy, level, founditems, backpack, found)



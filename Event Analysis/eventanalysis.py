
import pandas as pd
import sqlite3



conn = sqlite3.connect('D:\\Documents\\Python\\Repository\\Databases\\event.db')
c = conn.cursor()

action = ""


# displays menu
def menuselector():
    selection = ""
    while not selection == "5":

        print("1 - Recreate Table")
        print("2 - Import CSV")
        print("3 - Print Table Contents")
        print("4 - Analyze Event Data")
        print("5 - Exit Program")

        selection = input("Make Selection: ")
        if selection == "1":
            createtable()
        elif selection == "2":
            importcsv()
        elif selection == "3":
            printtable()
        elif selection == "4":
            eventanalyzer()
        elif selection == "5":
            break
        else:
            print("Invalid Selection...")


# create event table if not exists
def createtable():
    print("Dropping Table")
    c.execute("""DROP TABLE IF EXISTS events""")
    print("Creating Table")
    c.execute("""CREATE TABLE events (
                col_1 text,
                col_2 integer,
                col_3 text,
                col_4 text,
                col_5 int,
                col_6 text)""")
    print("Table Created")


# import data from CSV file into event table
def importcsv():
    print("Reading data from CSV")

    ## event data (can be added as a user input)
    data = pd.read_csv (r'D:\Documents\\Python\\Repository\\Excel Test Data\\eventdata.csv')
    while True:
        print("(R)eplace or (A)ppend?")
        selection = input(">").upper()
        if selection == 'R':
            action = 'replace'
            print("Replacing")
            break
        elif selection == 'A':
            action = 'append'
            print("Adding to")
            break
        else:
            print("Invalid Selection... Try again")

    # depending on input, either replaces or appends to db table
    print("db Table")
    data.to_sql('events', conn, if_exists=action, index = True)
    print("Data added to table, fetching...")


# returns contents of event db table "events" to terminal
def printtable():
    print(pd.read_sql('SELECT SERVERSERIAL, EVENTCODE, LASTOCCURRENCE, NODE, SEVERITY, SERIAL from events', conn))


# runs analysis
#class Correlation:5

    # creates "correlation parent" object for each serverserial (each event becomes an object)
  #  def __init__(self)
  #      self.parent = event5
      

def eventanalyzer():
    print("Event Analyzer - Under Development")
    print(pd.read_sql('SELECT EVENTCODE, NODE, count(SERVERSERIAL) as "EVT" from events where LASTOCCURRENCE < 1520337629 + 1800 GROUP BY EVENTCODE, NODE ', conn))


print("Welcome to Event Analyzer v0.1")

menuselector()

conn.commit()
conn.close()

print("Exiting...")

#print("Complete")
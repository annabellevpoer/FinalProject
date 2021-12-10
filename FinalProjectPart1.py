# Name: Annabelle Poer
# ID: 1798854


#  item ID, manufacturer name, item type, price, service date, and list if it is damaged 
#  - sorted alphabetically by manufacturer

#  item ID, manufacturer name, price, service date, and list if it is damaged
#  - sorted by their item ID

#  item ID, manufacturer name, item type, price, service date, and list if it is damaged.
#  - order of service date from oldest to most recent

#  item ID, manufacturer name, item type, price, and service date.
#  - most expensive to least expensive

from datetime import date
from datetime import datetime





# puts every line from csv file into a list  
with open("ManufacturerList.csv") as f:
    manufacturer_list = f.read().splitlines() 

with open("PriceList.csv") as f:
    price_list = f.read().splitlines() 

with open("ServiceDatesList.csv") as f:
    dates_list = f.read().splitlines() 


id_dict = {}
all_items = []

# this loop splits each line of the file into a another list
# it then creates a dictionary (id_dict):
# the key of the dictionary is the itemID
# the value is an array including manufacturer name, item type, the damaged indicator
for x in manufacturer_list:
    file_line = x.split(',')
    itemID = file_line[0]
    file_line.pop(0)
    id_dict[itemID]= file_line
    
    
# appends price to array value of the map
for x in price_list:
    file_line = x.split(',')
    id_dict[file_line[0]].append(file_line[1])

# appends date to array value of the map
for x in dates_list:
    file_line = x.split(',')
    id_dict[file_line[0]].append(file_line[1])


#  now we have a map that holds all the fields from every input csv file given
# the keys are the itemID string
# the values are an array containing: manufacturer name, item type, the damaged indicator, price, date


# this loop creates an array (all_items) from the map we created
# the first element of the array is set as the map key itemID
# then we can append the value of the map, which is an array, to the end
#  so all_items contains (in this order) item ID, manufacturer name, item type, price, service date, damaged indicator.
#       for every itemID listed in all the csv files 
for x in id_dict:
    arr = id_dict[x]
    # print("arr: ", arr)
    arr.insert(0, x)
    arr.insert(5, arr.pop(3))
    all_items.append(arr)


def outputOne():
    # --------- (1) SORTS BY MANUFACTUREER ------------ #
    # item ID, manufacturer name, item type, price, service date,  damaged.
    list_one = (sorted(all_items, key=lambda x:x[1])) #  sorts the list by manufacturer

    f = open("FullInventory.csv", "w") # opens the csv file to write to it 
    for line in list_one: # writes each element of the list the file
        f.write(",".join(line))
        f.write("\n")

    f.close()
    # --------- (1) SORTS BY MANUFACTUREER ------------ #

def outputTwo():
    # ------------- (2) SORTS BY ID ---------------- #
    # newlist = all_items.copy()
    list_two = sorted(all_items, key=lambda x:x[0]) #  sorts the list by item id


    # what it looks like
    # item ID, manufacturer name, item type, the damaged indicator, price, date
    # item ID, manufacturer name, price,  date, the damaged indicator

    # print("\n--------- THE LIST ---------")
    # print(list_two)

    for line in list_two:
        filename = line[2] +".csv"
        f = open(filename, "w") # we want to make sure that each file is empty before we begin writing to it

    f.close()

    for line in (list_two):
        filename = line[2] +".csv"
        itemtype = line[2]
        (line).pop(2)  # remove the item type from the sorted array 
        # damagedindc = line[2] # the damaged indicator
        # (line).pop(2)  # remove the damaged indicator from the sorted array 
        # line.append(damagedindc) # add damagaed indicator to end of array
        # list_two.pop(2)
        # print("\n----------- LINE ------------")
        # print((line))
        f = open(filename, "a") # opens the file in append mode
        f.write(",".join(line))
        f.write("\n")
        line.insert(2, itemtype)

    f.close()

    # print("\n--------- THE LIST TWO ---------")
    # print(list_two)
    # ------------- (2) SORTS BY ID ---------------- #

def outputThree():
    # -------------- (3) SORTS BY ORDER SERVICE DATE, OLDEST -> RECENT---------------- #
    # print("\n--------- THE LIST all_items---------")
    # print(all_items)

    list_three = sorted((all_items), key=lambda x:datetime.strptime(x[4], "%m/%d/%Y")) #  sorts the list by date
    f = open("PastServiceDateInventory.csv", "w")

    today = date.today()
    for line in list_three:
        date_obj = datetime.strptime(line[4], "%m/%d/%Y").date()
        if(date_obj>today): # only write to file if date is past today (the day you execute this program) 
            f.write(",".join(line))
            f.write("\n")

    f.close()
    # -------------- #3 SORTS BY ORDER SERVICE DATE, OLDEST -> RECENT---------------- #

def outputFour():
    # -------------- (4) SORTS BY PRICE ---------------- #
    list_four = sorted(all_items, key=lambda x:x[4]) #  sorts the list by price

    f = open("DamagedInventory.csv", "w")
    for line in list_four:
        if(line[5] == 'damaged'):
            list(line).pop(5) # remove the damaged indicator from the array 
            f.write(",".join(line))
            f.write("\n")

    f.close()
    # -------------- (4) SORTS BY PRICE ---------------- #


outputOne()
outputTwo()
outputThree()
outputFour()
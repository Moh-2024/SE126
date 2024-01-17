import csv
totalrecords = 0
with open("week2/hw/lab2b.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #variables of each field
        if rec[0] == "D":
            compType = "Desktop"
        elif rec[0] == "L":
            compType = "Laptop"
        else:
            compType = "Error"
    # storing value for var representing field 2 (rec[1])
        if rec[1] == "DL":
            brand = "Dell"
        elif rec[1] == "GW":
            brand = "gateway"
        elif rec[1] == "HP":
            brand = rec[1]
        else:
            brand = "Error"

        processor = rec[2]
        ram = rec[3]
        firstDisk = rec[4]
        #if len(rec) == 2:

        numOfHdd = rec[5]
        #else:
            #numOfHdd = (" ")
        if len(rec) == 9:
            secondDisk = rec[6]
        else:
            secondDisk = "  "
        if len(rec) == 9:
            operatingSystem = rec[7]
        else:
            operatingSystem = rec[6]
        if len(rec) == 9:
            year = rec[8]
        else:
            year = rec[7]

        #final printed message for each machine
        print(f"{compType:10} {brand:10} {processor:10}{ram:10}{firstDisk:10} {numOfHdd:10}{secondDisk:10}{operatingSystem:10}{year:10}")
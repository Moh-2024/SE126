#w3d1 demo text file handling & storing to ID lists

import csv
#total counter for all records
totalRecords = 0

ListCompType = []
ListBrand = []
ListProcessor = []
ListRam = []
ListFirstDisk = []
ListNumOfHdd = []
ListSecondDisk = []
ListOperatingSystem = []
ListCompType = []
ListYear = []

#opening csv file
with open("week2/hw/lab2b.csv") as csvfile:
    #reading the file
    file = csv.reader(csvfile)
  #for loop to go through each row in the file
    for rec in file:
#checking what type of computer is it
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
        #adding records for the file to the varibales
        processor = rec[2]
        ram = rec[3]
        firstDisk = rec[4]
        numOfHdd = rec[5]
      #checking if the length of the list is 9
        if len(rec) == 9:
            secondDisk = rec[6]
            operatingSystem = rec[7]      
            year = rec[8]          
        else:
          #if the length is not 9 then the second disk is not present
            secondDisk = ""
            operatingSystem = rec[6]
            year = rec[7]

        totalRecords += 1
        ListCompType.append(compType)
        ListBrand.append(brand)
        ListProcessor.append(processor)
        ListRam.append(ram)
        ListFirstDisk.append(firstDisk)
        ListNumOfHdd.append(numOfHdd)
        ListSecondDisk.append(secondDisk)
        ListOperatingSystem.append(operatingSystem)
        ListYear.append(year)
#----- DISCONNECTED FROM FILE--------------------------------------

for i in range(0,totalRecords):
       print(f"{ListCompType[i]:10} {ListBrand[i]:10} {ListProcessor[i]:10}{ListRam[i]:10}{ListFirstDisk[i]:10}{ListNumOfHdd[i]:10}{ListSecondDisk[i]:20}{ListOperatingSystem[i]:25}{ListYear[i]:25}") 

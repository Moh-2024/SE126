#Mohammed Malek
#SE126
#Lab 2B
#You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output. The last line should print the number of computers in the file. Organization of the csv file:


#importing csv to read file
import csv

#initiliazing total records variable to 0
totalrecords = 0
#opening csv file
with open("week2/hw/lab2b.csv") as csvfile:
    #reading the file
    file = csv.reader(csvfile)
  #priting the header
    print("Type\t  Brand\t    CPU\t\tRAM\t  1st Disk No HDD   2nd Disk      OS       YR")
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

        #final printed message for each machine
        print(f"{compType:10} {brand:10} {processor:10}{ram:10}{firstDisk:10} {numOfHdd:10}{secondDisk:10}{operatingSystem:10}{year:10}")
        totalrecords += 1
#displaying the total number of records
print(f"\nTotal Records: {totalrecords}")
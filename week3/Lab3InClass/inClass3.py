#Mohammed Malek
#SE126
#Lab 3 Inclass
#Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops


#importing csv to read file
import csv

#initiliazing variables
totalRecords = 0
totalDesktopCost = 0
totalDesktops = 0
totalLaptopCost = 0
totalLaptops = 0

# making empty lists
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

print(f"{'compType':10} {'brand':10} {'processor':10}{'ram':10}{'firstDisk':10}{'numOfHdd':10}{'secondDisk':20}{'operatingSystem':25}{'year':25}")
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
        # adding the data to their specefic lists
        ListCompType.append(compType)
        ListBrand.append(brand)
        ListProcessor.append(processor)
        ListRam.append(ram)
        ListFirstDisk.append(firstDisk)
        ListNumOfHdd.append(numOfHdd)
        ListSecondDisk.append(secondDisk)
        ListOperatingSystem.append(operatingSystem)
        ListYear.append(year)
        
# for loop to display lists of computers
for i in range(0,totalRecords):
       print(f"{ListCompType[i]:10} {ListBrand[i]:10} {ListProcessor[i]:10}{ListRam[i]:10}{ListFirstDisk[i]:10}{ListNumOfHdd[i]:10}{ListSecondDisk[i]:20}{ListOperatingSystem[i]:25}{ListYear[i]:25}")            

#for loop to calculate total desktop and laptop costs
for i in range(0, totalRecords):
    #checking if the year is less than 16
    if(ListYear[i]<= '16'):
        #checking if computer type is either desktop and laptop
        if(ListCompType[i] == 'Desktop'):
            totalDesktopCost += 2000# adding total desktop cost
            totalDesktops += 1
        elif(ListCompType[i] == 'Laptop'):
            totalLaptopCost += 1500# adding total laptop cost
            totalLaptops += 1
#Calculating total cost
total = totalDesktopCost + totalLaptopCost

#Displaying results
print(f"\nTo replace {totalDesktops} it will cost  ${totalDesktopCost:6}")
print(f"To replace {totalLaptops} it will cost  ${totalLaptopCost:6}")
print(f"Your total Cost is:        ${total:6}")
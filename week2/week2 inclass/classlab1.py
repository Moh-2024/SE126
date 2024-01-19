#Mohammed Malek
#SE126
#LAB 2A Inclass
#The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event. Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit
#----------------------------------------------------------------------------------------------

#importing csv to read file
import csv

#declaring lists variables
names = []
maxOccupancy = []
numOfPeople = []
#total records counter
totalRecords = 0
# rooms that are over the max occupancy
overLimit = 0
#opening the file
with open("week2/week2 inclass/lab2a.csv") as csvfile:
  reader = csv.reader(csvfile)
  # for loop to read the file
  for row in reader:
    #adding the values to the lists
    names.append(row[0])
    maxOccupancy.append(int(row[1]))
    numOfPeople.append(int(row[2]))
    totalRecords += 1

#Displaying the results to the user
print("Room \t\t\t\t Max\t    Min\t\tOver")

#for loop to check which rooms are over the limit and displaying the results
for rec in range(0, totalRecords):
  if(numOfPeople[rec] > maxOccupancy[rec]):
    over = numOfPeople[rec] - maxOccupancy[rec]
    print(f"{names[rec]:20} {maxOccupancy[rec]:15} {numOfPeople[rec]:10} {over:10}")
    overLimit += 1
# displaying how many total records were processed
print("\nProcesed", totalRecords, "records")
# displaying how many rooms were over the limit
print("There are", overLimit, "rooms are over the limit")
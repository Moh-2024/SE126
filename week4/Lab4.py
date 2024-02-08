#Mohammmed Malek  
#SE126
#Lab 4 
# process the text file “lab4A_GOT_NEW.txt” to store each field into its own corresponding list
#Variable Dictionay: 
#  Lists - firstNames,lastNames, ages, nickNames, houseAllegiance ,mottosList
# Counter variables - starkTally, lannisterTally, targaryenTally, baratheonTally, watchTally, tullyTally
#----------------------------------------------------  


import csv

#creating empty lists
firstNames = []
lastNames = []
ages = []
nickNames = []
houseAllegiance = []
mottosList = []

#counter variables
starkTally = 0
lannisterTally = 0
targaryenTally = 0
baratheonTally = 0
watchTally = 0
tullyTally = 0

with open("week4/lab4A_GOT_NEW.txt") as csvfile:
  file = csv.reader(csvfile)

  for row in file:
    #adding data to lists
    firstNames.append(row[0])
    lastNames.append(row[1])
    ages.append(int(row[2]))
    nickNames.append(row[3])
    houseAllegiance.append(row[4])

#Displaying the Lists
print(f"\n\n{'First Name':20}\t {'Last Name':12}\t {'Age':4}\t {'Nick Name':15}\t {'House Allegiance':20}")
print("-------------------------------------------------------------------------------------------------------------------")
for i in range(0, len(firstNames)):
  print(f"{firstNames[i]:20}\t {lastNames[i]:12}\t {ages[i]:4}\t {nickNames[i]:15}\t {houseAllegiance[i]:20}")

# reprocessing the lists and assigning mottos to the given house Allegiance
for i in range(0, len(firstNames)):
  mottos = " "
  if houseAllegiance[i] == "House Stark":
    starkTally += 1
    mottos = "Winter is coming"
  elif houseAllegiance[i] == "House Baratheon":
    baratheonTally += 1
    mottos = "Ours is the Fury"
  elif houseAllegiance[i] == "House Tully":
    tullyTally += 1
    mottos = "Family.Duty.Honor"
  elif houseAllegiance[i] == "Night's Watch":
    watchTally += 1
    mottos = "And now my watch begins"
  elif houseAllegiance[i] == "House Lannister":
    lannisterTally += 1
    mottos = "Hear me roar!"
  elif houseAllegiance[i] == "House Targaryen":
    targaryenTally += 1
    mottos = "Fire & Blood"
  else:
    mottos = "ERROR!!!"
  #adding to mottos list
  mottosList.append(mottos)

#displalying the results
print(f"\n\n{'First Name':20}\t {'Last Name':12}\t {'Age':4}\t {'Nick Name':15}\t {'House Allegiance':20}\t {'Mottos':8}")
print("-------------------------------------------------------------------------------------------------------------------")
for i in range(0, len(firstNames)):
  print(f"{firstNames[i]:20}\t {lastNames[i]:12}\t {ages[i]:4}\t {nickNames[i]:15}\t {houseAllegiance[i]:20}\t {mottosList[i]:12}")

#reprocessing the list to find the total number of people and average age
totalNum = 0
totalAges = 0
avgAge = 0
for i in range(0, len(firstNames)):
  totalNum += 1
  totalAges += ages[i]
  avgAge = totalAges / totalNum
#Displaying the results
print(f"\n\n{'First Name':20}\t {'Last Name':12}\t {'Age':4}\t {'Nick Name':15}\t {'House Allegiance':20}\t {'Mottos':8}")
print("-------------------------------------------------------------------------------------------------------------------")
for i in range(0, len(firstNames)):
  print(f"{firstNames[i]:20}\t {lastNames[i]:12}\t {ages[i]:4}\t {nickNames[i]:15}\t {houseAllegiance[i]:20}\t {mottosList[i]:12}")
print(f"\n\nThe total number of people: {totalNum} with average age of {avgAge:.0f}")
print(f"The total number of people in House Stark: {starkTally:10}")
print(f"The total number of people in House Baratheon: {baratheonTally:6}")
print(f"The total number of people in House Tully: {tullyTally:10}")
print(f"The total number of people in House Lannister: {lannisterTally:6}")
print(f"The total number of people in House Targaryen: {targaryenTally:6}")
print(f"The total number of people in House Watch: {watchTally:10}")
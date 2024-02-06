#W5D1 - 1D List Review + function Review + sequential search

import csv

#create some empty lists
#from file

lastName = []
firstName  = []
test1 = []
test2 = []
test3 = []

#to be created
numAvg = []
letAvg = []

#---------FUNCTIONS----------------------
def funcMenu():
    print("~CLASS ACCOUNT MENU~")
    print("1. Show all students")
    print("2. Show Roster Only")
    print("3. Search for a student")
    print("4. EXIT")

    choice = int(input("Enter your choice [1-4]: "))
    #loop trap the user if they enter the wrong input
    while(choice < 0  or choice > 4):
        print("*INVALID ENTRY* DIGITS 1-4 ONLY")
        choice = int(input("Enter your choice [1-4]: "))
    return choice

def funcSecSearch(searchTerm):
    #search term is a local var name and only exists in the definition block
    #initialize foundIndex variable
    foundIndex = "" #set as empty

    #SEQUENTIAL SEARCH - "in sequence" -> start @ beginning (0) go to the end (len(listName))
    for i in range(0, len(lastName)):
        #look at each value in a list to find what you're looking for
        if lastName[i] == searchTerm:
            foundIndex = i
    return foundIndex

#---------FILE CONNECTION/LIST POPULATION----------------------
with open("week5/listPractice1-1.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        lastName.append(rec[0])
        firstName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[2]))
        test3.append(int(rec[2]))

#disconnect from file
print(f"{'LAST':12} \t{'FIRST':12} \t{'TEST 1':4}\t {'TEST 2':4}\t {'TEST 3':4}")
print("-------------------------------------------------------------------------------------")
for i in range(0,len(firstName)): 

    print(f"{lastName[i]:12} \t {firstName[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")


print(f"{'LAST':12} \t{'FIRST':12} \t{'TEST 1':4}\t {'TEST 2':4}\t {'TEST 3':4}")
print("-------------------------------------------------------------------------------------")
for i in range (0, len(firstName)):
    avg = (test1[i] + test2[i] + test3[i]) / 3
    numAvg.append(avg)

    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    elif avg < 60:
        letter = "F"
    else:
        letter = "ERROR @ I" + str(i)
    letAvg.append(letter)
#test file by printing 
print(f"{'LAST':12} \t{'FIRST':12} \t{'TEST 1':4}\t {'TEST 2':4}\t {'TEST 3':4}\t {'AVG':4}\t {'LETTER':4}")
print("-------------------------------------------------------------------------------------")
for i in range(0,len(firstName)): 

    print(f"{firstName[i]:12} \t {lastName[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]} \t{numAvg[i]:4.1f}\t {letAvg[i]:4}")

#-----------MAIN CODE---------------------------

#allow a user to choose an option from a menu and display certain data 
#user will repeatedly see the menu until they choose to exit

#show user menu, store choice into a var, use the var for the loop

menuChoice = funcMenu()

while(menuChoice != 4):
    #determine what user wants to do
    if(menuChoice == 1):
        print("\n\t--showing all file data---")
    elif(menuChoice == 2):
        print("\n\t---showing class names only---")
    elif(menuChoice == 3):
        print("\n\t-Search for a student")
        search = input("Enter the last name you are looking for: ")
        found = " "
        
        if(found != " "):
            #display results to the user
            print(f"{firstName[found]:12} \t {lastName[found]:12} \t {test1[found]} \t {test2[found]} \t {test3[found]} \t{numAvg[found]:4.1f}\t {letAvg[found]:4}")
        else: #found == "" --> it never changed --> NOT FOUND
            print(f"The student {search} cound not be found ")

        found = funcSecSearch(search)


    #give user opportunity to see menu/reselect, or exit
    #breaking out of the loop

    menuChoice = funcMenu()

print("\n\n\nThank you for using the program")

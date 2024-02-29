#Mohammed Malek
#SE126
#This application  allows a user to repeatedly choose an option from a menu to search through the data provided in the text file
#Variables Dictionary--------
#number = while loop counter
#studentID, lastName, firstName - all 1D lists
#studentClasses - 2D list
#-------------------------------------------------------------------------------------------------
import csv

def funcMenu():
  
  number = -1
  print("\n\t\t-----PLEASE CHOOSE FROM THE OPTION BELOW------")
  print("1. See all students report")
  print("2. Search for student[ID]")
  print("3. Search for student[lastName]")
  print("4. View Class roster")
  print("5. Exit/Quit")
  
  #using try and except to make sure the user enters a number
  try:  
    number = int(input("\nEnter a menu number [1-5]: "))
    #making sure the number is between 1 and 5
    if (number < 1 or number > 5):
      print("Error: Please enter a valid menu number between 1 and 5.")
    
  except ValueError:
      print("Wrong input")
      return funcMenu()

  return number

#binary search function
def funcBinarySearch(searchId, searchLastName, studentId, studentLastName):
  min = 0
  max = len(studentId) - 1

  while min <= max:
      mid = (min + max) // 2
      #if the record is found based on ID or Last Name
      if int(searchId) == int(studentId[mid]) or searchLastName == studentLastName[mid]:
          print("\nRecord Found!")
        #displaying the found record
          print(f"\nStudent ID\tLast Name\t{'First Name':<10}\t{'Class 1':<10}\t{'Class 2':<11}\tClass 3")
          print(f"{studentId[mid]: <12}{studentLastName[mid]: <12}{firstName[mid]: <12} {studentClasses[mid][0]: <12} {studentClasses[mid][1]: <12} {studentClasses[mid][2]: <12}")
        #returning the found record
          return searchId[mid], searchLastName[mid], studentId[mid], studentLastName[mid]
      elif int(searchId) < int(studentId[mid]):
          max = mid- 1
      else:
          min = mid + 1

  print("Could not find the record")
  return None
  
#calling funcMenu function
number = funcMenu()
while(number != 5):
  #empty lists
  studentID = []
  lastName = []
  firstName = []
  studentClasses = []

  with open("Lab5/lab5_students.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
      #adding the data to the lists
      studentID.append(rec[0])
      lastName.append(rec[1])
      firstName.append(rec[2])
      studentClasses.append([rec[3], rec[4], rec[5]])
  if (number == 1):
    #displaying the data 
    print("\n\nLISTS OF ALL STUDENTS:")
    print(f"Student ID\tLast Name\t{'First Name':<10}\t{'Class 1':<10}\t{'Class 2':<11}\tClass 3")
    for i in range(0, len(studentID)):
      print(f"{studentID[i]: <12}{lastName[i]: <12}{firstName[i]: <12} {studentClasses[i][0]: <12} {studentClasses[i][1]: <12} {studentClasses[i][2]: <12}")

  elif (number == 2):
    # asking user to enter ID they want to search
    answer = "y"
    while(answer == "y"):
      print("\n\nSEARCH FOR STUDENT BY ID:")
      searchId = input("Enter student ID: ")
      #calling in binary search function
      funcBinarySearch(searchId, "", studentID, lastName)

      #asking user if they want to search again
      answer = input("\nDo you want to search for another student? [y/n]: ").lower()
      while(answer != "y" and answer != "n"):
        #invalid input check
        print("Invalid Input")
        answer = input("\nPlease enter [y/n]: ").lower()
      
  elif(number == 3):
    answer = "y"
    while(answer == "y"):
      #searching student record with last name
      print("\n\nSEARCH FOR STUDENT BY LAST NAME:")
      searchLastName = input("Enter student last name: ")
      funcBinarySearch("0", searchLastName, studentID, lastName)

      answer = input("\nDo you want to search for another student? [y/n]: ").lower()
      while(answer != "y" and answer != "n"):
        print("Invalid Input")
        answer = input("\nPlease enter [y/n]: ").lower()

  elif(number == 4):
    #SEQUENTIAL SEARCH -- searching in sequencing (from beginning, through the end)

    searchClass = input("Enter the Class name you are looking for: ").upper()
    foundStudents = [] #allows for multiples in search
    seq_count = 0
    #for loop allows review of each value in list (sequence)
    for i in range(0, len(studentClasses)):
      for x in range(0, len(studentClasses[i])):
        #ask if search value matches current value in list (search)
          if studentClasses[i][x] == searchClass:
            foundStudents.append((i,x))
            seq_count += 1
          

    print(f"Student ID\tLast Name\t{'First Name':<10}\t{'Class 1':<10}\t{'Class 2':<11}\tClass 3")
    for i in range(0, len(foundStudents)):
      print(f"{studentID[foundStudents[i][0]]: <12} {lastName[foundStudents[i][0]]: <12} {firstName[foundStudents[i][0]]: <12} {studentClasses[foundStudents[i][0]][0]: <12} {studentClasses[foundStudents[i][0]][1]: <12} {studentClasses[foundStudents[i][0]][2]: <12}")
        
  number = funcMenu()
if(number == 5):
  print("Thank you for using the program!")










#--------------Extra-----------------------------
"""
  if id in studentID:
    print(f"Student ID\tLast Name\t{'First Name':<10}\t{'Class 1':<10}\t{'Class 2':<11}\tClass 3")
    print(f"{id: <12}{lastName[studentID.index(id)]: <12}{firstName[studentID.index(id)]: <12} {studentClasses[studentID.index(id)][0]: <12} {studentClasses[studentID.index(id)][1]: <12} {studentClasses[studentID.index(id)][2]: <12}")
  else:
    print("Student ID not found")
"""
#---------------------------------------------------

import csv

#create 1D lists [will be parallel to each other]
#base lists on fields in file

firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

#connnect to file & read data into 1D lists
with open ("week4/listPractice1-1.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #store data from file fields to their respective list
        #by PARALLEL - storing initial file record data at same position (index) in each list -> us e the same [INDEX] across each list to find "matching" data
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2])) # count as a int for math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnected from file------------------------------------

    print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
    print("----------------------------------------------------------------------")

#PROCESS the list --> for loop
for i in range(0,len(firstName)): 
    #len() --> return LENGTH of (item) -> for lists, it is the # of items in the list

    print(f"{firstName[i]:12} \t {lastName[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")

#calculate and store each student's AVERAGE TEST SCORE
average = 0
totalCount  = 0
average = []
grade = []

for i in range(0, len(test1)):

    #calcualte avg for student
    avg = (test1[i] + test2[i] + test3[i]) / 3 

    #append this avg to the average[]
    average.append(avg)

#displays the students first name and test average
print("\n\nWith first name and average")
print("----------------------------------------------------------------------")
print((f"{'FIRST NAME':15} \t {'AVERAGE'}"))
for i in range(0, len(firstName)):
    print(f"{firstName[i]:12} \t {average[i]:8.1f}")

for i in range(0, len(firstName)):
    if(average[i] >= 90):
      grade.append('A')
    elif(average[i] >= 80 and average[i] < 90):
      grade.append('B')
    elif(average[i] >= 70 and average[i] < 80):
      grade.append('C')
    elif(average[i] >= 60 and average[i] < 70):
      grade.append('D')
    else:
      grade.append('F')

print("\nWith Average and Grade letters")
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'} \t {'AVERAGE'} {'GRADE'}")
print("----------------------------------------------------------------------")
for i in range(0, len(firstName)):
  print(f"{firstName[i]:12} \t {lastName[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]} \t {average[i]:.1f} \t {grade[i]}")
  
allStudents = []
for i in range(0, len(firstName)):
    #add each student's data to their(index) place in the allStudents[]
      allStudents.append([firstName[i], lastName[i], test1[i], test2[i], test3[i], average[i], grade[i]])
print("\n2d lists for all students")
for i in range(0, len(allStudents)):
  print(f"{allStudents[i]}")
  
print("----------------------------------------------------------------------")
for i in range(0, len(allStudents)):
  for x in range(0, len(allStudents[i])):
    print(f"{allStudents[i][x]} ", end = " ")
  print()

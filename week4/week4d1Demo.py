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
        #by PARALLEL - storing initial file record data at same position (index) in each list --> us e the same [INDEX] across each list to find "matching" data
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

for i in range(0, len(test1)):

    #calcualte avg for student
    avg = (test1[i] + test2[i] + test3[i]) / 3 

    #append this avg to the average[]
    average.append(avg)

#displays the students first name and test average
print((f"{'FIRST NAME'} \t {'AVERAGE':}"))
for i in range(0, len(firstName)):
    print(f"{firstName[i]:12} \t {average[i]:8.1f}")

#SEQUENTIAL SEARCH - "in squence" -> from beginning THROUGH the end
lowName = ""
lowAvg = 100# start with highest value to drop to find the lowest

#determine if current average is lower than current lowAvg
for i in range(0, len(test1)):
    if(average[i] < lowAvg ):
        
        lowAvg = average[i]#current average is lower, so becomes new low value
        lowName = firstName[i]

#DISPLAY: total students in file
print(f"\nSTUDENTS IN FILE: {len(firstName)}")
print(f"LOWEST AVERAGE: {lowName} - {lowAvg}")

#----------------2D LISTS-----------------------------------
#use your 1D parallel lists to populate a new, 2D list
#HINT: the 2D list  is a list... populated with list 8D

allStudents = []
for i in range(0, len(firstName)):
    #add each student's data to their(index) place in the allStudents[]
      allStudents.append([firstName[i], lastName[i], test1[i], test2[i], test3[i], average[i]])

#display the 2D list to the console - for now, just get the lists to display ie ['floyd' , 'Eastern', ]      
for i in range(0, len(allStudents)):
    print(f"{allStudents[i]}")
#display the 2D list to the console ehere each value for wach list appears as a value(and not a list item)
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'} \t {'AVERAGE'}")
print("----------------------------------------------------------------------")
for i in range(0, len(allStudents)):
    for x in range (0, len(allStudents[i])):
        #inner for handles each value found at current list (allStudents[i])
        print(f"{allStudents[i][x]:12} ", end = "")

    #include an extra empty print() to cancel the interior print's end=""
    print()
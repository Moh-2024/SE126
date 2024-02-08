

totalUnderAge = 0
totalNotregistered =  0
notVoted = 0
totalVoted = 0
totalRecords = 0

ListID = []
ListAge = []
ListRegistration = []
ListVoted = []

import csv

with open("week3/w3-Lab3/voters_202040.csv") as csvfile:
  file = csv.reader(csvfile)

  print("Welcome to the program! ")
  for rec in file:
    
    ListID.append(rec[0])
    ListAge.append(rec[1])
    ListRegistration.append(rec[2])
    ListVoted.append(rec[3])

    totalRecords += 1
  
#checking if age is under 18
for i in range(0,totalRecords):
  if int(ListAge[i]) < 18:
      #adding 1 to under age
      totalUnderAge += 1
    
  else:  
      #initializing registeration to list of votes
      registration = ListRegistration[i]
          
      if(registration == 'Y'):
        # initializing voted to list of votes
        voted = ListVoted[i]
        
        if(voted == 'Y'):
          # adding 1 to total of votes
          totalVoted += 1
          
        else:
          #adding 1 to not voted if the user did not vote
          notVoted += 1
          
      else:
        #adding 1 to not registered if the user did not register
        totalNotregistered += 1
        
#Displaying the results
print("\nTotal number of voters under 18: ", totalUnderAge)
print("Not Registered:   ", totalNotregistered)
print("Not Voted:        ", notVoted)
print("Total Voted:      ", totalVoted)
print("Total Records:    ", totalRecords)

#goodbye message
print("\nThank you for using the program!")
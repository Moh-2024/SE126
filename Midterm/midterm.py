#Mohammed Malek
#SE126 Midterm project 
#This is a a trivia program. This program lets user choose the given category and displays 5 random question.
#It uses text files to determine the category and questions.
#variable dictionary: lists - Questions, options, answer, results
#random set of lists - selectedQ, selectedA, selectedO
#counter variable- score
#while loop- number
#-----------------------------------------------------------------------------------------------------------------


import csv
import random

def funcMenu():
  print("\nPlease select a category from the menu below:")
  print("\n\t\t 1. TECHNOLOGY")
  print("\t\t 2. SCIENCE")
  print("\t\t 3. GENERAL KNOWLEDGE")
  print("\t\t 4. EXIT")
  
  number = int(input("\nPLEASE CHOOSE OPTION BETWEEN 1 AND 4 THAN PRESS ENTER: "))

  while(number < 1 or number > 4):
    print("\n***********ERROR**********")
    print("Not a Valid Input")
    number = int(input("\nPLEASE CHOOSE OPTION BETWEEN 1 AND 4 THAN PRESS ENTER: "))

  return number
def funcImportQuestions(number):
  # if user chooses option 1
    if(number == 1):
      # opening file to read
      with open("Midterm/tech.txt") as csvfile:
        file = csv.reader(csvfile)
        return list(file)

    elif(number == 2):
      with open("Midterm/science.txt") as csvfile:
        file = csv.reader(csvfile)
        return list(file)

    elif(number == 3):
      with open("Midterm/general.txt") as csvfile:
        file = csv.reader(csvfile)
        return list(file)

    else:
      return []    

print("--------------WELCOME TO TRIVIA!--------------")
number =  funcMenu()
while(number != 4):

  #initiliazing lists of total questions, options and answers
  questions = []
  options = []
  answer = []
  results = []
  score = 0

  
#initiliazing random selected lists of questions, options and answers
  selectedQ = []
  selectedO = []
  selectedA = []
  #calling function to import questions of users category
  file = funcImportQuestions(number)

  #for loop to add questions, options and answers to lists
  for rec in file:
    questions.append(rec[0])
    options.append([rec[1], rec[2], rec[3]])
    answer.append(rec[4])
  # for loop to select random questions, options and answers  
  for i in range(len(questions)):
    selectedQ = random.sample(range(len(questions)), 5)
    selectedO = [options[i] for i in selectedQ]
    selectedA = [answer[i] for i in selectedQ]

  # for loop to display questions
  for i in range(len(selectedQ)):
    print(f"\n{i+1}. {questions[selectedQ[i]]} \n")
    #inner for loop to display options corresponding with questions
    for x in range(len(selectedO[i])):
      # adding letter option
      optionLetter = chr(ord('A') + x)
      print(optionLetter + ". " + selectedO[i][x])
    userAnswer = input("\nWhat is your answer? ").upper()
    #validating users input
    while(userAnswer != 'A' and userAnswer != 'B' and userAnswer != 'C'):
      print("*ERROR*  Please enter a valid answer")
      userAnswer = input("\nWhat is your answer? ").upper()
    #adding score
    if userAnswer.lower() == selectedA[i].lower():    
      score += 1
      results.append("Correct")
    else:
      results.append("Incorrect")

  print("\n******** RESULTS *********")
  #for loop to display results
  for i in range(0, len(selectedQ)):
    print(f"QUESTION {i+1}: {results[i]}")
  #displaying score
  print(f"\n\n--------   YOUR TOTAL SCORE IS: {score}/{len(selectedQ)}  ----------\n")
  #asking user to choose an option
  number = funcMenu()
#Goodbye message
print("\nTHANK YOU FOR USING THE PROGRAM!!")
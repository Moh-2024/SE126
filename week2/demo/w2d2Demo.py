import csv

totalRecords = 0
fNames = []
lNames = []
faveNums = []
faveAnimals = []
with open("week2/demo/w2d2Demo.txt") as csvfile:
    #we must indent when connected to & reading the file
    file = csv.reader(csvfile)
    for rec in file:

        fNames.append(rec[0])
        lNames.append(rec[1])
        faveNums.append(int(rec[2]))
        if len(rec) == 4:
            faveAnimals.append(rec[3])
        else:
            faveAnimals.append("")
            
print(faveAnimals)
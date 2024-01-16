import csv

totalRecords = 0
totalSalaries = 0

names = []
ages = []
salaries = []
print(f"{'Name':12} \t{'Age'} \t{'Salary':10}")
with open("week2/demo/example.csv") as exampleFile:
    file = csv.reader(exampleFile)

    for rec in file:
        print(f"{rec[0]:10} \t{rec[1]:3} \t{rec[2]:10}")

        names.append(rec[0])
        ages.append(int(rec[1]))
        salaries.append(float(rec[2]))

        totalRecords += 1
        totalSalaries += float(rec[2])

print(f"Total Records: {totalRecords} | total Salaries: {totalSalaries:.2f}")
for i in range(0,totalRecords):
    print(names[i],"is",ages[i],"years old")
totalAges = 0
for i in range(0, totalRecords):
    totalAges += ages[i]

average = totalAges / totalRecords
print(f"Average age: {average}")
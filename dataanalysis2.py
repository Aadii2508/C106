import numpy as num
import csv

file= open("Size of TV,%09Average time spent watching TV in a week (hours).csv")
file_data = csv.reader(file)

list= list(file_data)
list.pop(0)

marksList= []
dayspresent= []

for i in range(len(list)):
    marks= list[i][0]
    days = list[i][1]
    marksList.append(float(marks))
    dayspresent.append(float(days))

correlation = num.corrcoef(marksList , dayspresent)
print(correlation[0, 1])
# Week6Day1Lessons5&6 - Preparation for Project 3
# John Kowal  -  WALTER$

# Dictionaries

data = {}

file = open("WEEK6_sample_grades.csv")
for line in file:
    row = line.rstrip().split(",")
    x = eval(row[2])
    if len(row) == 3 and x == 100:
        if row[1] in data:
            data[row[1]] += x
        else:
            data[row[1]] = x
file.close()
print()
for key in data:
    print(key, ":", data[key])
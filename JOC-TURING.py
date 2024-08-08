# Week6Day1Lesson2 - Preparation for Project 3
# John Kowal  -  WALTER$

# FILES & ARRAYS

file = open("turing.txt")
lines = []
for line in file:
    lines.append(line.rstrip())
file.close()
print(lines[:2])
print(lines[-2:])

# Week6Day1Lesson7 - Preparation for Project 3
# John Kowal  -  WALTER$

# Dictionaries

def count_uniq(s):
    d = {}   # create a dictionary
    for char in s:
        if char not in d:
            d[char] = 1  # could be anything
    return len(d)  # number of keys
print()
print("Number of unique characters =", count_uniq("111224446"))
print("Number of unique characters =", count_uniq("30444775555"))
print("Number of unique characters =", count_uniq(""))

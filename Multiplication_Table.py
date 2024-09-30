# Week6Days4&5Lesson2 - Project 3 - Problem 2
# John Kowal  -  WALTER$

def multiplication_table(w, h, s):

    if w <= 0 or h <= 0:
        return None

    # Generate a 2D list where each entry is (i * j) * s
    return [[i * j * s for j in range(1, w + 1)] for i in range(1, h + 1)]

def print_2D(table):
    # Print each row of the table
    for row in table:
        print(row)

print()
print("5 3 1:")
print_2D(multiplication_table(5, 3, 1))
print()
print("5 3 2:")
print_2D(multiplication_table(5, 3, 2))

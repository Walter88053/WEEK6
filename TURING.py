# Week6Day1Lesson1 - Preparation for Project 3
# John Kowal  -  WALTER$

# FILES & ARRAYS

def lines():
    # Create an empty list to store the lines from a given file (turing.txt) as elements
    lines_list = []

    # Open the file
    file = open("turing.txt")

    # Read the data from the file
    file_data = file.read()

    # Split the file data into lines
    lines_list = file_data.splitlines()
    file.close()

    # Print all the lines from lines_list to verify it is the same as turing.txt
    print()
    for line in lines_list:
        print(line)
    print()
    first = [lines_list[0]]
    last = [lines_list[-1]]

    # printing result
    print("The first element of turing.txt is: " + str(first))
    print("The last element of turing.txt is: " + str(last))
    print("The total number of lines in turing.txt =", len(lines_list))

# Call main to execute
def main():
    lines()
main()
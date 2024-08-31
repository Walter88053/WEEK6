# Week6Days4&5Lesson2 - Project 3 - Problem 1
# John Kowal  -  WALTER$
#

import string
import re

def word_frequencies(filename):
    # Initialize an empty dictionary to store word counts
    map_by_value = {}

        # Open the file and read its contents
    with open(filename, 'r') as file:
            # Read the entire file content
        content = file.read()

            # Convert to lowercase and split into words
        words = content.lower().split()

            # Create a translation table to remove punctuation
        translator = str.maketrans('', '', string.punctuation)

            # Count the occurrences of each word
        for word in words:
                # Remove any punctuation from the word
            word = word.translate(translator)

                # If the word is not empty after removing punctuation
            if word:
                    # Increment the count for this word
                map_by_value[word] = map_by_value.get(word, 0) + 1

    return map_by_value
    print_map_by_value(word_frequencies("files/turing.txt"))
    
# Call the function and print the result
#filename = "turing.txt"
#frequencies = word_frequencies(filename)
#print(frequencies)

#def main():
#if __name__ == "__main__":
#   main()


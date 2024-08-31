# Week6Days4&5Lesson2 - Project 3 - Problem 1
# John Kowal  -  WALTER$

import string

def word_frequencies(filename):
    # Initialize an empty dictionary to store word counts
    map_by_value = {}

    # Open the file and read its contents
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the entire file content
        content = file.read()

        # Convert to lowercase
        content = content.lower()

        # Create a translation table to remove punctuation
        translator = str.maketrans('', '', string.punctuation + '\u002D\u0027\u2010\u2012\u2013\u2014')
        
        # Remove punctuation and split into words
        words = content.translate(translator).split()

        # Count the occurrences of each word
        for word in words:
            # Increment the count for this word
            map_by_value[word] = map_by_value.get(word, 0) + 1

    return map_by_value

def get_second_element(item):
    return item[1]

def print_map_by_value(freq_word):
    # Sort the dictionary by value (frequency) in descending order
    sorted_freq = sorted(freq_word.items(), key=get_second_element, reverse=True)

    # Print the sorted word frequencies
    for word, freq in sorted_freq:
        print(f"{freq:2d} {word}")

def main():
    filename = "turing.txt"
    print_map_by_value(word_frequencies(filename))

if __name__ == "__main__":
    main()

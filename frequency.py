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

        # Replace hyphens and em/en dashes with spaces
        content = content.replace('-', ' ').replace('–', ' ').replace('—', ' ')

        # Create a translation table to remove punctuation
        content = content.translate(str.maketrans('', '', string.punctuation))

        # Split into words and convert to lowercase
        words = content.lower().split()

        # Count the occurrences of each word
        for word in words:

            # If the word is not empty after removing punctuation
            for char in word:
                if char.isnumeric():
                    word = word.replace(char, '')
            if word:
                # Increment the count for this word
                map_by_value[word] = map_by_value.get(word, 0) + 1

    return map_by_value

def get_second_element(item):
    return item[1]

def print_map_by_value(freq_word):
    # Sort the dictionary by value (frequency) in descending order
    word_frequency_pairs = freq_word.items()

    # frequency (second element of each pair)
    sorted_freq = sorted(word_frequency_pairs, key=get_second_element, reverse=True)

    # Print the sorted word frequencies
    for word, freq in sorted_freq:
        print(f"{freq:2d} {word}")

def main():
    filename = "turing.txt"
    print_map_by_value(word_frequencies(filename))

if __name__ == "__main__":
    main()

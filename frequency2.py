# Week6Days4&5Lesson2 - Project 3 - Problem 1
# John Kowal  -  WALTER$

import string
import re

def word_frequencies(filename):
    # Initialize an empty dictionary to store word counts
    map_by_value = {}

    # Open the file and read its contents
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the entire file content
        content = file.read()

        # Convert to lowercase and split into words
        words = content.lower().split()

        # Create a translation table to remove punctuation
        translator = str.replace('', '', string.punctuation + '\u002D\u0027\u2010\u2012\u2013\u2014')


#        def remove_puncuation(text_only):
#           working = text_only.replace(".", " ")
#           text1 = working.translate(str.maketrans('\u2019', ' ', string.punctuation))
#           temp = text1.translate(str.maketrans('\u201d', ' ', string.punctuation))
#           temp1 = temp.translate(str.maketrans('\u2014', ' ', string.punctuation))
#           return re.sub(r"[^a-zA-Z/s]+", " ", temp1)

        # Count the occurrences of each word
        for word in words:
            # Remove any punctuation from the word
            word = re.sub("-", " ", word)
            word = re.sub("\u2013", " ", word)
            word = re.sub("\u2014", " ", word)
            word = re.sub(",", " ", word)
            word = re.sub("\.", " ", word)

            # If the word is not empty after removing punctuation
            if word:
                # Increment the count for this word
                map_by_value[word] = map_by_value.get(word, 0) + 1

    return map_by_value

def get_second_element(item):
    return item[1]

def print_map_by_value(freq_word):
    # Sort the dictionary by value (frequency) in descending order
#    sorted_freq = sorted(freq_word.items(), key=get_second_element, reverse=True)

    word_frequency_pairs = freq_word.items()

#   frequency (second element of each pair)
    sorted_freq = sorted(word_frequency_pairs, key=get_second_element, reverse=True)

    # Print the sorted word frequencies
    for word, freq in sorted_freq:
        print(f"{freq:2d} {word}")



def main():
    filename = "turing.txt"
    print_map_by_value(word_frequencies(filename))

if __name__ == "__main__":
    main()

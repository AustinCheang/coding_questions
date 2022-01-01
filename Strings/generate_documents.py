'''
You're given a string of available characters and a string representing a document that 
you need to generate. Write a function that determines if you can generate the document 
using the available characters. If you can generate the document, your function should 
return true; otherwise, it should return false.

You're only able to generate the document if the frequency of unique characters in the 
characters string is greater than or equal to the frequency of unique characters in the 
document string. For example, if you're given characters = "abcabc" and document = "aabbccc" 
you cannot generate the document because you're missing one c.

The document that you need to create may contain any characters, including special characters, 
capital letters, numbers, and spaces.

Sample input:
    characters = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"

Sample output:
    True

'''


def generateDocument_1(characters, document):
    # Time: O(m *(n+m)) where m and n are the length of document and characters
    # Space: O(1)
    for char in document:
        doc_freq = count_char_freq(char, document)
        char_freq = count_char_freq(char, characters)

        if doc_freq > char_freq:
            return False

    return True


def count_char_freq(character, target):
    freq = 0
    for char in target:
        if char == character:
            freq += 1

    return freq


def generateDocument_2(characters, document):
    # Time: O(c *(n+m)) where m and n are the length of document and characters, c is the length of unique characters in document
    # Space: O(c)
    counted = set()
    for char in document:
        if char in counted:
            continue
        doc_freq = count_char_freq(char, document)
        char_freq = count_char_freq(char, characters)

        if doc_freq > char_freq:
            return False

        counted.add(char)

    return True


def generateDocument_3(characters, document):
    # Time: O(n+m) | Space: O(c) where c is the len of unique character in characters
    char_dict = {}

    for char in characters:
        if char not in char_dict:
            char_dict[char] = 0

        char_dict[char] += 1

    for char in document:
        if char not in char_dict or char_dict[char] == 0:
            return False
        char_dict[char] -= 1

    return True


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

print(generateDocument_3(characters, document))

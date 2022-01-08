'''
Write a function that takes in a string and returns its longest substring 
without duplicate characters.

You can assume that there will only be one longest substring without 
duplication.

Sample input:
    string = "clementisacap"

Sample output:
    "mentisac"
'''


def longestSubstringWithoutDuplication(string):
    # Time: O(n) | Space: O(max(n, a)) where a is the number of unique charachters
    last_seen = {}
    start_index = 0
    output = [0, 1]

    for i, char in enumerate(string):
        if char in last_seen:
            start_index = max(start_index, last_seen[char] + 1)

        if output[1] - output[0] < i + 1 - start_index:
            output = [start_index, i+1]

        last_seen[char] = i
    return string[output[0]:output[1]]


string = "clementisacap"
string = "abccdeaabbcddef"

print(longestSubstringWithoutDuplication(string))

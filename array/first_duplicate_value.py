'''
Given an array of integers between 1 and n, inclusive, where n 
is the length of the array, write a function that returns the 
irst integer that appears more than once (when the array is read 
from left to right).

In other words, out of all the integers that might occur more 
than once in the input array, your function should return the 
one whose first duplicate value has the minimum index.

If no integer appears more than once, your function should 
return -1.

Note that you're allowed to mutate the input array.

Sample input:
    array = [2, 1, 5, 2, 3, 3, 4]

Sample output:
    2

'''


def firstDuplicateValue_1(array):
    # Time: O(n) | Space: O(n)
    track = set()

    for num in array:
        if num not in track:
            track.add(num)

        else:
            return num

    return -1


def firstDuplicateValue_2(array):
    # Time: O(n) | Space: O(1)
    for value in array:
        absValue = abs(value)
        print(f'absValue: {absValue}')
        if array[absValue - 1] < 0:
            print(f'array[absValue - 1]: {array[absValue - 1]}')
            return absValue

        array[absValue - 1] *= -1

    return -1


array = [2, 1, 5, 2, 3, 3, 4]

print(firstDuplicateValue_1(array))
print(firstDuplicateValue_2(array))

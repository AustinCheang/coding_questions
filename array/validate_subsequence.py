"""
Given two non-empty arrays of integers, write a function that determines 
whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily 
adjacent in the array but that are in the same order as they appear in the
array. For instance, the numbers [1, 3, 4] form a subsequence of the array 
[1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an 
array and the array itself are both valid subsequences of the array.

Sample input:
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]

Sample output:
    True
 """


def isValidSubsequence_1(array, sequence):
    # Time: O(n) | Space: O(1)
    array_pointer = 0
    sequence_pointer = 0

    while array_pointer < len(array) and sequence_pointer < len(sequence):
        if array[array_pointer] == sequence[sequence_pointer]:
            sequence_pointer += 1

        array_pointer += 1

    return len(sequence) == sequence_pointer


def isValidSubsequence_2(array, sequence):
    # Time: O(n) | Space: O(1)
    seq_pointer = 0

    for num in array:
        if seq_pointer == len(sequence):
            break
        if sequence[seq_pointer] == num:
            seq_pointer += 1

    return seq_pointer == len(sequence)


print(isValidSubsequence_2([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))

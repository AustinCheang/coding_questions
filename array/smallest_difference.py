'''
Write a function that takes in two non-empty arrays of integers, 
finds the pair of numbers (one from each array) whose absolute 
difference is closest to zero, and returns an array containing 
these two numbers, with the number from the first array in the 
first position.

Note that the absolute difference of two integers is the distance 
between them on the real number line. For example, the absolute 
difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with 
the smallest difference.

Sample input:
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]

Sample output:
    [28, 26]
'''


def smallestDifference_1(array_1, array_2):
    array_1.sort()
    array_2.sort()

    current_smallest = 10000
    array_1_pointer = 0
    array_2_pointer = 0

    for i in range(len(array_1)):
        for j in range(len(array_2)):
            if abs(array_1[i] - array_2[j]) < current_smallest:
                current_smallest = abs(array_1[i] - array_2[j])
                array_1_pointer = i
                array_2_pointer = j

    return [array_1[array_1_pointer], array_2[array_2_pointer]]


def smallestDifference_2(array_1, array_2):
    smallest = float("inf")
    current = float("inf")
    array_1_pointer = 0
    array_2_pointer = 0
    smallest_pair = []

    while array_1_pointer < len(array_1) and array_2_pointer < len(array_2):
        first_num = array_1[array_1_pointer]
        second_num = array_2[array_2_pointer]

        if first_num == second_num:
            return [first_num, second_num]

        elif first_num > second_num:
            current = first_num - second_num
            array_2_pointer += 1

        else:
            current = second_num - first_num
            array_1_pointer += 1

        if current < smallest:
            smallest = current
            smallest_pair = [first_num, second_num]

    return smallest_pair


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(smallestDifference_2(arrayOne, arrayTwo))

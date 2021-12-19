"""
Write a function that takes in a non-empty array of distinct integers and an integer 
representing a target sum. If any two numbers in the input array sum up to the target sum, 
the function should return them in an array, in any order. If no two numbers sum up to the 
target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array
you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

Sample input
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10

Sample output
    [-1, 11]

"""


def twoNumberSum_1(array, targetSum):
    # Time: O(N^2) | Space: O(1)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


def twoNumberSum_2(array, targetSum):
    # Time: O(nlog(n)) | Space: O(1)
    array.sort()

    start_pointer = 0
    end_pointer = len(array) - 1

    while start_pointer < end_pointer:
        current_sum = array[start_pointer] + array[end_pointer]

        if current_sum < targetSum:
            start_pointer += 1
        elif current_sum > targetSum:
            end_pointer -= 1
        else:
            return [array[start_pointer], array[end_pointer]]

    return []


def twoNumberSum_3(array, targetSum):
    # Time: O(n) | Space: O(n)
    remainders = []

    for num in array:
        remainder = targetSum - num

        if remainder not in remainders:
            remainders.append(num)
        else:
            return [num, remainder]

    return []


# print(twoNumberSum_3([3, 5, -4, 8, 11, 1, -1, 6], 10))

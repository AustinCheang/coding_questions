'''
Write a function that takes in a non-empty array of integers that are
sorted in ascending order and returns a new array of the same length
with the squares of the original integers also sorted in ascending order.

Sample input 1:
    array = [1, 2, 3, 5, 6, 8, 9]

Sample output 1:
    [1, 4, 9, 25, 36, 64, 81]

Sample input 2:
    array = [-7, -5, -3, 1, 3, 4, 9]

Sample output 2:
    [1, 9, 9, 16, 25, 49, 81]
'''


def sortedSquaredArray_1(array):
    # Time: O(nlog(n)) | Space: O(n)
    return sorted([num ** 2 for num in array])


def sortedSquaredArray_2(array):
    # Time: O(n) | Space: O(n)
    start_pointer = 0
    end_pointer = len(array) - 1

    sorted_array = [0 for _ in array]

    for i in range(len(array)-1, -1, -1):
        if abs(array[start_pointer]) > abs(array[end_pointer]):
            sorted_array[i] = array[start_pointer] ** 2
            start_pointer += 1
        else:
            sorted_array[i] = array[end_pointer] ** 2
            end_pointer -= 1
    return sorted_array


print(sortedSquaredArray_2([1, 2, 3, 5, 6, 8, 9]))

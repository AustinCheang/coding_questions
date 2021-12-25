'''
Write a function that takes in an array of integers and 
returns a sorted version of that array. Use the Insertion Sort algorithm to sort the array.

Sample input:
    array = [8, 5, 2, 9, 5, 6, 3]

Sample output:
    [2, 3, 5, 5, 6, 8, 9]
'''


def insertionSort_1(array):
    # Best: Time: O(n) | Space: O(1)
    # Average: Time: O(n^2) | Space: O(1)
    # Worst: Time: O(n^2) | Space: O(1)

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]

print(insertionSort_1(array))

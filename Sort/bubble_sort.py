'''
Write a function that takes in an array of integers and returns a sorted 
version of that array. Use the Bubble Sort algorithm to sort the array.

Sample input:
    array = [8, 5, 2, 9, 5, 6, 3]

Sample output:
    [2, 3, 5, 5, 6, 8, 9]
'''


def bubbleSort_1(array):
    # Best: O(n) time | O(1) space
    # Average: O(n^2) time | O(1) space
    # Worst: O(n^2) time | O(1) space
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                swap(j, j+1, array)
    return array


def bubbleSort_2(array):
    # Best: O(n) time | O(1) space
    # Average: O(n^2) time | O(1) space
    # Worst: O(n^2) time | O(1) space
    counter = 0
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter += 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]

print(bubbleSort_1(array))

'''
Write a function that takes in an array of integers and 
returns a sorted version of that array. Use the Selection 
Sort algorithm to sort the array.

Sample input:
    array = [8, 5, 2, 9, 5, 6, 3]

Sample output:
    [2, 3, 5, 5, 6, 8, 9]
'''


def selectionSort_1(array):
    current_index = 0

    while current_index < len(array) - 1:
        smallest_index = current_index
        # print(f'current_index: {current_index}')

        for i in range(current_index + 1, len(array)):
            if array[smallest_index] > array[i]:
                # print(f'found smallest: {array[i]}')
                smallest_index = i

        swap(current_index, smallest_index, array)
        # print(f'{array}')

        current_index += 1
    # print('-'*20)
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]
print(selectionSort_1(array))

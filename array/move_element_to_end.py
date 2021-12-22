'''
You're given an array of integers and an integer. Write a function that
moves all instances of that integer in the array to the end of the array
and returns the array.

The function should perform this in place (i.e., it should mutate the
input array) and doesn't need to maintain the order of the other integers.

Sample input:
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2

Sample output:
    [1, 3, 4, 2, 2, 2, 2, 2]
'''


def moveElementToEnd_1(array, toMove):
    # Time: O(nlog(n)) | Space: O(1)
    array.sort()
    target_index = 0
    found_flag = False

    for i in range(len(array)):
        if not found_flag:
            if array[i] == toMove:

                target_index = i
                found_flag = True
        else:
            if array[i] != toMove:
                temp = array[i]
                array[i] = array[target_index]
                array[target_index] = temp
                target_index += 1

    return array


def moveElementToEnd_2(array, toMove):
    # time: O(n) | Space: O(1)
    left_pointer = 0
    right_pointer = len(array) - 1

    while (left_pointer < right_pointer):
        if array[right_pointer] == toMove:
            right_pointer -= 1

        elif array[left_pointer] == toMove:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
            left_pointer += 1
            right_pointer -= 1

        else:
            left_pointer += 1

    return array


def moveElementToEnd_3(array, toMove):
    # time: O(n) | Space: O(1)
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove and array[j] != toMove:
            temp = array[j] - array[i]
            array[i] = array[i] + temp
            array[j] = array[j] - temp

        i += 1
    return array


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd_3(array, toMove))

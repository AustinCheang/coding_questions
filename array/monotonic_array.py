'''
Write a function that takes in an array of integers and returns a boolean
representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right,
are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing;
they simply don't increase. Similarly, non-decreasing elements aren't
necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

Sample input:
    array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample output:
    true
'''


def isMonotonic_1(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]

    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i-1]

        if break_direction(direction, array[i-1], array[i]):
            return False

    return True


def break_direction(direction, previous_num, current_num):
    difference = current_num - previous_num
    print(f'direction: {direction}')
    if direction > 0:
        print(f'difference: {difference}')
        return difference < 0
    return difference > 0


def isMonotonic_2(array):
    is_non_decrease = True
    is_non_increase = True

    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            is_non_decrease = False

        if array[i] < array[i-1]:
            is_non_increase = False

    return is_non_increase or is_non_decrease


array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

print(isMonotonic_2(array))

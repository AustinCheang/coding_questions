'''
Write a function that takes in an array of positive integers and returns the maximum 
sum of non-adjacent elements in the array.

If the input array is empty, the function should return 0.

Sample input:
    array = [75, 105, 120, 75, 90, 135]

Sample output:
    330 // 75 + 120 + 135
'''


def maxSubsetSumNoAdjacent_1(array):
    # Time: O(n) | Space: O(n)
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        max_sums = array[:]
        max_sums[1] = max(array[0], array[1])

        for i in range(2, len(max_sums)):
            max_sums[i] = max(max_sums[i-1], max_sums[i-2] + array[i])
            print(f'current max sum: {max_sums[i]}')

        return max_sums[-1]


def maxSubsetSumNoAdjacent_2(array):
    # Time: O(n) | Space: O(1)
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        largest = max(array[0], array[1])
        second_largest = array[0]

        for i in range(2, len(array)):
            current = max(largest, second_largest + array[i])
            second_largest = largest
            largest = current

        return largest


array = [75, 105, 120, 75, 90, 135]
# array = [4, 3, 5, 200, 5, 3]

print(maxSubsetSumNoAdjacent_1(array))

'''
Write a function that takes in a non-empty array of distinct 
integers and an integer representing a target sum. The function 
should find all triplets in the array that sum up to the target 
sum and return a two-dimensional array of all these triplets. 
The numbers in each triplet should be ordered in ascending order, 
and the triplets themselves should be ordered in ascending order 
with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should 
return an empty array.

Sample input: 
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0

Sample output:
    [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]] 
'''


def threeNumberSum_1(array, targetSum):
    # Time: O(n^3) | Space: O(n)
    ans = []
    array.sort()

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                if array[i] + array[j] + array[k] == targetSum:
                    ans.append([array[i], array[j], array[k]])

    return ans


def threeNumberSum_2(array, targetSum):
    # Time: O(n^2) | Space: O(n)
    ans = []
    array.sort()

    for i in range(len(array)):
        left_pointer = i + 1
        right_pointer = len(array) - 1
        start = array[i]

        while (left_pointer < right_pointer):
            left = array[left_pointer]
            right = array[right_pointer]
            temp_sum = start + left + right

            if temp_sum == targetSum:
                ans.append([start, left, right])
                left_pointer += 1
                right_pointer -= 1

            elif temp_sum > targetSum:
                right_pointer -= 1

            else:
                left_pointer += 1

    return ans


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
targetSum = 18

print(threeNumberSum_2(array, targetSum))

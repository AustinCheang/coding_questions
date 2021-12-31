'''
Write a function that takes in a non-empty string and that returns 
a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward 
and backward. Note that single-character strings are palindromes.

Sample input:
    string = "abcdcba"

Sample output:
    True
'''


def isPalindrome_1(string):
    # Time: O(n^2) due to looping the ans string and given string| Space: O(n)
    ans = ''
    # for i in range(len(string)-1, -1, -1):
    #     ans += string[i]

    for i in reversed(range(len(string))):
        ans += string[i]
    print(f'ans: {ans}')
    return ans == string


def isPalindrome_2(string):
    # Time: O(n) | Space: O(n)
    ans = []

    for i in reversed(range(len(string))):
        ans.append(string[i])

    ans = "".join(ans)
    print(f'ans: {ans}')
    return ans == string


def isPalindrome_3(string, i=0):  # Rercursion
    # Time: O(n) | Space: O(n) due to stack
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome_3(string, i+1)


def isPalindrome_3_2(string, i=0):  # Tail recursion
    # If a function is tail recursive, it's either making a simple
    # recursive call or returning the value from that call.
    # No computation is performed on the returned value. Thus,
    # there is no real need to preserve the stack frame for that call.
    # We won't need any of the local data once the tail recursive
    # call is made

    # Time: O(n)| Space: O(1)
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome_3_2(string, i+1)


def isPalindrome_4(string):  # Two pointers
    # Time: O(n) | Space: O(1)
    left_pointer = 0
    right_pointer = len(string) - 1

    while left_pointer < right_pointer:
        if string[left_pointer] != string[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    return True


string = "abcdcba"
print(f'string: {string}')

print(isPalindrome_4(string))

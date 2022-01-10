'''
Write a function that takes in a string of words separated by one 
or more whitespaces and returns a string that has these words in 
reverse order. For example, given the string "tim is great", your 
function should return "great is tim".

For this problem, a word can contain special characters, punctuation, 
and numbers. The words in the string will be separated by one or more 
whitespaces, and the reversed string must contain the same whitespaces 
as the original string. For example, given the string 
"whitespaces    4" you would be expected to return "4    whitespaces".

Note that you're not allowed to to use any built-in split or reverse 
methods/functions. However, you are allowed to use a built-in join 
method/function.

Also note that the input string isn't guaranteed to always contain words.

Sample input:
    stirng = "..H,, hello 678"

Sample output
    "678 hello ..H,,"
'''


def reverseWordsInString_1(string):
    # Time: O(n) | Space: O(n)
    words = []
    start_word = 0

    for index in range(len(string)):
        char = string[index]

        if char == ' ':
            words.append(string[start_word: index])
            start_word = index

        elif string[start_word] == ' ':
            words.append(" ")
            start_word = index

    words.append(string[start_word:])

    reverse_list(words)
    return "".join(words)


def reverse_list(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


def reverseWordsInString_2(string):
    # Time: O(n) | Space: O(n)
    chars = [char for char in string]

    reverse_list_range(chars, 0, len(chars)-1)
    # print(f'chars: {chars}')

    start_word = 0

    while start_word < len(chars):
        end_word = start_word
        # print(f'end_word: {end_word}')

        while end_word < len(chars) and chars[end_word] != " ":
            end_word += 1

        reverse_list_range(chars, start_word, end_word - 1)
        # print(f'chars: {chars}')
        start_word = end_word + 1

    return ''.join(chars)


def reverse_list_range(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


string = "..H,, hello 678"
print(reverseWordsInString_1(string))
print('-'*10)
print(reverseWordsInString_2(string))

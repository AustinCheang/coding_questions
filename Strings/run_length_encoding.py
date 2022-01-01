'''
Write a function that takes in a non-empty string and returns its run-length encoding.

From Wikipedia, "run-length encoding is a form of lossless data compression in which 
runs of data are stored as a single data value and count, rather than as the original run." 
For this problem, a run of data is any sequence of consecutive, identical characters. So the 
run "AAA" would be run-length-encoded as "3A".

To make things more complicated, however, the input string can contain all sorts of special 
characters, including numbers. And since encoded data must be decodable, this means that we 
can't naively run-length-encode long runs. For example, the run "AAAAAAAAAAAA" (12 As), can't 
naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA". 
Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the 
aforementioned run should be encoded as "9A3A".

Sample input:
    string = "AAAAAAAAAAAAABBCCCCDD"

Sample output:
    "9A4A2B4C2D"
'''


def runLengthEncoding(string):
    # Time: O(n) | Space: O(n)
    ans = []
    length = 1

    for i in range(1, len(string)):
        current_char = string[i]
        prev_char = string[i-1]

        if current_char != prev_char or length == 9:
            ans.append(str(length))
            ans.append(prev_char)
            length = 0

        length += 1

    ans.append(str(length))
    ans.append(string[len(string) - 1])
    print(ans)
    return ''.join(ans)


string = "AAAAAAAAAAAAABBCCCCDD"

print(runLengthEncoding(string))

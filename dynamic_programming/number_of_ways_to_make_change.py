'''
Given an array of distinct positive integers representing coin 
enominations and a single non-negative integer n representing a 
target amount of money, write a function that returns the number 
of ways to make change for that target amount using the given coin 
denominations.

Sample input:
    n = 6
    denoms = [1, 5]

Sample output:
    2 // 1x1 + 1x5 and 6x1
'''


def numberOfWaysToMakeChange(n, denoms):
    # Time: O(nd) where d is the number of denoms | Space: O(n)

    ways = [0 for i in range(n+1)]
    ways[0] = 1

    for coin in denoms:
        # print(f'coin: {coin}')
        for amount in range(len(ways)):
            # print(f'amount: {amount}')
            if amount >= coin:
                ways[amount] += ways[amount - coin]
                print(ways)

    return ways[-1]


n = 6
denoms = [1, 5]

print(numberOfWaysToMakeChange(n, denoms))

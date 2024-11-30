#!/usr/bin/env python3

"""Module of an algorithm that is non-greedy
"""


def makeChange(coins, total):
    """This function makes some changes
    to determine one of the best way to find
    coins and sum them up ti tital
    param: coins
    param: total
    """
    if total <= 0 or len(coins) == 0:
        return 0

    # sort the array by reverse order
    coins.sort(reverse=True)
    pieces, i = 0, 0

    while i < len(coins) and total != 0:
        if total < coins[i]:
            i += 1
            continue
        else:
            total -= coins[i]
            pieces += 1
            if total >= coins[i]:
                pass
            else:
                i += 1

    if total == 0:
        return pieces
    else:
        return -1


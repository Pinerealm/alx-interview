#!/usr/bin/python3
"""The 0-making_change module"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount, total.
    """
    if total <= 0:
        return 0
    if len(coins) == 0:
        return -1
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total = total % coin
    if total != 0:
        return -1
    return count

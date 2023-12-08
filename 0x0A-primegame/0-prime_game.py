#!/usr/bin/python3
"""The 0-prime_game module1"""


def isWinner(x, nums):
    """The isWinner function"""
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for i in range(max(n + 1, 2))]
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False

    c = 0
    for i in range(len(primes)):
        if primes[i]:
            c += 1
        primes[i] = c

    player = 0
    for n in nums:
        player += primes[n] % 2 == 1
    if player * 2 == len(nums):
        return None
    if player * 2 > len(nums):
        return "Maria"
    return "Ben"

#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """Calculates the least amount of operations to reach n characters
    given that the only operations allowed are Copy All and Paste and
    the initial string is the character 'H'

    Args:
        n (int): Number of characters to reach

    Returns:
        int: Minimum number of operations to reach n characters
    """
    if n <= 1:
        return 0
    i = 2
    operations = 0
    while i <= n:
        if n % i == 0:
            operations += i
            n /= i
        else:
            i += 1
    return operations

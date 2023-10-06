#!/usr/bin/python3
"""The Lockboxes Problem"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened.

    Args:
        boxes (list): List of lists representing boxes and keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or len(boxes) == 0:
        return False

    keys = [0]
    for key in keys:
        for box in boxes[key]:
            # print(f'{keys} {box}')
            if box not in keys and box < len(boxes):
                keys.append(box)

    if len(keys) == len(boxes):
        return True
    return False

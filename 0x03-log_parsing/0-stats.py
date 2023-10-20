#!/usr/bin/python3
"""Log parsing"""
import sys


def print_stats(file_size, status_codes):
    """Prints the stats

    Args:
        file_size (int): The file size
        status_codes (dict): The status codes
    """
    print(f'File size: {file_size}')
    for key in sorted(status_codes):
        if status_codes[key] > 0:
            print(f'{key}: {status_codes[key]}')


if __name__ == "__main__":
    line_count = file_size = 0
    status_codes = {}

    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                print_stats(file_size, status_codes)
                break
            line_contents = line.rstrip().split()

            line_count += 1
            if len(line_contents) < 2:
                continue
            code, size = line_contents[-2], line_contents[-1]
            if size.isdigit():
                file_size += int(size)

            if code.isdigit():
                status_codes[code] = status_codes.get(code, 0) + 1
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)

        except KeyboardInterrupt:
            print_stats(file_size, status_codes)
            raise

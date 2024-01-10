#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints statistics based on the computed metrics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing counts for each status code.
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def main():
    total_size = 0
    status_codes = {
            200: 0, 301: 0, 400: 0,
            401: 0, 403: 0, 404: 0,
            405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            tokens = line.split()
            if len(tokens) >= 8:
                status_code = int(tokens[-2])
                file_size = int(tokens[-1])
                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()

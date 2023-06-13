#!/usr/bin/python3
import sys

def print_stats(file_size, status_codes):
    """
    Prints the statistics for file size and status codes.

    Args:
        file_size (int): The total file size.
        status_codes (dict): A dictionary containing status codes and their counts.

    Returns:
        None
    """
    print("File size: {:d}".format(file_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{:d}: {:d}".format(code, count))

def parse_line(line):
    """
    Parses a log entry line and extracts the file size and status code.

    Args:
        line (str): A log entry line.

    Returns:
        tuple: A tuple containing the file size (int) and status code (int).
    """
    parts = line.split()
    file_size = int(parts[-1])
    status_code = int(parts[-2])
    return file_size, status_code

def main():
    file_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            file_size += parse_line(line)[0]
            status_code = parse_line(line)[1]
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
            print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)

if __name__ == "__main__":
    main()

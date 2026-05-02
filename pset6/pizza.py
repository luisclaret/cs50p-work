# This program will show the list of available pizzas

import csv
from tabulate import tabulate
import sys


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command lines arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command lines arguments")
    else:
        path = sys.argv[1].strip()
        if path.endswith(".csv"):
            print(prettier(path=path))
        else:
            sys.exit("Not a .csv file")


def prettier(path: str):
    row_lists = []
    try:
        with open(path, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                row_lists.append(row)
    except FileNotFoundError:
        sys.exit("No such a file exist")
    else:
        return tabulate(row_lists, headers="firstrow", tablefmt="grid")


if __name__ == "__main__":
    main()

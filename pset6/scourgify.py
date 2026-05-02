# This program will organize a csv

import sys
import csv


def main():
    if len(sys.argv) == 3:
        read_path = sys.argv[1]
        write_path = sys.argv[2]
        modified_data = organize(read_path=read_path)
        newfile(write_path=write_path, modified_data=modified_data)
    else:
        sys.exit("Problem executing the program. Two arguments expected! ")


def organize(read_path: str):
    row_list = []
    try:
        with open(read_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row_first_name = row["name"].split(",")[-1].strip()
                row_second_name = row["name"].split(",")[0].strip()
                house = row["house"]
                row_list.append(
                    {
                        "first": row_first_name,
                        "last": row_second_name,
                        "house": house,
                    }
                )
    except FileNotFoundError:
        sys.exit("File does not exist! ")
    else:
        return row_list


def newfile(write_path: str, modified_data: list):
    with open(write_path, "w") as csvfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(modified_data)


if __name__ == "__main__":
    main()

# This program is going to read how many lines of codes has a certain .py file

import sys


def main():
    print(read_path())


def read_path():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            path = sys.argv[1]  # Check if path exist
            if path.endswith(".py"):
                with open(path, "r") as file:
                    line_count = 0
                    for line in file:
                        if line.strip().startswith("#") or line.strip() == "":
                            pass
                        else:
                            line_count += 1
            else:
                sys.exit("No a python file")
    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return line_count


if __name__ == "__main__":
    main()

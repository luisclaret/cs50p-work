import random


def main():
    level = get_level()

    """
    operation_array = []
    # This will generate the numbers for the operation
    for i in range(10):
        (x, y) = (generate_integer(level=level), generate_integer(level=level))
        operation_array.append((x, y))
    """

    # This will prompt the user to answer each operation
    i = 0  # Start of the operation
    score = 0  # Initialization of score
    attemps = 3  # Initialization of attemps per operation
    while i < 10:
        if attemps == 3:
            (x, y) = (generate_integer(level=level), generate_integer(level=level))

        try:
            result = int(input(f"{x} + {y} = ").strip())
        except (ValueError, TypeError):
            if attemps == 1:
                attemps = 3
                i += 1
                print(f"{x} + {y} = {x + y}")
            else:
                print("EEE")
                attemps -= 1

        else:
            if result == (x + y) and attemps > 0:
                score += 1
                i += 1
                attemps = 3
            elif result != (x + y) and attemps > 0:
                print("EEE")
                attemps -= 1

            # Ask if the user has run out of attemps
            if attemps == 0:
                print(f"{x} + {y} = {x + y}")
                attemps = 3
                i += 1

    print("Score: ", score)


def get_level():
    while True:
        level_input = input("Level: ").strip()
        try:
            level_input = int(level_input)
        except (TypeError, ValueError):
            pass
        else:
            if level_input in (1, 2, 3):
                break
    return level_input


def generate_integer(level):
    if level == 1:
        number = random.randint(0, (10**level) - 1)
    else:
        number = random.randint((10 ** (level - 1)), (10**level) - 1)
    # number = random.randint(0, (10**level) - 1)
    return number


if __name__ == "__main__":
    main()

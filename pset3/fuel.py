# This code will translate fraction format to a percentage


def main():
    transformation()


def transformation():
    fraction_input = input("Faction: ")
    fraction_numbers = fraction_input.strip().split("/")
    try:
        x = int(fraction_numbers[0])
        y = int(fraction_numbers[1])
        division = x / y
    except (ValueError, ZeroDivisionError):
        transformation()
    else:
        if 0 <= division <= 0.01:
            print("E")
        elif 0.99 <= division <= 1:
            print("F")
        elif division > 1 or division < 0 or y == 0:
            transformation()
        else:
            print(str(int(round((division * 100)))) + "%")


def ispositive(num):
    return num > 0


if __name__ == "__main__":
    main()

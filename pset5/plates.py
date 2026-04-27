# Plates testing


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    number_found = False
    if 2 <= len(s) <= 6 and (s[0].isalpha() and s[1].isalpha()):
        for i in range(len(s)):
            if (
                not s[i].isalnum()
                or (not s[i].isdecimal() and number_found)
                or (s[i].isdecimal() and not number_found and int(s[i]) == 0)
            ):
                return False
            elif s[i].isdecimal():
                number_found = True
    else:
        return False
    return True


if __name__ == "__main__":
    main()

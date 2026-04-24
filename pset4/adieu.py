import inflect


def main():
    p = inflect.engine()
    name_list = userInput()
    print("Adieu, adieu, to", p.join(name_list))


def userInput():
    name_list = []
    while True:
        try:
            user_input = input("Name: ").strip()
            name_list.append(user_input)
        except EOFError:
            print()
            return name_list


if __name__ == "__main__":
    main()

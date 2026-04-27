def main():
    greeting = input().strip()
    print("$ ", value(greeting=greeting))


def value(greeting: str):
    greeting = greeting.lower()
    if greeting == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

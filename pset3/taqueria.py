def main():
    dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    accumulator = 0
    total(accumulator, dict)


def total(accumulator, dict):
    try:
        item = input("Item: ").title()
        item_price = dict[item]
    except EOFError:
        print("")
    except KeyError:
        total(accumulator, dict)
    else:
        accumulator = accumulator + item_price
        print(f"Total: ${accumulator:.2f}")
        total(accumulator, dict)


if __name__ == "__main__":
    main()

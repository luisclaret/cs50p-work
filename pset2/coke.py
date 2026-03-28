# This is a coke expending machine


def main():
    allowed_coins = [5, 10, 25]
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        input_coin = int(input("Insert Coin: "))
        amount_due = amount_due_calculation(amount_due, allowed_coins, input_coin)
    print(f"Change Owed: {-1 * amount_due}")


def amount_due_calculation(amount_due: int, allowed_coins: list, input_coin: int):
    if amount_due > 0 and input_coin in allowed_coins:
        amount_due = amount_due - input_coin
    return amount_due


if __name__ == "__main__":
    main()

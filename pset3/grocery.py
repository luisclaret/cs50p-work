def main():
    grocery_list = dict()
    groceryList(grocery_list)


def groceryList(grocery_list: dict):
    try:
        grocery = input().upper()
    except EOFError:
        for i in sorted(grocery_list):
            print(grocery_list[i], i)
    else:
        if grocery in grocery_list:
            grocery_list[grocery] += 1
        else:
            grocery_list[grocery] = 1
        groceryList(grocery_list)


if __name__ == "__main__":
    main()

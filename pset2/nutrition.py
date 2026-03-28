# This program tells you the nutrition values of the fruits


def main():
    fruits_dict = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 60,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }
    fruit = input("Item: ").strip().lower()
    if fruit not in fruits_dict:
        print("")
    else:
        print("Calories: ", fruits_dict[fruit])


if __name__ == "__main__":
    main()

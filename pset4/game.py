import random


def main():
    level_input = levelInput()
    guessInput(level_input=level_input)


def levelInput():
    while True:
        level_input = input("Level: ").strip()
        try:
            level_input = int(level_input)
        except (TypeError, ValueError):
            continue
        else:
            if level_input > 0:
                return level_input
            else:
                continue


def guessInput(level_input: int):
    random_number = random.randint(1, level_input)
    while True:
        guess_number = input("Guess: ").strip()
        try:
            guess_number = int(guess_number)
        except (TypeError, ValueError):
            continue
        else:
            if guess_number > 0:
                if guess_number > random_number:
                    print("Too large!")
                    continue
                elif guess_number < random_number:
                    print("Too small!")
                    continue
                else:
                    print("Just right!")
                    break
            else:
                continue


if __name__ == "__main__":
    main()

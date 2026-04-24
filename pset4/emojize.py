# This code will prompt the user for an input and will return the emoji
import emoji


def main():
    user_input = input("Input: ").strip()
    print(emoji.emojize(user_input, language="alias"))


if __name__ == "__main__":
    main()

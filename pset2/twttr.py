# This will eliminate all vowel from a word


def main():
    word = input("Input: ").strip()

    new_word = ""
    vowels = "aeiouAEIOU"

    for i in word:
        if i not in vowels:
            new_word = new_word + i

    print("Output: ", new_word)


if __name__ == "__main__":
    main()

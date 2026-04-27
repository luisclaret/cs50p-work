def main():
    word = input().strip()
    new_word = shorten(word=word)
    print(new_word)


def shorten(word: str):
    new_word = ""
    for letter in word:
        if letter not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            new_word = new_word + letter
    return new_word


if __name__ == "__main__":
    main()

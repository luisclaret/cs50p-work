# This program will change the variable name from camel case to snake case

# Camel case are: mainNav, helloWorld, etc


def main():
    camel_name = input("camelCase: ").strip()
    # print(split_words(camel_name))
    snake_name = convert_snake(split_words(camel_name))
    print(snake_name)


def split_words(camelCase: str):
    split_snake = []
    word = ""
    for _ in camelCase:
        if _.islower():
            word = word + _
        else:
            split_snake.append(word)
            word = _.lower()

    split_snake.append(word)
    return split_snake


def convert_snake(words: list):
    snake_word = ""
    for _ in words:
        snake_word = snake_word + _ + "_"
    snake_word = snake_word.rstrip("_")
    return snake_word


if __name__ == "__main__":
    main()

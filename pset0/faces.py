# This code will replace ":)" to 🙂 and ":(" to 🙁


# Function convert
def convert(string: str):
    return string.replace(":)", "\U0001f642").replace(
        ":(", "\U0001f641"
    )  # This is Unicodes


# main function
def main():
    string = input("Please enter the string: ")
    print(convert(string))


# calling main
main()

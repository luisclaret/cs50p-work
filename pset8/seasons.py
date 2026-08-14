import inflect
from datetime import date
import sys

p = inflect.engine()

def main():
    print(string_minutes(input("Date of Birth: ")))

def return_birth_date(s):
    try:
        birth_date = date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")

    return birth_date


def string_minutes(s):
    today = date.today()

    birth_date = return_birth_date(s)

    if today < birth_date:
        sys.exit("Invalid date")

    time_delta = today - birth_date
    return p.number_to_words(time_delta.days * 24 * 60, andword="").capitalize() + " " + p.plural_noun("minute", time_delta.days * 24 * 60)

if __name__ == "__main__":
    main()

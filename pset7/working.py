import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r'(1[0-2]|[1-9])(?::([0-5][0-9]))?\s(AM|PM)\sto\s(1[0-2]|[1-9])(?::([0-5][0-9]))?\s(AM|PM)'
    match = re.fullmatch(pattern, s)

    if not match:
        raise ValueError("The value is not valid")
    
    hour_1 = match.group(1)
    minute_1 = match.group(2) if match.group(2) is not None else "00"
    datepart_1 = match.group(3)

    hour_2 = match.group(4)
    minute_2 = match.group(5) if match.group(5) is not None else "00"
    datepart_2 = match.group(6)

    hour_1 = int(hour_1)
    hour_2 = int(hour_2)

    convert_string = f"{timechange(hour_1, datepart_1):02}:{minute_1} to {timechange(hour_2, datepart_2):02}:{minute_2}"

    return convert_string


def timechange(hour, time):
    if time == "AM":
        return 0 if hour == 12 else hour
    else:
        return 12 if hour == 12 else hour + 12

    ...

if __name__ == "__main__":
    main()

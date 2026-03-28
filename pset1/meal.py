def main():
    time = input("What time is it?: ").strip()
    complex_time = convert(time)
    # print(complex_time)
    if 7 <= complex_time <= 8:
        print("breakfast time")
    elif 12 <= complex_time <= 13:
        print("lunch time")
    elif 18 <= complex_time <= 19:
        print("dinner time")


def convert(time):
    (hour, minutes) = time.split(":")
    hour = float(hour)
    minutes = float(minutes)
    complex_time = hour + (minutes / 60)
    return complex_time


if __name__ == "__main__":
    main()

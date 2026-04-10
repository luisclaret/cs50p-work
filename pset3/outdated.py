def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    convertDate(months)


def convertDate(months: list):
    try:
        date = input("Date: ")
        date_type = checkStructure(date, months)
    except:
        convertDate(months)
    else:
        match date_type:
            case 0:
                convertDate(months)
            case 1:
                date_list = date.split(",")[0].split()
                date_list.append(date.split(",")[1].strip())
                print(
                    f"{date_list[2]}-{(months.index(date_list[0]) + 1):02}-{int(date_list[1]):02}"
                )
            case 2:
                date_list = date.split("/")
                print(
                    f"{int(date_list[2])}-{int(date_list[0]):02}-{int(date_list[1]):02}"
                )


def checkStructure(date: str, months: list):
    if (
        "," in date
        and len(date.split(",")) == 2
        and len(date.split(",")[0].split()) == 2
    ):
        try:
            int(date.split(",")[1].strip())
            int(months.index(date.split(",")[0].split()[0]))
            day = int((date.split(",")[0].split()[1]))
            if day > 31:
                return 0

        except (ValueError, KeyError):
            return 0
        else:
            return 1
    elif "/" in date and len(date.split("/")) == 3:
        try:
            for i in date.split("/"):
                int(i)
            if int(date.split("/")[0]) > 12 or int(date.split("/")[1]) > 31:
                return 0
        except ValueError:
            return 0
        else:
            return 2
    else:
        return 0


if __name__ == "__main__":
    main()

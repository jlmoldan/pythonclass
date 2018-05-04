# boolexpr.py
# Jason Moldan


def is_in_semester(month, day):
    if month < 1 or month > 5:
        return "False"
    elif month >= 1 and month <= 5:
        if month == 1 and day < 29 or month == 5 and day > 12:
            return "False"
        else:
            return "True"

def main():
    month = int(input("enter month:"))
    day = int(input("enter day:"))

    print(is_in_semester(month, day))


main()


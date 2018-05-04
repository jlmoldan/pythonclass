# boolif.py
# Jason Moldan


def isWithin(month, day, year):
    # if year < 1995 or year > 2017:
    #     return False
    if year < 1995 or year > 2016:
        return False
    elif year >= 1995 and year <= 2016:
        if year == 1995 and month < 7 or year == 2016 and month > 7:
            #print (day,month, year)
            return "False"
        elif year == 1995 and day < 26 or year == 2016 and day > 26:
            return "False"
        else:
            return "True"

def main():
    month = int(input("enter month:"))
    day = int(input("enter day:"))
    year = int(input("enter year:"))

    print(isWithin(month, day, year))


main()

# julian.py
# Jason Moldan
# With extra credit



def julian(month, day):
    daynum = 31*(month-1) + day
    if month >= 3:
        daynum = (31 * (month - 1) + day) - ((4 * month +23) // 10)
    return (daynum)

def julianLeap(month, day):
    daynum = 31*(month-1) + day
    if month >= 3:
        daynum = ((31 * (month - 1) + day) - ((4 * month +23) // 10) +1)
    return (daynum)


def main():
    month = int(input("enter month:"))
    day = int(input("enter day:"))
    year = int(input("enter year:"))

    if year  % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        #print ("leap")
        print(julianLeap(month, day))
    else:
        print(julian(month, day))

main()

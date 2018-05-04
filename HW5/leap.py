# leap.py
# Jason Moldan


def isLeap(y):
   return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def main():
    year = int(input("enter year:"))
    print (isLeap(year))

main()
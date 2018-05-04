# num2eng3.py
# Jason Moldan


def tens_to_english(num):
    if num == 2:
        return "twenty"
    elif num == 3:
        return "thirty"
    elif num == 4:
        return "fourty"
    elif num == 5:
        return "fifty"
    elif num == 6:
        return "sixty"
    elif num == 7:
        return "seventy"
    elif num == 8:
        return "eitghty"
    elif num == 9:
        return "nintey"
    else:
        return "invalid"


def main():
    number = int(input("enter number:"))

    print(tens_to_english(number))


main()







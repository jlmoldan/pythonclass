# num2eng2.py
# Jason Moldan

def teens_to_english(N):
    if N == 10:
        return "ten"
    elif N == 11:
        return "eleven"
    elif N == 12:
        return "twelve"
    elif N == 13:
        return "thirteen"
    elif N == 14:
        return "fourteen"
    elif N == 15:
        return "fifteen"
    elif N == 16:
        return "sixteen"
    elif N == 17:
        return "seventeen"
    elif N == 18:
        return "eightteeen"
    elif N == 19:
        return "nineteen"
    else:
        return "invalid"


def main():
    number = int(input("enter number:"))

    print(teens_to_english(number))


main()

# num2eng1.py
# Jason Moldan


def digit_to_english(N):
    # if 0 < N or N >= 10:
    #     return "Invalid"
    if N == 0:
        return "zero"
    elif N == 1:
        return "one"
    elif N == 2:
        return "two"
    elif N == 3:
        return "three"
    elif N == 4:
        return "four"
    elif N == 5:
        return "five"
    elif N == 6:
        return "six"
    elif N == 7:
        return "seven"
    elif N == 8:
        return "eight"
    elif N == 9:
        return "nine"
    else:
        return "invalid"
    
def main():
    number = int(input("enter number:"))

    print(digit_to_english(number))

main()

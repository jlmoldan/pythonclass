# score2grade.py
# Jason Moldan


def grade_is(score):
    if score <= 0 or score > 100:
        return "Bad input"
    elif score <=59:
        return "F"
    elif score >=60 and score <= 69:
        return "D"
    elif score >=70 and score <= 79:
        return "C"
    elif score >=80 and score <= 89:
        return "B"
    elif score >=90 and score <= 100:
        return "A"

def main():
    score = int(input("enter score:"))

    print(grade_is (score))

main()



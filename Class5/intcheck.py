# intcheck.py
# Jason Moldan




def compare(N):
    if N > 0:
       return "Greater than zero"
    elif N < 0:
       return "Less than zero"
    elif N ==0:
       return "Equals zero"

def main():
    print(compare(int(input("Enter an integer: "))))

main()
##### SEE NEXT PIECE ABOUT HAVING THE MAIN CALL THIS.....

# def main(x):
#     if x < 0:
#         print(x, "is Less than zero")
#         #return "Is Less than Zero"
#     elif x > 0:
#         print(x, "is Greater than zero")
#     else:
#         print(x, "is Equals zero")
# def main2(x):
#     if x < 0:
#         print(x, "is Less than zero")
#     else:
#         if x > 0:
#             print(x, "is Greater than zero")
#         else:
#             print(x, "is Equals zero")





#main(number)
#main2(number)
#





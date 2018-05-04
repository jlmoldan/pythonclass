# if x < 0:
#     print(x, "is invalid")
# elif x > 0:
#     print(x, "is positive")
# else:
#     print(x, "is 0")


def exor(a, b):
    y = a and not b or not a and b
    return y

def mystery(x):
    a = exor(exor(x,not x),exor(not x,x))
    return a

n = 47
result = mystery(n % 47 == 0)
print(result)


# def main2(x):
#     if x < 0:
#         print(x, "is Less than zero")
#     else:
#         if x > 0:
#             print(x, "is Greater than zero")
#         else:
#             print(x, "is Equals zero")
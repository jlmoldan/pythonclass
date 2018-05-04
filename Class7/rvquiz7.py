def exor(a, b):
    y = a and not b or not a and b
    return y

def mystery(x):
    a = exor(exor(x,not x),exor(not x,x))
    return a

n = 47
result = mystery(n % 47 == 0)
print(result)
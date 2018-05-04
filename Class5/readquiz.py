def pow(b, p):
    y = b ** p
    return y

def mystery(x):
    a = pow(x,2) + pow(2,x)
    return a

n = 6
result = mystery(n)
print(result)
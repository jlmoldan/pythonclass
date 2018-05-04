# fib.py
# Jason Moldan


def fib(N):
    fn_1,fn_2  = 0,1
    if N <= 1:
        return N
    else:
        for steps in range(N -1):
            fn = fn_1 + fn_2
            fn_1 = fn_2
            fn_2 = fn
    return fn

##print (fib(8))


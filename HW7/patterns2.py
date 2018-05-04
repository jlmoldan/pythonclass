#
#   patterns2.py:
#
#   Jason Moldan
#



def triangle(N):
    for i in reversed(range(1,N+1)):
        print (' ' * (N-i) + i*'*')
    print ("")

def hollow_box(N):
    print('*' * N)
    for i in range(N-2):
        print ('*' + ' ' * (N-2) + '*')
    print('*' * N)
    print ("")

def solid_diamond(N):
    for i in range(N+1):
        print((N - i) * ' ' + (2 * i + 1) * '*')
    for i in range(N- 1, -1, -1):
        print((N - i) * ' ' + (2 * i + 1) * '*')
    print ("")

def hollow_diamond(N):
    for i in range(N+1):
        if i == 0:
            print((N - i) * ' ' + (2 * i + 1) * '*')
        else:
            print ((N - i) * ' ' + '*' + (' ' * (2 * i-1)) + '*')
    for i in range(N- 1, -1, -1):
        if i == 0:
            print((N - i) * ' ' + (2 * i + 1) * '*')
        else:
            print((N - i) * ' '  + '*' + (' ' * (2 * i-1)) + '*')



N = int(input("Enter an integer N: "))
triangle(N)
hollow_box(N)
solid_diamond(N)
hollow_diamond(N)
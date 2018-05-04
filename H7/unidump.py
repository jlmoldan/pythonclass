#
# unidump.py:
#
#   Starting code H7-2
#
import time
N = int(input("Enter integer N: "))
#print ("0032:", end="")
# for row in range (32,N):
#     print("%04d" % row, end="")
for n in range (32,N):
    time.sleep(0.01)
    if n % 32 == 0: # and n != 32:
        print()
        print(str("%04d" %n)+": ", end="")
        # if n % 32 == 0 and n != 32:
        #     print()
    #print ("%d" % n, end=" ")
    print("%s" % (chr(n)), end=' ')


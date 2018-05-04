# Jason Moldan
# HW2

import math
start=input("enter a start integer: ")
start=int(start)
stop=input("enter a stop integer: ")

stop=int(stop)
stop=(stop + 1)

sum=0
for i in range(start, stop):
    #print (i)
    sum +=i
print (sum)

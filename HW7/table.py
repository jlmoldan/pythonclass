
print ("|  * | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |")
print ("--------------------------------------------------------")
#
# for row in range(10):
#     print("| ", "0".rstrip(),(row), " ", end="")

for row in range(10):
    print ("| %02d"%(row),"",end="")
    for col in range(10):
        print ("| %02d"%(row*col),"",end="")
        if col == 9:
            print (("|"), end="")
    print()



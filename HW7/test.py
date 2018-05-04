stop_codon_list = ["TAA", "TAG", "TGA"]  # the rest stop codons

for codon in (stop_codon_list):
    print (codon)

# # for x in range(0, 10):
# #         for y in range(0, 10):
# #             z = x * y
# #             print(z, end="\t")
# #         print() #creates the space after the loop
# #
#
#
#
# # n=int(input('Please enter a positive integer between 1 and 15: '))
# # for row in range(1,n+1):
# #     for col in range(1,n+1):
# #         print(row*col, "\t",end = "")
# #     print()
#
# # for row in range(10):
# #     print ((row),end="\t")
# #     for col in range(10):
# #         print ((row*col),end="\t")
# #     print()
# for row in range(10):
#     print ("| %02d"%(row),end="")
#     for col in range(10):
#         print ("| %02d"%(row*col),end="")
#     print()
#
# # #
# # for row in range(0, 10): print (('| %02d' %(row)), end="")
# #
# #     # for col in range(0, 10):
# #     #     print ("| %02d"%(row*col),end="\t")
#     # print()
#
# # n=int(9)
# # for row in range(1,n+1):
# #     print(*("{:3}".format(row*col) for col in range(1, n+1)))
#
# dedupe_list.py:
#
#   Starting code H7-3
#





def main():
    mylist = eval(input("Enter a list in proper Python format:"))
    output =[]
    for x in mylist:
        if x not in output:
            output.append(x)
    return output


    # newlist = []
    # for item in mylist:
    #     if item not in newlist:
    #         newlist = newlist + item
    # print (mylist)
    # print (newlist)

print (main())


#############     "a", "b", "c", "a", "a", "a", "dog", "cat"
###############   '1', '2', '3', '101', '1'
# def uniq(input):
#   output = []
#   for x in input:
#     if x not in output:
#       output.append(x)
#   return output


#
# def squeeze(s,ch):
#     result = ''
#     for c in s:
#         if c != ch:
#             result = result + c
#     return result
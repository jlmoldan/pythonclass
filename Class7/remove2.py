#
# Lab 7-5:
#
#   HTT9 Exercise 8, but for lists and elements
#

def squeeze(alist,elt):
#    result = ''
    newlist =[c for c in alist if c!=elt]   ##10.22 list comprehensions
    # for c in alist:
    #     if c != elt:
    #          newlist.append(c)
    #
    #          print (newlist)
    return (newlist)
def main():
    alist = ((input("enter a list: "))).split(' ')
    elt = (input("enter a element to remove: "))
    print (squeeze(alist, elt))

main()

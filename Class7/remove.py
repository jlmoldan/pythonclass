#
# Lab 7-4:
#
#   HTT9 Exercise 8
#

def squeeze(s,ch):
    result = ''
    for c in s:
        if c != ch:
            result = result + c
    return result
def main():
    #print (squeeze('moldan', 'o'))
    #print (squeeze(squeeze('mississippi', 's'),'i'))
    s = (input("enter a string: "))
    ch = (input("enter a character: "))
    print (squeeze(s, ch))

main()

##### NEED TO ADD input from user as per question